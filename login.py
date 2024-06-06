import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

# Create a connection to the database and a cursor
conn = sqlite3.connect('Grademaster.db')
cursor = conn.cursor()

# Create the users table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password TEXT NOT NULL
                )''')
conn.commit()

# Insert sample user data (uncomment to insert initially, then comment again)
# cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('1234567890', 'mmustudent'))
# conn.commit()

# Function to verify login credentials
def login():
    username = username_entry.get()
    password = password_entry.get()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    if cursor.fetchone():
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
    else:
        messagebox.showerror(title="Error", message="Invalid login")

# Create the main window
window = tk.Tk()
window.title("Login")
window.geometry('800x600')  # Adjust size as needed
window.configure(bg='#fff0f3')

# Load and display the image
img_path = "/mnt/data/user-login-page-with-two-characters-vector.jpg"  # Ensure the image path is correct
img = Image.open('login.png')
img = img.resize((350, 350), )
photo = ImageTk.PhotoImage(img)

# Create the UI elements
frame = tk.Frame(window, bg='#fff0f3')

# Image Label
img_label = tk.Label(frame, image=photo, bg='#fff0f3')

# Login Form
login_label = tk.Label(frame, text="User Login", bg='#FF69B4', fg="#FFFFFF", font=("Arial", 24, "bold"))
username_entry = tk.Entry(frame, font=("Arial", 16), bd=2, relief="groove", width=25)
password_entry = tk.Entry(frame, show="*", font=("Arial", 16), bd=2, relief="groove", width=25)
login_button = tk.Button(frame, text="Login", bg="#FF69B4", fg="#FFFFFF", font=("Arial", 16), command=login)

# Grid layout for UI elements
img_label.grid(row=0, column=0, rowspan=5, padx=20, pady=20)
login_label.grid(row=0, column=1, columnspan=2, pady=10)
username_entry.grid(row=1, column=1, columnspan=2, pady=10)
password_entry.grid(row=2, column=1, columnspan=2, pady=10)
login_button.grid(row=3, column=1, columnspan=2, pady=30)

frame.pack(expand=True)

window.mainloop()

# Close the database connection when done
conn.close()
