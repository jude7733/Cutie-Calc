import tkinter as tk
from tkinter import ttk

# create root window
root = tk.Tk()
root.title("Calculator")


# for preventing alphabet entry
def calresultack(input):
    if input.isdigit() == True:
        return True
    else:
        return False


def clear():
    eq.set(value=0)


def calcresult():
    result.config(text=eq.get())
    # eq.set(value='')
    # print(result.configure())


# tkinter variables
eq = tk.IntVar(value=0)

# tkinter widgets

entry = ttk.Entry(master=root, font=("arial", 22), textvariable=eq)
entry.grid(row=0, column=0, pady=5, sticky="w", columnspan=4)

result = ttk.Label(master=root, font=("arial", 24))
result.grid(row=1, column=2, pady=5)

clr = ttk.Button(root, text="C", width=4, command=clear)
clr.grid(row=5, column=0, padx=2, pady=2)

one = ttk.Button(root, text="1", width=4, command=lambda: eq.set(eq.get() + 1))
one.grid(row=2, column=0, padx=2, pady=2)
two = ttk.Button(root, text="2", width=4, command=lambda: eq.set(eq.get() + 2))
two.grid(row=2, column=1, padx=2, pady=2)
three = ttk.Button(root, text="3", width=4, command=lambda: eq.set(eq.get() + 3))
three.grid(row=2, column=2, padx=2, pady=2)
four = ttk.Button(root, text="4", width=4, command=lambda: eq.set(eq.get() + 4))
four.grid(row=3, column=0, padx=2, pady=2)
five = ttk.Button(root, text="5", width=4, command=lambda: eq.set(eq.get() + 5))
five.grid(row=3, column=1, padx=2, pady=2)
six = ttk.Button(root, text="6", width=4, command=lambda: eq.set(eq.get() + 6))
six.grid(row=3, column=2, padx=2, pady=2)
seven = ttk.Button(root, text="7", width=4, command=lambda: eq.set(eq.get() + 7))
seven.grid(row=4, column=0, padx=2, pady=2)
eight = ttk.Button(root, text="8", width=4, command=lambda: eq.set(eq.get() + 8))
eight.grid(row=4, column=1, padx=2, pady=2)
nine = ttk.Button(root, text="9", width=4, command=lambda: eq.set(eq.get() + 9))
nine.grid(row=4, column=2, padx=2, pady=2)
zero = ttk.Button(root, text="0", width=4, command=lambda: eq.set(eq.get() + 0))
zero.grid(row=5, column=1, padx=2, pady=2)
equal = ttk.Button(root, text="=", width=4, command=calcresult)
equal.grid(row=5, column=2, padx=2, pady=2)
add = ttk.Button(root, text="+", width=4)
add.grid(row=2, column=3, padx=2, pady=2)
sub = ttk.Button(root, text="-", width=4)
sub.grid(row=3, column=3, padx=2, pady=2)
mul = ttk.Button(root, text="*", width=4)
mul.grid(row=4, column=3, padx=2, pady=2)
div = ttk.Button(root, text="/", width=4)
div.grid(row=5, column=3, padx=2, pady=2)

root.mainloop()
