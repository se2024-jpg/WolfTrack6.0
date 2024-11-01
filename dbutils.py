'''
MIT License

Copyright (c) 2024 Girish G N, Joel Jogy George, Pravallika Vasireddy

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import sqlite3

def create_tables(db):
    """Create tables for clients and jobs if they do not exist."""
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS client (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                usertype TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company_name TEXT,
                location TEXT,
                job_position TEXT,
                salary INTEGER,
                status TEXT
            )
        ''')
        conn.commit()

def add_client(value_set, db):
    """Insert a new client into the client table."""
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO client (name, username, password, usertype) VALUES (?, ?, ?, ?)", value_set)
        conn.commit()

def find_user(username, db):
    """Find a user in the client table by username."""
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM client WHERE username = ?", (username,))
        return cursor.fetchone()  # Return the found row

def add_job(data, db):
    """Insert a new job into the jobs table."""
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO jobs (company_name, location, job_position, salary, status) VALUES (?, ?, ?, ?, ?)", data)
        conn.commit()

def get_job_applications(db):
    """Retrieve all job applications."""
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM jobs")
        return cursor.fetchall()  # Return all rows

def update_job_application_by_id(job_id, company, location, job_position, salary, status, db):
    """Update a job application by its ID."""
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE jobs SET company_name=?, location=?, job_position=?, salary=?, status=? WHERE id=?",
                       (company, location, job_position, salary, status, job_id))
        conn.commit()

def delete_job_application_by_company(company_name, db):
    """Delete job applications by company name."""
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM jobs WHERE company_name=?", (company_name,))
        conn.commit()

def get_job_applications_by_status(db, status):
    """Retrieve job applications by their status."""
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM jobs WHERE status = ?", (status,))
        return cursor.fetchall()  # Return all rows
