import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk


def create_db():
    conn = sqlite3.connect('Grademaster.db')
    cursor = conn.cursor()
   
    cursor.execute('''CREATE TABLE IF NOT EXISTS Courses (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      course_name TEXT NOT NULL)''')
   
    cursor.execute('''CREATE TABLE IF NOT EXISTS Classes (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      class_name TEXT NOT NULL,
                      course_id INTEGER,
                      lecturer_name TEXT NOT NULL,
                      FOREIGN KEY (course_id) REFERENCES Courses (id))''')
   
    cursor.execute('''CREATE TABLE IF NOT EXISTS Students (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      student_id TEXT NOT NULL,
                      student_name TEXT NOT NULL)''')
   
    cursor.execute('''CREATE TABLE IF NOT EXISTS Enrollments (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      student_id INTEGER,
                      class_id INTEGER,
                      FOREIGN KEY (student_id) REFERENCES Students (id),
                      FOREIGN KEY (class_id) REFERENCES Classes (id))''')
   
    conn.commit()
    conn.close()


create_db()


# GUI functions
def add_course():
    course_name = entry_course_name.get()
    if course_name:
        conn = sqlite3.connect('Grademaster.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Courses (course_name) VALUES (?)', (course_name,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Course added successfully!")
        load_courses()  # Refresh the course list
    else:
        messagebox.showerror("Error", "Course name cannot be empty!")


def enroll_student():
    student_id = entry_student_id.get()
    class_id = combo_classes.get().split(":")[0]
    if student_id and class_id:
        conn = sqlite3.connect('Grademaster.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM Students WHERE student_id = ?', (student_id,))
        student = cursor.fetchone()
        if student:
            cursor.execute('INSERT INTO Enrollments (student_id, class_id) VALUES (?, ?)',
                           (student[0], class_id))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Student enrolled successfully!")
        else:
            messagebox.showerror("Error", "Student ID not found!")
    else:
        messagebox.showerror("Error", "All fields must be filled!")


def load_courses():
    conn = sqlite3.connect('Grademaster.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, course_name FROM Courses')
    rows = cursor.fetchall()
    courses = [f"{row[0]}: {row[1]}" for row in rows]
    conn.close()


# Initialize the Tkinter window
root = tk.Tk()
root.title("Lecturer View - Manage Courses")


# Course Entry
tk.Label(root, text="Course Name").grid(row=0, column=0)
entry_course_name = tk.Entry(root)
entry_course_name.grid(row=0, column=1)
tk.Button(root, text="Add Course", command=add_course).grid(row=0, column=2)


# Enrollment Entry
tk.Label(root, text="Student ID").grid(row=2, column=0)
entry_student_id = tk.Entry(root)
entry_student_id.grid(row=2, column=1)
tk.Button(root, text="Enroll Student", command=enroll_student).grid(row=2, column=4)


# Load initial data
load_courses()


# Start the Tkinter main loop
root.mainloop()

