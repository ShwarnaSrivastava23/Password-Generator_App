import random
import string
from tkinter import *
import tkinter as tk

root = Tk()
root.geometry("500x300")
root.title("Password Generator")
root.config(bg="light blue")

def gen():
    num = int(e1.get())
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    password = s[0:num]

    show_data = Label(root,text="Password:", font = " time 15 bold",bg="white")
    show_data.place(x=30,y=245)

    show_lbl= Label(root, text = password, font = "time 15 bold", width=15, bg="white")
    show_lbl.place(x=150,y=245)


Title = Label(root,text="Password Generator",bg="grey",fg="black",font=("times new roman",30,"bold"))
Title.place(x=0,y=10,width=500)

Title_show = Label(root,text="Enter Password Length:",fg="white",bg="blue",font=("times new roman",18,"bold"))
Title_show.place(x = 30, y=90)

e1 = Entry(root,width=40,bd=5,font="times 13 roman")
e1.place(x=30,y=140)

button = Button(root,text = "Generate Password",fg="black",bg="yellow",font="time 15 bold",width=34,command = gen)
button.place(x=30,y=175,width=400,height=30)


root.mainloop()