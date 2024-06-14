import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import customtkinter

class ManageCourse:
    def __init__(self, root):
        self.root = root
        self.root.title("course Enrollment")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg='#fff0f3')
        self.root.focus_force()

        # Title
        title = tk.Label(self.root, text="Manage Course Details", font=("King", 20, "bold"), bg="#ff80b4", fg="#262626").place(x=10, y=15, width=1180, height=35)

        # Course Name
        lbl_name = tk.Label(self.root, text="Course Name", font=("King", 15), bg="#fff0f3")
        lbl_name.place(x=10, y=60)

        self.var_name = tk.StringVar()
        self.txt_name = tk.Entry(self.root, textvariable=self.var_name, font=("King", 15), bg="#ffffff")
        self.txt_name.place(x=150, y=60, width=200)

        # Credit Hour
        lbl_credit_hours = tk.Label(self.root, text="Credit Hour", font=("King", 15), bg="#fff0f3")
        lbl_credit_hours.place(x=10, y=100)

        self.var_credit_hours = tk.StringVar()
        self.txt_credit_hours = tk.Entry(self.root, textvariable=self.var_credit_hours, font=("King", 15), bg="#ffffff")
        self.txt_credit_hours.place(x=150, y=100, width=200)

        # Charges
        lbl_charges = tk.Label(self.root, text="Charges", font=("King", 15), bg="#fff0f3")
        lbl_charges.place(x=10, y=140)

        self.var_charges = tk.StringVar()
        self.txt_charges = tk.Entry(self.root, textvariable=self.var_charges, font=("King", 15), bg="#ffffff")
        self.txt_charges.place(x=150, y=140, width=200)

        # Description
        lbl_description = tk.Label(self.root, text="Description", font=("King", 15), bg="#fff0f3")
        lbl_description.place(x=10, y=180)

        self.var_description = tk.StringVar()
        self.txt_description = tk.Entry(self.root, textvariable=self.var_description, font=("King", 15), bg="#ffffff")
        self.txt_description.place(x=150, y=180, width=500, height=100)

        # Buttons
        btn_save = tk.Button(self.root, text="Save", font=("King", 12), bg="#00c853", fg="#ffffff", command=self.save_course)
        btn_save.place(x=150, y=400, width=110, height=40)

        btn_update = tk.Button(self.root, text="Update", font=("King", 12), bg="#ffa000", fg="#ffffff", command=self.update_course)
        btn_update.place(x=270, y=400, width=110, height=40)

        btn_delete = tk.Button(self.root, text="Delete", font=("King", 12), bg="#d32f2f", fg="#ffffff", command=self.delete_course)
        btn_delete.place(x=390, y=400, width=110, height=40)

        btn_clear = tk.Button(self.root, text="Clear", font=("King", 12), bg="#616161", fg="#ffffff", command=self.clear_fields)
        btn_clear.place(x=510, y=400, width=110, height=40)

        # Search
        lbl_search = tk.Label(self.root, text="Course Name", font=("King", 15), bg="#fff0f3")
        lbl_search.place(x=720, y=60)

        self.var_search = tk.StringVar()
        self.txt_search = tk.Entry(self.root, textvariable=self.var_search, font=("King", 15), bg="#ffffff")
        self.txt_search.place(x=850, y=60, width=180)

        btn_search = tk.Button(self.root, text="Search", font=("King", 12), bg="#ff80b4", fg="#ffffff", command=self.search_course)
        btn_search.place(x=1070, y=60, width=120, height=28)

        # Treeview to display courses
        self.course_tree = ttk.Treeview(self.root, columns=("id", "name", "credit_hours", "charges", "description"), show='headings')
        self.course_tree.heading("id", text="Course ID")
        self.course_tree.heading("name", text="Course Name")
        self.course_tree.heading("credit_hours", text="Credit Hour")
        self.course_tree.heading("charges", text="Charges")
        self.course_tree.heading("description", text="Description")
        self.course_tree.column("id", width=50)
        self.course_tree.column("name", width=150)
        self.course_tree.column("credit_hours", width=100)
        self.course_tree.column("charges", width=100)
        self.course_tree.column("description", width=200)
        self.course_tree.place(x=720, y=100, width=470, height=340)
        self.course_tree.bind("<ButtonRelease-1>", self.get_selected_course)

        self.load_course()

    def execute_db(self, query, params=()):
        try:
            conn = sqlite3.connect('Grademaster.db')
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
        except Exception as e:
            print(f"Database Error: {e}")
            messagebox.showerror("Error", f"Database error: {e}")
        finally:
            conn.close()

    def save_course(self):
        if self.var_name.get() == "" or self.var_credit_hours.get() == "" or self.var_charges.get() == "" or self.var_description.get() == "":
            messagebox.showerror("Error", "All fields are required")
            return

        self.execute_db("INSERT INTO course (name, credit_hours, charges, description) VALUES (?, ?, ?, ?)",
                        (self.var_name.get(), self.var_credit_hours.get(), self.var_charges.get(), self.var_description.get()))
        
        messagebox.showinfo("Success", "Course added successfully!")
        self.load_course()
        self.clear_fields()

    def update_course(self):
        if self.var_name.get() == "" or self.var_credit_hours.get() == "" or self.var_charges.get() == "" or self.var_description.get() == "":
            messagebox.showerror("Error", "All fields are required")
            return

        selected_item = self.course_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a course to update")
            return

        course_id = self.course_tree.item(selected_item)['values'][0]

        self.execute_db("UPDATE course SET name=?, credit_hours=?, charges=?, description=? WHERE id=?",
                        (self.var_name.get(), self.var_credit_hours.get(), self.var_charges.get(), self.var_description.get(), course_id))
        
        messagebox.showinfo("Success", "Course updated successfully!")
        self.load_course()
        self.clear_fields()

    def delete_course(self):
        selected_item = self.course_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a course to delete")
            return

        course_id = self.course_tree.item(selected_item)['values'][0]

        self.execute_db("DELETE FROM course WHERE id=?", (course_id,))
        
        messagebox.showinfo("Success", "Course deleted successfully!")
        self.load_course()
        self.clear_fields()

    def clear_fields(self):
        self.var_name.set("")
        self.var_credit_hours.set("")
        self.var_charges.set("")
        self.var_description.set("")
        self.var_search.set("")

    def search_course(self):
        name = self.var_search.get()
        conn = sqlite3.connect('Grademaster.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM course WHERE name LIKE ?", ('%' + name + '%',))
        rows = cursor.fetchall()
        for row in self.course_tree.get_children():
            self.course_tree.delete(row)
        for row in rows:
            self.course_tree.insert('', 'end', values=row)
        conn.close()

    def load_course(self):
        for row in self.course_tree.get_children():
            self.course_tree.delete(row)
        conn = sqlite3.connect('Grademaster.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Courses")
        rows = cursor.fetchall()
        for row in rows:
            self.course_tree.insert('', 'end', values=row)
        conn.close()

    def get_selected_course(self, event):
        selected_item = self.course_tree.selection()
        if not selected_item:
            return
        course_data = self.course_tree.item(selected_item)['values']
        self.var_name.set(course_data[1])
        self.var_credit_hours.set(course_data[2])
        self.var_charges.set(course_data[3])
        self.var_description.set(course_data[4])

if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = ManageCourse(root)
    root.mainloop()
