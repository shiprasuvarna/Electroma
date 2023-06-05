from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

img = PhotoImage(file='login.png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Log in',fg='#57a1f8',bg='white',font=('Microasoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

user = Entry(frame,width=25,fg='black',border=2,bg="white",font=('Microasoft YaHei UI Light',23,'bold'))
user.place(x=30,y=80)
user.insert(0,'Username')

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)


root.mainloop()
