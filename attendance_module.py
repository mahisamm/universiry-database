# attendance_module.py
import sqlite3
from datetime import date

def mark_attendance(roll, status):
    conn = sqlite3.connect("student_data.db")
    cur = conn.cursor()
    today = str(date.today())
    cur.execute("INSERT INTO attendance VALUES (NULL,?,?,?)", (roll, today, status))
    conn.commit()
    conn.close()

def get_attendance_by_roll(roll):
    conn = sqlite3.connect("student_data.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM attendance WHERE roll=?", (roll,))
    rows = cur.fetchall()
    conn.close()
    return rows
