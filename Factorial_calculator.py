from tkinter import *
import math 
root=Tk()
root.title("! of a number")
def cal():
    t=e.get()
    t=int(t)
    result.config(text=math.factorial(t))
a=Label(root,text="Square_Root Calculator...",font=("Arial",32,"bold"))
a.pack()
e=Entry(root,font=("Arial",32,"bold"),bg="cyan",fg="blue")
e.pack()
b=Button(root,text="Calculate",font=("Arial",32,"bold"),bg="lime",command=cal)
b.pack()
result=Label(root,text="Result",font=("Arial",32,"bold"),fg="red",bg="hotpink")
result.pack()
root.config(bg="pink")
root.mainloop()