import sqlite3
import tkinter as tk
import tkinter as ttk
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

def load_student_classes():
    student_id = entry_student_id.get()
    if student_id:
        conn = sqlite3.connect('Grademaster.db')
        cursor = conn.cursor()
        
        query = '''SELECT Classes.class_name, Courses.course_name, Classes.lecturer_name
                   FROM Enrollments
                   JOIN Students ON Enrollments.student_id = Students.id
                   JOIN Classes ON Enrollments.class_id = Classes.id
                   JOIN Courses ON Classes.course_id = Courses.id
                   WHERE Students.student_id = ?'''
        
        cursor.execute(query, (student_id,))
        rows = cursor.fetchall()
        
        for row in tree.get_children():
            tree.delete(row)
        
        for row in rows:
            tree.insert("", "end", values=row)
        
        conn.close()
    else:
        messagebox.showerror("Error", "Student ID cannot be empty!")

# Initialize the Tkinter window
root = tk.Tk()
root.title("Student View - Enrolled Classes")

# Student ID Entry
tk.Label(root, text="Student ID").grid(row=0, column=0)
entry_student_id = tk.Entry(root)
entry_student_id.grid(row=0, column=1)
tk.Button(root, text="View Classes", command=load_student_classes).grid(row=0, column=2)

# Classes List
tree = ttk.Treeview(root, columns=("Class Name", "Course Name", "Lecturer Name"), show="headings")
tree.heading("Class Name", text="Class Name")
tree.heading("Course Name", text="Course Name")
tree.heading("Lecturer Name", text="Lecturer Name")
tree.grid(row=1, column=0, columnspan=3)

# Start the Tkinter main loop
root.mainloop()
