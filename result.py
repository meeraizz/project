from tkinter import *
from PIL import Image, ImageTk    #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
import customtkinter

class ResultClass:
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

if __name__=="__main__":
    root=customtkinter.CTk()
    obj=ResultClass(root)
    root.mainloop()        