import unittest
import sys
sys.path.append('./')
from unittest.mock import MagicMock, patch
import sqlite3
import dbutils


class TestDBUtils(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db = 'test_database.db'
        dbutils.create_tables(cls.db)

    @classmethod
    def tearDownClass(cls):
        conn = sqlite3.connect(cls.db)
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS client")
        cursor.execute("DROP TABLE IF EXISTS jobs")
        conn.commit()
        conn.close()

    def test_create_tables(self):
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='client'")
        client_table = cursor.fetchone()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='jobs'")
        jobs_table = cursor.fetchone()
        conn.close()

        self.assertIsNotNone(client_table)
        self.assertIsNotNone(jobs_table)

    def test_add_client(self):
        client_data = ('John Doe', 'johndoe', 'password123', 'user')
        dbutils.add_client(client_data, self.db)
        result = dbutils.find_user('johndoe', self.db)
        self.assertIsNotNone(result)
        self.assertEqual(result[1], 'John Doe')

    def test_find_user(self):
        # Add a user and then try to find it
        client_data = ('Jane Doe', 'janedoe', 'password456', 'user')
        dbutils.add_client(client_data, self.db)
        result = dbutils.find_user('janedoe', self.db)
        self.assertIsNotNone(result)
        self.assertEqual(result[1], 'Jane Doe')

    def test_add_job(self):
        job_data = ('CompanyX', 'LocationY', 'PositionZ', 50000, 'Open')
        dbutils.add_job(job_data, self.db)
        result = dbutils.get_job_applications(self.db)
        self.assertIsNotNone(result)
        self.assertEqual(result[0][1], 'CompanyX')

    def test_get_job_applications(self):
        # Assuming there are already jobs added
        result = dbutils.get_job_applications(self.db)
        self.assertIsNotNone(result)
        self.assertTrue(len(result) >= 0)

    def test_update_job_application_by_id(self):
        # Assuming there's at least one job in the database
        job_data = ('CompanyX', 'UpdatedLocation', 'UpdatedPosition', 60000, 'Closed')
        dbutils.update_job_application_by_id(*job_data, self.db)
        result = dbutils.get_job_applications(self.db)
        updated_job = [job for job in result if job[1] == 'CompanyX']
        self.assertIsNotNone(updated_job)
        self.assertEqual(updated_job[0][1:], job_data)

    def test_delete_job_application_by_company(self):
        # Assuming there's at least one job in the database
        dbutils.delete_job_application_by_company('UpdatedCompany', self.db)
        result = dbutils.get_job_applications(self.db)
        deleted_job = [job for job in result if job[1] == 'UpdatedCompany']
        self.assertEqual(len(deleted_job), 0)


if __name__ == '__main__':
    unittest.main()
