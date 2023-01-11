import tkinter
from tkinter import *

#create root window
root = Tk()
root.geometry("300x400")

#for preventing alphabet entry
def calresultack(input):
        if input.isdigit()==True:
            return True
        else:
            return False

def clear():
    num1.delete(0,END)
    num2.delete(0,END)

def add():
    n1=int(num1.get())
    n2=int(num2.get())
    ans=n1+n2
    result.config(text=ans)

def diff():
    n1=int(num1.get())
    n2=int(num2.get())
    ans=n1-n2
    result.config(text=ans) 

def div():
    n1=int(num1.get())
    n2=int(num2.get())
    ans=n1/n2
    ans=round(ans,10)
    result.config(text=ans) 

def mul():
    n1=int(num1.get())
    n2=int(num2.get())
    ans=n1*n2
    result.config(text=ans)    

Label(root,text="First num",font= ('Mistral 10 bold')).pack()
num1 = Entry(root,font=("arial", 22), fg="white", bg="black",width = 10)
num1.pack()
#reg = root.register(calresultack)
#num1.config(validate ="key",validatecommand =(reg, '%P'))

Label(root,text="Second num",font=('Mistral 10 bold')).pack()
num2 = Entry(root,font=("arial", 22), fg="white", bg="black",width = 10)
num2.pack()
#reg = root.register(calresultack)
#num2.config(validate ="key",validatecommand =(reg, '%P'))

result= Label(root,font=("arial", 24), fg="white", bg="black",text="")
result.pack(pady=5)

addition = Button(root,text = "+",height= 3, width=5,command=add).pack(side=LEFT)
subtraction = Button(root,text = "-",height= 3, width=5,command=diff).pack(side=LEFT)
multiplication = Button(root,text = "*",height= 3, width=5,command=mul).pack(side=RIGHT)
division = Button(root,text = "/",height= 3, width=5,command=div).pack(side=RIGHT)
clr = Button(root,text="clear",command=clear).pack(side=BOTTOM)

root.mainloop()