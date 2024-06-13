import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Courses Enrollment")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg='#fff0f3')
        self.root.focus_force()

        # Title
        title = tk.Label(self.root, text="Manage Course Details",font=("Arial", 20, "bold"), bg="#ff80b4", fg="#262626").place(x=10,y=15,width=1180,height=35)

        # Course Name
        lbl_course_name = tk.Label(self.root, text="Course Name", font=("Arial", 15), bg="#fff0f3")
        lbl_course_name.place(x=10, y=60)

        self.var_course_name = tk.StringVar()
        self.txt_course_name = tk.Entry(self.root, textvariable=self.var_course_name, font=("Arial", 15), bg="#ffffff")
        self.txt_course_name.place(x=150, y=60, width=200)

        # Credit Hour
        lbl_credit_hour = tk.Label(self.root, text="Credit Hour", font=("Arial", 15), bg="#fff0f3")
        lbl_credit_hour.place(x=10, y=100)

        self.var_credit_hour = tk.StringVar()
        self.txt_credit_hour = tk.Entry(self.root, textvariable=self.var_credit_hour, font=("Arial", 15), bg="#ffffff")
        self.txt_credit_hour.place(x=150, y=100, width=200)

        # Charges
        lbl_charges = tk.Label(self.root, text="Charges", font=("Arial", 15), bg="#fff0f3")
        lbl_charges.place(x=10, y=140)

        self.var_charges = tk.StringVar()
        self.txt_charges = tk.Entry(self.root, textvariable=self.var_charges, font=("Arial", 15), bg="#ffffff")
        self.txt_charges.place(x=150, y=140, width=200)

        # Description
        lbl_description = tk.Label(self.root, text="Description", font=("Arial", 15), bg="#fff0f3")
        lbl_description.place(x=10, y=180)

        self.var_description = tk.StringVar()
        self.txt_description = tk.Entry(self.root, textvariable=self.var_description, font=("Arial", 15), bg="#ffffff")
        self.txt_description.place(x=150, y=180, width=500, height=100)

        # Buttons
        btn_save = tk.Button(self.root, text="Save", font=("Arial", 12), bg="#00c853", fg="#ffffff", command=self.save_course)
        btn_save.place(x=150, y=400, width=110, height=40)

        btn_update = tk.Button(self.root, text="Update", font=("Arial", 12), bg="#ffa000", fg="#ffffff", command=self.update_course)
        btn_update.place(x=270, y=400, width=110, height=40)

        btn_delete = tk.Button(self.root, text="Delete", font=("Arial", 12), bg="#d32f2f", fg="#ffffff", command=self.delete_course)
        btn_delete.place(x=390, y=400, width=110, height=40)

        btn_clear = tk.Button(self.root, text="Clear", font=("Arial", 12), bg="#616161", fg="#ffffff", command=self.clear_fields)
        btn_clear.place(x=510, y=400, width=110, height=40)

        # Search
        lbl_search = tk.Label(self.root, text="Course Name", font=("Arial", 15), bg="#fff0f3")
        lbl_search.place(x=720, y=60)

        self.var_search = tk.StringVar()
        self.txt_search = tk.Entry(self.root, textvariable=self.var_search, font=("Arial", 15), bg="#ffffff")
        self.txt_search.place(x=850, y=60, width=180)

        btn_search = tk.Button(self.root, text="Search", font=("Arial", 12), bg="#ff80b4", fg="#ffffff", command=self.search_course)
        btn_search.place(x=1070, y=60, width=120, height=28)

        # Treeview to display courses
        self.course_tree = ttk.Treeview(self.root, columns=("Course ID", "Course Name", "Credit Hour", "Charges", "Description"), show='headings')
        self.course_tree.heading("Course ID", text="Course ID")
        self.course_tree.heading("Course Name", text="Course Name")
        self.course_tree.heading("Credit Hour", text="Credit Hour")
        self.course_tree.heading("Charges", text="Charges")
        self.course_tree.heading("Description", text="Description")
        self.course_tree.place(x=720, y=100, width=470, height=340)

    def fetch_students(self):
        conn = sqlite3.connect('GradeMaster.db')
        cursor = conn.cursor()
        cursor.execute("SELECT student_id, student_name FROM Students")
        rows = cursor.fetchall()
        for row in rows:
            self.student_list.append(f"{row[0]}: {row[1]}")
        conn.close()

    def fetch_courses(self):
        conn = sqlite3.connect('GradeMaster.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, course_name FROM Courses")
        rows = cursor.fetchall()
        for row in self.course_tree.get_children():
            self.course_tree.delete(row)
        for row in rows:
            self.course_tree.insert('', 'end', values=row)
        conn.close()

    def enroll_student(self):
        student = self.var_student_id.get()
        course = self.var_course_id.get()
        if student == "Select" or course == "Select":
            messagebox.showerror("Error", "Please select both student and course")
            return
        student_id = student.split(":")[0]
        course_id = course.split(":")[0]

        conn = sqlite3.connect('GradeMaster.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Enrollments (student_id, class_id) VALUES (?, ?)", (student_id, course_id))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Student enrolled successfully!")
        self.load_enrollments()

    def update_course(self):
        if self.var_course_name.get() == "" or self.var_credit_hour.get() == "" or self.var_charges.get() == "" or self.var_description.get() == "":
            messagebox.showerror("Error", "All fields are required")
            return

        selected_item = self.course_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a course to update")
            return

        course_id = self.course_tree.item(selected_item)['values'][0]

        self.execute_db("UPDATE Courses SET course_name=?, credit_hour=?, charges=?, description=? WHERE id=?", 
                        (self.var_course_name.get(), self.var_credit_hour.get(), self.var_charges.get(), self.var_description.get(), course_id))
        
        messagebox.showinfo("Success", "Course updated successfully!")
        self.load_courses()

    def save_course(self):
        if self.var_course_name.get() == "" or self.var_credit_hour.get() == "" or self.var_charges.get() == "" or self.var_description.get() == "":
            messagebox.showerror("Error", "All fields are required")
            return

        self.execute_db("INSERT INTO course (course_name, credit_hour, charges, description) VALUES (?, ?, ?, ?)", 
                        (self.var_course_name.get(), self.var_credit_hour.get(), self.var_charges.get(), self.var_description.get()))
        
        messagebox.showinfo("Success", "Course added successfully!")
        self.load_courses()
        self.clear_fields()

    def delete_course(self):
        selected_item = self.course_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a course to delete")
            return

        course_id = self.course_tree.item(selected_item)['values'][0]

        self.execute_db("DELETE FROM Courses WHERE id=?", (course_id,))
        
        messagebox.showinfo("Success", "Course deleted successfully!")
        self.load_courses()
        self.clear_fields()

    def clear_fields(self):
        self.var_course_name.set("")
        self.var_credit_hour.set("")
        self.var_charges.set("")
        self.var_description.set("")
        self.var_search.set("")

    def search_course(self):
        course_name = self.var_search.get()
        conn = sqlite3.connect('Grademaster.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Courses WHERE course_name LIKE ?", ('%' + course_name + '%',))
        rows = cursor.fetchall()
        for row in self.course_tree.get_children():
            self.course_tree.delete(row)
        for row in rows:
            self.course_tree.insert('', 'end', values=row)
        conn.close()

    def load_courses(self):
        for row in self.course_tree.get_children():
            self.course_tree.delete(row)
        conn = sqlite3.connect('Grademaster.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Courses")
        rows = cursor.fetchall()
        for row in rows:
            self.course_tree.insert('', 'end', values=row)
        conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    obj = CourseClass(root)
    root.mainloop()

