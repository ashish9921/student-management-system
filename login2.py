from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox

import mysql.connector
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("student Login")
        self.root.geometry("1350x750")


        self.name_var=StringVar()
        self.sir_var=StringVar()
        self.email_var=StringVar()
        self.pass_var=StringVar()

        self.im=Image.open("bg3.jpg")
        self.imn=ImageTk.PhotoImage(self.im)
        
        self.im_2=Image.open("log.jfif")
        self.imn2=ImageTk.PhotoImage(self.im_2)

                
        self.im_3=Image.open("sin.jfif")
        self.imn3=ImageTk.PhotoImage(self.im_3)
        
        self.root.config(bg="#081923")

        f_lable=Label(self.root,text= "SIGN UP",font=("times new romen" ,40,"bold"),bg="#081923",fg="white")
        f_lable.pack(pady=60)

        f_frame=Frame(self.root,bd=30,bg="#008EA4")
        f_frame.place(x=550,y=200,width=410,height=400)

        
        
    
        name_t=Label(f_frame,text="Name",font=("times new romen",20),bg="#008EA4")
        name_t.grid(row=1,column=0,sticky="w")

        name_e=Entry(f_frame,bd=5,width=15,font=("times new romen",20),textvariable=self.name_var)
        name_e.grid(row=1,column=1,padx=5)



        
        sir_t=Label(f_frame,text="Sir Name",font=("times new romen",20),bg="#008EA4")
        sir_t.grid(row=3,column=0, pady=10,sticky="w")

        sir_e=Entry(f_frame,bd=5,width=15,font=("times new romen",20),textvariable=self.sir_var)
        sir_e.grid(row=3,column=1,padx=5,pady=10)


        
        Email_t=Label(f_frame,text="Email",font=("times new romen",20),bg="#008EA4")
        Email_t.grid(row=5,column=0, pady=10,sticky="w")

        Email_e=Entry(f_frame,bd=5,width=15,font=("times new romen",20),textvariable=self.email_var)
        Email_e.grid(row=5,column=1,padx=5, pady=10)


        
        pass_t=Label(f_frame,text="Psssword",font=("times new romen",20),bg="#008EA4")
        pass_t.grid(row=7,column=0, pady=10,sticky="w")

        pass_e=Entry(f_frame,bd=5,width=15,font=("times new romen",20),textvariable=self.pass_var)
        pass_e.grid(row=7,column=1,padx=5, pady=10)
 

        s_frame=Label(self.root,image=self.imn)
        s_frame.place(x=320,y=200,width=230,height=400)


        LOG_t=Button(s_frame,image=self.imn2,width=140,height=40,command=self.log)
        LOG_t.grid(row=1,column=0, pady=300,padx=40)


        LOG_d=Button(f_frame,image=self.imn3,width=140,height=40,command=self.new)
        LOG_d.grid(row=8,columnspan=2,pady=20)



    def new(self):
        con=mysql.connector.connect(host="localhost",user="root",password="Man@1234",database="all_in_one")
        c=con.cursor() 
        c.execute('insert into clock2 value(%s,%s,%s,%s)',(self.name_var.get(),self.sir_var.get(),self.email_var.get(),self.pass_var.get()))   
        
        
        con.commit()
        con.close()  
    def log(self):
        self.root.destroy()
        import login
                
    
 
            
            
        
        


        
        
    

    
   



        





        



root=Tk()
obj=Register(root)
root.mainloop()





