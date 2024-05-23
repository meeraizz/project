from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class resultClass:
    def __init__(self,root):
        self.root = root
        self.root.title("Grade Master")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg='white')
        self.root.focus_force()

        #===title====
        title = Label(self.root,text="Add Student Result",font =("times new roman",20,"bold"),bg ="pink",fg ="#262626").place(x=10,y=15,width=1260,height=50)

        #====variables====
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_full_marks = StringVar()
        self.roll_list = []
        

        #===widgets===
        lbl_select = Label(self.root, text="Select Student", font=("times new roman", 20, "bold"), bg="white").place(x=50, y=100)
        lbl_name = Label(self.root, text="Name", font=("times new roman", 20, "bold"), bg="white").place(x=50, y=160)
        lbl_course = Label(self.root, text="Course", font=("times new roman", 20, "bold"), bg="white").place(x=50, y=220)
        lbl_marks_obtained = Label(self.root, text="Marks Obtained", font=("times new roman", 20, "bold"), bg="white").place(x=50, y=280)
        lbl_full_marks = Label(self.root, text="Full Marks", font=("times new roman", 20, "bold"), bg="white").place(x=50, y=340)

        self.txt_student = ttk.Combobox(self.root, textvariable=self.var_roll, values=self.roll_list, font=("times new roman", 15, "bold"), state='readonly', justify=CENTER)
        self.txt_student.place(x=280,y=100,width=200)
        self.txt_student.set("Select")
        btn_search=Button(self.root,text='Search',font=("times new roman",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2").place(x=500,y=100,width=100,height=28)

        txt_name = Entry(self.root,textvariable=self.var_name,font=("times new roman",20,"bold"),bg="lightyellow",state='readonly').place(x=280,y=160,width=320)
        txt_course = Entry(self.root,textvariable=self.var_course,font=("times new roman",20,"bold"),bg="lightyellow",state='readonly').place(x=280,y=220,width=320)
        txt_marks = Entry(self.root,textvariable=self.var_marks,font=("times new roman",20,"bold"),bg="lightyellow").place(x=280,y=280,width=320)
        txt_full_marks = Entry(self.root,textvariable=self.var_full_marks,font=("times new roman",20,"bold"),bg="lightyellow").place(x=280,y=340,width=320)

        #=====button======
        btn_add = Button(self.root,text="Submit",font=("times new roman",15),bg="lightgreen",activebackground="lightgreen",cursor="hand2").place(x=300,y=420,width=120,height=35)
        btn_add = Button(self.root,text="Clear",font=("times new roman",15),bg="lightgrey",activebackground="lightgrey",cursor="hand2").place(x=430,y=420,width=120,height=35)

        #==========================================================
    def fetch_roll(self):
        conn = sqlite3.connect(database="GradeMaster.db")
        cur = conn.cursor()
        try:
            cur.execute("SELECT roll FROM student")
            rows = cur.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.roll_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    def search(self):
        conn = sqlite3.connect(database="GradeMaster.db")
        cur = conn.cursor()
        try:
            cur.execute("SELECT name, course FROM student WHERE roll =?", (self.var_roll.get(),))
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
            cur.execute("SELECT * FROM result WHERE roll=? AND course=?", (self.var_roll.get(), self.var_course.get()))
            row = cur.fetchone()
            if row is not None:
                messagebox.showerror("Error", "Result already present", parent=self.root)
            else:
                per = (int(self.var_marks.get()) * 100 / int(self.var_full_marks.get()))
                cur.execute("INSERT INTO result (roll, name, course, marks_ob, full_marks, per) VALUES (?, ?, ?, ?, ?, ?)", (
                    self.var_roll.get(),
                    self.var_name.get(),
                    self.var_course.get(),
                    self.var_marks.get(),
                    self.var_full_marks.get(),
                    str(per)
                ))
                conn.commit()
                messagebox.showinfo("Success", "Result Added Successfully", parent=self.root)
                self.show()
    except Exception as ex:
        messagebox.showerror("Error", f"Error due to {str(ex)}")














if __name__=="__main__":
    root = Tk()
    obj = resultClass(root)
    root.mainloop()