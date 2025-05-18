from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import messagebox
from register import Register 
import sqlite3
import os  # Import Register

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login pages")
        self.root.geometry("1550x900+0+0")

        bg_image = Image.open("background_blur_image.jpg")
        zoomed_bg = bg_image.resize((1600, 900))
        self.bg = ImageTk.PhotoImage(zoomed_bg)
        bg = Label(self.root, image=self.bg)
        bg.place(x=0, y=0, relwidth=1, relheight=1)

        login_frame = Frame(self.root, bg="lightyellow")
        login_frame.place(x=350, y=100, width=800, height=500)

        title = Label(login_frame, text="Login Here", font=("times new roman", 30, "bold"), 
                      bg="lightyellow", fg="black")
        title.place(x=280, y=50)

        email = Label(login_frame, text="Email Address", font=("times new roman",18 , "bold"), 
                      bg="lightyellow", fg="gray")
        email.place(x=280, y=150)  

        self.txt_email = Entry(login_frame, font=("times new roman",18), bg="white", fg="gray")
        self.txt_email.place(x=280, y=180, width=350)

        pass_word = Label(login_frame, text="Password", font=("times new roman",18 , "bold"), 
                          bg="lightyellow", fg="gray")
        pass_word.place(x=280, y=230)  

        self.txt_pass = Entry(login_frame, font=("times new roman",18), bg="white", fg="gray", show="*")
        self.txt_pass.place(x=280, y=260, width=350)

        btn_reg = Button(login_frame, text="Register new account", font=("time new roman",14), 
                         bg="lightyellow", bd=0, fg="#B00857", cursor="hand2", command=self.register_window)
        btn_reg.place(x=280, y=300)


        btn_forget = Button(login_frame, text="Forget Password", font=("time new roman",13), 
                         bg="lightyellow", bd=0, fg="red", cursor="hand2", command=self.forget_password_window)
        btn_forget.place(x=500, y=304)


        btn_login = Button(login_frame, text="Login",command=self.login, font=("time new roman",14), 
                           bg="yellow", bd=0, fg="red", cursor="hand2")
        btn_login.place(x=280, y=340, width=120)


    def reset(self):
        self.cmd_quest.current(0)
        self.txt_new_pass.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_pass.delete(0,END)
        self.txt_email.delete(0,END)
         





    def forget_password(self):
        if self.cmd_quest.get()=="Select" or self.txt_answer.get()==""   or self.txt_new_pass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        else: 
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and question=? and answer=?",(self.txt_email.get(),self.cmd_quest.get(),self.txt_answer.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Select the Correct Security Question/ Enter answer",parent=self.root2)
                else: 
                    cur.execute("update employee set password=? where email=? ",(self.txt_new_pass.get(),self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Your Password Has Been Reset,please Login with new Password",parent=self.root2)
                    
                    self.reset()
                    self.root2.destroy()
                    
                



            except Exception as es:
               messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)       

        
    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset the password",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please enter the valid email address to reset the password",parent=self.root)
                else:
                   
                   con.close()
                   self.root2=Toplevel()
                   self.root2.title("Forget Password")
                   self.root2.geometry("350x400+530+150")
                   self.root2.config(bg="white")
                   self.root2.focus_force()
                   self.root2.grab_set()

                   t=Label(self.root2,text="Forget password",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)

#===================Forget password===============

                   question = Label(self.root2, text="Security Question", font=("times new roman", 15, "bold"), 
                   fg="black")
                   question.place(x=50, y=100) 

        
                   self.cmd_quest=ttk.Combobox(self.root2,font=("times new roman",13),state='readonly',justify=CENTER)

                   self.cmd_quest['values']=("Select","Your first pet name","Your birth place","Your best friend name")
                   self.cmd_quest.place(x=50,y=130,width=250)
                   self.cmd_quest.current(0)


                   answer = Label(self.root2, text="Answer", font=("times new roman", 15, "bold"), 
                    fg="black")
                   answer.place(x=50, y=180) 

                   self.txt_answer=Entry(self.root2,font=("times new roman",15),bg="lightblue")
                   self.txt_answer.place(x=50,y=210,width=250)


                   new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), 
                   fg="black")
                   new_password.place(x=50, y=260) 

                   self.txt_new_pass=Entry(self.root2,font=("times new roman",15),bg="lightblue")
                   self.txt_new_pass.place(x=50,y=290,width=250)

                   btn_change_password=Button(self.root2,text="Reset password",command=self.forget_password,bg="green",fg="white",font=("times new roman",15,"bold")).place(x=80,y=340)


                    
                    

            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)  

            

       



    def login(self):
        if self.txt_email.get()=="" or self.txt_pass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and password=?",(self.txt_email.get(),self.txt_pass.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error",f"Invalid USERNAME & PASSWORD: {str(es)}",parent=self.root)
                else:
                    messagebox.showinfo("Success",f"Welcome:-{self.txt_email.get()}",parent=self.root) 
                    self.root.destroy()
                    os.system("python dashboard.py")
                con.close()    

            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)        





    def register_window(self):
        self.root.destroy()
        import register
        root = Tk()
        obj = Register(root)
        root.mainloop()
        
if __name__ == "__main__":
   root = Tk()
   obj = Login(root)
   root.mainloop()
