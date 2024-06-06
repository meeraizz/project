from tkinter import *
from PIL import Image, ImageTk    #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
import customtkinter

class DetailsClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Grade Master")
        self.root.geometry("1550x500+60+150")
        self.root.config(bg="#fff0f3")
        self.root.focus_force()

        # Create a main frame to contain all widgets
        self.main_frame = Frame(self.root, bg="#fff0f3")
        self.main_frame.pack(fill=BOTH, expand=True)  

        # Call method to create and layout all widgets
        self.create_widgets()

    def create_widgets(self):
        #=====title======
        title=Label(self.main_frame, text="Manage Student Details", font=("king",23,"bold"), bg="#FFB3D2", fg="black")
        title.pack(fill=X)  # Fill the width of the main frame

        #=====variables====
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_course=StringVar()
        self.var_a_date=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_pin=StringVar()

        #=====widgets======
        #=======column 1=========
        lbl_id=Label(self.root,text="ID No.", font=("king",15,"bold"),bg="#fff0f3").place(x=450,y=60)
        lbl_name=Label(self.root,text="Name",font=("king",15,"bold"),bg="#fff0f3").place(x=450,y=100)                     
        lbl_email=Label(self.root,text="Email",font=("king",15,"bold"),bg="#fff0f3").place(x=450,y=140)
        lbl_gender=Label(self.root,text="Gender",font=("king",15,"bold"),bg="#fff0f3").place(x=450,y=180)
           
        lbl_state=Label(self.root,text="State",font=("king",15,"bold"),bg="#fff0f3").place(x=450,y=220)
        txt_state=Entry(self.root,textvariable=self.var_state,font=("king",15,"bold"),bg="lightyellow").place(x=600,y=220,width=150)
        
        lbl_city=Label(self.root,text="City",font=("king",15,"bold"),bg="#fff0f3").place(x=760,y=220)
        txt_city=Entry(self.root,textvariable=self.var_city,font=("king",15,"bold"),bg="lightyellow").place(x=840,y=220,width=150)
        
        lbl_pin=Label(self.root,text="Pin",font=("king",15,"bold"),bg="#fff0f3").place(x=1000,y=220)
        txt_pin=Entry(self.root,textvariable=self.var_pin,font=("king",15,"bold"),bg="lightyellow").place(x=1100,y=220,width=100)

        lbl_address=Label(self.root,text="Address",font=("king",15,"bold"),bg="#fff0f3").place(x=450,y=260)
        
        #====entry fields====
        self.txt_id=Entry(self.root,textvariable=self.var_id,font=("king",15,"bold"),bg="lightyellow").place(x=600,y=60,width=200)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("king",15,"bold"),bg="lightyellow").place(x=600,y=100,width=200)
        txt_email=Entry(self.root,textvariable=self.var_email,font=("king",15,"bold"),bg="lightyellow").place(x=600,y=140,width=200)
        self.txt_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female"),font=("king",15,"bold"),state='readonly',justify=CENTER)
        self.txt_gender.place(x=600,y=180,width=200)
        self.txt_gender.current(0)

       #=======column 2=========
        lbl_dob=Label(self.root,text="D.O.B", font=("king",15,"bold"),bg="#fff0f3").place(x=840,y=60)
        lbl_contact=Label(self.root,text="Contact",font=("king",15,"bold"),bg="#fff0f3").place(x=840,y=100)                     
        lbl_admission=Label(self.root,text="Admission",font=("king",15,"bold"),bg="#fff0f3").place(x=840,y=140)
        lbl_course=Label(self.root,text="Course",font=("king",15,"bold"),bg="#fff0f3").place(x=840,y=180)

        #====entry fields 2====
        self.course_list=[]
        #function_call to update the list
        self.fetch_course()
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("king",15,"bold"),bg="lightyellow").place(x=1000,y=60,width=200)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("king",15,"bold"),bg="lightyellow").place(x=1000,y=100,width=200)
        txt_admission=Entry(self.root,textvariable=self.var_a_date,font=("king",15,"bold"),bg="lightyellow").place(x=1000,y=140,width=200)
        self.txt_course=ttk.Combobox(self.root,textvariable=self.var_course,values=(" "),font=("king",15,"bold"),state='readonly',justify=CENTER)
        self.txt_course.place(x=1000,y=180,width=200,)
        self.txt_course.set("Select")
        
        #====text address=====
        self.txt_address=Text(self.root,font=("king",15,"bold"),bg="lightyellow")
        self.txt_address.place(x=600,y=260,width=600,height=100)

        #=====buttons=======
        self.btn_add=Button(self.root,text="Save",font=("king",15,"bold"),bg="#FF0090",fg="#fff0f3",cursor="hand2",command=self.add)
        self.btn_add.place(x=620,y=400,width=110,height=40)
        self.btn_update=Button(self.root,text="Update",font=("king",15,"bold"),bg="#FF66CC",fg="#fff0f3",cursor="hand2",command=self.update)
        self.btn_update.place(x=740,y=400,width=110,height=40)
        self.btn_delete=Button(self.root,text="Delete",font=("king",15,"bold"),bg="#DE3163",fg="#fff0f3",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=860,y=400,width=110,height=40)
        self.btn_clear=Button(self.root,text="Clear",font=("king",15,"bold"),bg="#F19CBB",fg="#fff0f3",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=980,y=400,width=110,height=40)

    #============================================
    def clear(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_a_date.set("")
        self.var_course.set("Select")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")                   
        self.txt_address.delete("1.0",END)

    def delete(self):
        con=sqlite3.connect(database="GradeMaster.db")
        cur=con.cursor()
        try:
            if self.var_id.get()=="":
                messagebox.showerror("Error","ID No. should be required",parent=self.root)
            else:
                cur.execute("select * from student where id=?",(self.var_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select student from the list first",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from student where id=?",(self.var_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Student deleted Successfully",parent=self.root)
                        self.clear()
                        self.show()
                        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def add(self):
        con=sqlite3.connect(database="GradeMaster.db")
        cur=con.cursor()
        try:
            if self.var_id.get()=="":
                messagebox.showerror("Error","ID Number should be required",parent=self.root)
            else:
                cur.execute("select * from student where id=?",(self.var_id.get(),))
                row=cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error","ID No. already present",parent=self.root)
                else:
                    cur.execute("insert into student (id,name,email,gender,dob,contact,admission,course,state,city,pin,address) values(?,?,?,?,?,?,?,?,?,?,?,?)", (
                        self.var_id.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),                    
                        self.txt_address.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def update(self):
        con=sqlite3.connect(database="GradeMaster.db")
        cur=con.cursor()
        try:
            if self.var_id.get()=="":
                messagebox.showerror("Error","ID No. should be required",parent=self.root)
            else:
                cur.execute("select * from student where id=?",(self.var_id.get(),))
                row=cur.fetchone()
                if row is None:
                    messagebox.showerror("Error","Select student from list",parent=self.root)
                else:
                    cur.execute("update student set name=?,email=?,gender=?,dob=?,contact=?,admission=?,course=?,state=?,city=?,pin=?,address=? where id=?",(
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),                    
                        self.txt_address.get("1.0",END),
                        self.var_id.get(),                    
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student Update Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def show(self):
        con=sqlite3.connect(database="GradeMaster.db")
        cur=con.cursor()
        try:
            cur.execute("select * from student")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def fetch_course(self):
        con=sqlite3.connect(database="GradeMaster.db")
        cur=con.cursor()
        try:
            cur.execute("select name from course")
            rows=cur.fetchall()
            if len(rows)>0:
                self.course_list = [row[0] for row in rows]
                self.txt_course.config(values=self.course_list)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def search(self):
        con=sqlite3.connect(database="GradeMaster.db")
        cur=con.cursor()
        try:
            cur.execute("select * from student where id=?",(self.var_search.get(),))
            row=cur.fetchone()
            # print(row)
            if row is not None:
                self.CourseTable.delete(*self.CourseTable.get_children())
                self.CourseTable.insert(" ",END,values=row)   
            else:
               messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


if __name__=="__main__":
    root=customtkinter.CTk()
    obj=DetailsClass(root)
    root.mainloop()        