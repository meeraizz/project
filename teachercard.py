import sqlite3
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
from editprofile import editprofile
import customtkinter
import os

class teachercard:
    def __init__(self, root, teacher_id):
        self.root = root
        self.teacher_id = teacher_id
        self.root.title("Grade Master")
        self.root.geometry("1200x750+50+200")
        self.root.config(bg='#fff0f3')
        self.root.focus_force()

        # =============Title==================
        title = Label(self.root, text="Profile", font=("King", 30, "bold"), bg="#ff80b4", fg="#262626")
        title.place(x=0, y=10, width=1960, height=70)

        # ============ Widgets ================
        self.profile_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        self.profile_frame.place(x=500, y=100, width=1000, height=650)

        # ============ Variables ==============
        self.var_teacher_name = StringVar()
        self.var_teacher_email = StringVar()
        self.var_teacher_contact = StringVar()
        self.var_teacher_course = StringVar()

        lbl_name = Label(self.root, text="Name", font=("King", 25, "bold"), bg="white")
        lbl_name.place(x=800, y=230)
        lbl_email = Label(self.root, text="Email", font=("King", 25, "bold"), bg="white")
        lbl_email.place(x=800, y=310)
        lbl_contact = Label(self.root, text="Contact", font=("King", 25, "bold"), bg="white")
        lbl_contact.place(x=800, y=390)
        lbl_courses = Label(self.root, text="Courses", font=("King", 25, "bold"), bg="white")
        lbl_courses.place(x=800, y=480)

        # ============ Profile picture ==========
        self.image_frame = Frame(self.root, bd=3, bg="white", width=200, height=200, relief=RIDGE)
        self.image_frame.place(x=550, y=150, width=200, height=220)
        self.default_image_path = os.path.join("images", "pfp.png")
        self.img_label = Label(self.image_frame, bg="white")
        self.img_label.place(x=0, y=0)
        self.display_image(self.default_image_path)

        # ============= Button ================
        btn_edit = Button(self.root, text="Edit", font=("King", 15, "bold"), bg="#ff80b4", fg="#262626", command=self.edit)
        btn_edit.place(x=1320, y=700, width=150, height=35)

        # Text fields to display the fetched data
        self.txt_name = Label(self.root, textvariable=self.var_teacher_name, font=("times new roman", 25, "bold"), bg="white", anchor='w', justify=LEFT)
        self.txt_name.place(x=1000, y=230, width=370, height=45)
        self.txt_email = Label(self.root, textvariable=self.var_teacher_email, font=("times new roman", 25, "bold"), bg="white", anchor='w', justify=LEFT)
        self.txt_email.place(x=1000, y=310, width=370, height=45)
        self.txt_contact = Label(self.root, textvariable=self.var_teacher_contact, font=("times new roman", 25, "bold"), bg="white", anchor='w', justify=LEFT)
        self.txt_contact.place(x=1000, y=390, width=370, height=45)
        self.txt_course = Label(self.root, textvariable=self.var_teacher_course, font=("times new roman", 25, "bold"), bg="white", anchor='w', justify=LEFT)
        self.txt_course.place(x=1000, y=450, width=370, height=100)

        self.load_teacher_data()

    def edit(self):
        teacher_data = {
            'id': self.teacher_id,
            'name': self.var_teacher_name.get(),
            'email': self.var_teacher_email.get(),
            'contact': self.var_teacher_contact.get(),
            'course': self.var_teacher_course.get(),
            'profile_picture': self.default_image_path  # Update this to fetch the actual path from the database if necessary
        }
        new_top = customtkinter.CTkToplevel(self.root)
        new_window = editprofile(new_top, teacher_data=teacher_data)
        new_top.transient(self.root)
        new_top.grab_set()
        new_top.focus_force()
        self.root.wait_window(new_top)  # Wait for the edit window to close
        self.load_teacher_data()  # Reload data


    def display_image(self, file_path):
        if os.path.exists(file_path):
            try:
                img = Image.open(file_path)
                img = img.resize((200, 220), Image.LANCZOS)
                self.img = ImageTk.PhotoImage(img)
                self.img_label.config(image=self.img)
                self.img_label.image = self.img
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load image: {str(e)}")
                self.img_label.config(image="")
        else:
            self.img_label.config(image="")

    def load_teacher_data(self):
        conn = sqlite3.connect("GradeMaster.db")
        cur = conn.cursor()
        try:
            cur.execute("SELECT name, email, contact, course, profile_picture FROM teacher WHERE id = ?", (self.teacher_id,))
            row = cur.fetchone()
            if row:
                self.var_teacher_name.set(row[0])
                self.var_teacher_email.set(row[1])
                self.var_teacher_contact.set(row[2])
                self.var_teacher_course.set(row[3])
                self.display_image(row[4])
            else:
                messagebox.showerror("Error", "Teacher data not found.")
        except Exception as ex:
            messagebox.showerror("Error", f"Error loading teacher data: {str(ex)}")
        finally:
            conn.close()


if __name__ == "__main__":
    root = customtkinter.CTk()
    # For testing, replace `any` with an actual teacher_id
    obj = teachercard(root, teacher_id=any)
    root.mainloop()
