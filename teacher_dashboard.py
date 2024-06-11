from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import customtkinter
from student_grade import gradeclass
from details_tcview import DetailsClass_tc
from teachercard import teachercard
from report import ReportClass

class GradeMastertc:
    def __init__(self, root):
        self.root = root
        self.root.title("Grade Master")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg='#fff0f3')
        self.root.focus_force()

        # ====icons=====
        self.logo_image = Image.open("images/Grade-Master_Logo.png")
        self.logo_image = self.logo_image.resize((70, 70), Image.LANCZOS) 
        self.logo_dash = ImageTk.PhotoImage(self.logo_image)

        # ======title==========
        title = Label(self.root, text="Grade Master", padx=10, compound=LEFT, image=self.logo_dash, font=("King", 40, "bold"), bg="#ffb3d2", fg="black")
        title.place(x=0, y=0, relwidth=1, height=70)

        # ===Menu===
        M_Frame = LabelFrame(self.root, text="Menu", font=("King", 15), bg="#fff0f3")
        M_Frame.place(x=10, y=70, width=1860, height=100)

        btn_course = Button(M_Frame, text="Course", font=("King", 20, "bold"), bg="#ffb3d2", fg="black", cursor="hand2", command=self.add_course)
        btn_course.place(x=200, y=10, width=270, height=60)

        btn_student = Button(M_Frame, text="Student", font=("King", 20, "bold"), bg="#ffb3d2", fg="black", cursor="hand2", command=self.add_student)
        btn_student.place(x=500, y=10, width=270, height=60)

        btn_profile = Button(M_Frame, text="Profile", font=("King", 20, "bold"), bg="#ffb3d2", fg="black", cursor="hand2", command=self.add_profile)
        btn_profile.place(x=800, y=10, width=270, height=60)

        btn_grade = Button(M_Frame, text="Grade", font=("King", 20, "bold"), bg="#ffb3d2", fg="black", cursor="hand2", command=self.add_grade)
        btn_grade.place(x=1100, y=10, width=270, height=60)


        btn_logout = Button(M_Frame, text="Logout", font=("King", 20, "bold"), bg="#ffb3d2", fg="black", cursor="hand2")
        btn_logout.place(x=1400, y=10, width=270, height=60)

        # ===content_windows===
        self.bg_img = Image.open("images/bg.jpg")
        self.bg_img = self.bg_img.resize((1000, 600), Image.LANCZOS) 
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img)
        self.lbl_bg.place(x=820, y=230, width=1000, height=600)

        #======update details=====
        self.lbl_course = Label(self.root, text="Total Course\n[ 0 ]", font=("King", 25), bd=10, relief="ridge", bg="#ffb3d2", fg="black").place(x=50, y=300, width=350, height=150)
        self.lbl_teacher = Label(self.root, text="Total Teacher\n[ 2 ]", font=("King", 25), bd=10, relief="ridge", bg="#ffb3d2", fg="black").place(x=430, y=300, width=350, height=150)
        self.lbl_student = Label(self.root, text="Total Student\n[ 2 ]", font=("King", 25), bd=10, relief="ridge", bg="#ffb3d2", fg="black").place(x=230, y=500, width=350, height=150)

        # ====footer=====
        footer = Label(self.root, text="Grade Master\n Contact Us:06-33xxx56", font=("times new roman", 15, "bold"), bg="#262626", fg="white")
        footer.pack(side=BOTTOM, fill=X)

    def add_course(self):
        new_root = customtkinter.CTk()
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def add_student(self):
        new_top = customtkinter.CTkToplevel(self.root)
        new_window = DetailsClass_tc(new_top)
        new_top.transient(self.root)  
        new_top.grab_set()  
        new_top.focus_force() 

    def add_grade(self):
        new_top = customtkinter.CTkToplevel(self.root)
        new_window = gradeclass(new_top)
        new_top.transient(self.root)  
        new_top.grab_set()  
        new_top.focus_force() 
    
    def add_profile(self):
        new_top = customtkinter.CTkToplevel(self.root)
        new_window = teachercard(new_top)
        new_top.transient(self.root)  
        new_top.grab_set()  
        new_top.focus_force() 

    def add_result(self):
        new_top = customtkinter.CTkToplevel(self.root)
        new_window = ReportClass(new_top)
        new_top.transient(self.root)  
        new_top.grab_set()  
        new_top.focus_force() 

if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = GradeMastertc(root)
    root.mainloop()
