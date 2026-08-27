import tkinter as tk

def Addition(a, b):
    return a + b

def Subtraction(a, b):
    return a - b

def Multiplication(a, b):
    return a * b

def floor_division(a, b):
    if b == 0:
        return "Undefined"
    return a // b

def division(a, b):
    if b == 0:
        return "Undefined"
    return a / b

def Modulus(a, b):
    if b == 0:
        return "Undefined"
    return a % b


def button_click(value):
    display.insert(tk.END, value)


def clear():
    display.delete(0, tk.END)


def calculate():
    expression = display.get()

    try:
        if '//' in expression:
            a, b = expression.split('//')
            result = floor_division(float(a), float(b))

        elif '+' in expression:
            a, b = expression.split('+')
            result = Addition(float(a), float(b))

        elif '-' in expression:
            a, b = expression.split('-')
            result = Subtraction(float(a), float(b))

        elif '*' in expression:
            a, b = expression.split('*')
            result = Multiplication(float(a), float(b))

        elif '/' in expression:
            a, b = expression.split('/')
            result = division(float(a), float(b))

        elif '%' in expression:
            a, b = expression.split('%')
            result = Modulus(float(a), float(b))

        else:
            result = "Invalid"

        display.delete(0, tk.END)
        display.insert(0, str(result))

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


def keyboard_input(event):
    if event.keysym == "Return":
        calculate()

    elif event.keysym == "BackSpace":
        text = display.get()
        display.delete(0, tk.END)
        display.insert(0, text[:-1])

    elif event.keysym == "Escape":
        clear()

    elif event.char in "0123456789.+-*/%":
        button_click(event.char)


window = tk.Tk()
window.title("My Calculator")
window.geometry("350x500")

display = tk.Entry(
    window,
    font=("Arial", 24),
    justify="right"
)
display.pack(
    padx=10,
    pady=20,
    fill="x"
)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "%", "+"],
    ["//", "C", "="]
]

for row in buttons:
    frame = tk.Frame(window)
    frame.pack()

    for button in row:

        if button == "C":
            command = clear

        elif button == "=":
            command = calculate

        else:
            command = lambda x=button: button_click(x)

        tk.Button(
            frame,
            text=button,
            font=("Arial", 18),
            width=5,
            height=2,
            command=command
        ).pack(side="left", padx=3, pady=3)

window.bind("<Key>", keyboard_input)

window.mainloop()
