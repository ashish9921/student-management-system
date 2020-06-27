
###-------my bro i tell you befor lern data base but you dont understand now problem is created "this program is not
#--------complited because of data base is not lern go to first complit web devhalpment tutorial 
#----lern php & php my admin django, and then com here



from tkinter import*
from tkinter import ttk
import pymysql
import mysql.connector


class student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Student Management System",bd=10 ,relief=GROOVE,font=("times new romen",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)

        #---variable--#
        self.roll_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self.add_var=StringVar()



        manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        manage_Frame.place(x=20,y=100,width=450,height=600)

        m_title=Label(manage_Frame,text="Manage Student",bg="crimson",fg="white", font=("times new romen",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll=Label(manage_Frame,text="Roll No",bg="crimson",fg="white", font=("times new romen",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        txt_roll=Entry(manage_Frame,textvariable=self.roll_var ,font=("times new romen",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20)
        
        lbl_name=Label(manage_Frame,text="Name",bg="crimson",fg="white", font=("times new romen",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        txt_name=Entry(manage_Frame,textvariable=self.name_var ,font=("times new romen",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20)
        
        lbl_Email=Label(manage_Frame,text="Email",bg="crimson",fg="white", font=("times new romen",20,"bold"))
        lbl_Email.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        txt_Email=Entry(manage_Frame,textvariable=self.email_var ,font=("times new romen",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=10,padx=20)
        
        lbl_Gender=Label(manage_Frame,text="Gender",bg="crimson",fg="white", font=("times new romen",20,"bold"))
        lbl_Gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")
        
        combo_gender=ttk.Combobox(manage_Frame,textvariable=self.gender_var ,font=("times new romen",13,"bold"),state="readonly")
        combo_gender["values"]=("male","femail","other")
        combo_gender.grid(row=4,column=1,pady=20)

        lbl_Contact=Label(manage_Frame,text="Contact",bg="crimson",fg="white", font=("times new romen",20,"bold"))
        lbl_Contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        txt_Contact=Entry(manage_Frame,textvariable=self.contact_var ,font=("times new romen",15,"bold"),bd=5,relief=GROOVE)
        txt_Contact.grid(row=5,column=1,pady=10,padx=20)

        lbl_Dbb=Label(manage_Frame,text="D.O.B",bg="crimson",fg="white", font=("times new romen",20,"bold"))
        lbl_Dbb.grid(row=6,column=0,pady=10,padx=20,sticky="w")
        txt_Dob=Entry(manage_Frame,textvariable=self.dob_var ,font=("times new romen",15,"bold"),bd=5,relief=GROOVE)
        txt_Dob.grid(row=6,column=1,pady=10,padx=20)

        lbl_Address=Label(manage_Frame,text="Address",bg="crimson",fg="white", font=("times new romen",20,"bold"))
        lbl_Address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        self.txt_address=Text(manage_Frame,width=29,height=3)
        self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="w")    

     
    #Button ####################################################################

        btn_Frame=Frame(manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=6,y=530,width=430)

        Add_btn=Button(btn_Frame,text="Add",width=10,command=self.add_student)
        Add_btn.grid(row=0,column=0,padx=10,pady=10)

        clear_btn=Button(btn_Frame,text="Clear",width=10,command=self.Clear)
        clear_btn.grid(row=0,column=1,padx=10,pady=10)

        Update_btn=Button(btn_Frame,text="Update",width=10,command=self.update_data)
        Update_btn.grid(row=0,column=2,padx=10,pady=10)
        
        delete=Button(btn_Frame,text="Delete",width=10,command=self.delet_data)
        delete.grid(row=0,column=3,padx=10,pady=10)


        delete=Button(self.root,text="<==",width=10,font=("times new roman ",10,"bold"),bg="#008EA4",fg="white",command=self.back)
        delete.place(x=20,y=30)
  



                 




        Detail_frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_frame.place(x=500,y=100,width=800,height=600)

        lbl_serch=Label(Detail_frame,text="Serch By",bg="crimson",fg="white", font=("times new romen",20,"bold"))
        lbl_serch.grid(row=0,column=0,pady=10,padx=20,sticky="w")    

        combo_serch=ttk.Combobox(Detail_frame,width=10,font=("times new romen",13,"bold"),state="readonly")
        combo_serch["values"]=("Roll","Name","Contact")
        combo_serch.grid(row=0,column=1,pady=20)

        txt_Serch=Entry(Detail_frame,font=("times new romen",14,"bold"),bd=5,relief=GROOVE)
        txt_Serch.grid(row=0,column=2,pady=10,padx=20)

        serch_btn=Button(Detail_frame,text="Serch",width=10)
        serch_btn.grid(row=0,column=3,padx=10,pady=12)

        show_btn=Button(Detail_frame,text="Show All",width=10,height=1)
        show_btn.grid(row=0,column=4,padx=10,pady=12)


#---------Table Frame ahe ha -------hava-----#

        
        Table_frame=Frame(Detail_frame,bd=4,relief=RIDGE,bg="crimson")
        Table_frame.place(x=10,y=70,width=760,height=500)
        
        scroll_bar_x=Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_bar_y=Scrollbar(Table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(Table_frame,columns=("Roll","Name","Email","Gender","Contact","DOB","Address"),xscrollcommand=scroll_bar_x.set,yscrollcommand=scroll_bar_y.set)
        scroll_bar_x.pack(side=BOTTOM,fill=X)
        scroll_bar_y.pack(side=RIGHT,fill=Y)
        scroll_bar_x.config(command=self.student_table.xview)
        scroll_bar_y.config(command=self.student_table.yview)
        self.student_table.heading("Roll",text="Roll No")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Contact",text="Contact")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Address",text="Address")

        self.student_table['show']="headings"
        self.student_table.column("Roll",width=120)
        self.student_table.column("Name",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Contact",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Address",width=120)
        self.event()
        

        self.student_table.pack(fill=BOTH,expand=1)
        self.feachdata()

    def add_student(self):
        con=mysql.connector.connect(host="localhost",user="root",password="Man@1234",database="my4")
        cur=con.cursor()
        cur.execute('insert into student value(%s,%s,%s,%s,%s,%s,%s)',(self.roll_var.get(),self.name_var.get(),self.email_var.get(),
        self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.txt_address.get('1.0',END)))
        con.commit()
        self.feachdata()
        self.Clear()
        con.close()

    def feachdata(self):
        con=mysql.connector.connect(host="localhost",user="root",password="Man@1234",database="my4")
        cur=con.cursor()
        cur.execute("select * from student")
        
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values=row)
                con.commit()
        con.close()   

    def Clear(self):
        self.roll_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete('1.0',END)

    def get_curser(self,ev):
        cursor_r=self.student_table.focus()
        content=self.student_table.item(cursor_r)
        rowa=content['values']
        

        self.roll_var.set(rowa[0])
        self.name_var.set(rowa[1])
        self.email_var.set(rowa[2])
        self.gender_var.set(rowa[3])
        self.contact_var.set(rowa[4])
        self.dob_var.set(rowa[5])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,rowa[6])

    def event(self):
        self.student_table.bind("<ButtonRelease>",self.get_curser)    

    def update_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="Man@1234",database="my4")
        cur=con.cursor()
        cur.execute('update student set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s',(self.name_var.get(),self.email_var.get(),
        self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.txt_address.get('1.0',END),self.roll_var.get()))
        con.commit()
        self.feachdata()
        self.Clear()
        con.close()

    
    def delet_data(self):


        con=mysql.connector.connect(host="localhost",user="root",password="Man@1234",database="my4")
        cur=con.cursor()
        cur.execute("delete from student where roll_no=%s",self.roll_var.get())
        con.commit()
        self.feachdata()
        self.Clear()
        con.close()
    def back(self):
        self.root.destroy()
        import apps    
            




        




   

        
root=Tk()
obj=student(root)
root=mainloop()