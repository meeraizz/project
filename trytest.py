import sqlite3
from customtkinter import CTk
from tkinter import *
from tkinter import ttk, messagebox, filedialog

class ProfilePage:
    def __init__(self, teacher_id):
        self.root = CTk()
        self.root.title("Profile Page")
        self.root.geometry("400x300")

        # Connect to the database
        self.conn = sqlite3.connect("GradeMaster.db")
        self.cur = self.conn.cursor()

        # Retrieve user data based on user_id
        self.cur.execute("SELECT * FROM teacher WHERE id=?", (teacher_id,))
        teacher_data = self.cur.fetchone()

        if teacher_data:
            self.display_profile(teacher_data)
        else:
            messagebox.showerror("Error", "User data not found.")

    def display_profile(self, teacher_data):
        # Display user information
        Label(self.root, text="Name:").pack()
        Label(self.root, text=teacher_data[1]).pack()

        Label(self.root, text="Email:").pack()
        Label(self.root, text=teacher_data[2]).pack()

        Label(self.root, text="Contact:").pack()
        Label(self.root, text=teacher_data[3]).pack()

        Label(self.root, text="Role:").pack()
        Label(self.root, text=teacher_data[4]).pack()

if __name__ == "__main__":
    # Example user_id for testing purposes
    teacher_id = 121
    profile_page = ProfilePage(teacher_id)
    profile_page.root.mainloop()
