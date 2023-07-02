import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import *

# create root window
root = ttk.Window(themename="darkly")
root.title("Cutie-Calc")
root.minsize(330, 330)

root.iconphoto(True, PhotoImage(file="Android-Lollipop-Calculator.png"))

Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)


# for preventing alphabet entry
def check_char(input):
    if input.isdigit() == True:
        return True
    else:
        return False


def clear():
    exp.set(value="0")
    ans.set(value="(̶◉͛‿◉̶)")
    operand_Stack.clear()
    operator_Stack.clear()


def numbers(num):
    if exp.get() == "0":
        temp.set(value=num)
        exp.set(value=str(num))
    else:
        temp.set(value=(temp.get() * 10) + num)
        if operator_Stack:
            exp.set(value=exp.get() + str(num))
        else:
            exp.set(value=(str(temp.get())))


def operators(op):
    def get_Precedence(x):
        if x == "*" or x == "/":
            return 3
        else:
            return 2

    def calc(a, b, c):
        if c == "+":
            return a + b
        elif c == "-":
            return a - b
        elif c == "*":
            return a * b
        elif c == "/":
            if b == 0:
                return "ಥ_ಥ"
            return a / b

    operand_Stack.append(temp.get())

    if operator_Stack:
        # if greater precedence
        if get_Precedence(op) > get_Precedence(operator_Stack[-1]):
            operator_Stack.append(op)
        else:
            if get_Precedence(op) <= get_Precedence(operator_Stack[-1]):
                a = operand_Stack.pop()
                b = operand_Stack.pop()
                c = operator_Stack.pop()
                operand_Stack.append(calc(b, a, c))
                if op == "=":
                    ans.set(value=operand_Stack[-1])
                    operand_Stack.pop()
                    exp.set(value="0")
                else:
                    operator_Stack.append(op)
    # if empty
    else:
        operator_Stack.append(op)
    if op != "=":
        exp.set(value=exp.get() + op)
    temp.set(value=0)

    # print("operand_Stack")
    # print(operand_Stack)
    # print("operator_Stack")
    # print(operator_Stack)


# variables
operand_Stack = []
operator_Stack = []

# tkinter variables
exp = ttk.StringVar(value="0")
temp = ttk.IntVar(value=0)
ans = ttk.IntVar(value="ʕ•́ᴥ•̀ʔっ")
themeVar = ttk.StringVar(value="darkly")

# tkinter widgets   
entry = ttk.Entry(
    master=root,
    font=("arial", 22),
    textvariable=exp,
    bootstyle=INFO,
    justify="right",
    validate="key",
    validatecommand=(root.register(check_char), "%P"),
)
entry.grid(row=0, column=0, padx=5, columnspan=4, sticky="EW")

result = ttk.Label(master=root, font=("arial", 20), textvariable=ans, bootstyle=LIGHT)
result.grid(row=1, column=0, pady=5, padx=10, columnspan=4, sticky="EW")

clr = ttk.Button(root, text="C", width=7, bootstyle=DANGER, command=clear)
clr.grid(row=5, column=0, padx=2, pady=2, sticky="NSEW")

# numbers
one = ttk.Button(root, text="7", width=7, command=lambda: numbers(7))
one.grid(row=2, column=0, padx=2, pady=2, sticky="NSEW")
two = ttk.Button(root, text="8", width=7, command=lambda: numbers(8))
two.grid(row=2, column=1, padx=2, pady=2, sticky="NSEW")
three = ttk.Button(root, text="9", width=7, command=lambda: numbers(9))
three.grid(row=2, column=2, padx=2, pady=2, sticky="NSEW")
four = ttk.Button(root, text="4", width=7, command=lambda: numbers(4))
four.grid(row=3, column=0, padx=2, pady=2, sticky="NSEW")
five = ttk.Button(root, text="5", width=7, command=lambda: numbers(5))
five.grid(row=3, column=1, padx=2, pady=2, sticky="NSEW")
six = ttk.Button(root, text="6", width=7, command=lambda: numbers(6))
six.grid(row=3, column=2, padx=2, pady=2, sticky="NSEW")
seven = ttk.Button(root, text="1", width=7, command=lambda: numbers(1))
seven.grid(row=4, column=0, padx=2, pady=2, sticky="NSEW")
eight = ttk.Button(root, text="2", width=7, command=lambda: numbers(2))
eight.grid(row=4, column=1, padx=2, pady=2, sticky="NSEW")
nine = ttk.Button(root, text="3", width=7, command=lambda: numbers(3))
nine.grid(row=4, column=2, padx=2, pady=2, sticky="NSEW")
zero = ttk.Button(root, text="0", width=7, command=lambda: numbers(0))
zero.grid(row=5, column=1, padx=2, pady=2, sticky="NSEW")

# operators
op_style = ttk.Style()
op_style.configure("INFO.TButton", font=("arial", 28))
equal = ttk.Button(
    root,
    text="=",
    width=7,
    bootstyle=INFO,
    style="INFO.Tbutton",
    command=lambda: operators("="),
)
equal.grid(row=5, column=2, padx=2, pady=2, sticky="NSEW")

add = ttk.Button(
    root, text="＋", width=7, bootstyle=SECONDARY, command=lambda: operators("+")
)
add.grid(row=2, column=3, padx=2, pady=2, sticky="NSEW")

sub = ttk.Button(
    root, text="—", width=7, bootstyle=SECONDARY, command=lambda: operators("-")
)
sub.grid(row=3, column=3, padx=2, pady=2, sticky="NSEW")

mul = ttk.Button(
    root, text="X", width=7, bootstyle=SECONDARY, command=lambda: operators("*")
)
mul.grid(row=4, column=3, padx=2, pady=2, sticky="NSEW")

div = ttk.Button(
    root, text="/", width=7, bootstyle=SECONDARY, command=lambda: operators("/")
)
div.grid(row=5, column=3, padx=2, pady=2, sticky="NSEW")

# theme
theme = ttk.Combobox(
    root,
    values=root.style.theme_names(),
    textvariable=themeVar,
    state="readonly",
    width=10,
    bootstyle=INFO,
)
theme.grid(row=6, column=0, pady=10, columnspan=2, sticky="EW")

# events
theme.bind("<<ComboboxSelected>>", lambda event: root.style.theme_use(themeVar.get()))

root.bind(
    "<KeyPress>",
    lambda event: numbers(int(event.char))
    if ((event.char).isdigit())
    else operators(event.char),
)

root.mainloop()
