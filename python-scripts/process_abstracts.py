import pandas as pd
import re
from os.path import exists


publish_date = "2022-10-14"
presentation_date = "2022-11-01"
tags = "workshop2022abstract"
target_folder = "../_posts/"


def create_file(row, id):
    title_col = "Presentation title"
    author_col = "Presenter name"
    company_col = "Presenter affiliation"
    co_auth_col = "Co-author names, affiliations"
    abstract_col = "Abstract of the contributed talk (150-500 words)"
    bio_col = "Short bio of the presenter"

    title = row[title_col]
    author = row[author_col]
    company = row[company_col]
    # str = str.replace(/\s+/g, '-')
    # title = title.strip(' .')
    # title_for_display = re.sub('\s|:|/|\?|&|\.|[^\x00-\x7F]|,|\(|\)|\'', '-', title)
    # file_name = target_folder + publish_date + '-' + title_for_display + '.md'
    short_title = title.split(' ')[0].lower()
    file_name = target_folder + publish_date + '-' + short_title + '-workshop-abstract-' + str(id+1) + '.md'
    print(file_name)
    # todo remove
    file_exists = exists(file_name)
    if file_exists:
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
        md_file.write('#### Co-authors\n')
        md_file.write(f'{row[co_auth_col]}\n')
        md_file.write('## Abstract\n')
        #abstract
        abstract = row[abstract_col]
        formatted_abstract = re.sub(r'\r\n|\r|\n', '\n\n', abstract)
        md_file.write(formatted_abstract)
        md_file.write('\n')
        md_file.write('## Biography\n')
        #biography
        bio = row[bio_col]
        md_file.write(bio)


if __name__ == "__main__":
    abstracts_data = pd.read_csv('~/Downloads/Abstract submission geosteering (Responses) - Form responses 1 (1).csv')
    print(abstracts_data)
    for index, row in abstracts_data.iterrows():
        create_file(row, index+1)


