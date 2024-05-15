from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class resultClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Grade Master")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg='white')
        self.root.focus_force()

        #===title====
        title=Label(self.root,text="Add Student Result",font=("times new roman",20,"bold"),bg="pink",fg="#262626").place(x=10,y=15,width=1260,height=50)


        #===widgets===
        lbl_select = Label(self.root, text="Select Student", font=("times new roman", 20, "bold"), bg="white").place(x=50, y=100)
        lbl_name = Label(self.root, text="Name", font=("times new roman", 20, "bold"), bg="white").place(x=50, y=160)
        lbl_course = Label(self.root, text="Course", font=("times new roman", 20, "bold"), bg="white").place(x=50, y=220)
        lbl_marks_obtained = Label(self.root, text="Marks Obtained", font=("times new roman", 20, "bold"), bg="white").place(x=50, y=280)
        lbl_full_marks = Label(self.root, text="Full Marks", font=("times new roman", 20, "bold"), bg="white").place(x=50, y=340)





















if __name__=="__main__":
    root=Tk()
    obj=resultClass(root)
    root.mainloop()