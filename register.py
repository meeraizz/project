from tkinter import *
from tkinter import messagebox, ttk
import customtkinter
from tkcalendar import DateEntry 
import sqlite3

class RegisterClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Register User")
        self.root.geometry("900x700+200+100")
        self.root.config(bg='#fff0f3')

        # Title Frame
        title_frame = Frame(self.root, bg="#ff80b4")
        title_frame.place(x=0, y=10, width=900, height=70)
        title = Label(title_frame, text="Register User", font=("King", 30, "bold"), bg="#ff80b4", fg="#262626")
        title.pack(fill=BOTH, expand=True)

        # Variables
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_address = StringVar()
        self.var_state = StringVar()
        self.var_pin = StringVar()
        self.var_password = StringVar()
        self.var_user_type = StringVar()

        # Left column labels and entries
        lbl_id = Label(self.root, text="ID Number", font=("king", 15, "bold"), bg="#fff0f3").place(x=50, y=100)
        self.entry_id = Entry(self.root, textvariable=self.var_id, font=("king", 15))
        self.entry_id.place(x=250, y=100, width=200)
        
        lbl_name = Label(self.root, text="Name", font=("king", 15, "bold"), bg="#fff0f3").place(x=50, y=140)
        self.entry_name = Entry(self.root, textvariable=self.var_name, font=("king", 15))
        self.entry_name.place(x=250, y=140, width=200)
        
        lbl_contact = Label(self.root, text="Contact Number", font=("king", 15, "bold"), bg="#fff0f3").place(x=50, y=180)
        self.entry_contact = Entry(self.root, textvariable=self.var_contact, font=("king", 15))
        self.entry_contact.place(x=250, y=180, width=200)
        
        lbl_email = Label(self.root, text="Email", font=("king", 15, "bold"), bg="#fff0f3").place(x=50, y=220)
        self.entry_email = Entry(self.root, textvariable=self.var_email, font=("king", 15))
        self.entry_email.place(x=250, y=220, width=200)
        
        lbl_gender = Label(self.root, text="Gender", font=("king", 15, "bold"), bg="#fff0f3").place(x=50, y=260)
        self.cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=["Male", "Female"], font=("king", 15), state='readonly')
        self.cmb_gender.place(x=250, y=260, width=200)
        self.cmb_gender.set("Select")
        
        lbl_dob = Label(self.root, text="Date of Birth", font=("king", 15, "bold"), bg="#fff0f3").place(x=50, y=300)
        self.entry_dob = DateEntry(self.root, textvariable=self.var_dob, font=("king", 15), date_pattern='y-mm-dd')
        self.entry_dob.place(x=250, y=300, width=200)

        # Right column labels and entries
        lbl_address = Label(self.root, text="Address", font=("king", 15, "bold"), bg="#fff0f3").place(x=500, y=100)
        self.entry_address = Entry(self.root, textvariable=self.var_address, font=("king", 15))
        self.entry_address.place(x=650, y=100, width=200)
        
        lbl_state = Label(self.root, text="State", font=("king", 15, "bold"), bg="#fff0f3").place(x=500, y=140)
        self.entry_state = Entry(self.root, textvariable=self.var_state, font=("king", 15))
        self.entry_state.place(x=650, y=140, width=200)
        
        lbl_pin = Label(self.root, text="Postcode", font=("king", 15, "bold"), bg="#fff0f3").place(x=500, y=180)
        self.entry_pin = Entry(self.root, textvariable=self.var_pin, font=("king", 15))
        self.entry_pin.place(x=650, y=180, width=200)
        
        lbl_user_type = Label(self.root, text="User Type", font=("king", 15, "bold"), bg="#fff0f3").place(x=500, y=220)
        self.cmb_user_type = ttk.Combobox(self.root, textvariable=self.var_user_type, values=["Student", "Teacher"], font=("king", 15), state='readonly')
        self.cmb_user_type.place(x=650, y=220, width=200)
        self.cmb_user_type.set("Select")
        
        lbl_password = Label(self.root, text="Password", font=("king", 15, "bold"), bg="#fff0f3").place(x=500, y=260)
        self.entry_password = Entry(self.root, textvariable=self.var_password, font=("king", 15), show='*')
        self.entry_password.place(x=650, y=260, width=200)

        btn_register = Button(self.root, text="Register", font=("King", 20), bg="#e0d2ef", activebackground="lightgreen", cursor="hand2", command=self.register_user)
        btn_register.place(x=375, y=350, width=150, height=45)

    def register_user(self):
        print("Register button clicked")  # Debugging statement
        if self.var_user_type.get() == "Select":
            messagebox.showerror("Error", "Please select user type (Student/Teacher)")
            return

        if self.var_user_type.get() == "Student":
            table_name = "Students"
        elif self.var_user_type.get() == "Teacher":
            table_name = "Teachers"
        else:
            messagebox.showerror("Error", "Invalid user type")
            return

        try:
            conn = sqlite3.connect('Grademaster.db')
            cursor = conn.cursor()
            print("Database connection successful")  # Debugging statement
            
            cursor.execute(f'''INSERT INTO users
                            (name, contact, email, gender, dob, address, state, pin, password)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                        (self.var_name.get(),
                            self.var_contact.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_address.get(),
                            self.var_state.get(),
                            self.var_pin.get(),
                            self.var_password.get()))
            
            conn.commit()
            conn.close()
            print("User registered successfully")  # Debugging statement

            messagebox.showinfo("Success", f"{self.var_user_type.get()} registered successfully!")
            self.clear_fields()

            print("Destroying window")  # Debugging statement
            # Destroy current window
            self.root.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            print(f"Error: {str(e)}")  # Debugging statement

    def clear_fields(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_address.set("")
        self.var_state.set("")
        self.var_pin.set("")
        self.var_password.set("")
        self.var_user_type.set("Select")


if __name__ == "__main__":
    root = customtkinter.CTk()
    register_obj = RegisterClass(root)
    root.mainloop()
