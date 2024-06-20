from tkinter import *
from tkinter import messagebox, ttk
import sqlite3
import customtkinter
from student_dashboard import GradeMaster as StudentDashboard  # Assuming these imports are correct
from teacher_dashboard import GradeMastertc as TeacherDashboard
from register import RegisterClass

class LoginClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Grade Master")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg='#fff0f3')
        self.root.focus_force()

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
        self.text_id = Entry(self.login_frame, textvariable=self.var_id, font=("King", 16), bd=2, relief="groove", width=25)
        self.text_id.place(x=150, y=150)

        lbl_password = Label(self.login_frame, text="Password", bg='#fff0f3', fg="#FF69B4", font=("King", 14))
        lbl_password.place(x=50, y=250)
        self.text_password = Entry(self.login_frame, textvariable=self.var_password, show="*", font=("King", 16), bd=2, relief="groove", width=25)
        self.text_password.place(x=150, y=250)

        #==========Button Widgets==========
        btn_login = Button(self.login_frame, text="Login", bg="#FF69B4", fg="black", font=("King", 16), command=self.login)
        btn_login.place(x=150, y=350, width=100, height=30)
        btn_register = Button(self.login_frame, text="Register", bg="#FF69B4", fg="black", font=("King", 16), command=self.open_register_window)
        btn_register.place(x=350, y=350, width=120, height=30)

        # Add Forgot Password button
        btn_forgot_password = Button(self.login_frame, text="Forgot Password?", bg="#FF69B4", fg="black", font=("King", 16), command=self.open_forgot_password_window)
        btn_forgot_password.place(x=200, y=420, width=220, height=30)

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

    # Function to open the forgot password window
    def open_forgot_password_window(self):
        forgot_window = Toplevel(self.root)
        forgot_window.title("Forgot Password")
        forgot_window.geometry("900x700+200+100")
        forgot_window.config(bg='#fff0f3')

        # Variables for the forgot password window
        var_forgot_id = StringVar()
        var_new_password = StringVar()

        Label(forgot_window, text="Enter ID", bg='#fff0f3', fg="#FF69B4", font=("Arial", 14)).place(x=200, y=150)
        Entry(forgot_window, textvariable=var_forgot_id, font=("Arial", 14), bd=2, relief="groove", width=25).place(x=400, y=150)

        Label(forgot_window, text="New Password", bg='#fff0f3', fg="#FF69B4", font=("Arial", 14)).place(x=200, y=200)
        Entry(forgot_window, textvariable=var_new_password, font=("Arial", 14), bd=2, relief="groove", width=25, show='*').place(x=400, y=200)

        Button(forgot_window, text="Submit", bg="#FF69B4", fg="black", font=("Arial", 14), command=lambda: self.reset_password(var_forgot_id.get(), var_new_password.get(), forgot_window)).place(x=400, y=250, width=100, height=30)

    # Function to reset password
    def reset_password(self, user_id, new_password, window):
        if user_id == "" or new_password == "":
            messagebox.showerror("Error", "All fields are required", parent=window)
            return

        conn = sqlite3.connect("GradeMaster.db")
        cur = conn.cursor()
        
        try:
            # Check if the user exists
            cur.execute("SELECT id FROM student WHERE id = ? UNION ALL SELECT id FROM teacher WHERE id = ?", (user_id, user_id))
            user = cur.fetchone()

            if user:
                # Update the password for the student
                cur.execute("UPDATE student SET password = ? WHERE id = ?", (new_password, user_id))
                # Update the password for the teacher
                cur.execute("UPDATE teacher SET password = ? WHERE id = ?", (new_password, user_id))
                conn.commit()

                messagebox.showinfo("Success", "Password has been reset successfully", parent=window)
                window.destroy()  # Close the forgot password window
            else:
                messagebox.showerror("Error", "User ID does not exist", parent=window)
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}", parent=window)
        finally:
            conn.close()

if __name__ == "__main__":
    root = customtkinter.CTk()
    obj = LoginClass(root)
    root.mainloop()
