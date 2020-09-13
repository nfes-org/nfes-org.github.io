from xml.dom import minidom
import regex
import os
import shutil
from bs4 import BeautifulSoup

import requests
import lxml

from html.parser import HTMLParser
from html.entities import name2codepoint


class MyHTMLParser(HTMLParser):
    def __init__(self, path_to_file):
        super().__init__()
        self.my_text = ''
        self.started_content = False
        self.path_to_file = path_to_file
        self.copied_files = []

    def handle_starttag(self, tag, attrs):
        if tag == 'asp:content':
            for attr in attrs:
                (id, value) = attr
                if value == 'MainContent':
                    self.started_content = True
                    return
            return
        if self.started_content:
            self.my_text += '<'
            self.my_text += tag
            for attr in attrs:
                if attr[0] == 'href' or attr[0] == 'src':
                    old_path: str = self.path_to_file + '/' + attr[1]
                    if os.path.isfile(old_path):
                        new_path = assets_prefix + attr[1]
                        shutil.copy(old_path, new_path)
                        self.copied_files.append(old_path)
                        self.my_text += ' ' + attr[0] + '=\"{}\"'.format(assets_prefix_for_site + attr[1])
                        continue
                self.my_text += ' ' + attr[0] + '=\"{}\"'.format(attr[1])
            self.my_text += '>\n'
        else:
            return

    def handle_endtag(self, tag):
        if tag == 'asp:content':
            self.started_content = False
            return
        if self.started_content:
            self.my_text += '</'
            self.my_text += tag
            self.my_text += '>\n\n'
        else:
            return

    def handle_data(self, data):
        if self.started_content:
            self.my_text += data + '\n'

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)


def add_recursively_to_string(s, xml_input):
    if len(xml_input.childNodes) == 0:
        if xml_input.nodeValue is None:
            return s
        else:
            new_str = s + xml_input.nodeValue
            return new_str
    else:
        new_str = s
        for child in xml_input.childNodes:
            new_str = new_str + "\n" + add_recursively_to_string(s, child)
        return new_str


posts_prefix = '../_posts/'
assets_prefix = '../assets/archive/'
assets_prefix_for_site = '/assets/archive/'
old_site_archive_prefix = '../old-site/WWWRoot/'


