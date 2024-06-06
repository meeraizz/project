import sqlite3
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
from io import BytesIO
import customtkinter
import os

class teacherprofiletcview:
    def __init__(self, root):
        self.root = root
        self.root.title("Grade Master")
        self.root.geometry("1850x750+50+200")
        self.root.config(bg='#fff0f3')
        self.root.focus_force()
        
        #========== Title===========
        title = Label(self.root, text="Teacher Profile", font=("King", 30, "bold"), bg="#ff80b4", fg="#262626")
        title.place(x=0, y=10, width=1960, height=70)

        #========Variables============
        self.var_teacher_tid = StringVar()
        self.var_teacher_name = StringVar()
        self.var_teacher_email = StringVar()
        self.var_teacher_contact = StringVar()
        self.var_teacher_course = StringVar()
        self.var_profile_picture = StringVar()
        self.tid_list = []

        #============Widgets==========
        lbl_tid = Label(self.root, text="Teacher ID", font=("times new roman", 25, "bold"), bg="#fff0f3")
        lbl_tid.place(x=600, y=150)
        self.cmb_tid = ttk.Combobox(self.root, textvariable=self.var_teacher_tid, font=("times new roman", 25, "bold"), state='readonly')
        self.cmb_tid.place(x=880, y=150, width=240, height=45)
        
        #==========Search button========
        btn_search = Button(self.root, text="Search", font=("times new roman", 20, "bold"), bg="#ff80b4", fg="#262626", command=self.fetch_teacher_details)
        btn_search.place(x=1130, y=150, width=120, height=45)

        lbl_name = Label(self.root, text="Name", font=("times new roman", 25, "bold"), bg="#fff0f3")
        lbl_name.place(x=600, y=230)
        lbl_email = Label(self.root, text="Email", font=("times new roman", 25, "bold"), bg="#fff0f3")
        lbl_email.place(x=600, y=310)
        lbl_contact = Label(self.root, text="Contact", font=("times new roman", 25, "bold"), bg="#fff0f3")
        lbl_contact.place(x=600, y=390)
        lbl_courses = Label(self.root, text="Courses", font=("times new roman", 25, "bold"), bg="#fff0f3")
        lbl_courses.place(x=600, y=480)

        self.txt_name = Entry(self.root, textvariable=self.var_teacher_name, font=("times new roman", 25, "bold"), bg="lightyellow")
        self.txt_name.place(x=880, y=230, width=370, height=45)
        self.txt_email = Entry(self.root, textvariable=self.var_teacher_email, font=("times new roman", 25, "bold"), bg="lightyellow")
        self.txt_email.place(x=880, y=310, width=370, height=45)
        self.txt_contact = Entry(self.root, textvariable=self.var_teacher_contact, font=("times new roman", 25, "bold"), bg="lightyellow")
        self.txt_contact.place(x=880, y=390, width=370, height=45)
        
        self.txt_course = Entry(self.root, textvariable=self.var_teacher_course, font=("times new roman", 25, "bold"), bg="lightyellow")
        self.txt_course.place(x=880, y=480, width=370, height=100)

        self.profile_frame = Frame(self.root, bg="white", bd=2, relief=RIDGE)
        self.profile_frame.place(x=1300, y=150, width=200, height=220)
        self.profile_picture = Label(self.profile_frame, bg="white")
        self.profile_picture.pack(fill=BOTH, expand=True)
        

        #=====Buttons========
        btn_upload = Button(self.root, text="Upload Image", font=("times new roman", 15, "bold"), bg="#ff80b4", fg="#262626", command=self.upload_image)
        btn_upload.place(x=1320, y=400, width=170, height=35)
        
        btn_clear = Button(self.root, text="Clear", font=("times new roman", 20, "bold"), bg="#ff80b4", fg="#262626", command=self.clear_data)
        btn_clear.place(x=880, y=600, width=150, height=40)
        
        btn_submit = Button(self.root, text="Submit", font=("times new roman", 20, "bold"), bg="#ff80b4", fg="#262626", command=self.submit_data)
        btn_submit.place(x=1100, y=600, width=150, height=40)

        #===== Load existing data if any =====
        self.load_tid_list()



    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.var_profile_picture.set(file_path)
            img = Image.open(file_path)
            img = img.resize((160, 160), Image.ANTIALIAS)

            # Convert the resized image to bytes
            img_bytes = BytesIO()
            img.save(img_bytes, format='JPEG')
            img_bytes.seek(0)

            # Create an ImageTk object from the bytes and resize it to fit inside the frame
            self.img = Image.open(img_bytes)
            self.img.thumbnail((200, 220), Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(self.img)

            # Update the existing Label widget with the resized image
            self.profile_picture.config(image=self.img)
            self.profile_picture.image = self.img



    def clear_data(self):
        self.var_teacher_tid.set("")
        self.var_teacher_name.set("")
        self.var_teacher_email.set("")
        self.var_teacher_contact.set("")
        self.var_teacher_course.set("")
        self.var_profile_picture.set("")
        self.profile_picture.config(image="")

    def submit_data(self):
        con = sqlite3.connect('GradeMaster.db')
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS teacher (
                        tid INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        email TEXT,
                        contact TEXT,
                        course TEXT,
                        profile_picture TEXT)""")
        if self.var_teacher_tid.get():
            cur.execute("UPDATE teacher SET name=?, email=?, contact=?, course=?, profile_picture=? WHERE tid=?",
                        (self.var_teacher_name.get(), self.var_teacher_email.get(), self.var_teacher_contact.get(), self.var_teacher_course.get(), self.var_profile_picture.get(), self.var_teacher_tid.get()))
            messagebox.showinfo("Success", "Teacher profile updated successfully")
        else:
            cur.execute("INSERT INTO teacher (name, email, contact, course, profile_picture) VALUES (?, ?, ?, ?, ?)",
                        (self.var_teacher_name.get(), self.var_teacher_email.get(), self.var_teacher_contact.get(), self.var_teacher_course.get(), self.var_profile_picture.get()))
            messagebox.showinfo("Success", "Teacher profile submitted successfully")
        con.commit()
        con.close()
        self.load_tid_list()  # Refresh the ID list

    def load_tid_list(self):
        con = sqlite3.connect('GradeMaster.db')
        cur = con.cursor()
        cur.execute("SELECT tid FROM teacher")
        rows = cur.fetchall()
        con.close()
        self.tid_list = [row[0] for row in rows]
        self.cmb_tid['values'] = self.tid_list

    def fetch_teacher_details(self):
        tid = self.var_teacher_tid.get()
        if tid:
            con = sqlite3.connect('GradeMaster.db')
            cur = con.cursor()
            cur.execute("SELECT name, email, contact, course, profile_picture FROM teacher WHERE tid=?", (tid,))
            row = cur.fetchone()
            con.close()
            if row:
                self.var_teacher_name.set(row[0])
                self.var_teacher_email.set(row[1])
                self.var_teacher_contact.set(row[2])
                self.var_teacher_course.set(row[3])
                self.var_profile_picture.set(row[4])
                if row[4] and os.path.exists(row[4]):
                    img = Image.open(row[4])
                    img = img.resize((160, 160), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(img)
                    self.profile_picture.config(image=img)
                    self.profile_picture.image = img
                else:
                    self.profile_picture.config(image="")
            else:
                messagebox.showerror("Error", "No teacher found with the selected ID")
        else:
            messagebox.showerror("Error", "Please select a Teacher ID")

if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = teacherprofiletcview(root)
    root.mainloop()
