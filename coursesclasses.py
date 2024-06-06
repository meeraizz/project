import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
import customtkinter

import sqlite3

def create_db():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Create table
    cursor.execute('''CREATE TABLE IF NOT EXISTS students
                      (id INTEGER PRIMARY KEY, name TEXT, grade TEXT)''')

    conn.commit()
    conn.close()

create_db()


class EnrollClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Course Enrollment")
        self.root.geometry("800x600+200+100")
        self.root.config(bg='#fff0f3')
        self.root.focus_force()

        # Title
        title = tk.Label(self.root, text="Enroll Student in Course", font=("King", 30, "bold"), bg="#ff80b4", fg="#262626").place(x=0, y=10, width=800, height=70)

        # Variables
        self.var_student_id = tk.StringVar()
        self.var_course_id = tk.StringVar()
        self.student_list = []
        self.course_list = []
        self.fetch_students()
        self.fetch_courses()

        # Widgets
        lbl_student = tk.Label(self.root, text="Select Student", font=("king", 20, "bold"), bg="#fff0f3").place(x=50, y=150)
        lbl_course = tk.Label(self.root, text="Select Course", font=("king", 20, "bold"), bg="#fff0f3").place(x=50, y=230)

        self.cmb_student = ttk.Combobox(self.root, textvariable=self.var_student_id, values=self.student_list, font=("king", 20, "bold"), state='readonly', justify=tk.CENTER)
        self.cmb_student.place(x=300, y=150, width=300, height=45)
        self.cmb_student.set("Select")

        self.cmb_course = ttk.Combobox(self.root, textvariable=self.var_course_id, values=self.course_list, font=("king", 20, "bold"), state='readonly', justify=tk.CENTER)
        self.cmb_course.place(x=300, y=230, width=300, height=45)
        self.cmb_course.set("Select")

        btn_enroll = tk.Button(self.root, text="Enroll", font=("King", 20), bg="#e0d2ef", activebackground="lightgreen", cursor="hand2", command=self.enroll_student).place(x=300, y=310, width=150, height=45)

        # Initialize Treeview to display enrollments
        self.tree = ttk.Treeview(self.root, columns=("Student ID", "Course Name"), show='headings')
        self.tree.heading("Student ID", text="Student ID")
        self.tree.heading("Course Name", text="Course Name")
        self.tree.place(x=50, y=380, width=700, height=200)

        self.load_enrollments()

    def fetch_students(self):
        conn = sqlite3.connect('Grademaster.db')
        cursor = conn.cursor()
        cursor.execute("SELECT student_id, student_name FROM Students")
        rows = cursor.fetchall()
        for row in rows:
            self.student_list.append(f"{row[0]}: {row[1]}")
        conn.close()

    def fetch_courses(self):
        conn = sqlite3.connect('Grademaster.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, course_name FROM Courses")
        rows = cursor.fetchall()
        for row in rows:
            self.course_list.append(f"{row[0]}: {row[1]}")
        conn.close()

    def enroll_student(self):
        student = self.var_student_id.get()
        course = self.var_course_id.get()
        if student == "Select" or course == "Select":
            messagebox.showerror("Error", "Please select both student and course")
            return
        student_id = student.split(":")[0]
        course_id = course.split(":")[0]

        conn = sqlite3.connect('Grademaster.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Enrollments (student_id, class_id) VALUES (?, ?)", (student_id, course_id))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Student enrolled successfully!")
        self.load_enrollments()

    def load_enrollments(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        conn = sqlite3.connect('Grademaster.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT Students.student_id, Students.student_name, Courses.id, Courses.course_name
            FROM Enrollments
            JOIN Students ON Enrollments.student_id = Students.id
            JOIN Courses ON Enrollments.class_id = Courses.id
        ''')
        rows = cursor.fetchall()
        for row in rows:
            self.tree.insert('', 'end', values=row)
        conn.close()

if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = EnrollClass(root)
    root.mainloop()

