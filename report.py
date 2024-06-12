from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
import customtkinter

class ReportClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Grade Master")
        self.root.geometry("1200x750+50+200")
        self.root.config(bg="#fff0f3")
        self.root.focus_force()

        # Create a main frame to contain all widgets
        self.main_frame = Frame(self.root, bg="#fff0f3")
        self.main_frame.pack(fill=BOTH, expand=True)

        # Call method to create and layout all widgets
        self.create_widgets()

    def create_widgets(self):
        # =====title======
        title = Label(self.main_frame, text="View Student Results", font=("king", 23, "bold"), bg="#FFB3D2", fg="black")
        title.pack(fill=X)  # Fill the width of the main frame

        # =====search======
        self.var_search = StringVar()
        self.var_id = ""

        lbl_search = Label(self.root, text="Search by ID No.", font=("king", 20, "bold"), bg="#fff0f3").place(x=250, y=100)
        txt_search = Entry(self.root, textvariable=self.var_search, font=("king", 20), bg="lightyellow").place(x=530, y=100, width=170)
        btn_search = Button(self.root, text="Search", font=("king", 15, "bold"), bg="#03a9f4", fg="#fff0f3", cursor="hand2", command=self.search).place(x=720, y=100, width=100, height=35)
        btn_clear = Button(self.root, text="Clear", font=("king", 15, "bold"), bg="#F19CBB", fg="#fff0f3", cursor="hand2", command=self.clear).place(x=840, y=100, width=100, height=35)

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

        # Separate labels for multiple courses and marks
        self.course1 = Label(self.root, font=("king", 15, "bold"), bg="#fff0f3", bd=2, relief=GROOVE)
        self.course1.place(x=300, y=330, width=150, height=50)
        self.course2 = Label(self.root, font=("king", 15, "bold"), bg="#fff0f3", bd=2, relief=GROOVE)
        self.course2.place(x=300, y=380, width=150, height=50)
        self.course3 = Label(self.root, font=("king", 15, "bold"), bg="#fff0f3", bd=2, relief=GROOVE)
        self.course3.place(x=300, y=430, width=150, height=50)

        self.marks1_var = StringVar()
        self.marks2_var = StringVar()
        self.marks3_var = StringVar()
        self.marks1 = Label(self.root, textvariable=self.marks1_var,font=("king", 15, "bold"), bg="#fff0f3", bd=2, relief=GROOVE)
        self.marks1.place(x=450, y=330, width=150, height=50)
        self.marks2 = Label(self.root, textvariable=self.marks2_var,font=("king", 15, "bold"), bg="#fff0f3", bd=2, relief=GROOVE)
        self.marks2.place(x=450, y=380, width=150, height=50)
        self.marks3 = Label(self.root, textvariable=self.marks3_var,font=("king", 15, "bold"), bg="#fff0f3", bd=2, relief=GROOVE)
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
                    # Clear previous results
                    self.clear()
                    # Display results
                    self.var_id = rows[0][0]
                    self.id.config(text=rows[0][1])
                    self.name.config(text=rows[0][2])
                    
                    for i, row in enumerate(rows):
                        if i == 0:
                            self.course1.config(text=row[3])
                            self.marks1_var.set(str(row[4]))
                            self.grades1.config(text=row[7])
                        elif i == 1:
                            self.course2.config(text=row[3])
                            self.marks2_var.set(str(row[4]))
                            self.grades2.config(text=row[7])
                        elif i == 2:
                            self.course3.config(text=row[3])
                            self.marks3_var.set(str(row[4]))
                            self.grades3.config(text=row[7])

                    marks = [row[4] for row in rows]
                    try:
                        marks = [int(mark) for mark in marks]
                        gpa = self.calculate_gpa(marks)
                        self.gpa.config(text=gpa)
                    except ValueError as ve:
                        messagebox.showerror("Error", f"Invalid mark found: {ve}", parent=self.root)
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

    def calculate_gpa(self, marks):
        # Implement your GPA calculation logic here
        total_marks = sum(marks)
        full_marks = len(marks) * 100
        percentage = (total_marks / full_marks) * 100
        if percentage >= 90:
            return 4.0
        elif percentage >= 80:
            return 3.7
        elif percentage >= 70:
            return 3.3
        elif percentage >= 60:
            return 3.0
        elif percentage >= 50:
            return 2.7
        else:
            return 2.0

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

if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = ReportClass(root)
    root.mainloop()