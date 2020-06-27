from tkinter import*
from tkinter import messagebox
from PIL import  Image ,ImageTk
import pymysql
import pyttsx3
import mysql.connector
class Login:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x750")
        self.root.title("file based Record System")
        f1=Frame(self.root,bd=10,relief=GROOVE)
        f1.place(x=450,y=150,height=310)

        self.user=StringVar()
        self.pass_word=StringVar()
        

        title=Label(f1,text="Login system",font=("times new roman",30,"bold")).grid(row=0,column=1,pady=10 ,padx=20)

        username=Label(f1,text="User Name",font=("times new roman",20,"bold")).grid(row=1,column=0,padx=10)

        txtuser=Entry(f1,bd=7,relief=GROOVE,width=27,textvariable=self.user,font=("arial 15 bold")).grid(row=1,column=1,pady=10,padx=10)
        

        passw=Label(f1,text="Password",font=("times new roman",20,"bold")).grid(row=2,column=0,padx=10)

        text_passw=Entry(f1,bd=7,relief=GROOVE,show="*",width=27,textvariable=self.pass_word,font=("arial 15 bold")).grid(row=2,column=1,pady=10,padx=10)

        btn_log=Button(f1,text="Login",font="arial 15 bold",bd=7,width=10,command=self.logfun)
        btn_log.place(x=10,y=220)

        btn_reset=Button(f1,text="Reset",font="arial 15 bold",bd=7,width=10,command=self.reset).place(x=170,y=220)

        btn_exit=Button(f1,text="Exit",font="arial 15 bold",bd=7,width=10,command=self.exitfun).place(x=320,y=220)
         

        
    def logfun(self):
        s=[]
        con=mysql.connector.connect(host="localhost",user="root",password="Man@1234",database="all_in_one")
        cur=con.cursor()
        cur.execute("select * from clock2")      
    
        rows=cur.fetchall()
        for r in rows:  
            if self.user.get()==r[0] and self.pass_word.get()==r[3]:
                self.tock(f"{r[0]} sir wellcom to jumanji ")
                self.root.destroy()
                import apps
            else:
                a=print("c")

        con.close()        
                
    def tock(self,a):  
        aa=pyttsx3.init()
        aa.say(a)
        aa.runAndWait() 


                

                    

                
               
                    


    
        
    
    def reset(self):
        self.user.set("")
        self.pass_word.set("")

    def exitfun(self):
        option=messagebox.askyesno("Exit","do you really want to exit?")
        if option>0:
            self.root.destroy()

    
root=Tk()
ob=Login(root)
root.mainloop()



