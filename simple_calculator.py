from tkinter import *
root=Tk()
var=StringVar()
def calc():
    t=e.get()
    k.config(text=eval(t))
l=Label(root,text="Simple_Calculator",bg="grey",font=("Comic Sans MS",32,"bold"))
l.pack()
e=Entry(root,bg="cyan",fg="red",textvariable=var,font=("Comic Sans MS",32,"bold"))
e.pack()
b=Button(root,text="Calculate",font=("Comic Sans MS",20,"bold"),bg="green",command=calc,width=20)
b.pack()
k=Label(root,text="Result",font=("Comic Sans MS",32,"bold"),bg="grey")
k.pack()
root.config(bg="grey")
root.mainloop()
