
import sqlite3

def add_student(name, roll, branch, class_, semester, contact):
    conn = sqlite3.connect("student_data.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO student VALUES (NULL,?,?,?,?,?,?)",
                (name, roll, branch, class_, semester, contact))
    conn.commit()
    conn.close()

def view_students():
    conn = sqlite3.connect("student_data.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    conn.close()
    return rows
