import sqlite3
import tkinter as tk
from tkinter import messagebox

# Database setup
def create_db():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Courses (
                      id INTEGER PRIMARY KEY,
                      course_name TEXT NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Classes (
                      id INTEGER PRIMARY KEY,
                      class_name TEXT NOT NULL,
                      course_id INTEGER,
                      FOREIGN KEY (course_id) REFERENCES Courses (id))''')
    
    conn.commit()
    conn.close()

create_db()

# GUI functions
def add_course():
    course_name = entry_course_name.get()
    if course_name:
        conn = sqlite3.connect('school.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Courses (course_name) VALUES (?)', (course_name,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Course added successfully!")
    else:
        messagebox.showerror("Error", "Course name cannot be empty!")

def add_class():
    class_name = entry_class_name.get()
    course_id = entry_course_id.get()
    if class_name and course_id:
        conn = sqlite3.connect('school.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Classes (class_name, course_id) VALUES (?, ?)', (class_name, course_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Class added successfully!")
    else:
        messagebox.showerror("Error", "Class name and Course ID cannot be empty!")

# Initialize the Tkinter window
root = tk.Tk()
root.title("School Management")

# Course Entry
tk.Label(root, text="Course Name").grid(row=0, column=0)
entry_course_name = tk.Entry(root)
entry_course_name.grid(row=0, column=1)
tk.Button(root, text="Add Course", command=add_course).grid(row=0, column=2)

# Class Entry
tk.Label(root, text="Class Name").grid(row=1, column=0)
entry_class_name = tk.Entry(root)
entry_class_name.grid(row=1, column=1)
tk.Label(root, text="Course ID").grid(row=2, column=0)
entry_course_id = tk.Entry(root)
entry_course_id.grid(row=2, column=1)
tk.Button(root, text="Add Class", command=add_class).grid(row=2, column=2)

# Start the Tkinter main loop
root.mainloop()

