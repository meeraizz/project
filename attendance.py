from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
import customtkinter
from datetime import datetime

class AttendanceManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Management")
        self.root.geometry("1600x750+0+200")
        self.root.config(bg='#fff0f3')
        self.root.focus_force()

        # =============Title==================
        title = Label(self.root, text="Attendance", font=("King", 30, "bold"), bg="#ff80b4", fg="#262626")
        title.place(x=0, y=10, width=1960, height=70)

        #=============variable===============
        self.student_id = None
        self.course_id = None

        # UI elements
        self.lbl_student = Label(self.root, text="Select Student", font=("King", 20, "bold"), bg="#fff0f3")
        self.lbl_student.place(x=800, y=150)
        self.cmb_student = ttk.Combobox(self.root, font=("King", 15), state='readonly')
        self.cmb_student.place(x=780, y=210)
        self.cmb_student.bind("<<ComboboxSelected>>", self.fetch_courses)

        self.lbl_course = Label(self.root, text="Select Course", font=("King", 20, "bold"), bg="#fff0f3")
        self.lbl_course.place(x=800, y=250)
        self.cmb_course = ttk.Combobox(self.root, font=("King", 15), state='readonly')
        self.cmb_course.place(x=780, y=300)
        self.cmb_course.bind("<<ComboboxSelected>>", self.load_calendar)

        self.lbl_date = Label(self.root, text="Select Date for Attendance", font=("King", 20, "bold"), bg="#fff0f3")
        self.lbl_date.place(x=690, y=360)
        
        # Create comboboxes for day, month, and year
        self.cmb_day = ttk.Combobox(self.root, values=list(range(1, 32)), font=("King", 15), state='readonly')
        self.cmb_day.place(x=780, y=430, width=80)
        self.cmb_day.set("Day")
        
        self.cmb_month = ttk.Combobox(self.root, values=list(range(1, 13)), font=("King", 15), state='readonly')
        self.cmb_month.place(x=890, y=430, width=80)
        self.cmb_month.set("Month")
        
        self.cmb_year = ttk.Combobox(self.root, values=list(range(1900, 2025)), font=("King", 15), state='readonly')
        self.cmb_year.place(x=1000, y=430, width=100)
        self.cmb_year.set("Year")

        self.btn_mark_attendance = Button(self.root, text="Mark Present", font=("King", 15), bg="#ff80b4", fg="#262626", command=self.mark_attendance)
        self.btn_mark_attendance.place(x=750, y=500, width=190, height=35)

        self.btn_mark_absent = Button(self.root, text="Mark Absent", font=("King", 15), bg="#e0d2ef", fg="#262626", command=self.mark_absent)
        self.btn_mark_absent.place(x=960, y=500, width=190, height=35)

        self.fetch_students()

    def fetch_students(self):
        try:
            conn = sqlite3.connect(database="GradeMaster.db")
            cur = conn.cursor()
            cur.execute("SELECT id, name FROM student")
            rows = cur.fetchall()
            if rows:
                self.students = rows
                self.cmb_student['values'] = [f"{row[0]} - {row[1]}" for row in rows]
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching students: {str(e)}")
        finally:
            conn.close()

    def fetch_courses(self, event=None):
        selected_student = self.cmb_student.get().split(" - ")[0]
        self.student_id = int(selected_student)
        try:
            conn = sqlite3.connect(database="GradeMaster.db")
            cur = conn.cursor()
            cur.execute("SELECT cid, course_name FROM Courses WHERE cid IN (SELECT cid FROM Enrollments WHERE student_id=?)", (self.student_id,))
            rows = cur.fetchall()
            if rows:
                self.courses = rows
                self.cmb_course['values'] = [f"{row[0]} - {row[1]}" for row in rows]
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching courses: {str(e)}")
        finally:
            conn.close()

    def load_calendar(self, event=None):
        selected_course = self.cmb_course.get().split(" - ")[0]
        self.course_id = int(selected_course)
        
    def mark_attendance(self):
        self.mark_status("Present")

    def mark_absent(self):
        self.mark_status("Absent")

    def mark_status(self, status):
        if self.student_id is None or self.course_id is None:
            messagebox.showwarning("Warning", "Please select both a student and a course.")
            return

        if self.cmb_day.get() == "Day" or self.cmb_month.get() == "Month" or self.cmb_year.get() == "Year":
            messagebox.showwarning("Warning", "Please select a valid date.")
            return

        selected_date = f"{self.cmb_year.get()}-{self.cmb_month.get()}-{self.cmb_day.get()}"
        formatted_date = datetime.strptime(selected_date, "%Y-%m-%d").date()
        try:
            conn = sqlite3.connect(database="GradeMaster.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM Attendance WHERE student_id=? AND course_id=? AND date=?", 
                        (self.student_id, self.course_id, formatted_date))
            existing_entry = cur.fetchone()
            if existing_entry:
                messagebox.showinfo("Info", "Attendance for this date has already been marked.")
                return

            cur.execute("INSERT INTO Attendance (student_id, course_id, date, status) VALUES (?, ?, ?, ?)",
                        (self.student_id, self.course_id, formatted_date, status))
            conn.commit()
            messagebox.showinfo("Success", f"Attendance marked as {status} successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Error marking attendance: {str(e)}")
        finally:
            conn.close()

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = AttendanceManager(root)
    root.mainloop()
