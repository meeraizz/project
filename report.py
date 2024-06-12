from tkinter import *
from tkinter import ttk, messagebox, filedialog
import sqlite3
import customtkinter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class ReportClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Grade Master")
        self.root.geometry("1200x750+50+200")
        self.root.config(bg="#fff0f3")
        self.root.focus_force()

        self.main_frame = Frame(self.root, bg="#fff0f3")
        self.main_frame.pack(fill=BOTH, expand=True)

        self.create_widgets()

    def create_widgets(self):
        # =====title======
        title = Label(self.main_frame, text="View Student Results", font=("king", 23, "bold"), bg="#FFB3D2", fg="black")
        title.pack(fill=X)  

        # =====search======
        self.var_search = StringVar()
        self.var_id = ""
        self.var_student_id = StringVar()

        lbl_search = Label(self.root, text="Search by ID No.", font=("king", 20, "bold"), bg="#fff0f3").place(x=250, y=100)
        txt_search = Entry(self.root, textvariable=self.var_search, font=("king", 20), bg="lightyellow").place(x=530, y=100, width=170)
        btn_search = Button(self.root, text="Search", font=("king", 15, "bold"), bg="#03a9f4", fg="#fff0f3", cursor="hand2", command=self.search).place(x=720, y=100, width=100, height=35)
        btn_clear = Button(self.root, text="Clear", font=("king", 15, "bold"), bg="#F19CBB", fg="#fff0f3", cursor="hand2", command=self.clear).place(x=840, y=100, width=100, height=35)
        btn_print = Button(self.root, text="Print", font=("king", 15, "bold"), bg="#DE3163", fg="#fff0f3", cursor="hand2", command=self.print_as_pdf).place(x=950, y=100, width=100, height=35)

        # =====result_labels======
        lbl_id = Label(self.root, text="ID No.", font=("king", 15, "bold"), bg="#FFB3D2", bd=2, relief=GROOVE).place(x=300, y=180, width=150, height=50)
        lbl_name = Label(self.root, text="Name", font=("king", 15, "bold"), bg="#FFB3D2", bd=2, relief=GROOVE).place(x=300, y=230, width=150, height=50)
        lbl_course = Label(self.root, text="Course", font=("king", 15, "bold"), bg="#FFB3D2", bd=2, relief=GROOVE).place(x=300, y=280, width=150, height=50)
        lbl_marks = Label(self.root, text="Marks", font=("king", 15, "bold"), bg="#FFB3D2", bd=2, relief=GROOVE).place(x=450, y=280, width=150, height=50)
        lbl_grades = Label(self.root, text="Grades", font=("king", 15, "bold"), bg="#FFB3D2", bd=2, relief=GROOVE).place(x=600, y=280, width=150, height=50)
        lbl_gpa = Label(self.root, text="GPA", font=("king", 15, "bold"), bg="#FFB3D2", bd=2, relief=GROOVE).place(x=750, y=280, width=150, height=50)

        self.id = Label(self.root, font=("king", 15, "bold"), bg="#fff0f3", bd=2, relief=GROOVE)
        self.id.place(x=450, y=180, width=450, height=50)
        self.name = Label(self.root, font=("king", 15, "bold"), bg="#fff0f3", bd=2, relief=GROOVE)
        self.name.place(x=450, y=230, width=450, height=50)

        self.course1 = Label(self.root, font=("king", 15, "bold"), bg="#fff0f3", bd=2, relief=GROOVE)
        self.course1.place(x=300, y=330, width=150, height=50)
        self.course2 = Label(self.root, font=("king", 15, "bold"), bg="#fff0f3", bd=2, relief=GROOVE)
        self.course2.place(x=300, y=380, width=150, height=50)
        self.course3 = Label(self.root, font=("king", 15, "bold"), bg="#fff0f3", bd=2, relief=GROOVE)
        self.course3.place(x=300, y=430, width=150, height=50)

        self.marks1_var = StringVar()
        self.marks2_var = StringVar()
        self.marks3_var = StringVar()
        self.marks1 = Label(self.root, textvariable=self.marks1_var, font=("king", 15, "bold"), bg="#fff0f3", bd=2, relief=GROOVE)
        self.marks1.place(x=450, y=330, width=150, height=50)
        self.marks2 = Label(self.root, textvariable=self.marks2_var, font=("king", 15, "bold"), bg="#fff0f3", bd=2, relief=GROOVE)
        self.marks2.place(x=450, y=380, width=150, height=50)
        self.marks3 = Label(self.root, textvariable=self.marks3_var, font=("king", 15, "bold"), bg="#fff0f3", bd=2, relief=GROOVE)
        self.marks3.place(x=450, y=430, width=150, height=50)

        self.grades1 = Label(self.root, font=("king", 15, "bold"), bg="#fff0f3", bd=2, relief=GROOVE)
        self.grades1.place(x=600, y=330, width=150, height=50)
        self.grades2 = Label(self.root, font=("king", 15, "bold"), bg="#fff0f3", bd=2, relief=GROOVE)
        self.grades2.place(x=600, y=380, width=150, height=50)
        self.grades3 = Label(self.root, font=("king", 15, "bold"), bg="#fff0f3", bd=2, relief=GROOVE)
        self.grades3.place(x=600, y=430, width=150, height=50)

        self.gpa = Label(self.root, font=("king", 15, "bold"), bg="#fff0f3", bd=2, relief=GROOVE)
        self.gpa.place(x=750, y=330, width=150, height=50)

    # =========================================================
    def search(self):
        con = sqlite3.connect(database="GradeMaster.db")
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "ID No. should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM grade WHERE id=?", (self.var_search.get(),))
                rows = cur.fetchall()
                if len(rows) > 0:
                    self.clear()

                    self.var_id = rows[0][0]
                    self.id.config(text=rows[0][1])
                    self.name.config(text=rows[0][2])
                    
                    for i, row in enumerate(rows):
                        if i == 0:
                            self.course1.config(text=row[3])
                            self.marks1_var.set(str(row[6]))
                            self.grades1.config(text=row[9])                       
                            self.course2.config(text=row[4])
                            self.marks2_var.set(str(row[7]))
                            self.grades2.config(text=row[10])                       
                            self.course3.config(text=row[5])
                            self.marks3_var.set(str(row[8]))
                            self.grades3.config(text=row[11])

                    self.calculate_gpa(rows)
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

    def fetch_student_courses(self):
        id = self.var_student_id.get()
        if not id:
            messagebox.showerror("Error", "Please enter student ID.")
            return []

        con = sqlite3.connect(database="GradeMaster.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT course_name, credit_hours, grade FROM course WHERE student_id=?", (id,))
            rows = cur.fetchall()
            return rows
        except Exception as ex:
            messagebox.showerror("Error", f"Error fetching student courses: {str(ex)}")
            return []
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
                grade = row[9]  # Adjust according to the correct column index for the grade
                credit_hours = row[6]  # Adjust according to the correct column index for the credit hours
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

    def clear(self):
        self.var_id = ""
        self.id.config(text="")
        self.name.config(text="")
        self.course1.config(text="")
        self.course2.config(text="")
        self.course3.config(text="")
        self.marks1.config(text="")
        self.marks2.config(text="")
        self.marks3.config(text="")
        self.grades1.config(text="")
        self.grades2.config(text="")
        self.grades3.config(text="")
        self.gpa.config(text="")
        self.var_search.set("")

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
            c.drawString(100, 690, f"Course: {self.course1.cget('text')} - Marks: {self.marks1_var.get()} - Grade: {self.grades1.cget('text')}")
            c.drawString(100, 670, f"Course: {self.course2.cget('text')} - Marks: {self.marks2_var.get()} - Grade: {self.grades2.cget('text')}")
            c.drawString(100, 650, f"Course: {self.course3.cget('text')} - Marks: {self.marks3_var.get()} - Grade: {self.grades3.cget('text')}")
            c.drawString(100, 630, f"GPA: {self.gpa.cget('text')}")
            c.save()
            messagebox.showinfo("Success", f"Result saved as {file_path}", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Failed to generate PDF: {str(ex)}", parent=self.root)

if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = ReportClass(root)
    root.mainloop()
