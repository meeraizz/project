from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class TeacherProfile:
    def __init__(self, root):
        self.root = root
        self.root.title("Teacher Profile")
        self.root.geometry("800x600+200+100")
        self.root.config(bg='white')
        self.root.focus_force()

        # Variables
        self.var_teacher_id = StringVar()
        self.var_teacher_name = StringVar()
        self.var_teacher_email = StringVar()
        self.var_teacher_contact = StringVar()
        self.course_list = []

        # Title
        title = Label(self.root, text="Teacher Profile", font=("times new roman", 20, "bold"), bg="pink", fg="#262626").place(x=10, y=15, width=780, height=50)

        # Widgets
        lbl_select = Label(self.root, text="Select Teacher", font=("times new roman", 20, "bold"), bg="white").place(x=50, y=100)
        
        self.txt_teacher = ttk.Combobox(self.root, textvariable=self.var_teacher_id, font=("times new roman", 15, "bold"), state='readonly', justify=CENTER)
        self.txt_teacher.place(x=250, y=100, width=200)
        self.txt_teacher.set("Select")
        self.fetch_teachers()
        
        btn_search = Button(self.root, text='Search', command=self.search_teacher, font=("times new roman", 15, "bold"), bg="#03a9f4", fg="white", cursor="hand2").place(x=500, y=100, width=100, height=28)
        
        lbl_name = Label(self.root, text="Name", font=("times new roman", 20, "bold"), bg="white").place(x=50, y=160)
        lbl_email = Label(self.root, text="Email", font=("times new roman", 20, "bold"), bg="white").place(x=50, y=220)
        lbl_contact = Label(self.root, text="Contact", font=("times new roman", 20, "bold"), bg="white").place(x=50, y=280)
        
        self.txt_name = Entry(self.root, textvariable=self.var_teacher_name, font=("times new roman", 20, "bold"), bg="lightyellow", state='readonly').place(x=250, y=160, width=320)
        self.txt_email = Entry(self.root, textvariable=self.var_teacher_email, font=("times new roman", 20, "bold"), bg="lightyellow", state='readonly').place(x=250, y=220, width=320)
        self.txt_contact = Entry(self.root, textvariable=self.var_teacher_contact, font=("times new roman", 20, "bold"), bg="lightyellow", state='readonly').place(x=250, y=280, width=320)

        self.profile_frame = Frame(self.root, bg="white", bd=2, relief=RIDGE)
        self.profile_frame.place(x=600, y=160, width=160, height=160)

        self.profile_picture = Label(self.profile_frame, bg="white")
        self.profile_picture.pack(fill=BOTH, expand=True)
        
        lbl_courses = Label(self.root, text="Courses", font=("times new roman", 20, "bold"), bg="white").place(x=50, y=340)
        self.course_listbox = Listbox(self.root, font=("times new roman", 15), bg="lightyellow")
        self.course_listbox.place(x=250, y=340, width=320, height=150)

    def fetch_teachers(self):
        conn = sqlite3.connect("GradeMaster.db")
        cur = conn.cursor()
        try:
            cur.execute("SELECT tid, name FROM teacher")
            rows = cur.fetchall()
            if rows:
                for row in rows:
                    self.txt_teacher['values'] = (*self.txt_teacher['values'], row[1])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        conn.close()

    def search_teacher(self):
        conn = sqlite3.connect("GradeMaster.db")
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM teacher WHERE name=?", (self.var_teacher_id.get(),))
            row = cur.fetchone()
            if row:
                self.var_teacher_name.set(row[1])
                self.var_teacher_email.set(row[2])
                self.var_teacher_contact.set(row[3])
                self.load_profile_picture(row[4])
                self.fetch_courses(row[0])
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        conn.close()

    def load_profile_picture(self, img_path):
        try:
            img = Image.open(img_path)
            img = img.resize((160, 160), Image.ANTIALIAS)
            self.photoimg = ImageTk.PhotoImage(img)
            self.profile_picture.config(image=self.photoimg)
        except Exception as ex:
            messagebox.showerror("Error", f"Error loading profile picture: {str(ex)}")

    def fetch_courses(self, teacher_id):
        self.course_listbox.delete(0, END)
        conn = sqlite3.connect("GradeMaster.db")
        cur = conn.cursor()
        try:
            cur.execute("""
                SELECT c.name FROM course c
                JOIN teacher_course tc ON c.cid = tc.course_id
                WHERE tc.teacher_id=?
            """, (teacher_id,))
            rows = cur.fetchall()
            if rows:
                for row in rows:
                    self.course_listbox.insert(END, row[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        conn.close()

if __name__ == "__main__":
    root = Tk()
    obj = TeacherProfile(root)
    root.mainloop()
