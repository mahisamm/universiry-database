
import sqlite3

def add_marks(roll, subject, marks):
    conn = sqlite3.connect("student_data.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO academics VALUES (NULL,?,?,?)", (roll, subject, marks))
    conn.commit()
    conn.close()

def get_marks_by_roll(roll):
    conn = sqlite3.connect("student_data.db")
    cur = conn.cursor()
    cur.execute("SELECT subject, marks FROM academics WHERE roll=?", (roll,))
    rows = cur.fetchall()
    conn.close()
    return rows
