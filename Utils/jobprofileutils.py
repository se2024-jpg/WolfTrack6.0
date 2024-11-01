from flask import Flask, render_template, request
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string
import spacy
import typing

# LINE CHANGE 1: Moved downloads outside of global scope to improve initialization
def download_nltk_resources():
    try:
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        nltk.download('wordnet', quiet=True)
    except Exception as e:
        print(f"Warning: NLTK resource download failed: {e}")

# LINE CHANGE 2: Improved skill set definition with frozenset for immutability
SAMPLE_SKILLS = frozenset([
    'python', 'java', 'javascript', 'communication', 'teamwork', 
    'problem-solving', 'leadership', 'data analysis', 'ai', 'ml', 
    'c', 'r', 'c++', 'hadoop', 'scala', 'flask', 'pandas', 'spark', 
    'scikit-learn', 'numpy', 'php', 'sql', 'mysql', 'css', 'mongdb', 
    'nltk', 'fastai', 'keras', 'pytorch', 'tensorflow', 'linux', 
    'ruby', 'django', 'react', 'reactjs', 'ui', 'tableau'
])

# LINE CHANGE 3: Add type hints and docstrings
def preprocess_text(text: str) -> typing.List[str]:
    """
    Preprocess input text by tokenizing, removing punctuation and stopwords, and lemmatizing.
    
    Args:
        text (str): Input text to preprocess
    
    Returns:
        List[str]: Processed tokens
    """
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
def extract_skills(text: str) -> typing.List[str]:
    """
    Extract skills from input text using semantic similarity.
    
    Args:
        text (str): Input text to extract skills from
    
    Returns:
        List[str]: Extracted skills
    """
    doc = nlp(text)
    skills = []
    processed_skills = set()
    
    for token in doc:
        # Check if the token is similar to any of the sample skills
        for skill in SAMPLE_SKILLS:
            if skill not in processed_skills:
                similarity = nlp(skill).similarity(token)
                if similarity > 0.7:  # Adjust the threshold as needed
                    skills.append(token.text)
                    processed_skills.add(skill)
                    break  # Move to the next token once a similar skill is found
    
    return list(set(skills))

# LINE CHANGE 5: Safe initialization of spaCy and NLTK resources
def initialize_nlp_resources():
    download_nltk_resources()
    try:
        nlp = spacy.load("en_core_web_md")
        lemmatizer = WordNetLemmatizer()
        return nlp, lemmatizer
    except Exception as e:
        print(f"Error initializing NLP resources: {e}")
        return None, None

# Safe initialization
app = Flask(__name__)
nlp, lemmatizer = initialize_nlp_resources()