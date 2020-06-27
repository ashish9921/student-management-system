from tkinter import*
from PIL import ImageTk,Image


def pahila():
    root.destroy()
    import clock

def dusara():
    root.destroy()
    import student_imfo

def tisara():
    root.destroy()
    import software    

root=Tk()
root.geometry("1350x750")

root.config(bg="#081923")
im=Image.open("cl.jfif")
imn=ImageTk.PhotoImage(im)

im2=Image.open("download.jfif")
imn2=ImageTk.PhotoImage(im2)

im3=Image.open("3rd.jpg")
imn3=ImageTk.PhotoImage(im3)


first=Button(image=imn,command=pahila)
first.place(x=200,y=200 ,width=320,height=250)

lab_1=Label(root,text="DIGITAL CLOCK",font=("time new roman ",20,"bold"),bg="#087587",fg="white")
lab_1.place(x=200,y=470,width=320,height=70)

first_2=Button(image=imn2,command=dusara)
first_2.place(x=540,y=200,width=320,height=250)

lab_2=Label(root,text="STUDENT INFO",font=("time new roman ",20,"bold"),bg="#008EA4",fg="white")
lab_2.place(x=540,y=470,width=320,height=70)

first_3=Button(image=imn3,text="Corse",command=tisara)
first_3.place(x=880,y=200 ,width=320,height=250)

lab_3=Label(root,text="STUDENT CORSE",font=("time new roman ",20,"bold"),bg="#DF002A",fg="white")
lab_3.place(x=880,y=470,width=320,height=70)

root.mainloop()