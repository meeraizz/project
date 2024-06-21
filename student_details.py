import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
import customtkinter

class DetailsClass:
    def __init__(self, root, student_data=None):
        self.root = root
        self.root.title("Grade Master")
        self.root.geometry("1350x500+50+200")
        self.root.config(bg="#fff0f3")
        self.root.focus_force()

        self.main_frame = Frame(self.root, bg="#fff0f3")
        self.main_frame.pack(fill=BOTH, expand=True)

        self.create_widgets()
        if student_data:
            self.populate_data(student_data)

    def create_widgets(self):
        # Title
        title = Label(self.main_frame, text="Manage Student Details", font=("king", 23, "bold"), bg="#FFB3D2", fg="black")
        title.pack(fill=X, padx=20, pady=10)

        # Variables
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()

        # Entry fields and labels
        lbl_id = Label(self.main_frame, text="ID No.", font=("king", 15, "bold"), bg="#fff0f3")
        lbl_id.place(x=450, y=60)
        txt_id = Entry(self.main_frame, textvariable=self.var_id, font=("king", 15, "bold"), bg="lightyellow")
        txt_id.place(x=600, y=60, width=200)

        lbl_name = Label(self.main_frame, text="Name", font=("king", 15, "bold"), bg="#fff0f3")
        lbl_name.place(x=450, y=100)
        txt_name = Entry(self.main_frame, textvariable=self.var_name, font=("king", 15, "bold"), bg="lightyellow")
        txt_name.place(x=600, y=100, width=200)

        lbl_email = Label(self.main_frame, text="Email", font=("king", 15, "bold"), bg="#fff0f3")
        lbl_email.place(x=450, y=140)
        txt_email = Entry(self.main_frame, textvariable=self.var_email, font=("king", 15, "bold"), bg="lightyellow")
        txt_email.place(x=600, y=140, width=200)

        lbl_gender = Label(self.main_frame, text="Gender", font=("king", 15, "bold"), bg="#fff0f3")
        lbl_gender.place(x=450, y=180)
        self.txt_gender = ttk.Combobox(self.main_frame, textvariable=self.var_gender, values=("Select", "Male", "Female"),
                                       font=("king", 15, "bold"), state='readonly', justify=CENTER)
        self.txt_gender.place(x=600, y=180, width=200)
        self.txt_gender.current(0)

        lbl_dob = Label(self.main_frame, text="D.O.B", font=("king", 15, "bold"), bg="#fff0f3")
        lbl_dob.place(x=840, y=60)
        txt_dob = Entry(self.main_frame, textvariable=self.var_dob, font=("king", 15, "bold"), bg="lightyellow")
        txt_dob.place(x=1000, y=60, width=200)

        lbl_contact = Label(self.main_frame, text="Contact", font=("king", 15, "bold"), bg="#fff0f3")
        lbl_contact.place(x=840, y=100)
        txt_contact = Entry(self.main_frame, textvariable=self.var_contact, font=("king", 15, "bold"), bg="lightyellow")
        txt_contact.place(x=1000, y=100, width=200)


        lbl_state = Label(self.main_frame, text="State", font=("king", 15, "bold"), bg="#fff0f3")
        lbl_state.place(x=450, y=220)
        txt_state = Entry(self.main_frame, textvariable=self.var_state, font=("king", 15, "bold"), bg="lightyellow")
        txt_state.place(x=600, y=220, width=150)

        lbl_city = Label(self.main_frame, text="City", font=("king", 15, "bold"), bg="#fff0f3")
        lbl_city.place(x=760, y=220)
        txt_city = Entry(self.main_frame, textvariable=self.var_city, font=("king", 15, "bold"), bg="lightyellow")
        txt_city.place(x=840, y=220, width=150)

        lbl_pin = Label(self.main_frame, text="Pin", font=("king", 15, "bold"), bg="#fff0f3")
        lbl_pin.place(x=1000, y=220)
        txt_pin = Entry(self.main_frame, textvariable=self.var_pin, font=("king", 15, "bold"), bg="lightyellow")
        txt_pin.place(x=1100, y=220, width=100)

        lbl_address = Label(self.main_frame, text="Address", font=("king", 15, "bold"), bg="#fff0f3")
        lbl_address.place(x=450, y=260)
        self.txt_address = Text(self.main_frame, font=("king", 15, "bold"), bg="lightyellow")
        self.txt_address.place(x=600, y=260, width=600, height=100)

        # Button
        btn_save = Button(self.main_frame, text="Save", font=("king", 15, "bold"), bg="#FF0090", fg="#fff0f3", cursor="hand2", command=self.save)
        btn_save.place(x=1090, y=400, width=110, height=40)

    #=========================================================================
    def populate_data(self, data):
        self.var_id.set(data.get('id', ''))
        self.var_name.set(data.get('name', ''))
        self.var_email.set(data.get('email', ''))
        self.var_gender.set(data.get('gender', ''))
        self.var_dob.set(data.get('dob', ''))
        self.var_contact.set(data.get('contact', ''))
        self.var_state.set(data.get('state', ''))
        self.var_city.set(data.get('city', ''))
        self.var_pin.set(data.get('pin', ''))
        self.txt_address.delete(1.0, END)
        self.txt_address.insert(END, data.get('address', ''))

    def save(self):
        try:
            con = sqlite3.connect('GradeMaster.db')
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS student (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            email TEXT,
                            gender TEXT,
                            dob TEXT,
                            contact INTEGER,
                            state TEXT,
                            city TEXT,
                            pin INTEGER,
                            address TEXT)""")

            if self.var_id.get():
                cur.execute("""UPDATE student SET name=?, email=?, gender=?, dob=?, contact=?, 
                            state=?, city=?, pin=?, address=? WHERE id=?""",
                            (self.var_name.get(), self.var_email.get(), self.var_gender.get(),
                            self.var_dob.get(), self.var_contact.get(),
                             self.var_state.get(), self.var_city.get(),
                            self.var_pin.get(), self.txt_address.get("1.0", END), self.var_id.get()))
                messagebox.showinfo("Success", "Student profile updated successfully")
            else:
                cur.execute("""INSERT INTO student (name, email, gender, dob, contact,
                            state, city, pin, address) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                            (self.var_name.get(), self.var_email.get(), self.var_gender.get(),
                            self.var_dob.get(), self.var_contact.get(), 
                             self.var_state.get(), self.var_city.get(),
                            self.var_pin.get(), self.txt_address.get("1.0", END)))
                messagebox.showinfo("Success", "Student profile submitted successfully")

            con.commit()
            self.close_window()
            print("Data saved successfully.")
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error interacting with database: {e}")
            print(f"Error interacting with database: {e}")
        finally:
            con.close()

    def close_window(self):
        self.root.destroy() 

if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = DetailsClass(root)
    root.mainloop()