
import sqlite3

def connect():
    conn = sqlite3.connect("student_data.db")
    cur = conn.cursor()


    cur.execute("""
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY,
        name TEXT,
        roll TEXT,
        branch TEXT,
        class TEXT,
        semester TEXT,
        contact TEXT
    )
    """)


    cur.execute("""
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY,
        roll TEXT,
        date TEXT,
        status TEXT
    )
    """)


    cur.execute("""
    CREATE TABLE IF NOT EXISTS academics (
        id INTEGER PRIMARY KEY,
        roll TEXT,
        subject TEXT,
        marks INTEGER
    )
    """)

    conn.commit()
    conn.close()
