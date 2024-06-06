import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import sqlite3
import customtkinter

# Create a connection to the database and a cursor
conn = sqlite3.connect('Grademaster.db')
cursor = conn.cursor()

# Create the users table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id TEXT PRIMARY KEY,
                    password TEXT NOT NULL,
                    role TEXT NOT NULL
                )''')
conn.commit()

# Function to register a new user
def register():
    user_id = id_entry.get()
    password = password_entry.get()
    role = role_combobox.get()
    
    if not user_id or not password or not role:
        messagebox.showerror(title="Error", message="All fields are required")
        return
    
    try:
        cursor.execute('INSERT INTO users (id, password, role) VALUES (?, ?, ?)', (user_id, password, role))
        conn.commit()
        messagebox.showinfo(title="Success", message="Registration successful")
    except sqlite3.IntegrityError:
        messagebox.showerror(title="Error", message="ID already exists")

# Create the main window
window = tk.Tk()
window.title("Registration")
window.geometry('600x500')
window.configure(bg='#fff0f3')

# Create the UI elements
frame = tk.Frame(window, bg='#fff0f3')

# Image Label
img_label = tk.Label(frame, bg='#fff0f3')

# Registration Form
register_label = tk.Label(frame, text="Registration Form", bg='#fff0f3', fg="#FF69B4", font=("Arial", 24, "bold"))
id_label = tk.Label(frame, text="ID", bg='#fff0f3', fg="#FF69B4", font=("Arial", 14))
id_entry = tk.Entry(frame, font=("Arial", 14), bd=2, relief="groove", width=30)
password_label = tk.Label(frame, text="Password", bg='#fff0f3', fg="#FF69B4", font=("Arial", 14))
password_entry = tk.Entry(frame, show="*", font=("Arial", 14), bd=2, relief="groove", width=30)
role_label = tk.Label(frame, text="Role", bg='#fff0f3', fg="#FF69B4", font=("Arial", 14))
role_combobox = ttk.Combobox(frame, values=["Teacher", "Student"], font=("Arial", 14), width=28)
register_button = tk.Button(frame, text="Submit", bg="#FF69B4", fg="#FFFFFF", font=("Arial", 14), command=register)

# Grid layout for UI elements
img_label.grid(row=0, column=0, rowspan=5, padx=20, pady=20)
register_label.grid(row=0, column=1, columnspan=2, pady=10)
id_label.grid(row=1, column=1, sticky='e')
id_entry.grid(row=1, column=2, pady=10)
password_label.grid(row=2, column=1, sticky='e')
password_entry.grid(row=2, column=2, pady=10)
role_label.grid(row=3, column=1, sticky='e')
role_combobox.grid(row=3, column=2, pady=10)
register_button.grid(row=4, column=1, columnspan=2, pady=30)

frame.pack(expand=True)

window.mainloop()

# Close the database connection when done
conn.close()
