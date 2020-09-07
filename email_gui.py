from tkinter import *
import os
import feat2 
from tkinter import filedialog as fd

filename=[]
def choose():
   filename.append(fd.askopenfilename())
   attachmentarea.configure(state='normal')
   attachmentarea.insert(END, ((filename[-1]).split('/')[-1])+"\n")
   attachmentarea.configure(state='disabled')

def back():
   e2.delete(0,END)
   e1.delete(0,END)
   textarea.delete(1.0,END)
   attachmentarea.configure(state='normal')
   attachmentarea.delete(1.0,END)
   attachmentarea.configure(state='disabled')


def submit():
    sub = e2.get()
    to = e1.get()
    body = textarea.get(1.0,END)

    feat2.mail(to, sub, body, filename)
    print("Mail sent.")
    back()



m=Tk()
m.geometry("780x600")

m.iconbitmap(r'your_icon_path')

m.title("New Message")
l1=Label(m,text="To").place(x=40,y=10)
l2=Label(m,text="Subject").place(x=10,y=40)
e1=Entry(m,bd=5)
e1.grid(row=0,column=1)
e1.place(x=60,y=10,width=180)
e2=Entry(m,bd=5)
e2.grid(row=1,column=1)
e2.place(x=60,y=40,width=180)
#e3=Entry(m)
#e3.place(x=10,y=90,width=450,height=300)
textarea=Text()
textarea.place(x=10,y=90)
b1=Button(m,text="Send",width=12,height=2, command = submit).place(x=680,y=190)

b2=Button(m,text="Attach",width=12,height=2, command = choose)
b2.place(x=10,y=500)

attachmentarea=Text(width=30, height=4, bg='#C0C0C0')
attachmentarea.place(x=120,y=500)

#photo=PhotoImage(file=r"C:\Users\Lenovo\Desktop\Folder\Code\python\images\android.png")
#attachment=Button(m,image=photo,width=40,height=30).place(x=10,y=397)
#p1=PhotoImage(file=r"C:\Users\Lenovo\Desktop\Folder\Code\python\images\android.png")
#emo=Button(m,image=p1,width=40,height=30).place(x=80,y=397)


m.mainloop()
