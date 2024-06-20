from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import customtkinter

class AttendanceReport:
    def __init__(self, root, student_id):
        self.root = root
        self.student_id = student_id
        self.root.title("Attendance Report")
        self.root.geometry("1200x750+50+200")
        self.root.config(bg='#fff0f3')
        self.root.focus_force()

        #==============Variable================
        self.attendance_tree = None
        self.var_student_id = tk.StringVar(value=student_id)

        # =============Title==================
        title = Label(self.root, text="Attendance Report", font=("King", 30, "bold"), bg="#ff80b4", fg="#262626")
        title.place(x=0, y=10, width=1960, height=70)

        # UI elements
        self.lbl_student = Label(self.root, text="Select Student", font=("King", 20, "bold"), bg="#fff0f3")
        self.lbl_student.place(x=800, y=150)

        self.cmb_student = ttk.Combobox(self.root, textvariable=self.var_student_id, font=("King", 20), state='readonly')
        self.cmb_student.place(x=750, y=190)

        self.btn_view_report = Button(self.root, text="View Attendance Report", command=self.fetch_attendance_report, bg="#ff80b4", fg="#262626", font=("King", 15, "bold"))
        self.btn_view_report.place(x=780, y=250)

        self.attendance_tree = ttk.Treeview(self.root, columns=("Course", "Date", "Status"), show="headings", height=15)
        self.attendance_tree.heading("Course", text="Course")
        self.attendance_tree.heading("Date", text="Date")
        self.attendance_tree.heading("Status", text="Status")
        self.attendance_tree.place(x=550, y=350, width=700, height=450)



    def fetch_attendance_report(self, event=None):
        # Use self.student_id in your query to fetch attendance report
        try:
            conn = sqlite3.connect(database="GradeMaster.db")
            cur = conn.cursor()
            cur.execute("""
                SELECT Courses.course_name, Attendance.date, Attendance.status
                FROM Attendance
                JOIN Courses ON Attendance.course_id = Courses.cid
                WHERE Attendance.student_id = ?
            """, (self.student_id,))
            rows = cur.fetchall()
            if rows:
                # Clear the existing data in the treeview
                for item in self.attendance_tree.get_children():
                    self.attendance_tree.delete(item)
                # Insert new data
                for row in rows:
                    self.attendance_tree.insert("", "end", values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching attendance report: {str(e)}")
        finally:
            conn.close()

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = AttendanceReport(root,student_id=any)
    root.mainloop()
