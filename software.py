from tkinter import*
from tkinter import ttk,messagebox
import time
import os 

class file_app:
    def __init__(self,root):
        self.root=root
        self.root.title("file Based Record System")
        self.root.geometry("1350x750")

        self.s_id=StringVar()
        self.name_id=StringVar()
        self.course_id=StringVar()
        self.add_id=StringVar()
        self.city_id=StringVar()
        self.contact_id=StringVar()
        self.date_id=StringVar()
        self.degree_id=StringVar()
        self.proof_id=StringVar()
        self.payment_id=StringVar()
        


        all_Frame=Frame(self.root,bd=10,relief=GROOVE,bg="royalblue")
        all_Frame.place(x=0,y=0,width=1350,height=700)

        app_title=Label(self.root,text="File Based Record system",bd=10, relief=GROOVE,font=("time now roman",35,"bold"),bg="yellow",fg="black")
        app_title.pack(fill=X,pady=10)

        student_Frame=Frame(self.root,bd=10,relief=GROOVE,bg="royalblue")
        student_Frame.place(x=20,y=100,width=880,height=400)

        stitle=Label(student_Frame,text="Student Details",font=("times new roma",20,"bold"),bg="royalblue")
        stitle.grid(row=0,columnspan=7,pady=10,padx=10)

        student_id=Label(student_Frame,text="Student ID",font=("times new roma",20,"bold"),bg="royalblue")
        student_id.grid(row=1,column=0,pady=10,sticky="w")

        txtid=Entry(student_Frame,bd=7,textvariable=self.s_id,relief=GROOVE,width=20,font="arial 15 bold")
        txtid.grid(row=1,column=1)

        student_name=Label(student_Frame,text="Name",font=("times new roma",20,"bold"),bg="royalblue")
        student_name.grid(row=2,column=0,pady=10,sticky="w")

        txt_name=Entry(student_Frame,bd=7,textvariable=self.name_id,relief=GROOVE,width=20,font="arial 15 bold")
        txt_name.grid(row=2,column=1)

        student_course=Label(student_Frame,text="Course",font=("times new roma",20,"bold"),bg="royalblue")
        student_course.grid(row=3,column=0,pady=10,sticky="w")

        txt_course=Entry(student_Frame,bd=7,textvariable=self.course_id,relief=GROOVE,width=20,font="arial 15 bold")
        txt_course.grid(row=3,column=1)

        student_add=Label(student_Frame,text="Address",font=("times new roma",20,"bold"),bg="royalblue")
        student_add.grid(row=4,column=0,pady=10,sticky="w")

        txt_add=Entry(student_Frame,bd=7,textvariable=self.add_id,relief=GROOVE,width=20,font="arial 15 bold")
        txt_add.grid(row=4,column=1)

        student_city=Label(student_Frame,text="City",font=("times new roma",20,"bold"),bg="royalblue")
        student_city.grid(row=5,column=0,pady=10,sticky="w")

        txt_city=Entry(student_Frame,bd=7,textvariable=self.city_id,relief=GROOVE,width=20,font="arial 15 bold")
        txt_city.grid(row=5,column=1)

        student_no=Label(student_Frame,text="Phone No.",font=("times new roma",20,"bold"),bg="royalblue")
        student_no.grid(row=1,column=2,pady=10,sticky="w")

        txt_no=Entry(student_Frame,bd=7,textvariable=self.contact_id,relief=GROOVE,width=20,font="arial 15 bold")
        txt_no.grid(row=1,column=3)

        student_DOB=Label(student_Frame,text="DOB",font=("times new roma",20,"bold"),bg="royalblue")
        student_DOB.grid(row=2,column=2,pady=10,sticky="w")

        txt_DOB=Entry(student_Frame,bd=7,textvariable=self.date_id,relief=GROOVE,width=20,font="arial 15 bold")
        txt_DOB.grid(row=2,column=3)

        student_Select=Label(student_Frame,text="Select Degree",font=("times new roma",20,"bold"),bg="royalblue")
        student_Select.grid(row=3,column=2,pady=10,sticky="w")


        combo_gender=ttk.Combobox(student_Frame,textvariable=self.degree_id ,font=("times new romen",13,"bold"),state="readonly")
        combo_gender["values"]=("postgraduate","graduate","12Th pass")
        combo_gender.grid(row=3,column=3,pady=20)


        student_idp=Label(student_Frame,text="ID Proof",font=("times new roma",20,"bold"),bg="royalblue")
        student_idp.grid(row=4,column=2,pady=10,sticky="w")


        combo_id=ttk.Combobox(student_Frame ,textvariable=self.proof_id,font=("times new romen",13,"bold"),state="readonly")
        combo_id["values"]=("Passport","Driving lisuns","voting card")
        combo_id.grid(row=4,column=3,pady=20)

        
        student_pement=Label(student_Frame,text="Pement Mode",font=("times new roma",20,"bold"),bg="royalblue")
        student_pement.grid(row=5,column=2,pady=10,sticky="w")


        combo_pement=ttk.Combobox(student_Frame ,textvariable=self.payment_id,font=("times new romen",13,"bold"),state="readonly")
        combo_pement["values"]=("Cash","UPI","online banking")
        combo_pement.grid(row=5,column=3,pady=20)

        student_btn=Frame(self.root,bd=10,relief=GROOVE,bg="gray")
        student_btn.place(x=20,y=540,width=1330,height=100)

        btn_save=Button(student_btn,text="Save" ,width=25,height=3,bg="violet",command=self.save_data)
        btn_save.grid(padx=20,pady=10,row=0,column=0)

        btn_delet=Button(student_btn,text="Delete" ,width=25,height=3,bg="violet",command=self.delete)
        btn_delet.grid(padx=20,pady=10,row=0,column=1)

        btn_Clear=Button(student_btn,text="Clear" ,width=25,height=3,bg="violet",command=self.clear)
        btn_Clear.grid(padx=20,pady=10,row=0,column=2)

        btn_Logout=Button(student_btn,text="Logout" ,width=25,height=3,bg="violet",command=self.logout)
        btn_Logout.grid(padx=20,pady=10,row=0,column=3)

        btn_Exit=Button(student_btn,text="Exit" ,width=25,height=3,bg="violet",command=self.exit)
        btn_Exit.grid(padx=20,pady=10,row=0,column=4)

        student_txt=Frame(self.root,bd=10,relief=GROOVE,bg="royalblue")
        student_txt.place(x=940,y=100,width=400,height=400)

        stitle_1=Label(student_txt,text="Student Details",font=("times new roma",20,"bold"),bg="royalblue",bd=10,relief=GROOVE)
        stitle_1.pack(fill=X)

        scrol_y=Scrollbar(student_txt,orient=VERTICAL)
        scrol_y.pack(side=RIGHT,fill=Y)

        self.file_list=Listbox(student_txt,yscrollcommand=scrol_y.set)
        self.file_list.pack(fill=BOTH,expand=1)
        scrol_y.config(command=self.file_list.yview)
        self.show_files()
        self.file_list.bind("<ButtonRelease-1>",self.get_data)

    def save_data(self):
   

            if self.s_id.get()=="" or self.add_id.get()=="" or self.city_id.get()=="":
                msg=messagebox.showerror("error","please fill all the filds")


            else:
                f=open("E:\\my creation\\software\\record system\\files\\"+str(self.s_id.get())+".txt","w")
                f.write(
                    str(self.s_id.get())+","+
                    str(self.name_id.get())+","+
                    str(self.course_id.get())+","+
                    str(self.add_id.get())+","+
                    str(self.city_id.get())+","+
                    str(self.contact_id.get())+","+
                    str(self.degree_id.get())+","+
                    str(self.date_id.get())+","+
                    str(self.payment_id.get())+","+
                    str(self.proof_id.get())
                       )    
                f.close()  
                self.show_files()     
    def show_files(self):
        files=os.listdir("E:\\my creation\\software\\record system\\files\\")
        if len(files)>0:
            
            self.file_list.delete(0,END)
            for i in files:
                self.file_list.insert(END,i)

    def get_data(self,ev):
        get_curse=self.file_list.curselection()
        f1=open("E:\\my creation\\software\\record system\\files\\"+self.file_list.get(get_curse))
        valu=[]
        for f in f1:
            valu=f.split(",")
            print(valu)
        self.s_id.set(valu[0])
        self.name_id.set(valu[1])
        self.course_id.set(valu[2])
        self.add_id.set(valu[3])
        self.city_id.set(valu[4])
        self.contact_id.set(valu[5])
        self.date_id.set(valu[6])
        self.degree_id.set(valu[7])
        self.proof_id.set(valu[8])
        self.payment_id.set(valu[9])  

    def clear (self):

        self.s_id.set("")
        self.name_id.set("")
        self.course_id.set("")
        self.add_id.set("")
        self.city_id.set("")
        self.contact_id.set("")
        self.date_id.set("")
        self.degree_id.set("")
        self.proof_id.set("")
        self.payment_id.set("")  
    def delete(self):
        present ="no"
        if self.s_id.get()=="":
            messagebox.showerror("error","sir id is not awaylable")
        else:
            s=os.listdir("E:\\my creation\\software\\record system\\files\\")   
            if len(s)>0:
                for i in s:
                    if i.split(".")[0]==self.s_id.get():
                        present="yes"
                    if present=="yes":
                        ask=messagebox.askquestion("Delete","sir you want to delete this file?")
                        if ask>str(0):
                            os.remove("E:\\my creation\\software\\record system\\files\\"+self.s_id.get()+".txt")
                            self.show_files()      
    
    def exit (self):
        option=messagebox.askyesno("Exit","do you really want to exit?")
        if option>(0):
            self.root.destroy()

    def logout(self):
        self.root.destroy()
        import login

 





root=Tk()
ob=file_app(root)
root.mainloop()