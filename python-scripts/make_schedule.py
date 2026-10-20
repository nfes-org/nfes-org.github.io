"""Build the seminar schedule post from a CSV export of the agenda sheet.

The CSV is expected to have a header row containing "Time slot" (anything
above it, such as a spreadsheet title, is skipped) and these columns:

    Time slot | Duration | Presentation | Presenter | Organisation | ID

Rows are read in order and classified by what they contain:

* only "Time slot" filled      -> a session heading
* a time slot, but no ID       -> a break, registration, closing remarks ...
* a time slot and an ID        -> a talk, grouped with the talks around it

Talks are grouped per session into one <tr> block with a rowspan, the same
shape the Apps Script version produced. The ID (ID_007, 7, 007 ...) is
matched against the abstract posts in _posts/ to link each talk to its
abstract.
"""

import csv
import glob
import os
import re

from seminar_config import (
    abstract_suffix,
    agenda_csv as csv_path,
    announcement_url,
    cover,
    day_heading,
    registration_url,
    schedule_name as output_name,
    seminar_date,
    seminar_date_long,
    site_url,
    target_folder as posts_folder,
)

# --- configuration ------------------------------------------------------

preliminary = True

sponsorship_note = """### Available sponsorship and marketing packages

NFES offers high visibility to our partners at the seminar.
Sponsorship and marketing packages are available starting from 15,000 NOK.

For more details on the opportunities, please contact:

- Annette Larsen: [alarsen@logtek.no](mailto:alarsen@logtek.no)
"""

# --- reading the agenda -------------------------------------------------

COLUMNS = ("Time slot", "Duration", "Presentation", "Presenter", "Organisation", "ID")


def read_rows(path):
    """Return the agenda rows as dicts, skipping anything above the header."""
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = [[(c or "").strip() for c in row] for row in csv.reader(f)]

    header_index = next(
        (i for i, row in enumerate(rows) if "Time slot" in row), None
    )
    if header_index is None:
        raise SystemExit(f'{path}: no header row containing "Time slot"')

    header = rows[header_index]
    index_of = {name: header.index(name) for name in COLUMNS if name in header}
    missing = [name for name in COLUMNS if name not in index_of]
    if missing:
        raise SystemExit(f"{path}: missing column(s) {', '.join(missing)}")

    agenda = []
    for row in rows[header_index + 1:]:
        entry = {
            name: (row[i] if i < len(row) else "") for name, i in index_of.items()
        }
        if any(entry.values()):
            agenda.append(entry)
    return agenda


def is_heading(entry):
    """A merged session row: a label in the first column and nothing else."""
    return bool(entry["Time slot"]) and not any(
        entry[name] for name in COLUMNS if name != "Time slot"
    )


def split_time(slot):
    """"09:10-09:35" -> ("09:10", "09:35"); endash and spaces allowed."""
    parts = [p.strip() for p in re.split(r"[-–—]", slot, maxsplit=1)]
    start = parts[0] if parts else ""
    end = parts[1] if len(parts) > 1 else ""
    return start, end


# --- linking talks to their abstracts -----------------------------------

def abstract_urls():
    """Map an abstract number to the URL and the path of its published post."""
    urls = {}
    pattern = os.path.join(posts_folder, f"*{abstract_suffix}.md")
    for path in sorted(glob.glob(pattern)):
        name = os.path.basename(path)[: -len(".md")]
        match = re.match(r"(\d{4})-(\d{2})-(\d{2})-(\d+-.*)$", name)
        if not match:
            continue
        year, month, day, slug = match.groups()
        # Jekyll drops the date prefix from the file name to build the URL.
        urls[int(slug.split("-", 1)[0])] = (
            f"{site_url}/{year}/{month}/{day}/{slug}.html",
            path,
        )
    return urls


def abstract_number(value):
    """"ID_007", "007", "7" -> 7; anything without digits -> None."""
    digits = re.search(r"\d+", value)
    return int(digits.group()) if digits else None


def has_co_authors(path):
    """True when the abstract post lists co-authors, so the talk gets "et al."."""
    try:
        with open(path, encoding="utf-8") as f:
            return "#### Co-authors" in f.read()
    except FileNotFoundError:
        return False


