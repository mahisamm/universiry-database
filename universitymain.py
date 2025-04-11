# main.py
from universitydatabase import connect
from student_module import add_student, view_students
from attendance_module import mark_attendance, get_attendance_by_roll
from academics_module import add_marks, get_marks_by_roll
from visualize import show_attendance_pie, show_marks_bar

connect()  # Initialize tables

while True:
    print("\n===== University Student System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Mark Attendance")
    print("4. View Attendance")
    print("5. Add Marks")
    print("6. View Marks")
    print("7. Visualize Attendance (Pie)")
    print("8. Visualize Marks (Bar)")
    print("9. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Name: ")
        roll = input("Roll No: ")
        branch = input("Branch: ")
        class_ = input("Class: ")
        semester = input("Semester: ")
        contact = input("Contact: ")
        add_student(name, roll, branch, class_, semester, contact)

    elif choice == '2':
        for s in view_students():
            print(s)

    elif choice == '3':
        roll = input("Roll No: ")
        status = input("Status (Present/Absent): ")
        mark_attendance(roll, status)

    elif choice == '4':
        roll = input("Roll No: ")
        for a in get_attendance_by_roll(roll):
            print(a)

    elif choice == '5':
        roll = input("Roll No: ")
        subject = input("Subject: ")
        marks = int(input("Marks: "))
        add_marks(roll, subject, marks)

    elif choice == '6':
        roll = input("Roll No: ")
        for m in get_marks_by_roll(roll):
            print(m)

    elif choice == '7':
        roll = input("Roll No: ")
        show_attendance_pie(roll)

    elif choice == '8':
        roll = input("Roll No: ")
        show_marks_bar(roll)

    elif choice == '9':
        break

    else:
        print("Invalid choice!")
