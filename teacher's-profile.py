from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3


class TeacherProfile:
    def __init__(self, root):
        self.root = root
        self.root.title("Teacher Profile")
        self.root.geometry("800x600+200+100")
        self.root.config(bg='white')
        self.root.focus_force()

        # Variables
        self.var_teacher_id = StringVar()
        self.var_teacher_name = StringVar()
        self.var_teacher_email = StringVar()
        self.var_teacher_contact = StringVar()
        self.course_list = []

        # Title
        title = Label(self.root, text="Teacher Profile", font=("times new roman", 20, "bold"), bg="pink", fg="#262626").place(x=10, y=15, width=780, height=50)

        # Widgets
        lbl_select = Label(self.root, text="Select Teacher", font=("times new roman", 20, "bold"), bg="white").place(x=50, y=100)
        
        self.txt_teacher = ttk.Combobox(self.root, textvariable=self.var_teacher_id, font=("times new roman", 15, "bold"), state='readonly', justify=CENTER)
        self.txt_teacher.place(x=250, y=100, width=200)
        self.txt_teacher.set("Select")


if __name__ == "__main__":
    root = Tk()
    obj = TeacherProfile(root)
    root.mainloop()