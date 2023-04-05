import spacy
from spacy import displacy
import imgkit
from bs4 import BeautifulSoup
import aspose.words as aw
from aspose.words import Paragraph
import nltk

def reading_a_file(filename):
    doc = aw.Document('C:/Users/Radzivill/Desktop/Homework/NLIIS/Лаб №1/EYAZIS_2_2/EYAZIS_2_2/EYAZIS/Project_2/static/file/' + filename)
    nltk.download("punkt")
    if doc.first_section.body.first_paragraph:
        doc.first_section.body.first_paragraph.remove()
        text = doc.get_text()
        sentences = nltk.sent_tokenize(text)
        # list_text = text.split(".")
        sentences = sentences[:-2]
        # text = (".".join(list_text)) + '.'
    return sentences

def sentence_parsing(text):

    nlp = spacy.load("ru_core_news_sm")
    doc = nlp(text)
    html = displacy.render(doc, style="dep")
    soup = BeautifulSoup(html, 'html.parser')

    for tag in soup.find_all(text="ADP"):
        tag.replace_with("сложение")

    for tag in soup.find_all(text="ADJ"):
        tag.replace_with("прилагательное")

    for tag in soup.find_all(text="ADV"):
        tag.replace_with("наречие")

    for tag in soup.find_all(text="AUX"):
        tag.replace_with("вспомогательное предложение")

    for tag in soup.find_all(text="CCONJ"):
        tag.replace_with("координирующее соединение")

    for tag in soup.find_all(text="CONJ"):
        tag.replace_with("соединение")

    for tag in soup.find_all(text="DET"):
        tag.replace_with("определитель")

    for tag in soup.find_all(text="NOUN"):
        tag.replace_with("существительное")

    for tag in soup.find_all(text="NUM"):
        tag.replace_with("числительное")

    for tag in soup.find_all(text="PROPN"):
        tag.replace_with("имя собственное")

    for tag in soup.find_all(text="PART"):
        tag.replace_with("частица")

    for tag in soup.find_all(text="PUNCT"):
        tag.replace_with("пунктуация")

    for tag in soup.find_all(text="VERB"):
        tag.replace_with("глагол")

    for tag in soup.find_all(text="SCONJ"):
        tag.replace_with("подчинительный союз")

    with open('C:\\Users\\Radzivill\\Desktop\\Homework\\NLIIS\\Лаб №1\\EYAZIS_2_2\\EYAZIS_2_2\\EYAZIS\\Project_2\\templates\\dependency.html', 'w', encoding='utf-8') as f:
        f.write(soup.prettify())

    # html_file = 'D:/Job/EYAZIS_2_2/EYAZIS/Project_2/templates/dependency.html'
    # img_file = 'D:/Job/EYAZIS_2_2/EYAZIS/Project_2/static/img/img.png'
    # path_to_wkhtmltoimage = r'D:/Job/EYAZIS_2_2/EYAZIS/Project_2/static/additional_resources/wkhtmltopdf/bin/wkhtmltoimage.exe'
    # options = {
    #     'encoding': "UTF-8"
    # }
    # imgkit.from_file(html_file, img_file, options=options, config=imgkit.config(wkhtmltoimage=path_to_wkhtmltoimage))