import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import customtkinter



class StudentView:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Classes")
        self.root.geometry("1200x600+80+50")
        self.root.config(bg='#fff0f3')
        self.root.focus_force()

        # Title
        title = tk.Label(self.root, text="Student Classes", font=("King", 20, "bold"), bg="#ff80b4", fg="#262626")
        title.place(x=10, y=15, width=1180, height=35)

        # Variables
        self.var_student_id = tk.StringVar()

        # Widgets
        lbl_student = tk.Label(self.root, text="Enter Student ID", font=("King", 15), bg="#fff0f3")
        lbl_student.place(x=10, y=60)

        self.entry_student_id = tk.Entry(self.root, textvariable=self.var_student_id, font=("King", 15), bg="#ffffff")
        self.entry_student_id.place(x=170, y=60, width=200)

        btn_show_classes = tk.Button(self.root, text="Show Classes", font=("King", 12), bg="#ff80b4", fg="#ffffff", command=self.show_classes)
        btn_show_classes.place(x=390, y=60, width=120, height=28)

        # Initialize Treeview to display classes and teachers
        self.tree = ttk.Treeview(self.root, columns=("Class Name",  "Credit Hours", "Charges", "Description"), show='headings')
        self.tree.heading("Class Name", text="Class Name")

        self.tree.heading("Credit Hours", text="Credit Hours")
        self.tree.heading("Charges", text="Charges")
        self.tree.heading("Description", text="Description")
        self.tree.place(x=10, y=100, width=1180, height=480)

    def show_classes(self):
        student_id = self.var_student_id.get()
        if not student_id:
            messagebox.showerror("Error", "Please enter a student ID")
            return

        for row in self.tree.get_children():
            self.tree.delete(row)

        conn = sqlite3.connect('Grademaster.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT Classes.class_name, Classes.credit_hours, Classes.charges, Classes.description
            FROM Enrollments
            JOIN Classes ON Enrollments.class_id = Classes.id
            WHERE Enrollments.student_id = (
                SELECT id FROM Students WHERE student_id = ?
            )
        ''', (student_id,))
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                self.tree.insert('', 'end', values=row)
        else:
            messagebox.showinfo("Info", "No classes found for the entered student ID")
        conn.close()

if __name__ == "__main__":
    root = customtkinter.CTk()
    StudentView(root)
    root.mainloop()