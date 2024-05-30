from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class GradeMaster:
    def __init__(self,root):
        self.root=root
        self.root.title("Grade Master")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg='white')

if __name__=="__main__":
    root=Tk()
    obj=GradeMaster(root)
    root.mainloop()