def describe_talk(entry, urls, missing):
    start, _ = split_time(entry["Time slot"])
    number = abstract_number(entry["ID"])
    url, path = urls.get(number, (None, None))

    who = entry["Presenter"]
    if entry["Organisation"]:
        who += f" ({entry['Organisation']})"
    if path and has_co_authors(path):
        who += " et al."

    line = f"{start}: {who}: <b>{entry['Presentation']}</b>"
    if url:
        line += f' <a href="{url}">(abstract)</a>'
    else:
        missing.append((entry["ID"], entry["Presentation"]))
    return line


# --- building the table -------------------------------------------------

def build_table(agenda, urls, missing):
    parts = ['<table class="nice-table" id="table">']
    parts.append(f'<tr>\n<th colspan="3"><b>{day_heading}</b></th>\n</tr>')

    session = ""
    talks = []
    trailing_notes = []

    def flush():
        """Emit the talks collected so far as one rowspan block."""
        if not talks:
            return
        first_start, _ = split_time(talks[0]["Time slot"])
        _, last_end = split_time(talks[-1]["Time slot"])
        span = len(talks)

        parts.append("<tr>")
        parts.append(f'<td rowspan="{span}">{first_start} - {last_end}</td>')
        parts.append(f'<td rowspan="{span}">{session}</td>')
        parts.append(f"<td>{describe_talk(talks[0], urls, missing)}</td>")
        parts.append("</tr>")
        for talk in talks[1:]:
            parts.append("<tr>")
            parts.append(f"<td>{describe_talk(talk, urls, missing)}</td>")
            parts.append("</tr>")
        talks.clear()

    for position, entry in enumerate(agenda):
        if is_heading(entry):
            flush()
            label = entry["Time slot"]
            # A heading with no rows under it is a note, not a session.
            rest = agenda[position + 1:]
            if not any(not is_heading(later) for later in rest):
                trailing_notes.append(label)
                continue
            session = label
            # Headings such as "Welcome & Introduction" label rows that are
            # not talks; show them as a full-width heading instead.
            following = next((later for later in rest if not is_heading(later)), None)
            if following is not None and not following["ID"]:
                parts.append(f'<tr>\n<th colspan="3"><b>{label}</b></th>\n</tr>')
        elif entry["ID"]:
            talks.append(entry)
        else:
            flush()
            start, end = split_time(entry["Time slot"])
            interval = f"{start} - {end}" if end else start
            parts.append("<tr>")
            parts.append(f"<td>{interval}</td>")
            parts.append(f'<td colspan="2"><b>{entry["Presentation"]}</b></td>')
            parts.append("</tr>")

    flush()
    parts.append("</table>")
    return "\n".join(parts), trailing_notes


def build_post(agenda, urls, missing):
    table, trailing_notes = build_table(agenda, urls, missing)

    out = ["---"]
    out.append("tags: News")
    out.append(f'title: "Schedule for NFES Formation Evaluation Seminar, {seminar_date_long}"')
    out.append(f"presentation_date: {seminar_date}")
    out.append(f"cover: {cover}")
    out.append(f'excerpt: "The schedule for the {seminar_date_long} NFES Seminar is now available!"')
    out.append("---")
    out.append("")
    out.append(f"[**To the event announcement**]({announcement_url})")
    out.append("")
    out.append(f"[**Online registration is open!**]({registration_url})")
    out.append("")
    if preliminary:
        out.append("The program is preliminary while we await confirmations from the presenters.")
        out.append("")
    out.append(table)
    out.append("")
    for note in trailing_notes:
        out.append(note)
        out.append("")
    out.append(sponsorship_note)
    return "\n".join(out)


if __name__ == "__main__":
    agenda = read_rows(csv_path)
    urls = abstract_urls()
    missing = []

    output_path = os.path.join(posts_folder, output_name)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(build_post(agenda, urls, missing))
    print(f"wrote {output_path}")

    if missing:
        print(f"\n{len(missing)} talk(s) without a matching abstract post:")
        for talk_id, title in missing:
            print(f"  - {talk_id or '(no ID)'}: {title}")
