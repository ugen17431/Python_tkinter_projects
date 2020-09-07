from tkinter import *
root=Tk()
root.title("Buttons")
def cal():
    t=e.get()
    root.config(bg=t)
e=Entry(root,width="20",bg="cyan",font=("Helvitica",35,"bold"),fg="red")
e.pack()
b=Button(root,text="Click to change theme",width=20,bg="yellow",command=cal,font=("Helvitica",35,"bold"))
b.pack()
root.mainloop()

#font=(family,size,weight)
