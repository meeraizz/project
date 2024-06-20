import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
import customtkinter

class StudentView:
    def __init__(self, root, student_id):
        self.root = root
        self.student_id = student_id
        self.root.title("Student Courses")
        self.root.geometry("800x600+200+100")
        self.root.config(bg='#fff0f3')
        self.root.focus_force()

        # Title
        title = tk.Label(self.root, text="Student Courses", font=("King", 30, "bold"), bg="#ff80b4", fg="#262626")
        title.place(x=0, y=10, width=800, height=70)

        # Variables
        self.var_student_id = tk.StringVar(value=student_id)
        self.var_course = tk.StringVar()

        # Widgets
        lbl_student = tk.Label(self.root, text="Student ID", font=("king", 20, "bold"), bg="#fff0f3")
        lbl_student.place(x=50, y=150)

        self.entry_student_id = tk.Entry(self.root, textvariable=self.var_student_id, font=("king", 20, "bold"), justify=tk.CENTER, state='readonly')
        self.entry_student_id.place(x=300, y=150, width=300, height=45)

        # Course Enrollment Section
        lbl_course = tk.Label(self.root, text="Select Course", font=("king", 20, "bold"), bg="#fff0f3")
        lbl_course.place(x=50, y=220)

        self.combo_course = ttk.Combobox(self.root, textvariable=self.var_course, font=("king", 20, "bold"), state="readonly")
        self.combo_course.place(x=300, y=220, width=300, height=45)
        self.load_courses()

        btn_enroll = tk.Button(self.root, text="Enroll", font=("King", 20), bg="#e0d2ef", activebackground="lightgreen", cursor="hand2", command=self.enroll_course)
        btn_enroll.place(x=620, y=220, width=150, height=45)

        # Initialize Treeview to display enrolled courses
        self.tree = ttk.Treeview(self.root, columns=("Student ID", "Course Name"), show='headings')
        self.tree.heading("Student ID", text="Student ID")
        self.tree.heading("Course Name", text="Course Name")
        self.tree.place(x=50, y=300, width=700, height=250)

        # Show enrolled courses on initialization
        self.show_courses()

    def load_courses(self):
        conn = sqlite3.connect('GradeMaster.db')
        cursor = conn.cursor()
        cursor.execute("SELECT course_name FROM Courses")
        courses = cursor.fetchall()
        conn.close()
        self.combo_course['values'] = [course[0] for course in courses]

    def show_courses(self):
        student_id = self.var_student_id.get()
        if not student_id:
            messagebox.showerror("Error", "Student ID not available")
            return

        for row in self.tree.get_children():
            self.tree.delete(row)

        conn = sqlite3.connect('GradeMaster.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT student.id, Courses.course_name
            FROM Enrollments
            JOIN student ON Enrollments.student_id = student.id
            JOIN Courses ON Enrollments.cid = Courses.cid
            WHERE student.id = ?
        ''', (student_id,))
        rows = cursor.fetchall()
        conn.close()

        if rows:
            for row in rows:
                self.tree.insert('', 'end', values=row)



    def enroll_course(self):
        student_id = self.var_student_id.get()
        course_name = self.var_course.get()
        if not student_id:
            messagebox.showerror("Error", "Student ID not available")
            return
        if not course_name:
            messagebox.showerror("Error", "Please select a course")
            return

        conn = sqlite3.connect('GradeMaster.db')
        cursor = conn.cursor()

        try:
            # Check if student ID is valid
            cursor.execute("SELECT id FROM student WHERE id = ?", (student_id,))
            student = cursor.fetchone()
            if not student:
                messagebox.showerror("Error", "Invalid Student ID")
                return
            student_id = student[0]

            # Get the course ID from the course name
            cursor.execute("SELECT cid FROM Courses WHERE course_name = ?", (course_name,))
            course = cursor.fetchone()
            if not course:
                messagebox.showerror("Error", "Invalid Course")
                return
            course_id = course[0]

            # Check if the student is already enrolled in the course
            cursor.execute("SELECT * FROM Enrollments WHERE student_id = ? AND cid = ?", (student_id, course_id))
            enrollment = cursor.fetchone()
            if enrollment:
                messagebox.showinfo("Info", "Student already enrolled in this course")
            else:
                # Enroll the student in the course
                cursor.execute("INSERT INTO Enrollments (student_id, cid) VALUES (?, ?)", (student_id, course_id))
                conn.commit()
                messagebox.showinfo("Success", "Enrollment successful")

            # Update the displayed courses
            self.show_courses()

        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))

        finally:
            conn.close()

if __name__ == "__main__":
    root = customtkinter.CTk()
    StudentView(root, student_id=any)
    root.mainloop()
