from tkinter import *
import os
from PIL import ImageTk,Image

#Main screen
root = Tk()
root.title('Movie Ticketing System')
root.geometry("637x688")
root.resizable(0,0)
root.geometry("637x688")
root.resizable(0,0)
pic=Image.open('account.png')
ren=ImageTk.PhotoImage(pic)
img=Label(root,image=ren)
img.place(x=0,y=0)

def goto_homepage():
    root.destroy()
    os.system('python newww.py')



std_id=Entry(root,bd=10,width=21,relief=FLAT, font=('arial',14,'bold'), bg='#00437c', fg='turquoise3')
std_id.place(x=260,y=178)

last=Entry(root,bd=10,width=21,relief= FLAT, font=('arial',14,'bold'), bg='#00437c', fg='white')
last.place(x=260,y=236)

email=Entry(root,bd=10,width=21,relief= FLAT, font=('arial',14,'bold'), bg='#00437c', fg='white')
email.place(x=260,y=292)


phone=Entry(root,bd=10,width=21,relief= FLAT, font=('arial',14,'bold'), bg='#00437c', fg='white')
phone.place(x=260,y=350)


password=Entry(root,bd=10,width=21,relief= FLAT, font=('arial',14,'bold'), bg='#00437c', fg='white')
password.place(x=260,y=407)


c_password=Entry(root,bd=10,width=21,relief= FLAT, font=('arial',14,'bold'), bg='#00437c', fg='white')
c_password.place(x=260,y=465)

submit_btn=Button(root,text="submit",width=27,height=2,font=("arial",14,'bold'),fg='white',bg='#00437c',relief=FLAT,activebackground='#00437c',command=goto_homepage)
submit_btn.place(x=157,y=586)

root.mainloop()
