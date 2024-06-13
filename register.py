import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
import customtkinter
from tkcalendar import DateEntry  # To include a date picker for Date of Birth

# Create the main database and tables if they don't exist
def create_db():
    conn = sqlite3.connect('Grademaster.db')
    cursor = conn.cursor()
    
    # Create Students table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Students
                      (student_id INTEGER PRIMARY KEY, name TEXT, contact_number TEXT, email TEXT, gender TEXT, dob TEXT, address TEXT, state TEXT, postcode TEXT, password TEXT)''')
    
    # Create Teachers table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Teachers
                      (teacher_id INTEGER PRIMARY KEY, name TEXT, contact_number TEXT, email TEXT, gender TEXT, dob TEXT, address TEXT, state TEXT, postcode TEXT, password TEXT)''')
    
    conn.commit()
    conn.close()

create_db()

# Register class for registering new users
class RegisterClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Register User")
        self.root.geometry("900x700+200+100")
        self.root.config(bg='#fff0f3')

        # Title Frame
        title_frame = tk.Frame(self.root, bg="#ff80b4")
        title_frame.place(x=0, y=10, width=900, height=70)
        title = tk.Label(title_frame, text="Register User", font=("King", 30, "bold"), bg="#ff80b4", fg="#262626")
        title.pack(fill=tk.BOTH, expand=True)

        # Variables
        self.var_id = tk.StringVar()
        self.var_name = tk.StringVar()
        self.var_contact = tk.StringVar()
        self.var_email = tk.StringVar()
        self.var_gender = tk.StringVar()
        self.var_dob = tk.StringVar()
        self.var_address = tk.StringVar()
        self.var_state = tk.StringVar()
        self.var_postcode = tk.StringVar()
        self.var_password = tk.StringVar()
        self.var_user_type = tk.StringVar()

        # Left column labels and entries
        lbl_id = tk.Label(self.root, text="ID Number", font=("king", 15, "bold"), bg="#fff0f3").place(x=50, y=100)
        self.entry_id = tk.Entry(self.root, textvariable=self.var_id, font=("king", 15))
        self.entry_id.place(x=250, y=100, width=200)
        
        lbl_name = tk.Label(self.root, text="Name", font=("king", 15, "bold"), bg="#fff0f3").place(x=50, y=140)
        self.entry_name = tk.Entry(self.root, textvariable=self.var_name, font=("king", 15))
        self.entry_name.place(x=250, y=140, width=200)
        
        lbl_contact = tk.Label(self.root, text="Contact Number", font=("king", 15, "bold"), bg="#fff0f3").place(x=50, y=180)
        self.entry_contact = tk.Entry(self.root, textvariable=self.var_contact, font=("king", 15))
        self.entry_contact.place(x=250, y=180, width=200)
        
        lbl_email = tk.Label(self.root, text="Email", font=("king", 15, "bold"), bg="#fff0f3").place(x=50, y=220)
        self.entry_email = tk.Entry(self.root, textvariable=self.var_email, font=("king", 15))
        self.entry_email.place(x=250, y=220, width=200)
        
        lbl_gender = tk.Label(self.root, text="Gender", font=("king", 15, "bold"), bg="#fff0f3").place(x=50, y=260)
        self.cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=["Male", "Female"], font=("king", 15), state='readonly')
        self.cmb_gender.place(x=250, y=260, width=200)
        self.cmb_gender.set("Select")
        
        lbl_dob = tk.Label(self.root, text="Date of Birth", font=("king", 15, "bold"), bg="#fff0f3").place(x=50, y=300)
        self.entry_dob = DateEntry(self.root, textvariable=self.var_dob, font=("king", 15), date_pattern='y-mm-dd')
        self.entry_dob.place(x=250, y=300, width=200)

        # Right column labels and entries
        lbl_address = tk.Label(self.root, text="Address", font=("king", 15, "bold"), bg="#fff0f3").place(x=500, y=100)
        self.entry_address = tk.Entry(self.root, textvariable=self.var_address, font=("king", 15))
        self.entry_address.place(x=650, y=100, width=200)
        
        lbl_state = tk.Label(self.root, text="State", font=("king", 15, "bold"), bg="#fff0f3").place(x=500, y=140)
        self.entry_state = tk.Entry(self.root, textvariable=self.var_state, font=("king", 15))
        self.entry_state.place(x=650, y=140, width=200)
        
        lbl_postcode = tk.Label(self.root, text="Postcode", font=("king", 15, "bold"), bg="#fff0f3").place(x=500, y=180)
        self.entry_postcode = tk.Entry(self.root, textvariable=self.var_postcode, font=("king", 15))
        self.entry_postcode.place(x=650, y=180, width=200)
        
        lbl_user_type = tk.Label(self.root, text="User Type", font=("king", 15, "bold"), bg="#fff0f3").place(x=500, y=220)
        self.cmb_user_type = ttk.Combobox(self.root, textvariable=self.var_user_type, values=["Student", "Teacher"], font=("king", 15), state='readonly')
        self.cmb_user_type.place(x=650, y=220, width=200)
        self.cmb_user_type.set("Select")
        
        lbl_password = tk.Label(self.root, text="Password", font=("king", 15, "bold"), bg="#fff0f3").place(x=500, y=260)
        self.entry_password = tk.Entry(self.root, textvariable=self.var_password, font=("king", 15), show='*')
        self.entry_password.place(x=650, y=260, width=200)

        btn_register = tk.Button(self.root, text="Register", font=("King", 20), bg="#e0d2ef", activebackground="lightgreen", cursor="hand2", command=self.register_user)
        btn_register.place(x=375, y=350, width=150, height=45)

    def register_user(self):
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

        conn = sqlite3.connect('Grademaster.db')
        cursor = conn.cursor()
        
        cursor.execute(f'''INSERT INTO {table_name} 
                           (name, contact_number, email, gender, dob, address, state, postcode, password)
                           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (self.var_name.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_address.get(),
                        self.var_state.get(),
                        self.var_postcode.get(),
                        self.var_password.get()))
        
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", f"{self.var_user_type.get()} registered successfully!")
        self.clear_fields()

    def clear_fields(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_address.set("")
        self.var_state.set("")
        self.var_postcode.set("")
        self.var_password.set("")
        self.var_user_type.set("Select")

# Main application window
if __name__ == "__main__":
    root = customtkinter.CTk()
    register_obj = RegisterClass(root)
    root.mainloop()
