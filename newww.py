from tkinter import *
import os
from PIL import ImageTk,Image
#Main screen
master = Tk()
master.title('Movie Ticketing System')

master.geometry("639x698")
master.resizable(0,0)
load=Image.open('Login.png')
render=ImageTk.PhotoImage(load)
img=Label(master,image=render)
img.place(x=0,y=0)

def goto_sign():
    master.destroy()
    os.system('python signuppage.py')

def goto_login():
    master.destroy()
    os.system('python login.py')

btn=Image.open('/reg_img/Loginbtn.png')
ren=ImageTk.PhotoImage(btn)
img=Label(master,image=ren)
img.place(x=187,y=451)
login_img=Image.open("/reg_img/Loginbtn.png")
login_img=ImageTk.PhotoImage(login_img)

btn1=Image.open('/reg_img/ca button.png')
rend=ImageTk.PhotoImage(btn)
img=Label(master,image=rend)
img.place(x=187,y=451)
ca_img=Image.open("/reg_img/ca button.png")
ca_img=ImageTk.PhotoImage(ca_img)

#button
std_login_btn=Button(master,image=login_img,width=255,height=40,relief= FLAT, font=('arial',14,'bold'), bg='#00437c', fg='white',activebackground='#00437c', command=goto_login)
std_login_btn.place(x=187,y=361)


login_btn=Button(master,image=ca_img,width=21,height=2,relief= FLAT,border=0, font=('arial',14,'bold'), bg='#00437c', fg='white',activebackground='#00437c',command=goto_sign)
login_btn.place(x=187,y=451)

master.mainloop()
