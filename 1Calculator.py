from tkinter import ttk
from tkinter import *
import math
from ttkthemes import ThemedTk

window = ThemedTk(theme="equilux")
window.config(themebg="equilux")
window.title("Calculator")
window.geometry("345x202")

var = StringVar()
result = ""

def clear():
    global result
    result = ""
    var.set(result)

def press(num):
    global result
    result = result + str(num)
    var.set(result)

def equalpress():
    try:
        global result
        total = str(eval(result))
        var.set(total)
        result = ""
    except:
        var.set('error')
        result = ""

def backspace():
    global result
    result = txt.get()[:-1]
    if result == "":
        result = ""
    var.set(result)

#s = ttk.Style()
#s.configure('.', font=('Helvetica', 25))
#last 2 lines are optional and just make the buttons larger, not the entry tho

txt = ttk.Entry(window, width=37, font=("Arial", 12),text=var)
txt.grid(column=0, row=0, columnspan=4)

btn7 = ttk.Button(text="7", command= lambda: press(7))
btn7.grid(column=0, row=3)

btn8 = ttk.Button(text="8", command= lambda: press(8))
btn8.grid(column=1, row=3)

btn9 = ttk.Button(text="9", command= lambda: press(9))
btn9.grid(column=2, row=3)

btn4 = ttk.Button(text="4", command= lambda: press(4))
btn4.grid(column=0, row=4)

btn5 = ttk.Button(text="5", command= lambda: press(5))
btn5.grid(column=1, row=4)

btn6 = ttk.Button(text="6", command= lambda: press(6))
btn6.grid(column=2, row=4)

btn1 = ttk.Button(text="1", command= lambda: press(1))
btn1.grid(column=0, row=5)

btn2 = ttk.Button(text="2", command= lambda: press(2))
btn2.grid(column=1, row=5)

btn3 = ttk.Button(text="3", command= lambda: press(3))
btn3.grid(column=2, row=5)

btn0 = ttk.Button(text="0", command= lambda: press(0))
btn0.grid(column=0, row=6)

btnplus = ttk.Button(text="+", command= lambda: press("+"))
btnplus.grid(column=3, row=3)

btnminus = ttk.Button(text="-", command= lambda: press("-"))
btnminus.grid(column=3, row=4)

btnmultiply = ttk.Button(text="x", command= lambda: press("*"))
btnmultiply.grid(column=3, row=5)

btndivide = ttk.Button(text=":", command= lambda: press("/"))
btndivide.grid(column=3, row=2)

btnclear = ttk.Button(text="clear",command= clear)
btnclear.grid(column=0, row=2)

btnequal = ttk.Button(text="=", command= equalpress)
btnequal.grid(column=3, row=6)

btnLpar = ttk.Button(text="(", command= lambda: press("("))
btnLpar.grid(column=1, row=2)

btnRpar = ttk.Button(text=")", command= lambda: press(")"))
btnRpar.grid(column=2, row=2)

btndot = ttk.Button(text=".", command= lambda: press("."))
btndot.grid(column=1, row=6)

btndel = ttk.Button(text="backspace", command=backspace)
btndel.grid(column=2, row=6)

btnpower = ttk.Button(text="^", command= lambda: press("**"))
btnpower.grid(column=2, row=1)

btnSqrRoot = ttk.Button(text="√ ", command= lambda: press("math.sqrt("))
btnSqrRoot.grid(column=1, row=1)

btnpi = ttk.Button(text="π", command= lambda: press(3.14))
btnpi.grid(column=0, row=1)

btnabs = ttk.Button(text="abs", command= lambda: press("abs("))
btnabs.grid(column=3, row=1)

window.mainloop()
