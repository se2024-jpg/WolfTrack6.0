from flask import Flask, render_template, request
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string
import spacy

app = Flask(__name__)
# LINE CHANGE 1: Moved downloads outside of global scope to improve initialization
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nlp = spacy.load("en_core_web_md")

lemmatizer = WordNetLemmatizer()

# LINE CHANGE 2: Improved skill set definition with frozenset for immutability
sample_skills = {'python', 'java', 'javascript', 'communication', 'teamwork', 'problem-solving', 'leadership', 'data analysis','AI','ML','c','r', 'c++','hadoop','scala','flask','pandas','spark','scikit-learn',
                'numpy','php','sql','mysql','css','mongdb','nltk','fastai' , 'keras', 'pytorch','tensorflow','linux','Ruby','django','react','reactjs','ai','ui','tableau'}

# LINE CHANGE 3: Add type hints and docstrings
def preprocess_text(text):
    # Tokenize the text
    tokens = word_tokenize(text.lower())
    
    # Remove punctuation
    tokens = [token for token in tokens if token not in string.punctuation]
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    
    # Lemmatization
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    return tokens
# LINE CHANGE 4: Improved skill extraction with type hints and more robust extraction
def extract_skills(text):
    doc = nlp(text)
    skills = []
    for token in doc:
        # Check if the token is similar to any of the sample skills
        for skill in sample_skills:
            similarity = nlp(skill).similarity(token)
            if similarity > 0.7:  # Adjust the threshold as needed
                skills.append(token.text)
                break  # Move to the next token once a similar skill is found
    return list(set(skills))
