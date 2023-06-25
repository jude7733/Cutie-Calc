import tkinter as tk
from tkinter import ttk

# create root window
root = tk.Tk()
root.title("Calculator")


# for preventing alphabet entry
def check_char(input):
    if input.isdigit() == True:
        return True
    else:
        return False

def clear():
    exp.set(value='0')

def numbers(num):
    if exp.get() == '0':
        temp.set(value=num)
        exp.set(value=str(num))
    else:
        temp.set(value=(temp.get() * 10) + num)
        if operator_Stack:
            exp.set(value=exp.get() + str(num))
        else:
            exp.set(value=(str(temp.get())))

def operators(op):
    operand_Stack.append(temp.get())
    operator_Stack.append(op)
    exp.set(value=exp.get() + op)
    temp.set(value=0)
    print(operand_Stack)
    print(operator_Stack)

def calcresult():
    result.config(text=exp.get())
    operand_Stack.append(temp.get())
    print(operand_Stack)
    # exp.set(value='')
    # print(result.configure())

# variables
operand_Stack = []
operator_Stack = []

# tkinter variables
exp = tk.StringVar(value='0')
temp = tk.IntVar(value=0)

# tkinter widgets
entry = ttk.Entry(
    master=root,
    font=("arial", 22),
    textvariable=exp,
    justify="right",
    validate="key",
    validatecommand=(root.register(check_char), "%P"),
)
entry.grid(row=0, column=0, pady=5, sticky="w", columnspan=4)

result = ttk.Label(master=root, font=("arial", 20))
result.grid(row=1, column=2, pady=5, columnspan=4, sticky="e")

clr = ttk.Button(root, text="C", width=7, command=clear)
clr.grid(row=5, column=0, padx=2, pady=2)

one = ttk.Button(root, text="7", width=7, command=lambda: numbers(7))
one.grid(row=2, column=0, padx=2, pady=2)
two = ttk.Button(root, text="8", width=7, command=lambda: numbers(8))
two.grid(row=2, column=1, padx=2, pady=2)
three = ttk.Button(root, text="9", width=7, command=lambda: numbers(9))
three.grid(row=2, column=2, padx=2, pady=2)
four = ttk.Button(root, text="4", width=7, command=lambda: numbers(4))
four.grid(row=3, column=0, padx=2, pady=2)
five = ttk.Button(root, text="5", width=7, command=lambda: numbers(5))
five.grid(row=3, column=1, padx=2, pady=2)
six = ttk.Button(root, text="6", width=7, command=lambda: numbers(6))
six.grid(row=3, column=2, padx=2, pady=2)
seven = ttk.Button(root, text="1", width=7, command=lambda: numbers(1))
seven.grid(row=4, column=0, padx=2, pady=2)
eight = ttk.Button(root, text="2", width=7, command=lambda: numbers(2))
eight.grid(row=4, column=1, padx=2, pady=2)
nine = ttk.Button(root, text="3", width=7, command=lambda: numbers(3))
nine.grid(row=4, column=2, padx=2, pady=2)
zero = ttk.Button(root, text="0", width=7, command=lambda: numbers(0))
zero.grid(row=5, column=1, padx=2, pady=2)

expual = ttk.Button(root, text="=", width=7, command=calcresult)
expual.grid(row=5, column=2, padx=2, pady=2)
add = ttk.Button(root, text="+", width=7, command=lambda: operators("+"))
add.grid(row=2, column=3, padx=2, pady=2)
sub = ttk.Button(root, text="-", width=7, command=lambda: operators("-"))
sub.grid(row=3, column=3, padx=2, pady=2)
mul = ttk.Button(root, text="*", width=7, command=lambda: operators("*"))
mul.grid(row=4, column=3, padx=2, pady=2)
div = ttk.Button(root, text="/", width=7, command=lambda: operators("/"))
div.grid(row=5, column=3, padx=2, pady=2)

root.mainloop()
