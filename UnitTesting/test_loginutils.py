import sys
sys.path.append('./')
import unittest
from flask import session, Flask
from unittest.mock import patch, MagicMock
from login_utils import get_session_identifier, login_user

class TestLoginUtils(unittest.TestCase):

    def setUp(self):
            self.app = Flask(__name__)
            self.app.secret_key = 'thisisasecretkey'  # Set a secret key for the Flask app

    def test_get_session_identifier(self):
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        address = "127.0.0.1"

        with patch('login_utils.get_headers') as mock_get:
            mock_get.return_value = user_agent, address

            session_id = get_session_identifier()
            expected_session_id = '1e994ac16daffba2b8c73c1cf2c2db63b62ef8539f9b2f0f0b6b1a2ed95f1d35eb7d919b1ea6d23a88f7977624654ae8496e5ce986c7c057e252b93183476018'

            self.assertEqual(session_id, expected_session_id)

    def test_login_user(self):
        with self.app.test_request_context(
            environ_base={
                'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
                'REMOTE_ADDR': '127.0.0.1'
            }
        ):
            user = [29, 'aaaaaaaa', 'aaaaaaaa', b'$2b$12$AolQMfJR7M2SmzW8PIpMi.VJFg/R96cWnLXouHEYskkgEjZNHsdqm', 'student']
            login_user(self.app, user, remember=True, duration=None, force=False, fresh=True)

            self.assertEqual(session["user_id"], 29)
            self.assertEqual(session["type"], 'student')
            self.assertTrue(session["_fresh"])
            self.assertEqual(session["_remember"], 'set')
            self.assertIsNone(session.get("_remember_seconds"))
    
    def test_login_user_without_remember(self):
        with self.app.test_request_context(
            environ_base={
                'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
                'REMOTE_ADDR': '127.0.0.1'
            }
        ):
            user = [29, 'aaaaaaaa', 'aaaaaaaa', b'$2b$12$AolQMfJR7M2SmzW8PIpMi.VJFg/R96cWnLXouHEYskkgEjZNHsdqm', 'student']
            login_user(self.app, user, remember=False, duration=None, force=False, fresh=True)

            self.assertEqual(session["user_id"], 29)
            self.assertEqual(session["type"], 'student')
            self.assertTrue(session["_fresh"])
            self.assertIsNone(session.get("_remember"))
            self.assertIsNone(session.get("_remember_seconds"))

    def test_login_user_inactive_user_without_force(self):
        with self.app.test_request_context(
            environ_base={
                'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
                'REMOTE_ADDR': '127.0.0.1'
            }
        ):
            user = [29, 'aaaaaaaa', 'aaaaaaaa', b'$2b$12$AolQMfJR7M2SmzW8PIpMi.VJFg/R96cWnLXouHEYskkgEjZNHsdqm', 'inactive']
            login_success = login_user(self.app, user, remember=False, duration=None, force=False, fresh=True)

            self.assertTrue(login_success)

    def test_login_user_inactive_user_with_force(self):
        with self.app.test_request_context(
            environ_base={
                'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
                'REMOTE_ADDR': '127.0.0.1'
            }
        ):
            user = [29, 'aaaaaaaa', 'aaaaaaaa', b'$2b$12$AolQMfJR7M2SmzW8PIpMi.VJFg/R96cWnLXouHEYskkgEjZNHsdqm', 'inactive']
            login_success = login_user(self.app, user, remember=False, duration=None, force=True, fresh=True)

            self.assertTrue(login_success)


    def test_login_user_with_custom_duration(self):
        with self.app.test_request_context(
            environ_base={
                'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
                'REMOTE_ADDR': '127.0.0.1'
            }
        ):
            import datetime
            user = [29, 'aaaaaaaa', 'aaaaaaaa', b'$2b$12$AolQMfJR7M2SmzW8PIpMi.VJFg/R96cWnLXouHEYskkgEjZNHsdqm', 'student']
            duration = datetime.timedelta(days=7)  # Set a custom duration for remember me
            login_user(self.app, user, remember=True, duration=duration, force=False, fresh=True)

            self.assertEqual(session["user_id"], 29)
            self.assertEqual(session["type"], 'student')
            self.assertTrue(session["_fresh"])
            self.assertEqual(session["_remember"], 'set')
            self.assertAlmostEqual(session["_remember_seconds"], 604800.0, delta=0.1)  # Check for an approximate duration

    def test_login_user_without_user_agent(self):
        with self.app.test_request_context(
            environ_base={
                'REMOTE_ADDR': '127.0.0.1'
            }
        ):
            user = [29, 'aaaaaaaa', 'aaaaaaaa', b'$2b$12$AolQMfJR7M2SmzW8PIpMi.VJFg/R96cWnLXouHEYskkgEjZNHsdqm', 'student']
            login_user(self.app, user, remember=True, duration=None, force=False, fresh=True)

            self.assertEqual(session["user_id"], 29)
            self.assertEqual(session["type"], 'student')
            self.assertTrue(session["_fresh"])
            self.assertEqual(session["_remember"], 'set')
            self.assertIsNone(session.get("_remember_seconds"))


if __name__ == '__main__':
    unittest.main()
