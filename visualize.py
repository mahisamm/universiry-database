import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def show_attendance_pie(roll):
    conn = sqlite3.connect("student_data.db")
    df = pd.read_sql_query("SELECT status FROM attendance WHERE roll=?", conn, params=(roll,))
    plt.title(f"Attendance Pie for Roll: {roll}")
    df['status'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
    plt.ylabel("")
    plt.show()

def show_marks_bar(roll):
    conn = sqlite3.connect("student_data.db")
    df = pd.read_sql_query("SELECT subject, marks FROM academics WHERE roll=?", conn, params=(roll,))
    sns.barplot(data=df, x="subject", y="marks")
    plt.title(f"Marks by Subject for Roll: {roll}")
    plt.ylim(0, 100)
    plt.xticks(rotation=45)
    plt.show()
