from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
import customtkinter

class gradeclass:
    def __init__(self, root):
        self.root = root
        self.root.title("Grade Master")
        self.root.geometry("1200x750+50+200")
        self.root.config(bg='#fff0f3')
        self.root.focus_force()

        # ===title====
        title = Label(self.root, text="Add Student Result", font=("King", 30, "bold"), bg="#ff80b4", fg="#262626").place(x=0, y=10, width=1960, height=70)

        # ====variables====
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_course_name = StringVar()
        self.var_marks = StringVar()
        self.var_full_marks = StringVar(value="100") 
        self.id_list = []
        self.course_list = []

        # Initialize comboboxes before fetching data
        self.txt_student = ttk.Combobox(self.root, textvariable=self.var_id, values=self.id_list, font=("king", 20, "bold"), state='readonly', justify=CENTER)
        self.txt_student.place(x=880, y=150, width=200, height=45)
        self.txt_student.set("Select")

        self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course_name, values=self.course_list, font=("king", 20, "bold"), state='readonly', justify=CENTER)
        self.txt_course.place(x=880, y=310, width=370, height=45)
        self.txt_course.set("Select")

        # Fetching data after initializing comboboxes
        self.fetch_id()
        self.fetch_course()

        # ===widgets===
        lbl_select = Label(self.root, text="Select Student", font=("king", 20, "bold"), bg="#fff0f3").place(x=600, y=150)
        lbl_name = Label(self.root, text="Name", font=("king", 25, "bold"), bg="#fff0f3").place(x=600, y=230)
        lbl_course = Label(self.root, text="Select Course", font=("king", 20, "bold"), bg="#fff0f3").place(x=600, y=310)
        lbl_marks = Label(self.root, text="Marks", font=("king", 25, "bold"), bg="#fff0f3").place(x=600, y=390)

        btn_search = Button(self.root, text='Search', font=("King", 20), bg="#e0d2ef", fg="black", cursor="hand2", command=self.search).place(x=1100, y=150, width=150, height=45)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("king", 20, "bold"), bg="lightyellow", state='readonly').place(x=880, y=230, width=370, height=45)
        txt_marks = Entry(self.root, textvariable=self.var_marks, font=("king", 20, "bold"), bg="lightyellow").place(x=880, y=390, width=370, height=45)

        # =====button======
        btn_save = Button(self.root, text="Save", font=("King", 20), bg="#e0d2ef", activebackground="lightgreen", cursor="hand2", command=self.save).place(x=880, y=540, width=150, height=45)
        btn_clear = Button(self.root, text="Clear", font=("King", 20), bg="#ffb3d2", activebackground="lightgrey", cursor="hand2", command=self.clear).place(x=1100, y=540, width=150, height=45)

    def fetch_id(self):
        conn = sqlite3.connect(database="GradeMaster.db")
        cur = conn.cursor()
        try:
            cur.execute("SELECT id FROM student")
            rows = cur.fetchall()
            if rows:
                self.id_list = [row[0] for row in rows]
                self.txt_student['values'] = self.id_list
        except Exception as ex:
            messagebox.showerror("Error", f"Error fetching student IDs: {str(ex)}")
        finally:
            conn.close()

    def fetch_course(self):
        conn = sqlite3.connect(database="GradeMaster.db")
        cur = conn.cursor()
        try:
            cur.execute("SELECT course_name FROM Courses")
            rows = cur.fetchall()
            if rows:
                self.course_list = [row[0] for row in rows]
                if hasattr(self, 'txt_course'):
                    self.txt_course['values'] = self.course_list
        except Exception as ex:
            messagebox.showerror("Error", f"Error fetching courses: {str(ex)}")
        finally:
            conn.close()

    def search(self):
        conn = sqlite3.connect(database="GradeMaster.db")
        cur = conn.cursor()
        try:
            cur.execute("SELECT name FROM student WHERE id=?", (self.var_id.get(),))
            row = cur.fetchone()
            if row:
                self.var_name.set(row[0])
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error searching for student: {str(ex)}")
        finally:
            conn.close()

    def save(self):
        conn = sqlite3.connect(database="GradeMaster.db")
        cur = conn.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Please first search student record", parent=self.root)
            else:
                cur.execute("SELECT * FROM grade WHERE id=? AND course=?", (self.var_id.get(), self.var_course_name.get()))
                row = cur.fetchone()
                if row:
                    messagebox.showerror("Error", "Result already present", parent=self.root)
                else:
                    cur.execute("INSERT INTO grade (id, name, course, marks) VALUES (?, ?, ?, ?)", (
                        self.var_id.get(),
                        self.var_name.get(),
                        self.var_course_name.get(),
                        self.var_marks.get(),
                    ))
                    conn.commit()
                    messagebox.showinfo("Success", "Result Added Successfully", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error saving result: {str(ex)}")
        finally:
            conn.close()

    def clear(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_course_name.set("")
        self.var_marks.set("")
        self.txt_student.set("Select")
        self.txt_course.set("Select")

if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = gradeclass(root)
    root.mainloop()
