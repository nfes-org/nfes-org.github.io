from xml.dom import minidom
import regex


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

        # file
        files = xml_input.getElementsByTagName('file')
        assert 0 <= len(files) <= 1
        self.original_file = None
        self.original_html = None
        if len(files) > 0:
            self.original_file = files[0].childNodes[0].nodeValue
            # TODO get original html from file

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
        letters_only: str = regex.sub(r'[^\p{Latin}]', u'', clean_title)
        letters_only = letters_only[0:30]
        file_name = self.date + '-' + letters_only
        with open(posts_prefix + file_name, 'w') as file:
            file.write('---\n')
            # preamble
            file.write('title: ' + clean_title + '\n')
            file.write('---\n')
            # main part




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

