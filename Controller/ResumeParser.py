'''
MIT License

Copyright (c) 2023 Shonil B, Akshada M, Rutuja R, Sakshi B

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import io
import pdfminer
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
# Docx resume
import docx2txt
import PyPDF2
# Wordcloud
import re
import numpy as np
import operator
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('punkt')
set(stopwords.words('english'))
from wordcloud import WordCloud
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import cv2
import pytesseract


# def read_pdf_resume(pdf_doc):
#     resource_manager = PDFResourceManager()
#     fake_file_handle = io.StringIO()
#     converter = TextConverter(resource_manager, fake_file_handle)
#     page_interpreter = PDFPageInterpreter(resource_manager, converter)
#     with open(pdf_doc, 'rb') as fh:
#         for page in PDFPage.get_pages(fh, caching=True,check_extractable=True):
#             page_interpreter.process_page(page)
#         text = fake_file_handle.getvalue()
#     # close open handles
#     converter.close()
#     fake_file_handle.close()
#     if text:
#         return text


def read_image_resume(file):
    image = cv2.imread(file)
    text = pytesseract.image_to_string(image)
    print(text)
    if text:
        return text


def read_pdf_resume(file):
    # creating a pdf file object
    pdfFileObj = open(file, 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # creating a page object
    pageObj = pdfReader.getPage(0)

    # extracting text from page
    text = pageObj.extractText()
    # closing the pdf file object
    pdfFileObj.close()
    print("TEST\n\n\n\n\n", text)
    return text


def read_word_resume(word_doc):
    resume = docx2txt.process(word_doc)
    resume = str(resume)
    # print(resume)
    text = ''.join(resume)
    text = text.replace("\n", "")
    print(text)
    if text:
        return text


def clean_job_decsription(jd):
    ''' a function to create a word cloud based on the input text parameter'''
    ## Clean the Text
    # Lower
    clean_jd = jd.lower()
    # remove punctuation
    clean_jd = re.sub(r'[^\w\s]', '', clean_jd)
    # remove trailing spaces
    clean_jd = clean_jd.strip()
    # remove numbers
    clean_jd = re.sub('[0-9]+', '', clean_jd)
    # tokenize
    clean_jd = word_tokenize(clean_jd)
    # remove stop words
    stop = stopwords.words('english')
    clean_jd = [w for w in clean_jd if not w in stop]
    return (clean_jd)


def create_word_cloud(jd):
    corpus = jd
    fdist = FreqDist(corpus)
    # print(fdist.most_common(100))
    words = ' '.join(corpus)
    words = words.split()

    # create a empty dictionary
    data = dict()
    #  Get frequency for each words where word is the key and the count is the value
    for word in (words):
        word = word.lower()
        data[word] = data.get(word, 0) + 1

        # Sort the dictionary in reverse order to print first the most used terms
    dict(sorted(data.items(), key=operator.itemgetter(1), reverse=True))
    word_cloud = WordCloud(width=800, height=800,
                           background_color='white', max_words=500)
    word_cloud.generate_from_frequencies(data)


def get_resume_score(text):
    cv = CountVectorizer(stop_words='english')
    count_matrix = cv.fit_transform(text)
    count_matrix_array = count_matrix.toarray()
    print("\nSimilarity Scores:")

    # get the match percentage
    matchPercentage = cosine_similarity(count_matrix_array)[0][1] * 100
    matchPercentage = round(matchPercentage, 2)  # round to two decimal

    print("Your resume matches about " + str(matchPercentage+50) + "% of the job description.")
    return str(matchPercentage+50)


def resume_analyzer(jobtext, file):
    if file.endswith(".pdf"):
        print("\n\n\n\n\n\nn\n\n")
        resume = read_pdf_resume(file)
    elif file.endswith(".jpeg") or file.endswith(".jpg") or file.endswith(".png"):
        resume = read_image_resume(file)
    else:
        resume = read_word_resume(file)
    job_description = jobtext
    ## Get a Keywords Cloud
    clean_jd = clean_job_decsription(job_description)
    create_word_cloud(clean_jd)
    text = [resume, job_description]

    ## Get a Match score
    return get_resume_score(text)

