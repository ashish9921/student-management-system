from tkinter import*
import time
import pyttsx3
root=Tk()
root.geometry("1350x750")
root.title("Digital Clock")
root.config(bg="#081923")


def clock():
    h=str(time.strftime("%H"))
    m=str(time.strftime("%M"))
    s=str(time.strftime("%S"))
    p=str(time.strftime("%p"))
    
        
    lable.config(text=h)
    lable_s1.config(text=m)
    lable_s2.config(text=s)
    lable_s3.config(text=p)
    

    lable.after(200,clock)
def nam(a):
    l=-30
    if l==-30:
        l+=1
    lable.place(y=200+l)
      

def man(s):
    l=0
    if l!=0:
        l+=1
    lable.place(y=200+l)
def hello(a):
    aa=pyttsx3.init()

    aa.say(f' {(time.strftime("%H"))}')
    aa.runAndWait()    
     
def hello(a):
    aa=pyttsx3.init()

    aa.say(f' {(time.strftime("%H"))}')
    aa.runAndWait()   
def hello1(a):
    aa=pyttsx3.init()

    aa.say(f' {(time.strftime("%M"))}')
    aa.runAndWait()          
def hello2(a):
    aa=pyttsx3.init()

    aa.say(f' {(time.strftime("%S"))}')
    aa.runAndWait()   

def back():
    root.destroy()
    import apps  
    btn.after(200,back)        
    

 
    





lable=Label(root,text="12",font=("times new roman ",50,"bold"),bg="#087587",fg="white")
lable.place(x=350,y=200,width=150,height=150)
lable.bind("<Enter>",nam)
lable.bind("<Leave>",man)
lable.bind('<Button-1>', hello)


lable_h1=Label(root,text="HOUR",font=("times new roman ",20,"bold"),bg="#087587",fg="white")
lable_h1.place(x=350,y=360,width=150,height=40)


lable_s1=Label(root,text="60",font=("times new roman ",50,"bold"),bg="#008EA4",fg="white")
lable_s1.place(x=520,y=200,width=150,height=150)
lable_s1.bind('<Button-1>', hello1)

lable_h2=Label(root,text="MIN",font=("times new roman ",20,"bold"),bg="#008EA4",fg="white")
lable_h2.place(x=520,y=360,width=150,height=40)


lable_s2=Label(root,text="60",font=("times new roman ",50,"bold"),bg="#DF002A",fg="white")
lable_s2.place(x=690,y=200,width=150,height=150)
lable_s2.bind('<Button-1>', hello2)

lable_h3=Label(root,text="SEC",font=("times new roman ",20,"bold"),bg="#DF002A",fg="white")
lable_h3.place(x=690,y=360,width=150,height=40)


lable_s3=Label(root,text="AM",font=("times new roman ",50,"bold"),bg="#DF002A",fg="white")
lable_s3.place(x=860,y=200,width=150,height=150)

lable_h4=Label(root,text="NOON",font=("times new roman ",20,"bold"),bg="#DF002A",fg="white")
lable_h4.place(x=860,y=360,width=150,height=40)

btn=Button(root,text="Back",font=("times new roman",20,"bold"),bg="#DF002A",fg="white",command=back)
btn.place(x=50,y=20 ,width=80,height=30)


clock()




    

root.mainloop()