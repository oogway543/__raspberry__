import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
         conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_table(conn):
    sql_projects = """
    CREATE TABLE IF NOT EXISTS led (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date text NOT NULL,
        state INTEGER NOT NULL
    """

    try:
        c = conn.cursor()
        c.execute(sql_projects)
        print("Table created successfully")
    except Error as e:
        print(e)