import requests
import pandas as pd
import re
from urllib.parse import urlparse, parse_qs
from os.path import exists
import os


publish_date = "2025-10-21"
presentation_date = "2025-11-12"
tags = "workshop2025abstract"
target_folder = "../_posts/"


def pad_to_three(number):
    if number <= 999:
        return str(number).zfill(3)
    return str(number)


def drive_to_direct_url(url: str):
    if not isinstance(url, str) or "drive.google.com" not in url:
        return None, None, None

    parts = urlparse(url)
    path = parts.path.strip("/").split("/")

    # case 1: /file/d/<id>/
    if len(path) >= 3 and path[0] == "file" and path[1] == "d":
        file_id = path[2]
        return "file", file_id, f"https://drive.google.com/uc?export=view&id={file_id}"

    # case 2: ?id=<id>
    q = parse_qs(parts.query)
    if "id" in q:
        file_id = q['id'][0]
        return "image", file_id, f"https://drive.google.com/uc?export=view&id={file_id}"

    return None, None, None


def download_file(url: str, id: str = "new_file", out_dir="."):
    r = requests.get(url, allow_redirects=True, timeout=10)
    r.raise_for_status()

    ctype = r.headers.get("Content-Type", "").lower()
    if "pdf" in ctype:
        ext = ".pdf"
    elif ctype.startswith("image/"):
        ext = "." + ctype.split("/")[1].split(";")[0]
    else:
        ext = ".pdf"

    path = f"{out_dir}/{id}{ext}"
    with open(path, "wb") as f:
        f.write(r.content)
    return path


def is_downloadable_image(url: str, timeout=6):
    print(url)
    url = url.strip()
    if not isinstance(url, str) or not url.startswith(("http://","https://")):
        return False
    try:
        # 1) Try HEAD
        h = requests.head(url, allow_redirects=True, timeout=timeout)
        ct = h.headers.get("Content-Type","").lower()
        if h.ok and ct.startswith("image/"):
            return True
        # Some servers block HEAD → fall back to a tiny GET
        g = requests.get(url, stream=True, allow_redirects=True, timeout=timeout)
        if not g.ok:
            return False
        ctype = g.headers.get("Content-Type", "").lower()
        if ctype.startswith("image/"):
            print("Image")
            return "image"
        if "pdf" in ctype:
            print("Pdf")
            return "pdf"
    except requests.RequestException:
        return False


def create_file(row, id, overwrite=False):
    title_col = "Presentation title"
    author_col = "Presenter name"
    company_col = "Presenter affiliation"
    co_auth_col = "Co-author names, affiliations"
    abstract_col = "Abstract"
    bio_col = "Short bio of the presenter"
    embeded_pic_col = "[Either] Upload your picture here"
    extenal_pic_col = "[Or] Add your link here"

    title = row[title_col]
    author = row[author_col]
    company = row[company_col]
    # str = str.replace(/\s+/g, '-')
    # title = title.strip(' .')
    # title_for_display = re.sub('\s|:|/|\?|&|\.|[^\x00-\x7F]|,|\(|\)|\'', '-', title)
    # file_name = target_folder + publish_date + '-' + title_for_display + '.md'
    short_title = title.split(' ')[0].lower()
    file_name = target_folder + publish_date + '-' + pad_to_three(id+1) + '-' + short_title + '-workshop-abstract' + '.md'
    print(file_name)
    # todo remove
    file_exists = exists(file_name)
    if not overwrite and file_exists:
        return
    with open(file_name, 'w') as md_file:
        # header
        md_file.write('---\n')
        md_file.write(f'tags: {tags}\n')
        md_file.write(f'title: "{title} ({author}, {company})"\n')
        md_file.write(f'presentation_date: {presentation_date}\n')
        md_file.write('---\n')
        # body
        md_file.write('#### Presenter\n')
        md_file.write(f'**{author}** from {company}\n')
        if pd.notna(row[co_auth_col]) and str(row[co_auth_col]).strip() != '':
            # print(f'Co author: {row[co_auth_col]}')
            md_file.write('#### Co-authors\n')
            md_file.write(f'{row[co_auth_col]}\n')
        md_file.write('## Abstract\n')
        #abstract
        abstract = row[abstract_col]
        formatted_abstract = re.sub(r'\r\n|\r|\n', '\n\n', abstract)
        md_file.write(formatted_abstract)
        md_file.write('\n\n')

        if pd.notna(row[embeded_pic_col]):
            file_type, file_id, url = drive_to_direct_url(row[embeded_pic_col])
            print(f"Found {file_type}")
            # todo incorrect behavior detects via link formating
            if file_type == "image":
                local_path = download_file(url, file_id, out_dir="../assets/seminar_2025/illustrations")
                local_path = local_path.lstrip(".")
                if local_path.endswith(".pdf"):
                    md_file.write(f"[Supporting pdf (download)]({local_path}) \n ")
                else:
                    md_file.write(f"![Supporting figure]({local_path}) \n ")
            elif file_type == "file":
                md_file.write(f"[Supporting document (download from Google Drive)]({url}) \n")
        if pd.notna(row[extenal_pic_col]) and is_downloadable_image(row[extenal_pic_col]):
            md_file.write(f"**Link to an illustration**: [Exteral website]({row[extenal_pic_col].strip()}) \n")

        md_file.write('\n')

        md_file.write('## Biography\n')
        #biography
        bio = row[bio_col]
        md_file.write(bio)


if __name__ == "__main__":
    abstracts_data = pd.read_csv('~/Downloads/2025 Abstract submission formation evaluation (Responses) - Form responses 1 (1).csv')
    abstracts_data = abstracts_data.rename(columns=lambda c: "Abstract" if c.startswith("Abstract of the contributed talk") else c)

    print(abstracts_data)
    for index, row in abstracts_data.iterrows():
        create_file(row, index+1, overwrite=True)


