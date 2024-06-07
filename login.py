from tkinter import *
from tkinter import messagebox, ttk
import sqlite3
import customtkinter
from student_dashboard import GradeMaster as StudentDashboard
from teacher_dashboard import GradeMastertc as TeacherDashboard
from register import UserClass  

class LoginClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Grade Master")
        self.root.geometry("800x600")
        self.root.config(bg='#fff0f3')

        # Frame
        self.frame = Frame(self.root, bg='#fff0f3')
        self.frame.pack(expand=True)

        # Login Form
        login_label = Label(self.frame, text="User Login", bg='#FF69B4', fg="#FFFFFF", font=("Arial", 24, "bold"))
        id_label = Label(self.frame, text="ID", bg='#fff0f3', fg="#FF69B4", font=("Arial", 14))
        self.id_entry = Entry(self.frame, font=("Arial", 16), bd=2, relief="groove", width=25)
        password_label = Label(self.frame, text="Password", bg='#fff0f3', fg="#FF69B4", font=("Arial", 14))
        self.password_entry = Entry(self.frame, show="*", font=("Arial", 16), bd=2, relief="groove", width=25)
        role_label = Label(self.frame, text="Role", bg='#fff0f3', fg="#FF69B4", font=("Arial", 14))
        self.role = StringVar()
        self.role_combobox = ttk.Combobox(self.frame, textvariable=self.role, values=["Teacher", "Student"], font=("Arial", 14), width=28)
        login_button = Button(self.frame, text="Login", bg="#FF69B4", fg="#FFFFFF", font=("Arial", 16), command=self.login)
        register_button = Button(self.frame, text="Register", bg="#FF69B4", fg="#FFFFFF", font=("Arial", 16), command=self.open_register_window)

        # Grid layout for UI elements
        login_label.grid(row=0, column=1, columnspan=2, pady=10)
        id_label.grid(row=1, column=1, sticky='e', padx=10)
        self.id_entry.grid(row=1, column=2, pady=10)
        password_label.grid(row=2, column=1, sticky='e', padx=10)
        self.password_entry.grid(row=2, column=2, pady=10)
        role_label.grid(row=3, column=1, sticky='e', padx=10)
        self.role_combobox.grid(row=3, column=2, pady=10)
        login_button.grid(row=4, column=1, pady=30)
        register_button.grid(row=4, column=2, pady=30)

    # Function to verify login credentials
    def login(self):
        conn = sqlite3.connect("GradeMaster.db")
        cur = conn.cursor()
        user_id = self.id_entry.get()
        password = self.password_entry.get()
        role = self.role.get()
        cur.execute('SELECT * FROM users WHERE id = ? AND password = ? AND role = ?', (user_id, password, role))
        if cur.fetchone():
            messagebox.showinfo(title="Login Success", message="You successfully logged in.")
            self.root.destroy()  # Close the login window
            if role == "Student":
                root = customtkinter.CTk()
                app = StudentDashboard(root)
                root.mainloop()
            elif role == "Teacher":
                root = customtkinter.CTk()
                app = TeacherDashboard(root)
                root.mainloop()
        else:
            messagebox.showerror(title="Error", message="Invalid login")
        conn.close()

    # Function to open the registration window
    def open_register_window(self):
        register_window = Toplevel(self.root)
        register_window.title("Register")
        register_window.geometry("800x600")
        UserClass(register_window)

if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = LoginClass(root)
    root.mainloop()
