import sys
sys.path.append('./')
import sqlite3
import unittest
from dbutils import create_tables, add_client, search_username, find_user, add_job, get_job_applications, update_job_application_by_id, delete_job_application_by_company

database = 'testdatbase.db'
class TestDbUtils(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()
        create_tables(database)

    def tearDown(self):
        self.conn.close()

    def test_create_tables(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.cursor.fetchall()
        table_names = [table[0] for table in tables]
        self.assertIn('client', table_names)
        self.assertIn('jobs', table_names)

    def test_add_client(self):
        self.delete_all_data()
        user_details = ('John Doe', 'johndoe', 'password123', 'student')
        add_client(user_details,database)
        self.setUp()
        self.cursor.execute("SELECT * FROM client WHERE username=?", ('johndoe',))
        user_in_database = self.cursor.fetchone()

        self.assertIsNotNone(user_in_database)

        with self.assertRaises(sqlite3.IntegrityError):
            add_client(user_details,database)


    def test_search_username(self):
        existing_username = 'johndoe'
        result = search_username(existing_username,database)[0]

        self.assertEqual(result, existing_username)


    def test_find_user(self):
        existing_username = 'johndoe'
        user = find_user(existing_username,database)

        self.assertIsNotNone(user)


    def test_get_job_applications(self):
        self.setUp()
        jobs = get_job_applications(database)
        self.assertIsNotNone(jobs)
        self.tearDown()


    def delete_all_data(self):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()
        self.cursor.execute("DELETE FROM client WHERE username=?",('johndoe',))
        self.conn.commit()
        self.conn.close()

if __name__ == '__main__':
    unittest.main()
