from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class GradeMaster:
    def __init__(self, root):
        self.root = root
        self.root.title("Grade Master")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg='white')

        # ====icons=====
        # Open and resize the image
        self.logo_image = Image.open("images/Grade-Master_Logo.png")
        self.logo_image = self.logo_image.resize((50, 50), Image.LANCZOS)  # Use LANCZOS for high-quality downsampling
        self.logo_dash = ImageTk.PhotoImage(self.logo_image)

        # ======title==========
        title = Label(self.root, text="Grade Master", padx=10, compound=LEFT, image=self.logo_dash, font=("King", 20, "bold"), bg="#ffb3d2", fg="black")
        title.place(x=0, y=0, relwidth=1, height=50)

        # ===Menu===
        M_Frame = LabelFrame(self.root, text="Menu", font=("King", 15), bg="white")
        M_Frame.place(x=10, y=70, width=1250, height=80)

        # Calculate button width and spacing to fit within 1250 pixels
        btn_width = 150
        btn_spacing = 10
        total_width = 7 * btn_width + 6 * btn_spacing
        start_x = (1250 - total_width) // 2

        btn_course = Button(M_Frame, text="Course", font=("King", 15, "bold"), bg="#ffb3d2", fg="black", cursor="hand2", command=self.add_course)
        btn_course.place(x=start_x, y=5, width=btn_width, height=40)

        btn_student = Button(M_Frame, text="Student", font=("King", 15, "bold"), bg="#ffb3d2", fg="black", cursor="hand2", command=self.add_student)
        btn_student.place(x=start_x + (btn_width + btn_spacing) * 1, y=5, width=btn_width, height=40)

        btn_grade = Button(M_Frame, text="Grade", font=("King", 15, "bold"), bg="#ffb3d2", fg="black", cursor="hand2", command=self.add_result)
        btn_grade.place(x=start_x + (btn_width + btn_spacing) * 2, y=5, width=btn_width, height=40)

        btn_result = Button(M_Frame, text="Result", font=("King", 15, "bold"), bg="#ffb3d2", fg="black", cursor="hand2")
        btn_result.place(x=start_x + (btn_width + btn_spacing) * 3, y=5, width=btn_width, height=40)

        btn_teacher = Button(M_Frame, text="Teacher", font=("King", 15, "bold"), bg="#ffb3d2", fg="black", cursor="hand2")
        btn_teacher.place(x=start_x + (btn_width + btn_spacing) * 4, y=5, width=btn_width, height=40)

        btn_logout = Button(M_Frame, text="Logout", font=("King", 15, "bold"), bg="#ffb3d2", fg="black", cursor="hand2")
        btn_logout.place(x=start_x + (btn_width + btn_spacing) * 5, y=5, width=btn_width, height=40)

        btn_exit = Button(M_Frame, text="Exit", font=("King", 15, "bold"), bg="#ffb3d2", fg="black", cursor="hand2")
        btn_exit.place(x=start_x + (btn_width + btn_spacing) * 6, y=5, width=btn_width, height=40)

        # ===content_windows===
        self.bg_img=Image.open("images/bg.jpg")
        self.lbl_img=self.bg_img.resize((100,100),Image.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=570,y=190,width=620,height=450)

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
    root = Tk()
    obj = GradeMaster(root)
    root.mainloop()
 