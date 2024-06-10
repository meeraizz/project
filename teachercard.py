import sqlite3
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import customtkinter
import os
from editprofile import editprofile


class teachercard:
    def __init__(self, root):
        self.root = root
        self.root.title("Grade Master")
        self.root.geometry("1850x800+50+200")
        self.root.config(bg='#fff0f3')
        self.root.focus_force()

        #=============Title==================
        title = Label(self.root, text="Profile", font=("King", 30, "bold"), bg="#ff80b4", fg="#262626")
        title.place(x=0, y=10, width=1960, height=70)

        # ============ Widgets ================
        self.profile_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        self.profile_frame.place(x=500, y=100, width=1000, height=650)

        # ============Variables==============
        self.var_teacher_tid = StringVar()
        self.var_teacher_name = StringVar()
        self.var_teacher_email = StringVar()
        self.var_teacher_contact = StringVar()
        self.var_teacher_course = StringVar()
        self.var_profile_picture = StringVar()
        self.tid_list = []


        lbl_name = Label(self.root, text="Name", font=("King", 25, "bold"), bg="white")
        lbl_name.place(x=800, y=310)
        lbl_email = Label(self.root, text="Email", font=("King", 25, "bold"), bg="white")
        lbl_email.place(x=800, y=390)
        lbl_contact = Label(self.root, text="Contact", font=("King", 25, "bold"), bg="white")
        lbl_contact.place(x=800, y=480)
        lbl_courses = Label(self.root, text="Courses", font=("King", 25, "bold"), bg="white")
        lbl_courses.place(x=800, y=560)

        #============Profile picture==========
        self.image_frame = Frame(root, bd=3, bg="white", width=200, height=200, relief=RIDGE)
        self.image_frame.place(x=550, y=150, width=200, height=220)
        self.default_image_path = os.path.join("images", "pfp.png")
        self.img_label = Label(self.image_frame, bg="white")
        self.img_label.place(x=0, y=0)
        self.display_image(self.default_image_path)

        #===============Button==============
        btn_edit = Button(self.root, text="Edit", font=("King", 15, "bold"), bg="#ff80b4", fg="#262626",command=self.edit)
        btn_edit.place(x=1320, y=700, width=150, height=35)


        self.lbl_name = Label(self.root, textvariable=self.var_teacher_name, font=("times new roman", 25, "bold"), bg="white", anchor="w")
        self.lbl_name.place(x=980, y=310, width=370, height=45)

        self.lbl_email = Label(self.root, textvariable=self.var_teacher_email, font=("times new roman", 25, "bold"), bg="white", anchor="w")
        self.lbl_email.place(x=980, y=390, width=370, height=45)

        self.lbl_contact = Label(self.root, textvariable=self.var_teacher_contact, font=("times new roman", 25, "bold"), bg="white", anchor="w")
        self.lbl_contact.place(x=980, y=480, width=370, height=45)

        self.lbl_course = Label(self.root, textvariable=self.var_teacher_course, font=("times new roman", 25, "bold"), bg="white", anchor="nw", justify=LEFT, wraplength=360)
        self.lbl_course.place(x=980, y=560, width=370, height=100)


    def edit(self):
        self.root.destroy()
        self.new_win = customtkinter.CTk()
        self.new_obj = editprofile(self.new_win)
        self.new_win.mainloop()


    def display_image(self, file_path):
        if os.path.exists(file_path):
            img = Image.open(file_path)
            img = img.resize((200, 220),Image.LANCZOS )
            self.img = ImageTk.PhotoImage(img)
            self.img_label.config(image=self.img)
            self.img_label.image = self.img
        else:
            self.img_label.config(image="")

    def fetch_teachers(self):
        conn = sqlite3.connect(database="GradeMaster.db")
        cur = conn.cursor()
        try:
            cur.execute("SELECT tid, name FROM teacher")
            rows = cur.fetchall()
            if rows:
                self.tid_list = [row[0] for row in rows]
                self.txt_teacher['values'] = [row[1] for row in rows]
            else:
                print("No records found in the teacher table.")
        except Exception as ex:
            print("Error fetching data from the teacher table:", ex)
            messagebox.showerror("Error", f"Error fetching data from the teacher table: {str(ex)}")
        finally:
            conn.close()









if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = teachercard(root)
    root.mainloop()