import sqlite3
from tkinter import *
from tkinter import ttk, messagebox,filedialog
from PIL import Image, ImageTk
import os
import customtkinter

class teacherprofile:
    def __init__(self, root):
        self.root = root
        self.root.title("Grade Master")
        self.root.geometry("1200x520+80+170")
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
        self.tid_list = []  # Initialize tid_list

        #============Widgets==========
        lbl_select = Label(self.root, text="Select Teacher", font=("king", 20, "bold"), bg="#fff0f3")
        lbl_select.place(x=400, y=150)
        lbl_name = Label(self.root, text="Name", font=("king", 25, "bold"), bg="#fff0f3")
        lbl_name.place(x=400, y=230)
        lbl_email = Label(self.root, text="Email", font=("king", 25, "bold"), bg="#fff0f3")
        lbl_email.place(x=400, y=310)
        lbl_contact = Label(self.root, text="Contact", font=("king", 25, "bold"), bg="#fff0f3")
        lbl_contact.place(x=400, y=390)
        lbl_courses = Label(self.root, text="Courses", font=("king", 25, "bold"), bg="#fff0f3")
        lbl_courses.place(x=400, y=470)

        self.txt_teacher = ttk.Combobox(self.root, textvariable=self.var_teacher_tid, font=("king", 20, "bold"), state='readonly', justify=CENTER)
        self.txt_teacher.place(x=740, y=150, width=200, height=45)
        self.txt_teacher.set("Select")
        self.txt_name = Entry(self.root, textvariable=self.var_teacher_name, font=("king", 25, "bold"), bg="lightyellow", state='readonly')
        self.txt_name.place(x=740, y=230, width=370, height=45)
        self.txt_email = Entry(self.root, textvariable=self.var_teacher_email, font=("king", 25, "bold"), bg="lightyellow", state='readonly')
        self.txt_email.place(x=740, y=310, width=370, height=45)
        self.txt_contact = Entry(self.root, textvariable=self.var_teacher_contact, font=("king", 25, "bold"), bg="lightyellow", state='readonly')
        self.txt_contact.place(x=880, y=390, width=370, height=45)
        self.txt_contact.place(x=740, y=390, width=370, height=45)
        self.profile_frame = Frame(self.root, bg="white", bd=2, relief=RIDGE)
        self.profile_frame.place(x=1200, y=150, width=160, height=160)
        self.profile_picture = Label(self.profile_frame, bg="white")
        self.profile_picture.pack(fill=BOTH, expand=True)
        self.txt_course = Entry(self.root, textvariable=self.var_teacher_course, font=("king", 25, "bold"), bg="lightyellow", state='readonly')
        self.txt_course.place(x=880, y=470, width=370, height=135)

        #==========Image==============
        self.image_frame = Frame(root, bd=3, bg="white", width=200, height=200, relief=RIDGE)
        self.image_frame.place(x=1300, y=150, width=200, height=220)
        self.default_image_path = "images/pfp.png"
        self.img_label = Label(self.image_frame, bg="white")
        self.img_label.place(x=0, y=0)
        self.display_image(self.default_image_path)

        #=====Buttons========
        btn_search = Button(self.root, text='Search', font=("King", 20), bg="#e0d2ef", fg="black", cursor="hand2", command=self.search)
        btn_search.place(x=1000, y=150, width=150, height=45)

        self.fetch_teachers()
        self.txt_teacher.bind("<<ComboboxSelected>>", self.update_teacher_tid)

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

    def search(self):
        selected_tid = self.var_teacher_tid.get()
        if selected_tid:
            conn = sqlite3.connect(database="GradeMaster.db")
            cur = conn.cursor()
            try:
                cur.execute("SELECT name, email, contact, course, profile_picture FROM teacher WHERE tid=?", (selected_tid,))
                teacher_data = cur.fetchone()
                if teacher_data:
                    self.var_teacher_name.set(teacher_data[0])
                    self.var_teacher_email.set(teacher_data[1])
                    self.var_teacher_contact.set(teacher_data[2])
                    self.var_teacher_course.set(teacher_data[3])
                    # Update profile picture if available
                    if teacher_data[3]:
                        # Update profile picture using the fetched path or data
                        pass  # Update profile picture here
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}")
            finally:
                conn.close()
        else:
            messagebox.showerror("Error", "Please select a teacher", parent=self.root)
            
    def update_teacher_tid(self, event):
        selected_teacher_name = self.txt_teacher.get()
        if selected_teacher_name:
            index = self.txt_teacher.current()
            self.var_teacher_tid.set(self.tid_list[index])

if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = teacherprofile(root)
    root.mainloop()