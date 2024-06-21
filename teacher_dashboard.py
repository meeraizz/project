from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import customtkinter
from student_grade import gradeclass
from teachercard import teachercard
from details_tcview import detailsclasstc
from report import ReportClass
from coursesclasses import ManageCourse

class GradeMastertc:
    def __init__(self, root, teacher_id):
        self.root = root
        self.teacher_id = teacher_id
        self.root.title("Grade Master")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg='#fff0f3')
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.focus_force()

        # ====icons=====
        self.logo_image = Image.open("images/Grade-Master_Logo.png")
        self.logo_image = self.logo_image.resize((70, 70), Image.LANCZOS)
        self.logo_dash = ImageTk.PhotoImage(self.logo_image)

        # ======title==========
        title = Label(self.root, text="Grade Master", padx=10, compound=LEFT, image=self.logo_dash, font=("King", 40, "bold"), bg="#ffb3d2", fg="black")
        title.place(x=0, y=0, relwidth=1, height=70)

        M_Frame = LabelFrame(self.root, text="Menu", font=("King", 15), bg="#fff0f3")
        M_Frame.place(x=10, y=70, width=1860, height=100)

        btn_course = Button(M_Frame, text="Course", font=("King", 20, "bold"), bg="#ffb3d2", fg="black", cursor="hand2", command=self.add_course)
        btn_course.place(x=200, y=10, width=270, height=60)

        btn_student = Button(M_Frame, text="Student", font=("King", 20, "bold"), bg="#ffb3d2", fg="black", cursor="hand2", command=self.add_student)
        btn_student.place(x=500, y=10, width=270, height=60)

        btn_profile = Button(M_Frame, text="Profile", font=("King", 20, "bold"), bg="#ffb3d2", fg="black", cursor="hand2", command=self.show_profile)
        btn_profile.place(x=800, y=10, width=270, height=60)

        btn_grade = Button(M_Frame, text="Grade", font=("King", 20, "bold"), bg="#ffb3d2", fg="black", cursor="hand2", command=self.add_grade)
        btn_grade.place(x=1100, y=10, width=270, height=60)

        btn_logout = Button(M_Frame, text="Logout", font=("King", 20, "bold"), bg="#ffb3d2", fg="black", cursor="hand2", command=self.logout)
        btn_logout.place(x=1400, y=10, width=270, height=60)

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

        # Call the update_counts method to set initial counts
        self.update_counts()
        # Schedule the update_counts method to be called every 5 seconds
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

        # Schedule the next update
        self.root.after(5000, self.update_counts)

    def add_course(self):
        new_top = customtkinter.CTkToplevel(self.root)
        new_window = ManageCourse(new_top)
        new_top.transient(self.root)
        new_top.grab_set()
        new_top.focus_force()

    def add_student(self):
        new_top = customtkinter.CTkToplevel(self.root)
        new_window = detailsclasstc(new_top)
        new_top.transient(self.root)
        new_top.grab_set()
        new_top.focus_force()

    def add_grade(self):
        new_top = customtkinter.CTkToplevel(self.root)
        new_window = gradeclass(new_top)
        new_top.transient(self.root)
        new_top.grab_set()
        new_top.focus_force()

    def show_profile(self):
        new_top = customtkinter.CTkToplevel(self.root)
        profile_window = teachercard(new_top, self.teacher_id)
        new_top.transient(self.root)
        new_top.grab_set()
        new_top.focus_force()

    def add_result(self):
        new_top = customtkinter.CTkToplevel(self.root)
        new_window = ReportClass(new_top, self.teacher_id)
        new_top.transient(self.root)
        new_top.grab_set()
        new_top.focus_force()

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
    obj = GradeMastertc(root, teacher_id=1)
    root.mainloop()
