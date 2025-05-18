from tkinter import *
from PIL import Image, ImageTk
from tkinter import PhotoImage
from tkinter import ttk
from tkinter import messagebox
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
import sqlite3
import os

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1550x900+0+0")
        self.root.config(bg="white")

        # ===== Logo Image (resized) =====
        original_image = Image.open("logo_image.png")
        resized_image = original_image.resize((80, 60)) 
        self.logo_dash = ImageTk.PhotoImage(resized_image)
        
        

        # ===== Title Label with Image =====
        title = Label(self.root,
                      text="  Student Result Management System",  # space for image
                      image=self.logo_dash,
                      padx=10,
                      compound=LEFT,
                      font=("goudy old style", 20, "bold"),
                      bg="#330054",
                      fg="white")
        title.place(x=0, y=0, relwidth=1, height=50)

        #------------menu---------------
        M_Frame=LabelFrame(self.root,text="Menu",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1500,height=80)

        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=120,y=5,width=200,height=40)

        btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=340,y=5,width=200,height=40)

        btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=560,y=5,width=200,height=40)

        btn_view=Button(M_Frame,text="View Student Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=780,y=5,width=200,height=40)

        btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=1000,y=5,width=200,height=40)

        btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit_).place(x=1230,y=5,width=200,height=40)

      #--------------Content_window----------------
        self.bg_img = PhotoImage(file="images.png")
        self.lbl_bg = Label(self.root, image=self.bg_img)
        self.lbl_bg.place(x=400, y=180, width=920, height=350)
        
        

      #=================Update-details=================
        self.lbl_course=Label(self.root,text="Total Courses\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=400,y=530,width=300,height=100)

        self.lbl_student=Label(self.root,text="Total Students\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_student.place(x=710,y=530,width=300,height=100)

        self.lbl_result=Label(self.root,text="Total Results\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_result.place(x=1020,y=530,width=300,height=100)


      
      
      
      #----------footer---------------

        footer = Label(self.root,
               text=" SRMS - Student Result Management System\nContact us for any technical issue: 9820862240",
               font=("goudy old style", 12),
               bg="#262626",
               fg="white")
        footer.pack(side=BOTTOM, fill=X)
        self.update_details()  
    
    def update_details(self):
        con=sqlite3.connect(database="rms.db") 
        cur=con.cursor()
        try:
            cur.execute("select * from course")    
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Course\n[{str(len(cr))}]")
            self.lbl_course.after(200,self.update_details)


            cur.execute("select * from student")    
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")


            cur.execute("select * from result")    
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")


           
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")
             

    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)  
    
    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentClass(self.new_win) 
    
    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)     

    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)  

    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")
                                   
    def exit_(self):
        op=messagebox.askyesno("Confirm","Do you really want to exit?",parent=self.root)
        if op==True:
            self.root.destroy()
            


if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop() 