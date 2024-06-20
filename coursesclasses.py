import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import customtkinter

class ManageCourse:
    def __init__(self, root):
        self.root = root
        self.root.title("Course Enrollment")
        self.root.geometry("1200x750+50+200")
        self.root.config(bg='#fff0f3')
        self.root.focus_force()

        # Title
        title = tk.Label(self.root, text="Manage Course Details", font=("King", 30, "bold"), bg="#ff80b4", fg="#262626")
        title.place(x=10, y=15, width=1960, height=70)

        # Course ID (Hidden)
        self.var_id = tk.IntVar()

        # Course Name
        lbl_name = tk.Label(self.root, text="Course Name", font=("King", 20), bg="#fff0f3")
        lbl_name.place(x=200, y=150)
        self.var_name = tk.StringVar()
        self.txt_name = tk.Entry(self.root, textvariable=self.var_name, font=("King", 20), bg="#ffffff")
        self.txt_name.place(x=400, y=150, width=200)

        # Credit Hour
        lbl_credit_hours = tk.Label(self.root, text="Credit Hour", font=("King", 20), bg="#fff0f3")
        lbl_credit_hours.place(x=200, y=210)
        self.var_credit_hours = tk.IntVar()
        self.txt_credit_hours = tk.Entry(self.root, textvariable=self.var_credit_hours, font=("King", 20), bg="#ffffff")
        self.txt_credit_hours.place(x=400, y=210, width=200)

        # Charges
        lbl_charges = tk.Label(self.root, text="Charges", font=("King", 20), bg="#fff0f3")
        lbl_charges.place(x=200, y=290)
        self.var_charges = tk.StringVar()
        self.txt_charges = tk.Entry(self.root, textvariable=self.var_charges, font=("King", 20), bg="#ffffff")
        self.txt_charges.place(x=400, y=290, width=200)

        # Description
        lbl_description = tk.Label(self.root, text="Description", font=("King", 20), bg="#fff0f3")
        lbl_description.place(x=200, y=370)
        self.var_description = tk.StringVar()
        self.txt_description = tk.Entry(self.root, textvariable=self.var_description, font=("King", 20), bg="#ffffff")
        self.txt_description.place(x=400, y=370, width=500, height=100)

        # Buttons
        btn_save = tk.Button(self.root, text="Save", font=("King", 15), bg="#ff80b4", fg="black", command=self.save_course)
        btn_save.place(x=400, y=500, width=110, height=40)

        btn_update = tk.Button(self.root, text="Update", font=("King", 15), bg="#e0d2ef", fg="black", command=self.update_course)
        btn_update.place(x=520, y=500, width=110, height=40)

        btn_delete = tk.Button(self.root, text="Delete", font=("King", 15), bg="#ff80b4", fg="black", command=self.delete_course)
        btn_delete.place(x=640, y=500, width=110, height=40)

        btn_clear = tk.Button(self.root, text="Clear", font=("King", 15), bg="#e0d2ef", fg="black", command=self.clear_fields)
        btn_clear.place(x=760, y=500, width=110, height=40)

        # Search
        lbl_search = tk.Label(self.root, text="Search by Course Name", font=("King", 20), bg="#fff0f3")
        lbl_search.place(x=950, y=150)
        self.var_search = tk.StringVar()
        self.txt_search = tk.Entry(self.root, textvariable=self.var_search, font=("King", 15), bg="#ffffff")
        self.txt_search.place(x=1300, y=150, width=200)

        btn_search = tk.Button(self.root, text="Search", font=("King", 15), bg="#ff80b4", fg="black", command=self.search_course)
        btn_search.place(x=1550, y=150, width=80, height=28)


        self.course_tree = ttk.Treeview(self.root, columns=("id", "name", "credit_hour", "charges", "description"), show='headings')
        self.course_tree.heading("id", text="Course ID")
        self.course_tree.heading("name", text="Course Name")
        self.course_tree.heading("credit_hour", text="Credit Hour")
        self.course_tree.heading("charges", text="Charges")
        self.course_tree.heading("description", text="Description")
        self.course_tree.column("id", width=80)
        self.course_tree.column("name", width=200)
        self.course_tree.column("credit_hour", width=100)
        self.course_tree.column("charges", width=100)
        self.course_tree.column("description", width=300)
        self.course_tree.place(x=950, y=200, width=800, height=600)
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

        self.execute_db("INSERT INTO Courses (course_name, credit_hour, charges, description) VALUES (?, ?, ?, ?)",
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

        self.execute_db("UPDATE Courses SET course_name=?, credit_hour=?, charges=?, description=? WHERE course_id=?",
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

        self.execute_db("DELETE FROM Courses WHERE course_id=?", (course_id,))
        
        messagebox.showinfo("Success", "Course deleted successfully!")
        self.load_course()
        self.clear_fields()

    def clear_fields(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_credit_hours.set("")
        self.var_charges.set("")
        self.var_description.set("")
        self.var_search.set("")
        self.course_tree.selection_remove(self.course_tree.selection())

    def search_course(self):
            name = self.var_search.get()
            conn = sqlite3.connect('Grademaster.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Courses WHERE course_name LIKE ?", ('%' + name + '%',))
            rows = cursor.fetchall()
            self.course_tree.delete(*self.course_tree.get_children())
            for row in rows:
                self.course_tree.insert('', 'end', values=row)
            conn.close()

    def load_course(self):
        self.course_tree.delete(*self.course_tree.get_children())
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
        self.var_id.set(course_data[0])
        self.var_name.set(course_data[1])
        self.var_credit_hours.set(course_data[2])
        self.var_charges.set(course_data[3])
        self.var_description.set(course_data[4])

if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = ManageCourse(root)
    root.mainloop()