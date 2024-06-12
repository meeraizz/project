import sqlite3
from tkinter import *
from tkinter import messagebox

class DetailsClass:
    def __init__(self, root, student_id):
        self.root = root
        self.student_id = student_id
        self.root.title("Edit Student Details")
        self.root.geometry("400x400")

        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()
        self.var_address = StringVar()

        Label(self.root, text="Name").pack()
        Entry(self.root, textvariable=self.var_name).pack()
        Label(self.root, text="Email").pack()
        Entry(self.root, textvariable=self.var_email).pack()
        Label(self.root, text="Gender").pack()
        Entry(self.root, textvariable=self.var_gender).pack()
        Label(self.root, text="D.O.B").pack()
        Entry(self.root, textvariable=self.var_dob).pack()
        Label(self.root, text="Contact").pack()
        Entry(self.root, textvariable=self.var_contact).pack()
        Label(self.root, text="State").pack()
        Entry(self.root, textvariable=self.var_state).pack()
        Label(self.root, text="City").pack()
        Entry(self.root, textvariable=self.var_city).pack()
        Label(self.root, text="Pin").pack()
        Entry(self.root, textvariable=self.var_pin).pack()
        Label(self.root, text="Address").pack()
        self.txt_address = Text(self.root, height=4, width=40)
        self.txt_address.pack()

        Button(self.root, text="Save", command=self.save_data).pack()

        self.load_student_data()

    def load_student_data(self):
        con = sqlite3.connect(database="GradeMaster.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM users WHERE id=?", (self.student_id,))
            row = cur.fetchone()
            if row:
                self.var_name.set(row[1])
                self.var_email.set(row[2])
                self.var_gender.set(row[3])
                self.var_dob.set(row[4])
                self.var_contact.set(row[5])
                self.var_state.set(row[6])
                self.var_city.set(row[7])
                self.var_pin.set(row[8])
                self.txt_address.delete("1.0", END)
                self.txt_address.insert(END, row[9])
        except Exception as ex:
            messagebox.showerror("Error", f"Error loading student data: {str(ex)}")
        finally:
            con.close()

    def save_data(self):
        name = self.var_name.get()
        email = self.var_email.get()
        gender = self.var_gender.get()
        dob = self.var_dob.get()
        contact = self.var_contact.get()
        state = self.var_state.get()
        city = self.var_city.get()
        pin = self.var_pin.get()
        address = self.txt_address.get("1.0", END)

        con = sqlite3.connect(database="GradeMaster.db")
        cur = con.cursor()
        try:
            cur.execute("""
                UPDATE users
                SET name=?, email=?, gender=?, dob=?, contact=?, state=?, city=?, pin=?, address=?
                WHERE id=?
            """, (name, email, gender, dob, contact, state, city, pin, address, self.student_id))
            con.commit()
            messagebox.showinfo("Success", "Student data updated successfully")
            self.root.destroy()
        except Exception as ex:
            messagebox.showerror("Error", f"Error updating student data: {str(ex)}")
        finally:
            con.close()

if __name__ == "__main__":
    root = Tk()
    obj = DetailsClass(root, student_id=1)  # Example student_id
    root.mainloop()
