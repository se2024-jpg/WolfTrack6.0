import sqlite3

def create_tables():
    conn = sqlite3.connect('database.db')
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
    conn.close()


def add_client(value_set):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    print(value_set)
    # Inserting rows into the 'client' table
    cursor.execute("INSERT INTO client (name, username, password, usertype) VALUES (?, ?, ?, ?)",
                       value_set)
    conn.commit()
    conn.close()

def search_username(data):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Querying the 'client' table
    cursor.execute("SELECT username FROM client Where username = '"+str(data)+"'")
    rows = cursor.fetchone()
    conn.close()
    return rows

def find_user(data):
    conn = sqlite3.connect('database.db')
    print('Data==>', data)
    cursor = conn.cursor()
    # Querying the 'client' table
    cursor.execute("SELECT * FROM client where username ='"+str(data)+"'")
    rows = cursor.fetchone()
    conn.close()
    print('rowsss->>>', rows)
    return rows

def add_job(data):
    conn = sqlite3.connect('database.db')
    print('Data==>', data)
    cursor = conn.cursor()
    # Inserting rows into the 'jobs' table
    cursor.execute("INSERT INTO jobs (company_name, location, job_position, salary, status) VALUES (?, ?, ?, ?, ?)", data)
    conn.commit()
    conn.close()

def get_job_applications():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jobs")
    rows = cursor.fetchall()  # Use fetchall() to get all rows
    conn.close()
    print('rows ->>>', rows)
    return rows


def update_job_application_by_id(company, location, jobposition, salary, status):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Update the 'jobs' table based on jobid
    cursor.execute("UPDATE jobs SET company_name=?, location=?, job_position=?, salary=?, status=? WHERE company_name=?",
                   (company, location, jobposition, salary, status, company))

    conn.commit()
    conn.close()


def delete_job_application_by_company(company_name):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Delete the job application from the 'jobs' table based on the company name
    cursor.execute("DELETE FROM jobs WHERE company_name=?", (company_name,))

    conn.commit()
    conn.close()

def get_job_applications_by_status(db, status):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jobs WHERE status = ?", (status,))
    rows = cursor.fetchall()  # Use fetchall() to get all rows
    conn.close()
    print('rows ->>>', rows)
    return rows



