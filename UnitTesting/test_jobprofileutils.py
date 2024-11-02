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

if __name__ == '__main__':
    unittest.main()
