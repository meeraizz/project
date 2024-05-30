from tkinter import *
from PIL import Image, ImageTk    #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
import customtkinter

class ReportClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Grade Master")
        self.root.geometry("1000x400+60+150")
        self.root.config(bg="#fff0f3")
        self.root.focus_force()

        # Create a main frame to contain all widgets
        self.main_frame = Frame(self.root, bg="#fff0f3")
        self.main_frame.pack(fill=BOTH, expand=True)         

        # Call method to create and layout all widgets
        self.create_widgets()

    def create_widgets(self):
        #=====title======
        title=Label(self.main_frame, text="View Student Results", font=("consolas",23,"bold"), bg="#FFB3D2", fg="black")
        title.pack(fill=X)  # Fill the width of the main frame

        #======search======
        self.var_search=StringVar()

        lbl_search=Label(self.root,text="Search by ID No.", font=("consolas", 20, "bold"), bg="#fff0f3").place(x=280,y=100)
        txt_search=Entry(self.root,textvariable=self.var_search, font=("consolas", 20), bg="lightyellow").place(x=530,y=100,width=170)
        btn_search=Button(self.root,text="Search",font=("consolas",15,"bold"),bg="#03a9f4",fg="#fff0f3",cursor="hand2").place(x=720,y=100,width=100,height=35)
        btn_clear=Button(self.root,text="Clear",font=("consolas",15,"bold"),bg="#F19CBB",fg="#fff0f3",cursor="hand2").place(x=840,y=100,width=100,height=35)


if __name__=="__main__":
    root=customtkinter.CTk()
    obj=ReportClass(root)
    root.mainloop()        