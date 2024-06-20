from tkinter import *
from tkinter import messagebox, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3
import customtkinter
import matplotlib.pyplot as plt
from datetime import datetime

class AttendanceReport:
    def __init__(self, root, student_id):
        self.root = root
        self.student_id = student_id
        self.root.title("Attendance Report")
        self.root.geometry("1600x770+0+200")
        self.root.config(bg='#fff0f3')
        self.root.focus_force()

        #==============Variables================
        self.attendance_tree = None
        self.var_student_id = StringVar(value=student_id)
        self.var_selected_course = StringVar()

        # =============Title==================
        title = Label(self.root, text="Attendance Report", font=("King", 30, "bold"), bg="#ff80b4", fg="#262626")
        title.place(x=0, y=10, width=1960, height=70)

        # UI elements
        self.lbl_student = Label(self.root, text="Student ID", font=("King", 20, "bold"), bg="#fff0f3")
        self.lbl_student.place(x=200, y=150)

        self.entry_student = Entry(self.root, textvariable=self.var_student_id, font=("King", 20), state='readonly')
        self.entry_student.place(x=450, y=150)

        self.lbl_course = Label(self.root, text="Select Course", font=("King", 20, "bold"), bg="#fff0f3")
        self.lbl_course.place(x=200, y=210)
        self.cmb_course = ttk.Combobox(self.root, textvariable=self.var_selected_course, font=("King", 18), state='readonly')
        self.cmb_course.place(x=450, y=210)
        self.cmb_course.bind("<<ComboboxSelected>>", self.display_attendance_data)

        self.btn_view_report = Button(self.root, text="Show Attendance Trend", command=self.plot_attendance_trend, bg="#ff80b4", fg="#262626", font=("King", 15, "bold"))
        self.btn_view_report.place(x=450, y=290)

        self.attendance_tree = ttk.Treeview(self.root, columns=("Course", "Date", "Status"), show="headings", height=15)
        self.attendance_tree.heading("Course", text="Course")
        self.attendance_tree.heading("Date", text="Date")
        self.attendance_tree.heading("Status", text="Status")
        self.attendance_tree.place(x=950, y=200, width=800, height=600)

        # Canvas for plotting attendance trend
        self.canvas_frame = Frame(self.root, bg="#fff0f3")
        self.canvas_frame.place(x=250, y=400, width=420, height=300)
        
        self.figure = plt.Figure(figsize=(5, 3), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, self.canvas_frame)
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

        # Fetch course options and initialize
        self.fetch_courses()

    def fetch_courses(self):
        """Fetch and populate course options"""
        try:
            conn = sqlite3.connect(database="GradeMaster.db")
            cur = conn.cursor()
            cur.execute("SELECT cid, course_name FROM Courses WHERE cid IN (SELECT course_id FROM Attendance WHERE student_id=?)", (self.student_id,))
            rows = cur.fetchall()
            if rows:
                self.courses = rows
                self.cmb_course['values'] = [f"{row[0]} - {row[1]}" for row in rows]
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching courses: {str(e)}")
        finally:
            conn.close()

    def display_attendance_data(self, event=None):
        """Fetch and display attendance data in the Treeview"""
        try:
            conn = sqlite3.connect(database="GradeMaster.db")
            cur = conn.cursor()
            selected_course = self.cmb_course.get().split(" - ")[0]
            cur.execute("""
                SELECT Courses.course_name, Attendance.date, Attendance.status
                FROM Attendance
                JOIN Courses ON Attendance.course_id = Courses.cid
                WHERE Attendance.student_id = ? AND Attendance.course_id = ?
                ORDER BY Attendance.date ASC
            """, (self.student_id, selected_course))
            rows = cur.fetchall()
            if rows:
                # Clear the existing data in the treeview
                for item in self.attendance_tree.get_children():
                    self.attendance_tree.delete(item)
                # Insert new data
                for row in rows:
                    self.attendance_tree.insert("", "end", values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching attendance data: {str(e)}")
        finally:
            conn.close()

    def plot_attendance_trend(self):
        """Plot the attendance trend using Matplotlib"""
        try:
            conn = sqlite3.connect(database="GradeMaster.db")
            cur = conn.cursor()
            selected_course = self.cmb_course.get().split(" - ")[0]
            cur.execute("""
                SELECT Attendance.date, Attendance.status
                FROM Attendance
                WHERE Attendance.student_id = ? AND Attendance.course_id = ?
                ORDER BY Attendance.date ASC
            """, (self.student_id, selected_course))
            data = cur.fetchall()
            if not data:
                messagebox.showinfo("Info", "No attendance data to plot.")
                return

            dates = [datetime.strptime(row[0], '%Y-%m-%d') for row in data]
            status = [1 if row[1] == 'Present' else 0 for row in data]  # Assuming 'Present' is one status and anything else is considered 'Absent'

            # Clear the previous plot
            self.ax.clear()

            self.ax.plot(dates, status, marker='o', linestyle='-', color='b', label='Attendance Status')
            self.ax.set_title('Attendance Trend')
            self.ax.set_xlabel('Date')
            self.ax.set_ylabel('Status (1=Present, 0=Absent)')
            self.ax.set_xticks(dates)
            self.ax.set_xticklabels([date.strftime('%Y-%m-%d') for date in dates], rotation=45)
            self.ax.grid(True)
            self.ax.legend()

            # Update canvas with new plot
            self.canvas.draw()
        except Exception as e:
            messagebox.showerror("Error", f"Error plotting attendance trend: {str(e)}")
        finally:
            conn.close()

if __name__ == "__main__":
    root = customtkinter.CTk()
    # Replace 1221109567 with a valid student_id from your database
    app = AttendanceReport(root, student_id=1221109567)
    root.mainloop()
