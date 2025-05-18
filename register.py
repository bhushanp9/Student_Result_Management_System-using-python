from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import os


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration window")
        self.root.geometry("1550x900+0+0")

        # ======= Zoomed-in Background Image =======
        bg_image = Image.open("background_blur_image.jpg")

        # Resize the image to match the full window (or even bigger to zoom in)
        zoomed_bg = bg_image.resize((1600, 900))  # Zoomed-in size

        self.bg = ImageTk.PhotoImage(zoomed_bg)
        bg = Label(self.root, image=self.bg)
        bg.place(x=0, y=0, relwidth=1, relheight=1)



  #==============Left Image ===================


        self.left=ImageTk.PhotoImage(file="registration_background_image.png") 
        left=Label(self.root,image=self.left).place(x=300,y=100,width=800,height=500)


   #===============Register frame===============
        title = Label(self.root, text="Register Here", font=("times new roman", 20, "bold"), 
              bg="lightblue", fg="black")
        title.place(x=600, y=150) 

#================row 1

        

        f_name = Label(self.root, text="First Name", font=("times new roman", 15, "bold"), 
               fg="black")
        f_name.place(x=570, y=205) 

        self.txt_fname=Entry(self.root,font=("times new roman",15),bg="lightblue")
        self.txt_fname.place(x=570,y=240,width=200)



        self.var_lname=StringVar()
        l_name = Label(self.root, text="Last Name", font=("times new roman", 15, "bold"), 
               fg="black")
        l_name.place(x=850, y=205) 

        self.txt_lname=Entry(self.root,font=("times new roman",15),bg="lightblue",textvariable=self.var_lname)
        self.txt_lname.place(x=850,y=240,width=200)




 #=================================================== row 2
        contact = Label(self.root, text="Contact No", font=("times new roman", 15, "bold"), 
               fg="black")
        contact.place(x=570, y=285) 

        self.txt_contact=Entry(self.root,font=("times new roman",15),bg="lightblue")
        self.txt_contact.place(x=570,y=320,width=200)


        email = Label(self.root, text="Email", font=("times new roman", 15, "bold"), 
               fg="black")
        email.place(x=850, y=285) 

        self.txt_email=Entry(self.root,font=("times new roman",15),bg="lightblue")
        self.txt_email.place(x=850,y=320,width=200)




 #=========================================row3


        question = Label(self.root, text="Security Question", font=("times new roman", 15, "bold"), 
               fg="black")
        question.place(x=570, y=365) 

        
        self.cmd_quest=ttk.Combobox(self.root,font=("times new roman",13),state='readonly',justify=CENTER)

        self.cmd_quest['values']=("Select","Your first pet name","Your birth place","Your best friend name")
        self.cmd_quest.place(x=570,y=400,width=200)
        self.cmd_quest.current(0)


        answer = Label(self.root, text="Answer", font=("times new roman", 15, "bold"), 
               fg="black")
        answer.place(x=850, y=365) 

        self.txt_answer=Entry(self.root,font=("times new roman",15),bg="lightblue")
        self.txt_answer.place(x=850,y=400,width=200)    


 
 #=================================================== row 4

        password = Label(self.root, text="Password", font=("times new roman", 15, "bold"), 
               fg="black")
        password.place(x=570, y=445) 

        self.txt_password=Entry(self.root,font=("times new roman",15),bg="lightblue")
        self.txt_password.place(x=570,y=480,width=200)


        cpassword = Label(self.root, text="Confirm Password", font=("times new roman", 15, "bold"), 
               fg="black")
        cpassword.place(x=850, y=445) 

        self.txt_cpassword=Entry(self.root,font=("times new roman",15),bg="lightblue")
        self.txt_cpassword.place(x=850,y=480,width=200)    
       

       #=====================================
        self.var_chk=IntVar()

        chk = Checkbutton(self.root, text="I Agree terms and conditions",variable=self.var_chk,onvalue=1,font=("times new roman",14))
        chk.place(x=570, y=530) 



        btn_registered=Button(self.root,text='Register Now',font=("times new roman",15),bg="orange",activebackground="lightgray",cursor="hand2",command=self.register_data).place(x=850,y=525,width=200)



        btn_sign_in=Button(self.root,text='SignIn',command=self.login_window,font=("times new roman",15),bg="red",activebackground="lightgray",cursor="hand2",).place(x=470,y=460,width=80)


    

    def login_window(self):
       self.root.destroy()
       from login import Login  # ✅ Import the class, not the file/module
       root = Tk()
       obj = Login(root)        # ✅ Create object of Login class
       root.mainloop()
    

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.cmd_quest.current(0)

    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_email.get()==""or self.cmd_quest.get()=="Select"or self.txt_contact.get()=="" or self.txt_answer.get()=="" or self.txt_password.get()==""or   self.txt_cpassword.get()=="":

          messagebox.showerror("Error","All Fields are Required",parent=self.root)
        
        elif self.txt_password.get()!=self.txt_cpassword.get()=="":
            messagebox.showerror("Error","Password & Confirm password should be same",parent=self.root)   
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree our terms and conditions",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db") 
                cur=con.cursor()
                cur.execute("select * from employee where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already Exist,Please try with another email",parent=self.root)
                else:
                    cur.execute("insert into employee (f_name,l_name,contact,email,question,answer,password) values(?,?,?,?,?,?,?)",
                       (self.txt_fname.get(),
                        self.txt_lname.get(),
                        self.txt_contact.get(),
                        self.txt_email.get(),
                        self.cmd_quest.get(),
                        self.txt_answer.get(),
                        self.txt_password.get(),) )
                con.commit()
                con.close()
                messagebox.showinfo("Success","Register Successful",parent=self.root) 
                self.clear()
                self.login_window()

                
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)    

    
        



if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()