from unittest.main import main
from flask import app
from flask.typing import StatusCode
import unittest
import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from main import app

class FlaskTest(unittest.TestCase):

    #check if response is 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/login")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    #check if response is 200
    def test_admin(self):
        tester = app.test_client(self)
        response = tester.get("/main_login/admin_login")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    #check if content returned is application/json
    def test_admin_content(self):
        tester = app.test_client(self)
        response = tester.get("/main_login/admin_login")
        self.assertEqual(response.content_type, "text/html")

    #check if response is 200
    def test_user(self):
        tester = app.test_client(self)
        response = tester.get("/main_login/user_login")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    #check if content returned is application/json
    def test_user_content(self):
        tester = app.test_client(self)
        response = tester.get("/main_login/user_login")
        self.assertEqual(response.content_type, "text/html")

    #check if content returned is application/json
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/login")
        self.assertEqual(response.content_type, "text/html")

    #check if content returned is application/json
    def test_main_landing_page_content(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.content_type, "text/html")
    
    #check if response is 200
    def test_main_landing_page_status(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    #check data returned
    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get("/login")
        self.assertEqual(b'WolfTrack' in response.data, True)

if __name__=="__main__":
     unittest.main()