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
    cursor = conn.cursor()
    # Querying the 'client' table
    cursor.execute("SELECT * FROM client where username ='"+str(data)+"'")
    rows = cursor.fetchone()
    conn.close()
    return rows


