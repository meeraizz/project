import sqlite3
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import customtkinter
import os

class editprofile:
    def __init__(self, root, teacher_data=None):
        self.root = root
        self.root.title("Grade Master")
        self.root.geometry("1200x750+50+350")
        self.root.config(bg='#fff0f3')
        self.root.focus_force()

        #=============Title==================
        title = Label(self.root, text="Teacher Profile", font=("King", 30, "bold"), bg="#ff80b4", fg="#262626")
        title.place(x=0, y=10, width=1960, height=70)

        # ============Variables==============
        self.var_teacher_id = StringVar()
        self.var_teacher_name = StringVar()
        self.var_teacher_email = StringVar()
        self.var_teacher_contact = StringVar()
        self.var_teacher_course = StringVar()
        self.var_profile_picture = StringVar()

        #==============Widgets================
        lbl_id = Label(self.root, text="Teacher ID", font=("times new roman", 25, "bold"), bg="#fff0f3")
        lbl_id.place(x=600, y=150)
        self.txt_id = Entry(self.root, textvariable=self.var_teacher_id, font=("times new roman", 25, "bold"), bg="lightyellow", state='readonly')
        self.txt_id.place(x=880, y=150, width=240, height=45)

        lbl_name = Label(self.root, text="Name", font=("King", 25, "bold"), bg="#fff0f3")
        lbl_name.place(x=600, y=230)
        lbl_email = Label(self.root, text="Email", font=("King", 25, "bold"), bg="#fff0f3")
        lbl_email.place(x=600, y=310)
        lbl_contact = Label(self.root, text="Contact", font=("King", 25, "bold"), bg="#fff0f3")
        lbl_contact.place(x=600, y=390)
        lbl_courses = Label(self.root, text="Courses", font=("King", 25, "bold"), bg="#fff0f3")
        lbl_courses.place(x=600, y=480)

        self.txt_name = Entry(self.root, textvariable=self.var_teacher_name, font=("times new roman", 25, "bold"), bg="lightyellow")
        self.txt_name.place(x=880, y=230, width=370, height=45)
        self.txt_email = Entry(self.root, textvariable=self.var_teacher_email, font=("times new roman", 25, "bold"), bg="lightyellow")
        self.txt_email.place(x=880, y=310, width=370, height=45)
        self.txt_contact = Entry(self.root, textvariable=self.var_teacher_contact, font=("times new roman", 25, "bold"), bg="lightyellow")
        self.txt_contact.place(x=880, y=390, width=370, height=45)
        self.txt_course = Entry(self.root, textvariable=self.var_teacher_course, font=("times new roman", 25, "bold"), bg="lightyellow")
        self.txt_course.place(x=880, y=480, width=370, height=100)

        #==========Image==============
        self.image_frame = Frame(self.root, bd=3, bg="white", width=200, height=200, relief=RIDGE)
        self.image_frame.place(x=1300, y=150, width=200, height=220)
        self.default_image_path = os.path.join("images", "pfp.png")
        self.img_label = Label(self.image_frame, bg="white")
        self.img_label.place(x=0, y=0)
        self.display_image(self.default_image_path)

        #============Buttons============
        btn_upload = Button(self.root, text="Upload Image", font=("times new roman", 15, "bold"), bg="#ff80b4", fg="#262626", command=self.upload_image)
        btn_upload.place(x=1320, y=400, width=170, height=35)
        btn_clear = Button(self.root, text="Clear", font=("times new roman", 20, "bold"), bg="#ff80b4", fg="#262626", command=self.clear_data)
        btn_clear.place(x=880, y=600, width=150, height=40)
        btn_submit = Button(self.root, text="Submit", font=("times new roman", 20, "bold"), bg="#ff80b4", fg="#262626", command=self.submit_data)
        btn_submit.place(x=1100, y=600, width=150, height=40)

        # Load existing data if any
        if teacher_data:
            self.populate_data(teacher_data)

    def populate_data(self, data):
        self.var_teacher_id.set(data.get('id', ''))
        self.var_teacher_name.set(data.get('name', ''))
        self.var_teacher_email.set(data.get('email', ''))
        self.var_teacher_contact.set(data.get('contact', ''))
        self.var_teacher_course.set(data.get('course', ''))
        profile_picture = data.get('profile_picture', self.default_image_path)
        self.var_profile_picture.set(profile_picture)
        self.display_image(profile_picture)

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

    def upload_image(self):
        file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file",
                                               filetypes=(("JPG File", "*.jpg"), ("PNG File", "*.png"), ("All Files", "*.*")))
        if file_path:
            self.var_profile_picture.set(file_path)
            self.display_image(file_path)

    def clear_data(self):
        self.var_teacher_id.set("")
        self.var_teacher_name.set("")
        self.var_teacher_email.set("")
        self.var_teacher_contact.set("")
        self.var_teacher_course.set("")
        self.var_profile_picture.set(self.default_image_path)
        self.display_image(self.default_image_path)

    def submit_data(self):
        try:
            con = sqlite3.connect('GradeMaster.db')
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS teacher (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            email TEXT,
                            contact TEXT,
                            course TEXT,
                            profile_picture TEXT)""")
            if self.var_teacher_id.get():
                cur.execute("UPDATE teacher SET name=?, email=?, contact=?, course=?, profile_picture=? WHERE id=?",
                            (self.var_teacher_name.get(), self.var_teacher_email.get(), self.var_teacher_contact.get(), self.var_teacher_course.get(), self.var_profile_picture.get(), self.var_teacher_id.get()))
                messagebox.showinfo("Success", "Teacher profile updated successfully")
            else:
                cur.execute("INSERT INTO teacher (name, email, contact, course, profile_picture) VALUES (?, ?, ?, ?, ?)",
                            (self.var_teacher_name.get(), self.var_teacher_email.get(), self.var_teacher_contact.get(), self.var_teacher_course.get(), self.var_profile_picture.get()))
                messagebox.showinfo("Success", "Teacher profile submitted successfully")
            con.commit()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error interacting with database: {e}")
        finally:
            con.close()
            self.root.destroy()  # Close window after submission

if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = editprofile(root)
    root.mainloop()
