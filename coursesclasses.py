import tkinter as tk
from tkinter import Listbox, simpledialog, messagebox

class GradeMasterApp
 def __init__(self, root):
        self.root = root
        self.root.tile("Courses")

        self.subjects = []

        self.listbox = tk.Listbox(root)
        self.listbox.pack(fill=tk.Both, expand=1) 

        self.add_button = tk.Button(root, text="Add Subject", command=self.add_subject)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(root, text="Delete Subject", command=self.delete_subject)
        self.delete_button.pack(side=tk.LEFT, padx=5, pady=5)

    def add_subject(self):
        new_subject = simpledialog.askstring("Add Subject", "Enter the subject name:")
        if new_subject:
            self.subjects.append(new_subject)
            self.update_listbox()

    def edit_subject(self):
        selected_index = self.listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Edit Subject","No subject selected")
