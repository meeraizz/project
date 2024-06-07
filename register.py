from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import sqlite3
import customtkinter


class UserClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Grade Master")
        self.root.geometry("800x600")
        self.root.config(bg='#fff0f3')

        # Variables
        self.user_id = StringVar()
        self.password = StringVar()
        self.role = StringVar()

        # Frame
        self.frame = Frame(self.root, bg='#fff0f3')
        self.frame.pack(expand=True)

        # UI Elements
        register_label = Label(self.frame, text="Registration Form", bg='#fff0f3', fg="#FF69B4", font=("Arial", 24, "bold"))
        id_label = Label(self.frame, text="ID", bg='#fff0f3', fg="#FF69B4", font=("Arial", 14))
        self.id_entry = Entry(self.frame, textvariable=self.user_id, font=("Arial", 14), bd=2, relief="groove", width=30)
        password_label = Label(self.frame, text="Password", bg='#fff0f3', fg="#FF69B4", font=("Arial", 14))
        self.password_entry = Entry(self.frame, show="*", textvariable=self.password, font=("Arial", 14), bd=2, relief="groove", width=30)
        role_label = Label(self.frame, text="Role", bg='#fff0f3', fg="#FF69B4", font=("Arial", 14))
        self.role_combobox = ttk.Combobox(self.frame, textvariable=self.role, values=["Teacher", "Student"], font=("Arial", 14), width=28)
        register_button = Button(self.frame, text="Submit", bg="#FF69B4", fg="#FFFFFF", font=("Arial", 14), command=self.register)

        # Grid layout for UI elements

        register_label.grid(row=0, column=1, columnspan=2, pady=10)
        id_label.grid(row=1, column=1, sticky='e')
        self.id_entry.grid(row=1, column=2, pady=10)
        password_label.grid(row=2, column=1, sticky='e')
        self.password_entry.grid(row=2, column=2, pady=10)
        role_label.grid(row=3, column=1, sticky='e')
        self.role_combobox.grid(row=3, column=2, pady=10)
        register_button.grid(row=4, column=1, columnspan=2, pady=30)

    # Function to register a new user
    def register(self):
        conn = sqlite3.connect(database="GradeMaster.db")
        cur = conn.cursor()
        user_id = self.user_id.get()
        password = self.password.get()
        role = self.role.get()

        if not user_id or not password or not role:
            messagebox.showerror(title="Error", message="All fields are required")
            return

        try:
            cur.execute('INSERT INTO users (id, password, role) VALUES (?, ?, ?)', (user_id, password, role))
            conn.commit()
            messagebox.showinfo(title="Success", message="Registration successful")
        except sqlite3.IntegrityError:
            messagebox.showerror(title="Error", message="ID already exists")

if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = UserClass(root)  
    root.mainloop()


