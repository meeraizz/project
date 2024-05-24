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


        # Title
        title = Label(self.root, text="Teacher Profile", font=("times new roman", 20, "bold"), bg="pink", fg="#262626").place(x=10, y=15, width=780, height=50)



if __name__ == "__main__":
    root = Tk()
    obj = TeacherProfile(root)
    root.mainloop()