from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
import customtkinter

class gradeclass:
    def __init__(self, root):
        self.root = root
        self.root.title("Grade Master")
        self.root.geometry("1500x750+0+200")
        self.root.config(bg='#fff0f3')
        self.root.focus_force()

        # ===title====
        title = Label(self.root, text="Add Student Result", font=("King", 30, "bold"), bg="#ff80b4", fg="#262626").place(x=0, y=10, width=1960, height=70)

        # ====variables====
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_course_name = StringVar()
        self.var_marks = StringVar()
        self.var_grade = StringVar()
        self.var_full_marks = StringVar(value="100") 
        self.id_list = []
        self.course_list = []
        self.course_dict = {}  # Dictionary to map course names to course IDs

        # Initialize comboboxes before fetching data
        self.txt_student = ttk.Combobox(self.root, textvariable=self.var_id, values=self.id_list, font=("king", 20, "bold"), state='readonly', justify=CENTER)
        self.txt_student.place(x=880, y=150, width=200, height=45)
        self.txt_student.set("Select")
        self.txt_student.bind("<<ComboboxSelected>>", self.fetch_course)

        self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course_name, values=self.course_list, font=("king", 20, "bold"), state='readonly', justify=CENTER)
        self.txt_course.place(x=880, y=310, width=370, height=45)
        self.txt_course.set("Select")
        self.txt_course.bind("<<ComboboxSelected>>", self.course_selected)

        # Fetching data after initializing comboboxes
        self.fetch_id()

        # ===widgets===
        lbl_select = Label(self.root, text="Select Student", font=("king", 20, "bold"), bg="#fff0f3").place(x=600, y=150)
        lbl_name = Label(self.root, text="Name", font=("king", 20, "bold"), bg="#fff0f3").place(x=600, y=230)
        lbl_course = Label(self.root, text="Select Course", font=("king", 20, "bold"), bg="#fff0f3").place(x=600, y=310)
        lbl_marks = Label(self.root, text="Marks", font=("king", 20, "bold"), bg="#fff0f3").place(x=600, y=390)
        lbl_grade = Label(self.root, text="Grade", font=("king", 20, "bold"), bg="#fff0f3").place(x=600, y=530)

        btn_search = Button(self.root, text='Search', font=("King", 20), bg="#e0d2ef", fg="black", cursor="hand2", command=self.search).place(x=1100, y=150, width=150, height=45)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("king", 20, "bold"), bg="lightyellow", state='readonly').place(x=880, y=230, width=370, height=45)
        txt_marks = Entry(self.root, textvariable=self.var_marks, font=("king", 20, "bold"), bg="lightyellow").place(x=880, y=390, width=370, height=45)
        txt_grade = Entry(self.root, textvariable=self.var_grade, font=("king", 20, "bold"), bg="lightyellow", state='readonly').place(x=880, y=530, width=370, height=45)

        # =====button======
        btn_save = Button(self.root, text="Save", font=("King", 20), bg="#e0d2ef", activebackground="lightgreen", cursor="hand2", command=self.save).place(x=880, y=620, width=150, height=45)
        btn_clear = Button(self.root, text="Clear", font=("King", 20), bg="#ffb3d2", activebackground="lightgrey", cursor="hand2", command=self.clear).place(x=1100, y=620, width=150, height=45)
        btn_calculate_grade = Button(self.root, text="Calculate", font=("King", 20), bg="#e0d2ef", cursor="hand2", command=self.calculate_grade).place(x=970, y=450, width=200, height=45)

    def fetch_id(self):
        conn = sqlite3.connect(database="GradeMaster.db")
        cur = conn.cursor()
        try:
            cur.execute("SELECT id FROM student")
            rows = cur.fetchall()
            if rows:
                self.id_list = [row[0] for row in rows]
                self.txt_student['values'] = self.id_list
        except Exception as ex:
            messagebox.showerror("Error", f"Error fetching student IDs: {str(ex)}")
        finally:
            conn.close()

    def fetch_course(self, event=None):
        conn = sqlite3.connect(database="GradeMaster.db")
        cur = conn.cursor()
        try:
            cur.execute('''SELECT Courses.cid, Courses.course_name 
                        FROM Enrollments 
                        JOIN Courses ON Enrollments.cid = Courses.cid
                        WHERE Enrollments.student_id = ?''', (self.var_id.get(),))
            rows = cur.fetchall()
            if rows:
                self.course_list = [row[1] for row in rows]  # Fetch course names
                self.course_dict = {row[1]: row[0] for row in rows}  # Mapping course name to course ID
                self.txt_course['values'] = self.course_list
        except Exception as ex:
            messagebox.showerror("Error", f"Error fetching courses: {str(ex)}")
        finally:
            conn.close()

    def search(self):
        conn = sqlite3.connect(database="GradeMaster.db")
        cur = conn.cursor()
        try:
            cur.execute("SELECT name FROM student WHERE id=?", (self.var_id.get(),))
            row = cur.fetchone()
            if row:
                self.var_name.set(row[0])
                self.fetch_course()  # Fetch courses for the selected student
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error searching for student: {str(ex)}")
        finally:
            conn.close()

    def course_selected(self, event=None):
        conn = sqlite3.connect(database="GradeMaster.db")
        cur = conn.cursor()
        try:
            course_id = self.course_dict.get(self.var_course_name.get())
            cur.execute("SELECT marks, grade FROM grade WHERE id=? AND course=?", (self.var_id.get(), course_id))
            row = cur.fetchone()
            if row:
                self.var_marks.set(row[0])  # Populate the marks field with the existing value
                self.var_grade.set(row[1])  # Populate the grade field with the existing value
            else:
                self.var_marks.set("")  # Clear the marks field if no data is found
                self.var_grade.set("")  # Clear the grade field if no data is found
        except Exception as ex:
            messagebox.showerror("Error", f"Error fetching course data: {str(ex)}")
        finally:
            conn.close()

    def save(self):
        conn = sqlite3.connect(database="GradeMaster.db")
        cur = conn.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Please first search for a student record", parent=self.root)
            else:
                course_id = self.course_dict.get(self.var_course_name.get())
                # Check if the record exists
                cur.execute("SELECT * FROM grade WHERE id=? AND course=?", (self.var_id.get(), course_id))
                row = cur.fetchone()

                if row:
                    # Update the existing record
                    cur.execute("UPDATE grade SET marks=?, grade=? WHERE id=? AND course=?", (
                        self.var_marks.get(),
                        self.var_grade.get(),
                        self.var_id.get(),
                        course_id
                    ))
                    messagebox.showinfo("Success", "Result updated successfully", parent=self.root)
                else:
                    # Insert a new record
                    cur.execute("INSERT INTO grade (id, name, course, marks, grade) VALUES (?, ?, ?, ?, ?)", (
                        self.var_id.get(),
                        self.var_name.get(),
                        course_id,
                        self.var_marks.get(),
                        self.var_grade.get(),
                    ))
                    messagebox.showinfo("Success", "Result added successfully", parent=self.root)

                conn.commit()
        except Exception as ex:
            messagebox.showerror("Error", f"Error saving result: {str(ex)}")
        finally:
            conn.close()

    def edit(self):
        conn = sqlite3.connect(database="GradeMaster.db")
        cur = conn.cursor()
        try:
            course_id = self.course_dict.get(self.var_course_name.get())
            cur.execute("SELECT marks, grade FROM grade WHERE id=? AND course=?", (self.var_id.get(), course_id))
            row = cur.fetchone()
            if row:
                self.var_marks.set(row[0])  # Populate the marks field with the existing value
                self.var_grade.set(row[1])  # Populate the grade field with the existing value
            else:
                messagebox.showerror("Error", "No record found to edit", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error fetching result for edit: {str(ex)}")
        finally:
            conn.close()

    def clear(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_course_name.set("")
        self.var_marks.set("")
        self.txt_student.set("Select")
        self.txt_course.set("Select")
        self.var_grade.set("")

    def calculate_grade(self):
        try:
            marks = float(self.var_marks.get())
            if marks >= 90:
                grade = "A+"
            elif 80 <= marks < 90:
                grade = "A"
            elif 75 <= marks < 80:
                grade = "A-"
            elif 70 <= marks < 75:
                grade = "B+"
            elif 65 <= marks < 70:
                grade = "B"
            elif 60 <= marks < 65:
                grade = "B-"
            elif 55 <= marks < 60:
                grade = "C+"
            elif 50 <= marks < 55:
                grade = "C"
            elif 45 <= marks < 50:
                grade = "C-"
            elif 40 <= marks < 45:
                grade = "D+"
            elif 35 <= marks < 40:
                grade = "D"
            else:
                grade = "E"
            self.var_grade.set(grade)
        except ValueError:
            messagebox.showerror("Error", "Invalid marks. Please enter a valid number.")

if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = gradeclass(root)
    root.mainloop()
