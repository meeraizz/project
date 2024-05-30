from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import customtkinter

class GradeMaster:
    def __init__(self, root):
        self.root = root
        self.root.title("Grade Master")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg='#fff0f3')

        # ====icons=====
        # Open and resize the image
        self.logo_image = Image.open("images/Grade-Master_Logo.png")
        self.logo_image = self.logo_image.resize((70, 70), Image.LANCZOS)  # Use LANCZOS for high-quality downsampling
        self.logo_dash = ImageTk.PhotoImage(self.logo_image)

        # ======title==========
        title = Label(self.root, text="Grade Master", padx=10, compound=LEFT, image=self.logo_dash, font=("King", 40, "bold"), bg="#ffb3d2", fg="black")
        title.place(x=0, y=0, relwidth=1, height=70)

        # ===Menu===
        M_Frame = LabelFrame(self.root, text="Menu", font=("King", 15), bg="#fff0f3")
        M_Frame.place(x=10, y=70, width=1860, height=100)

        btn_course = Button(M_Frame, text="Course", font=("King", 20, "bold"), bg="#ffb3d2", fg="black", cursor="hand2", command=self.add_course)
        btn_course.place(x=40, y=10, width=270, height=60)

        btn_student = Button(M_Frame, text="Student", font=("King", 20, "bold"), bg="#ffb3d2", fg="black", cursor="hand2", command=self.add_student)
        btn_student.place(x=340, y=10, width=270, height=60)

        btn_teacher = Button(M_Frame, text="Teacher", font=("King", 20, "bold"), bg="#ffb3d2", fg="black", cursor="hand2")
        btn_teacher.place(x=640, y=10, width=270, height=60)

        btn_grade = Button(M_Frame, text="Grade", font=("King", 20, "bold"), bg="#ffb3d2", fg="black", cursor="hand2", command=self.add_result)
        btn_grade.place(x=940, y=10, width=270, height=60)

        btn_result = Button(M_Frame, text="Result", font=("King", 20, "bold"), bg="#ffb3d2", fg="black", cursor="hand2")
        btn_result.place(x=1240, y=10, width=270, height=60)

        btn_logout = Button(M_Frame, text="Logout", font=("King", 20, "bold"), bg="#ffb3d2", fg="black", cursor="hand2")
        btn_logout.place(x=1540, y=10, width=270, height=60)


        # ===content_windows===
        self.bg_img = Image.open("images/bg.jpg")
        self.bg_img = self.bg_img.resize((1000, 600), Image.LANCZOS) 
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img)
        self.lbl_bg.place(x=820, y=190, width=1000, height=600)


        
        # ====footer=====
        footer = Label(self.root, text="Grade Master\n Contact Us:06-33xxx56", font=("times new roman", 15, "bold"), bg="#262626", fg="white")
        footer.pack(side=BOTTOM, fill=X)

    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = StudentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ResultClass(self.new_win)

if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = GradeMaster(root)
    root.mainloop()
