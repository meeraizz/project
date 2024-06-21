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
        self.root.title("Student Profile")
        self.root.geometry("1600x640+0+200")
        self.root.config(bg='#fff0f3')
        self.root.focus_force()

        # =============Title==================
        title = Label(self.root, text="Student Profile", font=("King", 30, "bold"), bg="#ff80b4", fg="#262626")
        title.place(x=0, y=10, width=1960, height=70)

        self.main_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        self.main_frame.place(x=500, y=100, width=1000, height=500)
        self.create_widgets()

    def create_widgets(self):
        # =====variables====
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()
        self.var_address = StringVar()

        # =====widgets======
        # =======column 1=========
        lbl_id = Label(self.main_frame, text="ID No.", font=("King", 15, "bold"), bg="white")
        lbl_id.place(x=30, y=60)
        self.txt_id = Label(self.main_frame, textvariable=self.var_id, font=("King", 15, "bold"), bg="#fff0f3", anchor='w')
        self.txt_id.place(x=200, y=60, width=250)

        lbl_name = Label(self.main_frame, text="Name", font=("King", 15, "bold"), bg="white")
        lbl_name.place(x=30, y=100)
        self.txt_name = Label(self.main_frame, textvariable=self.var_name, font=("King", 15, "bold"), bg="#fff0f3", anchor='w')
        self.txt_name.place(x=200, y=100, width=250)

        lbl_email = Label(self.main_frame, text="Email", font=("King", 15, "bold"), bg="white")
        lbl_email.place(x=30, y=140)
        self.txt_email = Label(self.main_frame, textvariable=self.var_email, font=("King", 15, "bold"), bg="#fff0f3", anchor='w')
        self.txt_email.place(x=200, y=140, width=250)

        lbl_gender = Label(self.main_frame, text="Gender", font=("King", 15, "bold"), bg="white")
        lbl_gender.place(x=30, y=180)
        self.txt_gender = Label(self.main_frame, textvariable=self.var_gender, font=("King", 15, "bold"), bg="#fff0f3", anchor='w')
        self.txt_gender.place(x=200, y=180, width=250)

        lbl_contact = Label(self.main_frame, text="Contact", font=("King", 15, "bold"), bg="white")
        lbl_contact.place(x=30, y=220)
        self.txt_contact = Label(self.main_frame, textvariable=self.var_contact, font=("King", 15, "bold"), bg="#fff0f3", anchor='w')
        self.txt_contact.place(x=200, y=220, width=250)

        lbl_address = Label(self.main_frame, text="Address", font=("King", 15, "bold"), bg="white")
        lbl_address.place(x=30, y=260)
        self.txt_address = Text(self.main_frame, font=("King", 15, "bold"), bg="#fff0f3", wrap=WORD)
        self.txt_address.place(x=200, y=260, width=250, height=100)

        # =======column 2=========
        lbl_dob = Label(self.main_frame, text="D.O.B", font=("King", 15, "bold"), bg="white")
        lbl_dob.place(x=500, y=60)
        self.txt_dob = Label(self.main_frame, textvariable=self.var_dob, font=("King", 15, "bold"), bg="#fff0f3", anchor='w')
        self.txt_dob.place(x=670, y=60, width=250)

        lbl_state = Label(self.main_frame, text="State", font=("King", 15, "bold"), bg="white")
        lbl_state.place(x=500, y=100)
        self.txt_state = Label(self.main_frame, textvariable=self.var_state, font=("King", 15, "bold"), bg="#fff0f3", anchor='w')
        self.txt_state.place(x=670, y=100, width=250)

        lbl_city = Label(self.main_frame, text="City", font=("King", 15, "bold"), bg="white")
        lbl_city.place(x=500, y=140)
        self.txt_city = Label(self.main_frame, textvariable=self.var_city, font=("King", 15, "bold"), bg="#fff0f3", anchor='w')
        self.txt_city.place(x=670, y=140, width=250)

        lbl_pin = Label(self.main_frame, text="Pin", font=("King", 15, "bold"), bg="white")
        lbl_pin.place(x=500, y=180)
        self.txt_pin = Label(self.main_frame, textvariable=self.var_pin, font=("King", 15, "bold"), bg="#fff0f3", anchor='w')
        self.txt_pin.place(x=670, y=180, width=250)

        # ============= Button ================
        btn_edit = Button(self.main_frame, text="Edit", font=("King", 15, "bold"), bg="#ff80b4", fg="#262626", command=self.edit)
        btn_edit.place(x=720, y=400, width=150, height=35)

        self.load_student_data()

    def edit(self):
        student_data = {
            'id': self.var_id.get(),
            'name': self.var_name.get(),
            'email': self.var_email.get(),
            'gender': self.var_gender.get(),
            'dob': self.var_dob.get(),
            'contact': self.var_contact.get(),
            'state': self.var_state.get(),
            'city': self.var_city.get(),
            'pin': self.var_pin.get(),
            'address': self.txt_address.get("1.0", END).strip()
        }
        new_top = customtkinter.CTkToplevel(self.root)
        new_window = DetailsClass(new_top, student_data=student_data)
        new_top.transient(self.root)
        new_top.grab_set()
        new_top.focus_force()
        self.root.wait_window(new_top)
        self.load_student_data()

    def load_student_data(self):
        con = sqlite3.connect(database="GradeMaster.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM student WHERE id=?", (self.student_id,))
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
                self.txt_address.delete("1.0", END)
                self.txt_address.insert("1.0", row[9])

            else:
                messagebox.showerror("Error", "Student data not found.")
        except Exception as ex:
            messagebox.showerror("Error", f"Error loading student data: {str(ex)}")
        finally:
            con.close()

if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = StudentCard(root, student_id=any)  
    root.mainloop()
