"""Settings shared by the scripts that build the seminar posts.

process_abstracts.py turns the submission form export into one post per
abstract; make_schedule.py turns the agenda export into the schedule post
and links it back to those abstracts. Both read everything below, so a new
seminar only needs this file edited.
"""

from datetime import date

# --- the seminar --------------------------------------------------------

seminar_year = 2026
seminar_date = "2026-11-04"
seminar_date_long = "November 4, 2026"

# Posts are published under the day the scripts are run.
publish_date = date.today().isoformat()

# --- where things live --------------------------------------------------

temp_folder = f"../seminar_{seminar_year}_temp/"
target_folder = "../_posts/"
illustrations_folder = f"../assets/seminar_{seminar_year}/illustrations"

abstracts_csv = temp_folder + (
    f"{seminar_year} Abstract submission formation evaluation (Responses)"
    " - Form responses 1 (1).csv"
)
# Either the spreadsheet itself or a CSV export of it.
agenda_file = temp_folder + "NFES_Seminar_Proposed_Agenda.xlsx"

# --- naming -------------------------------------------------------------

abstract_tag = f"workshop{seminar_year}abstract"
abstract_suffix = "-workshop-abstract"
schedule_name = f"{publish_date}-seminar-{seminar_year}-schedule.md"

site_url = "https://nfes.org"
announcement_url = "/2026/09/14/nfes-full-day-2026.html"
registration_url = "https://forms.gle/tCDhaU9mgRFxpNmW9"
cover = "assets/events/Norce-GeosteeringWorkshop24-19.jpg"
