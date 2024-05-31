from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
import customtkinter


class gradeclass:
    def __init__(self, root):
        self.root = root
        self.root.title("Grade Master")
        self.root.geometry("1500x700+80+170")
        self.root.config(bg='#fff0f3')
        self.root.focus_force()

        # ===title====
        title = Label(self.root, text="Add Student Result", font=("King", 30, "bold"), bg="#ff80b4", fg="#262626").place(x=0, y=10, width=1960, height=70)

        # ====variables====
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_full_marks = StringVar()
        self.id_list = []
        self.fetch_id()

        # ===widgets===
        lbl_select = Label(self.root, text="Select Student", font=("times new roman", 25, "bold"), bg="#fff0f3").place(x=600, y=150)
        lbl_name = Label(self.root, text="Name", font=("times new roman", 25, "bold"), bg="#fff0f3").place(x=600, y=230)
        lbl_course = Label(self.root, text="Course", font=("times new roman", 25, "bold"), bg="#fff0f3").place(x=600, y=310)
        lbl_marks_obtained = Label(self.root, text="Marks Obtained", font=("times new roman", 25, "bold"), bg="#fff0f3").place(x=600, y=390)
        lbl_full_marks = Label(self.root, text="Full Marks", font=("times new roman", 25, "bold"), bg="#fff0f3").place(x=600, y=470)

        self.txt_student = ttk.Combobox(self.root, textvariable=self.var_id, values=self.id_list, font=("times new roman", 20, "bold"), state='readonly', justify=CENTER)
        self.txt_student.place(x=880,y=150, width=200, height=45)
        self.txt_student.set("Select")
        btn_search = Button(self.root, text='Search', font=("King", 20), bg="#e0d2ef", fg="black", cursor="hand2", command=self.search).place(x=1100, y=150, width=150, height=45)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("times new roman", 20, "bold"), bg="lightyellow", state='readonly').place(x=880, y=230, width=370, height=45)
        txt_course = Entry(self.root, textvariable=self.var_course, font=("times new roman", 20, "bold"), bg="lightyellow", state='readonly').place(x=880, y=310, width=370, height=45)
        txt_marks = Entry(self.root, textvariable=self.var_marks, font=("times new roman", 20, "bold"), bg="lightyellow").place(x=880, y=390, width=370, height=45)
        txt_full_marks = Entry(self.root, textvariable=self.var_full_marks, font=("times new roman", 20, "bold"), bg="lightyellow").place(x=880, y=470, width=370, height=45)

        # =====button======
        btn_add = Button(self.root, text="Submit", font=("King", 20), bg="#e0d2ef", activebackground="lightgreen", cursor="hand2", command=self.add).place(x=880, y=540, width=150, height=45)
        btn_clear = Button(self.root, text="Clear", font=("King", 20), bg="#ffb3d2", activebackground="lightgrey", cursor="hand2").place(x=1100, y=540, width=150, height=45)

        # ==========================================================

    def fetch_id(self):
        conn = sqlite3.connect(database="GradeMaster.db")
        cur = conn.cursor()
        try:
            cur.execute("SELECT id FROM student")
            rows = cur.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.id_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def search(self):
        conn = sqlite3.connect(database="GradeMaster.db")
        cur = conn.cursor()
        try:
            cur.execute("SELECT name, course FROM student WHERE id =?", (self.var_id.get(),))
            row = cur.fetchone()
            if row is not None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def add(self):
        conn = sqlite3.connect(database="GradeMaster.db")
        cur = conn.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Please first search student record", parent=self.root)
            else:
                cur.execute("SELECT * FROM grade WHERE id=? AND course=?", (self.var_id.get(), self.var_course.get()))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Result already present", parent=self.root)
                else:
                    per = (int(self.var_marks.get()) * 100 / int(self.var_full_marks.get()))
                    cur.execute("INSERT INTO grade (id, name, course, marks_obt, full_marks, per) VALUES (?, ?, ?, ?, ?, ?)", (
                        self.var_id.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks.get(),
                        self.var_full_marks.get(),
                        str(per),
                    ))
                    conn.commit()
                    messagebox.showinfo("Success", "Result Added Successfully", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = gradeclass(root)
    obj.fetch_id()  
    root.mainloop()
