from tkinter import *
import webbrowser #use to do operations on webbrowser
root=Tk()
root.title("PY_browser")
def search():
    t=e.get() #gets input from the entry box
    webbrowser.open(t) #used to open the query said by user in entry box in browser
e=Entry(root,font=("Arial",35,"bold"),width=40,bg="pink",fg="red") # here user gives the input to search
e.pack()
b=Button(root,width=20,bg="lime",fg="blue",font=("Arial",35,"bold"),text="search",command=search) #button gives action by command
b.pack()
root.mainloop()