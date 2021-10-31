from flask.typing import StatusCode

import unittest
import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from main import app


# Testing template
class FlaskTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_add_new(self):
        rv = self.app.get('/add_New')
        statuscode = rv.status_code
        self.assertEqual(statuscode, 200)


if __name__ == "__main__":
    unittest.main()