import sqlite3
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
from student_details import DetailsClass
import customtkinter

class StudentCard:
    def __init__(self, root, student_id):
        self.root = root
        self.student_id = student_id
        self.root.title("Grade Master")
        self.root.geometry("1350x750+50+200")
        self.root.config(bg='#fff0f3')
        self.root.focus_force()

        # =============Title==================
        title = Label(self.root, text="Profile", font=("King", 30, "bold"), bg="#ff80b4", fg="#262626")
        title.place(x=0, y=10, width=1960, height=70)

        self.main_frame = Frame(self.root, bg="#fff0f3")
        self.main_frame.pack(fill=BOTH, expand=True)

        self.create_widgets()

    def create_widgets(self):
        # =====title======
        title = Label(self.main_frame, text="Manage Student Details", font=("king", 23, "bold"), bg="#FFB3D2", fg="black")
        title.pack(fill=X)  

        # =====variables====
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_a_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()
        self.var_address = StringVar()

        # =====widgets======
        # =======column 1=========
        lbl_id = Label(self.root, text="ID No.", font=("king", 15, "bold"), bg="#fff0f3")
        lbl_id.place(x=450, y=60)

        txt_id = Entry(self.root, textvariable=self.var_id, font=("king", 15, "bold"), bg="lightyellow", state='readonly')
        txt_id.place(x=600, y=60, width=170)

        lbl_name = Label(self.root, text="Name", font=("king", 15, "bold"), bg="#fff0f3")
        lbl_name.place(x=450, y=100)                     
        lbl_email = Label(self.root, text="Email", font=("king", 15, "bold"), bg="#fff0f3")
        lbl_email.place(x=450, y=140)
        lbl_gender = Label(self.root, text="Gender", font=("king", 15, "bold"), bg="#fff0f3")
        lbl_gender.place(x=450, y=180)

        lbl_state = Label(self.root, text="State", font=("king", 15, "bold"), bg="#fff0f3")
        lbl_state.place(x=450, y=220)
        txt_state = Entry(self.root, textvariable=self.var_state, font=("king", 15, "bold"), bg="lightyellow", state='readonly')
        txt_state.place(x=600, y=220, width=150)

        lbl_city = Label(self.root, text="City", font=("king", 15, "bold"), bg="#fff0f3")
        lbl_city.place(x=760, y=220)
        txt_city = Entry(self.root, textvariable=self.var_city, font=("king", 15, "bold"), bg="lightyellow", state='readonly')
        txt_city.place(x=840, y=220, width=150)

        lbl_pin = Label(self.root, text="Pin", font=("king", 15, "bold"), bg="#fff0f3")
        lbl_pin.place(x=1000, y=220)
        txt_pin = Entry(self.root, textvariable=self.var_pin, font=("king", 15, "bold"), bg="lightyellow", state='readonly')
        txt_pin.place(x=1100, y=220, width=100)

        lbl_address = Label(self.root, text="Address", font=("king", 15, "bold"), bg="#fff0f3")
        lbl_address.place(x=450, y=260)

        # ====entry fields====
        txt_name = Entry(self.root, textvariable=self.var_name, font=("king", 15, "bold"), bg="lightyellow", state='readonly')
        txt_name.place(x=600, y=100, width=200)
        txt_email = Entry(self.root, textvariable=self.var_email, font=("king", 15, "bold"), bg="lightyellow", state='readonly')
        txt_email.place(x=600, y=140, width=200)
        self.txt_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Select", "Male", "Female"), font=("king", 15, "bold"), state='readonly', justify=CENTER)
        self.txt_gender.place(x=600, y=180, width=200)
        self.txt_gender.current(0)
        # =======column 2=========
        lbl_dob = Label(self.root, text="D.O.B", font=("king", 15, "bold"), bg="#fff0f3")
        lbl_dob.place(x=900, y=60)
        lbl_contact = Label(self.root, text="Contact", font=("king", 15, "bold"), bg="#fff0f3")
        lbl_contact.place(x=840, y=100)                     
        lbl_admission = Label(self.root, text="Admission", font=("king", 15, "bold"), bg="#fff0f3")
        lbl_admission.place(x=840, y=140)
        lbl_course = Label(self.root, text="Course", font=("king", 15, "bold"), bg="#fff0f3")
        lbl_course.place(x=840, y=180)

        # ====entry fields 2====
        self.course_list = []

        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("king", 15, "bold"), bg="lightyellow", state='readonly')
        txt_dob.place(x=1000, y=60, width=200)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("king", 15, "bold"), bg="lightyellow", state='readonly')
        txt_contact.place(x=1000, y=100, width=200)
        txt_admission = Entry(self.root, textvariable=self.var_a_date, font=("king", 15, "bold"), bg="lightyellow", state='readonly')
        txt_admission.place(x=1000, y=140, width=200)
        self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course, values=(" "), font=("king", 15, "bold"), state='readonly', justify=CENTER)
        self.txt_course.place(x=1000, y=180, width=200)
        self.txt_course.set("Select")

        # ====text address=====
        self.txt_address = Text(self.root, font=("king", 15, "bold"), bg="lightyellow", state='normal')
        self.txt_address.place(x=600, y=260,  width=600, height=100)

        # ============= Button ================
        btn_edit = Button(self.root, text="Edit", font=("King", 15, "bold"), bg="#ff80b4", fg="#262626", command=self.edit)
        btn_edit.place(x=1000, y=500, width=150, height=35)

        self.load_student_data()

    def edit(self):
        student_data = {
            'id': self.var_id.get(),
            'name': self.var_name.get(),
            'email': self.var_email.get(),
            'contact': self.var_contact.get(),
            'course': self.var_course.get(),
            'gender': self.var_gender.get(),
            'dob': self.var_dob.get(),
            'admission': self.var_a_date.get(),
            'state': self.var_state.get(),
            'city': self.var_city.get(),
            'pin': self.var_pin.get(),
            'address': self.txt_address.get("1.0", END)
        }
        new_top = customtkinter.CTkToplevel(self.root)
        new_window = DetailsClass(new_top, student_data=student_data)
        new_top.transient(self.root)
        new_top.grab_set()
        new_top.focus_force()
        new_top.wait_window()  # Wait for the edit window to close
        self.load_student_data()  # Reload data

    def load_student_data(self):
        con = sqlite3.connect(database="GradeMaster.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM users WHERE id=?", (self.student_id,))
            row = cur.fetchone()
            if row:
                self.var_id.set(row[0])
                self.var_name.set(row[1])
                self.var_email.set(row[2])
                self.var_gender.set(row[3])
                self.var_dob.set(row[4])
                self.var_contact.set(row[5])
                self.var_state.set(row[6])
                self.var_city.set(row[7])
                self.var_pin.set(row[8])
                self.var_address.set(row[9])
            else:
                messagebox.showerror("Error", "Student data not found.")
        except Exception as ex:
            messagebox.showerror("Error", f"Error loading student data: {str(ex)}")
        finally:
            con.close()

if __name__ == "__main__":
    root = customtkinter.CTk()
    student_id = "1221109567"  # Replace with the actual student ID
    obj = StudentCard(root, student_id=any)
    root.mainloop()