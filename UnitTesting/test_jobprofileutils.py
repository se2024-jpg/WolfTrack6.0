import unittest
import sys
sys.path.append('./')
from unittest.mock import patch, MagicMock
from Utils.jobprofileutils import preprocess_text, extract_skills

class TestTextProcessing(unittest.TestCase):

    def test_preprocess_text(self):

        # Test stopwords removal
        text = "This is a test sentence with some stopwords and words like it and the"
        processed_text = preprocess_text(text)
        expected = ['test', 'sentence', 'stopwords', 'word', 'like']
        self.assertEqual(processed_text, expected)

        # Test lemmatization
        text = "He was running and jumping in the park with his friends"
        processed_text = preprocess_text(text)
        expected = ['running', 'jumping', 'park', 'friend']
        self.assertEqual(processed_text, expected)

    def test_extract_skills(self):
        text = "I have experience in Python, Java, and Communication"
        skills = extract_skills(text)

        expected = ['Python', 'Communication']

        self.assertEqual(sorted(skills), sorted(expected))

    def test_preprocess_text_with_empty_string(self):
        # Test with an empty string
        text = ""
        processed_text = preprocess_text(text)
        expected = []
        self.assertEqual(processed_text, expected)

    def test_preprocess_text_with_no_stopwords(self):
        # Test with text containing no stopwords
        text = "Unique words should remain unchanged"
        processed_text = preprocess_text(text)
        expected = ['Unique', 'words', 'remain', 'unchanged']
        self.assertEqual(processed_text, expected)

    def test_preprocess_text_with_numbers(self):
        # Test text that includes numbers
        text = "The year 2021 was quite significant"
        processed_text = preprocess_text(text)
        expected = ['year', '2021', 'significant']
        self.assertEqual(processed_text, expected)

    def test_preprocess_text_with_special_characters(self):
        # Test text that includes special characters
        text = "Hello!!! This is a test #1 with special @characters."
        processed_text = preprocess_text(text)
        expected = ['Hello', 'test', '1', 'special', 'characters']
        self.assertEqual(processed_text, expected)

    def test_extract_skills_with_varied_case(self):
        # Test skill extraction with mixed case
        text = "I am skilled in pYTHON, JaVa, and Communication"
        skills = extract_skills(text)
        expected = ['Python', 'Communication']
        self.assertEqual(sorted(skills), sorted(expected))

    def test_extract_skills_with_unrelated_words(self):
        # Test with unrelated words mixed in
        text = "My hobbies include painting and swimming but I am also good at C++, Python, and HTML."
        skills = extract_skills(text)
        expected = ['C++', 'Python', 'HTML']
        self.assertEqual(sorted(skills), sorted(expected))

    def test_extract_skills_with_repeated_skills(self):
        # Test with repeated skills in the text
        text = "I have experience in Python, Python, and Java"
        skills = extract_skills(text)
        expected = ['Python', 'Java']
        self.assertEqual(sorted(skills), sorted(expected))

    def test_extract_skills_with_no_skills(self):
        # Test extraction when no skills are present
        text = "I enjoy reading books and hiking."
        skills = extract_skills(text)
        expected = []
        self.assertEqual(skills, expected)

    def test_preprocess_text_with_long_text(self):
        # Test processing of a long text
        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        processed_text = preprocess_text(text)
        expected = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit', 'Sed', 'eiusmod', 'tempor', 'incididunt', 'labore', 'dolore', 'magna', 'aliqua']
        self.assertEqual(processed_text, expected)

if __name__ == '__main__':
    unittest.main()
