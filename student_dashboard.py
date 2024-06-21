import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import customtkinter
from student_grade import gradeclass
from teacher_profile import teacherprofile
from student_details import DetailsClass
from report import ReportClass
from coursesclasses_student import StudentView
from student_card import StudentCard
from attendancereport import AttendanceReport
import os

class GradeMaster:
    def __init__(self, root, student_id):
        self.root = root
        self.student_id = student_id
        self.root.title("Grade Master")
        
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.config(bg='#fff0f3')
        self.root.focus_force()

        # ====icons=====
        self.logo_image = Image.open("images/Grade-Master_Logo.png")
        self.logo_image = self.logo_image.resize((70, 70), Image.LANCZOS) 
        self.logo_dash = ImageTk.PhotoImage(self.logo_image)

        # ======title==========
        title = Label(self.root, text="Grade Master", padx=10, compound=LEFT, image=self.logo_dash, font=("King", 30, "bold"), bg="#ffb3d2", fg="black")
        title.place(x=0, y=0, relwidth=1, height=70)

        M_Frame = LabelFrame(self.root, text="Menu", font=("King", 15), bg="#fff0f3")
        M_Frame.place(x=10, y=70, width=1860, height=100)

        btn_course = Button(M_Frame, text="Course", font=("King", 20, "bold"), bg="#ffb3d2", fg="black", cursor="hand2", command=self.add_course)
        btn_course.place(x=50, y=10, width=270, height=60)

        btn_student = Button(M_Frame, text="Profile", font=("King", 20, "bold"), bg="#ffb3d2", fg="black", cursor="hand2", command=self.add_student)
        btn_student.place(x=350, y=10, width=270, height=60)

        btn_profile = Button(M_Frame, text="Teacher", font=("King", 20, "bold"), bg="#ffb3d2", fg="black", cursor="hand2", command=self.add_teacher)
        btn_profile.place(x=650, y=10, width=270, height=60)

        btn_grade = Button(M_Frame, text="Result", font=("King", 20, "bold"), bg="#ffb3d2", fg="black", cursor="hand2", command=self.add_result)
        btn_grade.place(x=950, y=10, width=270, height=60)

        btn_attendance = Button(M_Frame, text="Attendance", font=("King", 20, "bold"), bg="#ffb3d2", fg="black", cursor="hand2", command=self.attendance)
        btn_attendance.place(x=1250, y=10, width=270, height=60)

        btn_logout = Button(M_Frame, text="Logout", font=("King", 20, "bold"), bg="#ffb3d2", fg="black", cursor="hand2", command=self.logout)
        btn_logout.place(x=1550, y=10, width=270, height=60)

        self.bg_img = Image.open("images/bg.jpg")
        self.bg_img = self.bg_img.resize((1000, 600), Image.LANCZOS) 
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg = Label(self.root, image=self.bg_img)
        self.lbl_bg.place(x=820, y=230, width=1000, height=600)

        self.lbl_course = Label(self.root, text="Total Course\n[ 0 ]", font=("King", 20), bd=10, relief="ridge", bg="#ffb3d2", fg="black")
        self.lbl_course.place(x=50, y=300, width=350, height=150)
        self.lbl_teacher = Label(self.root, text="Total Teacher\n[ 0 ]", font=("King", 20), bd=10, relief="ridge", bg="#ffb3d2", fg="black")
        self.lbl_teacher.place(x=430, y=300, width=350, height=150)
        self.lbl_student = Label(self.root, text="Total Student\n[ 0 ]", font=("King", 20), bd=10, relief="ridge", bg="#ffb3d2", fg="black")
        self.lbl_student.place(x=230, y=500, width=350, height=150)
        
        self.update_counts()
        
        self.root.after(5000, self.update_counts)

    def fetch_total_courses(self):
        conn = sqlite3.connect(database="GradeMaster.db")
        cur = conn.cursor()
        try:
            cur.execute("SELECT COUNT(*) FROM Courses")
            total_courses = cur.fetchone()[0]
            return total_courses
        except Exception as ex:
            messagebox.showerror("Error", f"Error fetching total courses: {str(ex)}")
            return 0
        finally:
            conn.close()

    def fetch_total_teachers(self):
        conn = sqlite3.connect(database="GradeMaster.db")
        cur = conn.cursor()
        try:
            cur.execute("SELECT COUNT(*) FROM teacher")
            total_teachers = cur.fetchone()[0]
            return total_teachers
        except Exception as ex:
            messagebox.showerror("Error", f"Error fetching total teachers: {str(ex)}")
            return 0
        finally:
            conn.close()

    def fetch_total_students(self):
        conn = sqlite3.connect(database="GradeMaster.db")
        cur = conn.cursor()
        try:
            cur.execute("SELECT COUNT(*) FROM Student")
            total_students = cur.fetchone()[0]
            return total_students
        except Exception as ex:
            messagebox.showerror("Error", f"Error fetching total students: {str(ex)}")
            return 0
        finally:
            conn.close()

    def update_counts(self):
        total_courses = self.fetch_total_courses()
        total_teachers = self.fetch_total_teachers()
        total_students = self.fetch_total_students()

        self.lbl_course.config(text=f"Total Course\n[ {total_courses} ]")
        self.lbl_teacher.config(text=f"Total Teacher\n[ {total_teachers} ]")
        self.lbl_student.config(text=f"Total Student\n[ {total_students} ]")

        self.root.after(5000, self.update_counts)

    def add_student(self): 
        new_window = customtkinter.CTkToplevel(self.root)
        StudentCard(new_window, self.student_id)
        new_window.transient(self.root)  
        new_window.grab_set()  
        self.root.wait_window(new_window)  

    def add_course(self):
        new_window = customtkinter.CTkToplevel(self.root)
        StudentView(new_window, self.student_id)
        new_window.transient(self.root)
        new_window.grab_set()
        self.root.wait_window(new_window)

    def add_teacher(self):
        new_window = customtkinter.CTkToplevel(self.root)
        teacherprofile(new_window)  
        new_window.transient(self.root)
        new_window.grab_set()
        self.root.wait_window(new_window)

    def add_result(self):
        new_window = customtkinter.CTkToplevel(self.root)
        ReportClass(new_window, self.student_id)  
        new_window.transient(self.root)
        new_window.grab_set()
        self.root.wait_window(new_window)

    def attendance(self):
        new_window = customtkinter.CTkToplevel(self.root)
        AttendanceReport(new_window, self.student_id)  
        new_window.transient(self.root)
        new_window.grab_set()
        self.root.wait_window(new_window)

    def logout(self):
        messagebox.showinfo("Logout", "You have logged out")
        self.root.destroy()
        self.open_login_page()

    def open_login_page(self):
        import login
        login_root = customtkinter.CTk()
        login.LoginClass(login_root)
        login_root.mainloop()

if __name__ == "__main__":
    root = customtkinter.CTk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}+0+0")
    obj = GradeMaster(root, student_id=any)
    root.mainloop()