class PastPresentation:
    def __init__(self, xml_input):

        # date
        dates = xml_input.getElementsByTagName('date')
        assert len(dates) == 1
        self.date = dates[0].childNodes[0].nodeValue

        # title
        titles = xml_input.getElementsByTagName('title')
        assert len(titles) == 1
        self.title = titles[0].childNodes[0].nodeValue

        # author
        authors = xml_input.getElementsByTagName('author')
        assert 0 <= len(authors) <= 1
        self.author = None
        if len(authors) > 0:
            self.author = authors[0].childNodes[0].nodeValue
        # Abstract
        abstracts = xml_input.getElementsByTagName('Abstract')
        assert 0 <= len(abstracts) <= 1
        self.abstract = None
        if len(abstracts) > 0:
            self.abstract = ""
            self.abstract = add_recursively_to_string(self.abstract, abstracts[0])

        # CV
        cvs = xml_input.getElementsByTagName('CV')
        assert 0 <= len(cvs) <= 1
        self.cv = None
        if len(cvs) > 0:
            self.cv = ""
            self.cv = add_recursively_to_string(self.cv, cvs[0])

        # attachment
        # TODO figure out what to do with xattachementx
        attachment = xml_input.getElementsByTagName('attachment')
        assert 0 <= len(attachment) <= 1
        self.attachment = None
        self.attachment_description = None
        if len(attachment) > 0:
            a_filename = attachment[0].getElementsByTagName('filename')[0].childNodes[0]
            a_description = attachment[0].getElementsByTagName('linktext')[0].childNodes[0]
            self.attachment = a_filename.nodeValue
            self.attachment_description = a_description.nodeValue

        # file
        files = xml_input.getElementsByTagName('file')
        assert 0 <= len(files) <= 1
        self.original_file = None
        self.original_html = ''
        self.copied_files = []
        if len(files) > 0:
            self.original_file: str = files[0].childNodes[0].nodeValue
            if self.original_file.endswith('aspx'):
                print('processing {}'.format(self.original_file))
                try:
                    with open(old_site_archive_prefix + self.original_file) as html_file:
                        html_lines = html_file.readlines()
                        # all_html = ''
                        path_part = '/'.join(self.original_file.split('/')[0:-1])
                        parser = MyHTMLParser(old_site_archive_prefix + path_part)
                        for i in range(1, len(html_lines)):
                            # all_html = all_html + html_lines[i]
                            parser.feed(html_lines[i])

                        # mydoc = minidom.parse(old_site_archive_prefix + self.original_file)
                        # xmlstr = ElementTree.tostring(mydoc, encoding='utf8', method='xml')
                        # print(xmlstr)

                        parsed = parser.my_text

                        # soup = BeautifulSoup(all_html, features="lxml")
                        self.original_html = parsed
                        self.copied_files = parser.copied_files


                        # main_part = soup.find("asp:Content")
                        # print(main_part)
                except:
                    print('failed {}'.format(self.original_file))

        if self.original_html == '':
            if self.date is not None:
                self.original_html += '#### was presented {} \n\n'.format(self.date)
            if self.abstract is not None:
                self.original_html += '## Abstract \n\n'
                self.original_html += self.abstract + '\n\n'
            if self.cv is not None:
                self.original_html += '## CV \n\n'
                self.original_html += self.cv + '\n\n'

        if len(self.copied_files) > 0 or self.attachment is not None:
            if self.attachment is not None:
                my_attachment = old_site_archive_prefix + self.attachment
                self.copied_files.append(my_attachment)
                file_only = self.attachment.split('/')[-1]
                if my_attachment not in self.copied_files:
                    old_path: str = my_attachment
                    new_path = assets_prefix + file_only
                    shutil.copy(old_path, new_path)
                    # self.copied_files.append(old_path)
            else:
                my_attachment = self.copied_files[0]
                file_only = my_attachment.split('/')[-1]
                self.attachment_description = 'file'

            self.original_html += '\n\n<a class=\"button button--primary button--pill\" href=\"{}\">' \
                                  'Download {}' \
                                  '</a>'.format(assets_prefix_for_site + file_only, self.attachment_description)
                # print(self.original_html)
                # ''<a href' + '=\"{}\"'.format(assets_prefix_for_site + file_only)

    def make_post(self):
        """

        :return:
        """
        # ---
        # title: Post with Header Image
        # tags: [TeXt, blbla, featured]
        # category: test_ctegory
        # featured: true
        # cover: /screenshot.jpg
        # article_header:
        #   type: cover
        #   image:
        #     src: /screenshot.jpg
        # ---
        clean_title: str = self.title
        clean_title = clean_title.strip()
        if isinstance(self.author, str):
            clean_title += ' (' + self.author + ')'
        letters_only: str = regex.sub(r'[^\p{Latin}]', u'', clean_title)
        letters_only = letters_only[0:30]
        file_name = self.date + '-' + letters_only
        with open(posts_prefix + file_name + '.md', 'w') as file:

            # preamble
            file.write('---\n')
            file.write('title: \"' + clean_title + '\"\n')
            file.write('tags: presentation')
            if len(self.copied_files) > 0:
                file.write(' has_attachment')
            file.write('\n')
            file.write('---\n')
            # main part

            if self.original_html is not None:
                file.write(self.original_html)


# parse an xml file by name
mydoc = minidom.parse('../old-site/WWWRoot/App_Data/ArchiveData.xml')

top_items = mydoc.getElementsByTagName('Archive')

presentations = top_items[0].getElementsByTagName('presentation')

print(presentations)

p_list = []

for p in presentations:
    p_list.append(PastPresentation(p))

for p in p_list:
    p.make_post()
