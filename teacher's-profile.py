import sqlite3
import tkinter as tk
from tkinter import ttk

class TeacherApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Teacher Details")

        self.create_db()
        self.create_table()
        self.populate_table()

    def create_db(self):
        self.connection = sqlite3.connect('GradeMaster.db')
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.tree = ttk.Treeview(self, columns=('Name', 'Subject', 'Experience', 'Email'))
        self.tree.heading('#0', text='ID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Subject', text='Subject')
        self.tree.heading('Experience', text='Experience')
        self.tree.heading('Email', text='Email')
        self.tree.pack(fill='both', expand=True)

    def populate_table(self):
        self.cursor.execute("SELECT * FROM teacher")
        for row in self.cursor.fetchall():
            self.tree.insert('', 'end', text=row[0], values=row[1:])

if __name__ == "__main__":
    app = TeacherApp()
    app.mainloop()
