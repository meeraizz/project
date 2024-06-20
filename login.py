from tkinter import *
from tkinter import messagebox, ttk
import sqlite3
import customtkinter
from student_dashboard import GradeMaster as StudentDashboard  
from teacher_dashboard import GradeMastertc as TeacherDashboard
from register import RegisterClass

class LoginClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Grade Master")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg='#fff0f3')
        self.root.focus_force()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        #=========Title=========
        title = Label(self.root, text="Login", font=("King", 30, "bold"), bg="#ff80b4", fg="black")
        title.place(x=0, y=10, width=1960, height=70)

        #========Variables============
        self.var_id = StringVar()
        self.var_password = StringVar()
        self.var_role = StringVar()

        #=========Frame for Inputs=========
        self.login_frame = Frame(self.root, bg='#fff0f3', bd=2, relief="groove")
        self.login_frame.place(x=250, y=200, width=700, height=500)

        #==========Label and Entry Widgets===========
        lbl_role = Label(self.login_frame, text="Role", bg='#fff0f3', fg="#FF69B4", font=("Arial", 14))
        lbl_role.place(x=50, y=50)
        self.role_combobox = ttk.Combobox(self.login_frame, textvariable=self.var_role, font=("Arial", 14), width=23, state="readonly")
        self.role_combobox['values'] = ("Student", "Teacher")
        self.role_combobox.place(x=150, y=50)
        self.role_combobox.current(0)

        lbl_id = Label(self.login_frame, text="ID", bg='#fff0f3', fg="#FF69B4", font=("Arial", 14))
        lbl_id.place(x=50, y=150)
        self.text_id = Entry(self.login_frame, textvariable=self.var_id, font=("Arial", 16), bd=2, relief="groove", width=25)
        self.text_id.place(x=150, y=150)

        lbl_password = Label(self.login_frame, text="Password", bg='#fff0f3', fg="#FF69B4", font=("Arial", 14))
        lbl_password.place(x=50, y=250)
        self.text_password = Entry(self.login_frame, textvariable=self.var_password, show="*", font=("Arial", 16), bd=2, relief="groove", width=25)
        self.text_password.place(x=150, y=250)

        #==========Button Widgets==========
        btn_login = Button(self.login_frame, text="Login", bg="#FF69B4", fg="#FFFFFF", font=("Arial", 16), command=self.login)
        btn_login.place(x=150, y=350, width=150, height=45)
        btn_register = Button(self.login_frame, text="Register", bg="#FF69B4", fg="#FFFFFF", font=("Arial", 16), command=self.open_register_window)
        btn_register.place(x=350, y=350, width=150, height=45)

        #==========Logo==========
        try:
            self.logo_img = PhotoImage(file="images/Grade-Master_Logo.png") 
            logo_label = Label(self.root, image=self.logo_img, bg='#fff0f3')
            logo_label.place(x=1200, y=200, width=500, height=500)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load logo image: {e}")

    def login(self):
        conn = sqlite3.connect("GradeMaster.db")
        cur = conn.cursor()
        
        user_id = self.var_id.get()
        password = self.var_password.get()
        role = self.var_role.get()
        
        try:
            cur.execute('''
                        SELECT id, password, 'Student' AS role FROM student 
                        WHERE id = ? AND password = ?
                        UNION ALL
                        SELECT id, password, 'Teacher' AS role FROM teacher
                        WHERE id = ? AND password = ?
                        ''', (user_id, password, user_id, password))
            
            user_data = cur.fetchone()
            
            if user_data:
                messagebox.showinfo(title="Login Success", message="You successfully logged in.")
                self.root.destroy()  # Close the login window
                
                if user_data[2] == "Student":
                    root = customtkinter.CTk()
                    app = StudentDashboard(root, student_id=user_id)
                    root.mainloop()
                elif user_data[2] == "Teacher":
                    root = customtkinter.CTk()
                    app = TeacherDashboard(root, teacher_id=user_id)
                    root.mainloop()
            else:
                messagebox.showerror(title="Error", message="Invalid login")
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            conn.close()

    # Function to open the registration window
    def open_register_window(self):
        register_window = Toplevel(self.root)
        register_window.title("Register")
        register_window.geometry("800x600")
        RegisterClass(register_window)

if __name__ == "__main__":
    root = customtkinter.CTk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}+0+0")
    obj = LoginClass(root)
    root.mainloop()
