from tkinter import *
from PIL import Image, ImageTk    #pip install pillow
from tkinter import ttk,messagebox
import sqlite3

class DetailsClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Grade Master")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        #=====title======
        title=Label(self.root,text="Manage Student Details", font=("times new roman",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)

        #=====variables====
        self.var_roll=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()

        #=====widgets======
        lbl_roll=Label(self.root,text="Roll No.", font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)                     
        lbl_email=Label(self.root,text="Email",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=140)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=180)

        #====entry fields====
        self.txt_roll=Entry(self.root,textvariable=self.var_roll,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_roll.place(x=150,y=60,width=200)
        txt_duration=Entry(self.root,textvariable=self.var_duration,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=100,width=200)
        txt_charges=Entry(self.root,textvariable=self.var_charges,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=10,y=140,width=200)
        self.txt_description=Text(self.root,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_description.place(x=150,y=180,width=500,height=130)








if __name__=="__main__":
    root=Tk()
    obj=DetailsClass(root)
    root.mainloop()        