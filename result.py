from tkinter import *
from PIL import Image, ImageTk    #pip install pillow
from tkinter import ttk,messagebox
import sqlite3

class ResultClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Grade Master")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        #=====title======
        title=Label(self.root,text="Add Student Results", font=("times new roman",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=45)
        #=====widgets=====
        lbl_select=Label(self.root,text="Select Student",font=("times new roman",20,"bold"),bg="white").place(x=50,y=100)
        lbl_name=Label(self.root,text="Name",font=("times new roman",20,"bold"),bg="white").place(x=50,y=160)
        lbl_course=Label(self.root,text="Course",font=("times new roman",20,"bold"),bg="white").place(x=50,y=220)
        lbl_marks_ob=Label(self.root,text="Marks Obtained",font=("times new roman",20,"bold"),bg="white").place(x=50,y=280)
        lbl_full_marks=Label(self.root,text="Select Student",font=("times new roman",20,"bold"),bg="white").place(x=50,y=340)

if __name__=="__main__":
    root=Tk()
    obj=ResultClass(root)
    root.mainloop()    