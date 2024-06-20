import tkinter as tk
from tkinter import messagebox, filedialog
import sqlite3
import customtkinter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ReportClass:
    def __init__(self, root, student_id):
        self.root = root
        self.student_id = student_id
        self.root.title("Student Result")
        self.root.geometry("1600x770+0+200")
        self.root.config(bg="#fff0f3")
        self.root.focus_force()

        self.main_frame = tk.Frame(self.root, bg="#fff0f3")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.create_widgets()
        self.fetch_student_record()

    def create_widgets(self):
        title = tk.Label(self.main_frame, text="View Student Results", font=("king", 23, "bold"), bg="#ff80b4", fg="black")
        title.place(x=0, y=10, width=1960, height=70)

        self.var_id = ""
        self.var_student_id = tk.StringVar()
        
        btn_print = tk.Button(self.main_frame, text="Print", font=("king", 15, "bold"), bg="#DE3163", fg="#fff0f3", cursor="hand2", command=self.print_as_pdf)
        btn_print.place(x=800, y=500, width=100, height=35)

        lbl_id = tk.Label(self.main_frame, text="ID No.", font=("king", 15, "bold"), bg="#FFB3D2", bd=2, relief=tk.GROOVE)
        lbl_id.place(x=300, y=180, width=150, height=50)
        
        lbl_name = tk.Label(self.main_frame, text="Name", font=("king", 15, "bold"), bg="#FFB3D2", bd=2, relief=tk.GROOVE)
        lbl_name.place(x=300, y=230, width=150, height=50)
        
        lbl_course = tk.Label(self.main_frame, text="Course", font=("king", 15, "bold"), bg="#FFB3D2", bd=2, relief=tk.GROOVE)
        lbl_course.place(x=300, y=280, width=150, height=50)
        
        lbl_marks = tk.Label(self.main_frame, text="Marks", font=("king", 15, "bold"), bg="#FFB3D2", bd=2, relief=tk.GROOVE)
        lbl_marks.place(x=450, y=280, width=150, height=50)
        
        lbl_grades = tk.Label(self.main_frame, text="Grades", font=("king", 15, "bold"), bg="#FFB3D2", bd=2, relief=tk.GROOVE)
        lbl_grades.place(x=600, y=280, width=150, height=50)
        
        lbl_gpa = tk.Label(self.main_frame, text="GPA", font=("king", 15, "bold"), bg="#FFB3D2", bd=2, relief=tk.GROOVE)
        lbl_gpa.place(x=750, y=280, width=150, height=50)

        self.id = tk.Label(self.main_frame, font=("king", 15, "bold"), bg="#fff0f3", bd=2, relief=tk.GROOVE)
        self.id.place(x=450, y=180, width=450, height=50)
        
        self.name = tk.Label(self.main_frame, font=("king", 15, "bold"), bg="#fff0f3", bd=2, relief=tk.GROOVE)
        self.name.place(x=450, y=230, width=450, height=50)

        self.course_labels = []
        self.marks_vars = []
        self.grade_labels = []

        self.gpa = tk.Label(self.main_frame, font=("king", 15, "bold"), bg="#fff0f3", bd=2, relief=tk.GROOVE)
        self.gpa.place(x=750, y=330, width=150, height=50)

        self.graph_frame = tk.Frame(self.main_frame, bg="#fff0f3", bd=2, relief=tk.GROOVE)
        self.graph_frame.place(x=1000, y=180, width=500, height=300)

    def fetch_student_record(self):
        con = sqlite3.connect(database="GradeMaster.db")
        cur = con.cursor()
        try:
            query = """
                SELECT g.id, g.name, c.course_name, g.marks, g.grade, c.credit_hour
                FROM grade g
                JOIN Courses c ON g.course = c.cid
                WHERE g.id=?
            """
            cur.execute(query, (self.student_id,))
            rows = cur.fetchall()
            print(rows)  
            if rows:
                self.var_id = rows[0][0]
                self.id.config(text=rows[0][0])
                self.name.config(text=rows[0][1])

                for i, row in enumerate(rows):
                    course_lbl = tk.Label(self.main_frame, text=row[2], font=("king", 15, "bold"), bg="#fff0f3", bd=2, relief=tk.GROOVE)
                    course_lbl.place(x=300, y=330 + i * 50, width=150, height=50)
                    self.course_labels.append(course_lbl)

                    marks_var = tk.StringVar(value=str(row[3]))
                    marks_lbl = tk.Label(self.main_frame, textvariable=marks_var, font=("king", 15, "bold"), bg="#fff0f3", bd=2, relief=tk.GROOVE)
                    marks_lbl.place(x=450, y=330 + i * 50, width=150, height=50)
                    self.marks_vars.append(marks_var)

                    grade_lbl = tk.Label(self.main_frame, text=row[4], font=("king", 15, "bold"), bg="#fff0f3", bd=2, relief=tk.GROOVE)
                    grade_lbl.place(x=600, y=330 + i * 50, width=150, height=50)
                    self.grade_labels.append(grade_lbl)
                
                self.calculate_gpa(rows)  
                self.plot_graph(rows)  
            else:
                messagebox.showinfo("Info", "No record found for this student ID", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error fetching student record: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def calculate_gpa(self, rows):
        if not rows:
            self.gpa.config(text="N/A")
            return
        
        try:
            total_points = 0
            total_credits = 0
            grade_points = {'A+': 4.0, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'F': 0.0}

            for row in rows:
                grade = row[4]
                credit_hours = row[5]  
                points = grade_points.get(grade, 0) * credit_hours
                total_points += points
                total_credits += credit_hours

            if total_credits > 0:
                gpa = total_points / total_credits
                self.gpa.config(text=f"{gpa:.2f}")
            else:
                self.gpa.config(text="N/A")
        except Exception as ex:
            messagebox.showerror("Error", f"Error calculating GPA: {str(ex)}")

    def plot_graph(self, rows):
        if not rows:
            return

        courses = [row[2] for row in rows]
        marks = [row[3] for row in rows]
        
        # Calculate average marks
        average_marks = sum(marks) / len(marks) if len(marks) > 0 else 0

        # Plotting
        fig, ax = plt.subplots(figsize=(5, 3))  
        bar_width = 0.35
        index = range(len(courses))
        bar1 = ax.bar(index, marks, bar_width, label='Student Marks')
        ax.axhline(y=average_marks, color='r', linestyle='-', label='Average Marks')

        ax.set_xlabel('Courses')
        ax.set_ylabel('Marks')
        ax.set_title('Comparison of Student Marks with Average Marks')
        ax.set_xticks(index)
        ax.set_xticklabels(courses, rotation=45)
        ax.legend()

        self.graph_canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        self.graph_canvas.draw()

        self.graph_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.root.update()

    def print_as_pdf(self):
        if not self.var_id:
            messagebox.showerror("Error", "No data to print.", parent=self.root)
            return

        try:
            file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
            if not file_path:
                return  

            c = canvas.Canvas(file_path, pagesize=letter)
            c.drawString(100, 750, f"ID No.: {self.id.cget('text')}")
            c.drawString(100, 730, f"Name: {self.name.cget('text')}")
            c.drawString(100, 710, "Courses and Marks:")

            for i, (course_lbl, marks_var, grade_lbl) in enumerate(zip(self.course_labels, self.marks_vars, self.grade_labels)):
                c.drawString(100, 690 - i * 20, f"Course: {course_lbl.cget('text')} - Marks: {marks_var.get()} - Grade: {grade_lbl.cget('text')}")

            c.drawString(100, 690 - len(self.course_labels) * 20, f"GPA: {self.gpa.cget('text')}")
            c.save()
            messagebox.showinfo("Success", f"Result saved as {file_path}", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Failed to generate PDF: {str(ex)}", parent=self.root)

if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = ReportClass(root, student_id=any) 
    root.mainloop()