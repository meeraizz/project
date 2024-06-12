from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import sqlite3
import customtkinter
from student_dashboard import GradeMaster as StudentDashboard
from teacher_dashboard import GradeMastertc as TeacherDashboard 

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
        self.id_entry = Entry(self.frame, font=("Arial", 16), bd=2, relief="groove", width=25)
        self.password_entry = Entry(self.frame, show="*", font=("Arial", 16), bd=2, relief="groove", width=25)
        role_label = Label(self.frame, text="Role", bg='#fff0f3', fg="#FF69B4", font=("Arial", 14))
        self.role = StringVar()
        self.role_combobox = ttk.Combobox(self.frame, textvariable=self.role, values=["Teacher", "Student"], font=("Arial", 14), width=28)
        login_button = Button(self.frame, text="Login", bg="#FF69B4", fg="#FFFFFF", font=("Arial", 16), command=self.login)
        logout_button = Button(self.frame, text="Logout", bg="#FF69B4", fg="#FFFFFF", font=("Arial", 16), command=self.logout)

        # Grid layout for UI elements
        login_label.grid(row=0, column=1, columnspan=2, pady=10)
        self.id_entry.grid(row=1, column=1, columnspan=2, pady=10)
        self.password_entry.grid(row=2, column=1, columnspan=2, pady=10)
        role_label.grid(row=3, column=1, sticky='e')
        self.role_combobox.grid(row=3, column=2, pady=10)
        login_button.grid(row=4, column=1, pady=30)
        logout_button.grid(row=4, column=2, pady=30)

    # Function to verify login credentials
    def login(self):
        conn = sqlite3.connect("GradeMaster.db")
        cur = conn.cursor()
        user_id = self.id_entry.get()
        password = self.password_entry.get()
        role = self.role.get()
        cur.execute('SELECT * FROM users WHERE id = ? AND password = ? AND role = ?', (user_id, password, role))
        user_data = cur.fetchone()
        if user_data:
            messagebox.showinfo(title="Login Success", message="You successfully logged in.")
            self.root.destroy()  # Close the login window
            if role == "Student":
                root = customtkinter.CTk()
                app = StudentDashboard(root)
                root.mainloop()
            elif role == "Teacher":
                root = customtkinter.CTk()
                app = TeacherDashboard(root, teacher_id=user_id)  # Pass the teacher_id to the dashboard
                root.mainloop()
        else:
            messagebox.showerror(title="Error", message="Invalid login")
        conn.close()

    # Function to clear username and password fields (logout)
    def logout(self):
        self.id_entry.delete(0, END)
        self.password_entry.delete(0, END)

if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = LoginClass(root)  
    root.mainloop()
