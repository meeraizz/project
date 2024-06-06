import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
import customtkinter

class StudentView:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Classes and Teachers")
        self.root.geometry("800x600+200+100")
        self.root.config(bg='#fff0f3')
        self.root.focus_force()

        # Title
        title = tk.Label(self.root, text="Student Classes and Teachers", font=("King", 30, "bold"), bg="#ff80b4", fg="#262626").place(x=0, y=10, width=800, height=70)

        # Variables
        self.var_student_id = tk.StringVar()

        # Widgets
        lbl_student = tk.Label(self.root, text="Enter Student ID", font=("king", 20, "bold"), bg="#fff0f3").place(x=50, y=150)
        self.entry_student_id = tk.Entry(self.root, textvariable=self.var_student_id, font=("king", 20, "bold"), justify=tk.CENTER)
        self.entry_student_id.place(x=300, y=150, width=300, height=45)

        btn_show_classes = tk.Button(self.root, text="Show Classes", font=("King", 20), bg="#e0d2ef", activebackground="lightgreen", cursor="hand2", command=self.show_classes).place(x=300, y=220, width=200, height=45)

        # Initialize Treeview to display classes and teachers
        self.tree = ttk.Treeview(self.root, columns=("Class Name", "Teacher Name"), show='headings')
        self.tree.heading("Class Name", text="Class Name")
        self.tree.heading("Teacher Name", text="Teacher Name")
        self.tree.place(x=50, y=300, width=700, height=250)

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
            SELECT Classes.class_name, Classes.teacher_name
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
