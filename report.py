from tkinter import *
from PIL import Image, ImageTk    #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
import customtkinter
from student_grade import gradeclass

class ReportClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Grade Master")
        self.root.geometry("1100x500+60+150")
        self.root.config(bg="#fff0f3")
        self.root.focus_force()

        # Create a main frame to contain all widgets
        self.main_frame = Frame(self.root, bg="#fff0f3")
        self.main_frame.pack(fill=BOTH, expand=True)         

        # Call method to create and layout all widgets
        self.create_widgets()

    def create_widgets(self):
        #=====title======
        title=Label(self.main_frame, text="View Student Results", font=("king",23,"bold"), bg="#FFB3D2", fg="black")
        title.pack(fill=X)  # Fill the width of the main frame

        #======search======
        self.var_search=StringVar()
        self.var_id=""

        lbl_search=Label(self.root,text="Search by ID No.", font=("king", 20, "bold"), bg="#fff0f3").place(x=280,y=100)
        txt_search=Entry(self.root,textvariable=self.var_search, font=("king", 20), bg="lightyellow").place(x=530,y=100,width=170)
        btn_search=Button(self.root,text="Search",font=("king",15,"bold"),bg="#03a9f4",fg="#fff0f3",cursor="hand2",command=self.search).place(x=720,y=100,width=100,height=35)
        btn_clear=Button(self.root,text="Clear",font=("king",15,"bold"),bg="#F19CBB",fg="#fff0f3",cursor="hand2", command=self.clear).place(x=840,y=100,width=100,height=35)

        #=====result_labels======
        lbl_id=Label(self.root, text="ID No", font=("king",15,"bold"),bg="#fff0f3",bd=2,relief=GROOVE).place(x=150,y=230,width=150,height=50)
        lbl_name=Label(self.root, text="Name", font=("king",15,"bold"),bg="#fff0f3",bd=2,relief=GROOVE).place(x=300,y=230,width=150,height=50)
        lbl_course=Label(self.root, text="Course", font=("king",15,"bold"),bg="#fff0f3",bd=2,relief=GROOVE).place(x=450,y=230,width=150,height=50)
        lbl_marks=Label(self.root, text="Marks Obtained", font=("king",14,"bold"),bg="#fff0f3",bd=2,relief=GROOVE).place(x=600,y=230,width=150,height=50)
        lbl_full=Label(self.root, text="Total Marks", font=("king",15,"bold"),bg="#fff0f3",bd=2,relief=GROOVE).place(x=750,y=230,width=150,height=50)
        lbl_per=Label(self.root, text="Percentage", font=("king",15,"bold"),bg="#fff0f3",bd=2,relief=GROOVE).place(x=900,y=230,width=150,height=50)

        self.id=Label(self.root, font=("king",15,"bold"),bg="#fff0f3",bd=2,relief=GROOVE)
        self.id.place(x=150,y=280,width=150,height=50)
        self.name=Label(self.root, font=("king",15,"bold"),bg="#fff0f3",bd=2,relief=GROOVE)
        self.name.place(x=300,y=280,width=150,height=50)
        self.course=Label(self.root, font=("king",15,"bold"),bg="#fff0f3",bd=2,relief=GROOVE)
        self.course.place(x=450,y=280,width=150,height=50)
        self.marks=Label(self.root, font=("king",15,"bold"),bg="#fff0f3",bd=2,relief=GROOVE)
        self.marks.place(x=600,y=280,width=150,height=50)
        self.full=Label(self.root, font=("king",15,"bold"),bg="#fff0f3",bd=2,relief=GROOVE)
        self.full.place(x=750,y=280,width=150,height=50)
        self.per=Label(self.root, font=("king",15,"bold"),bg="#fff0f3",bd=2,relief=GROOVE)
        self.per.place(x=900,y=280,width=150,height=50)

        #======button delete=====
        btn_delete=Button(self.root,text="Delete",font=("king",15,"bold"),bg="#DE3163",fg="#fff0f3",cursor="hand2", command=self.delete).place(x=500,y=350,width=150,height=35)

#=========================================================
    def search(self):
            con=sqlite3.connect(database="Grademaster.db")
            cur=con.cursor()
            try:
                if self.var_search.get()=="":
                     messagebox.showerror("Error","ID No. should be required",parent=self.root)
                cur.execute("select * from grade where id=?",(self.var_search.get(),))
                row=cur.fetchone()
                # print(row)
                if row!=None:
                     self.var_id=row[0]
                     self.id.config(text=row[1])
                     self.name.config(text=row[2])
                     self.course.config(text=row[3])
                     self.marks.config(text=row[4])
                     self.full.config(text=row[5])
                     self.per.config(text=row[6])
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")

    def clear(self):
         self.var_id=""
         self.id.config(text="")
         self.name.config(text="")
         self.course.config(text="")
         self.marks.config(text="")
         self.full.config(text="")
         self.per.config(text="")
         self.var_search.set("")

    def delete(self):
        con=sqlite3.connect(database="Grademaster.db")
        cur=con.cursor()
        try:
            if self.var_id.get=="":
                messagebox.showerror("Error","Search Student Result First",parent=self.root)
            else:
                cur.execute("select * from grade where rid=?",(self.var_id,))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Student Result",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from grade where rid=?",(self.var_id,))
                        con.commit()
                        messagebox.showinfo("Delete","Result deleted Successfully",parent=self.root)
                        self.clear()
                        self.show()
                        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

if __name__=="__main__":
    root=customtkinter.CTk()
    obj=ReportClass(root)
    root.mainloop()