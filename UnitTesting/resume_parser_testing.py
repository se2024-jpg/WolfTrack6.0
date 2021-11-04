
import unittest
import sys, os, inspect


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from main import app


# Testing template
class ResumeAnalyzerTest(unittest.TestCase):


    def test_resume_parser(self):
        os.chdir("..")
        os.chdir(os.getcwd()+"/Controller/resume")
        text = "output"
        #print(text)
        self.assertIsNot(text, '')

    
    def test_word_cloud_creation(self):
        input = "Technical Stack Bootstrap, JS Python, Django, Celery, Redis and MySQL Solidity, Geth and IPFS"
        os.chdir("..")
        print(os.getcwd())
        pass


if __name__ == "__main__":
    unittest.main()