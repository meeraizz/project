from tkinter import *
from PIL import Image, ImageTk    #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
import customtkinter

class DetailsClass_tc:
    def __init__(self,root):
        self.root=root
        self.root.title("Grade Master")
        self.root.geometry("1850x750+50+200")
        self.root.config(bg="#fff0f3")
        self.root.focus_force()

        # Create a main frame to contain all widgets
        self.main_frame = Frame(self.root, bg="#fff0f3")
        self.main_frame.pack(fill=BOTH, expand=True)  

        title=Label(self.main_frame, text="Manage Student Details", font=("king",23,"bold"), bg="#FFB3D2", fg="black")
        title.place(x=0, y=10, width=1960, height=70)


        #=======search panel=====
        self.var_search=StringVar()
        lbl_search_id=Label(self.root,text="ID No.",font=("king",20,"bold"),bg="#fff0f3").place(x=600,y=150)
        txt_search_id=Entry(self.root,textvariable=self.var_search,font=("king",20,"bold"),bg="lightyellow").place(x=880, y=150, width=240, height=45)
        btn_search=Button(self.root,text="Search",font=("king",20,"bold"),bg="#ff80b4",fg="black",cursor="hand2",command=self.search).place(x=1130, y=150, width=120, height=45)

        #=====content========
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=600,y=230,width=650,height=500)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("id","name","email","gender","dob","contact","admission","course","state","city","pin","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("id",text="ID No.")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("email",text="Email")
        self.CourseTable.heading("gender",text="Gender")
        self.CourseTable.heading("dob",text="D.O.B")
        self.CourseTable.heading("contact",text="Contact")
        self.CourseTable.heading("admission",text="Admission")
        self.CourseTable.heading("course",text="Course")
        self.CourseTable.heading("state",text="State")
        self.CourseTable.heading("city",text="City")
        self.CourseTable.heading("pin",text="PIN")
        self.CourseTable.heading("address",text="Address")
        self.CourseTable["show"]="headings"
        self.CourseTable.column("id",width=100)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("email",width=100)
        self.CourseTable.column("gender",width=100)
        self.CourseTable.column("dob",width=100)
        self.CourseTable.column("contact",width=100)
        self.CourseTable.column("admission",width=100)
        self.CourseTable.column("course",width=100)
        self.CourseTable.column("state",width=100)
        self.CourseTable.column("city",width=100)
        self.CourseTable.column("pin",width=100)
        self.CourseTable.column("address",width=100)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        self.fetch_course()

    #============================================


    def get_data(self,ev):
        self.txt_id.config(state='readonly')
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        self.var_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_contact.set(row[5])
        self.var_a_date.set(row[6])
        self.var_course.set(row[7])
        self.var_state.set(row[8])
        self.var_city.set(row[9])
        self.var_pin.set(row[10])                   
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[11])



    def show(self):
        con=sqlite3.connect(database="Grademaster.db")
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
        con=sqlite3.connect(database="Grademaster.db")
        cur=con.cursor()
        try:
            cur.execute("select name from course")
            rows=cur.fetchall()
            if len(rows)>0:
                self.course_list = [row[0] for row in rows]
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def search(self):
        con=sqlite3.connect(database="Grademaster.db")
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
    obj=DetailsClass_tc(root)
    root.mainloop()        