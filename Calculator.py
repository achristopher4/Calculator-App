## Python Calculator App
## 8/17/21

from tkinter import *
from tkmacosx import *

root = Tk()
root.title("Simple Calculator")

ui = Entry(root, width=40, borderwidth=2, bg="#F4F4F4")
ui.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    c = ui.get()
    ui.delete(0, END)
    ui.insert(0, str(c) + str(number))

def button_clear():
    ui.delete(0, END)
    global num
    global action
    global stack
    num = None
    action = None
    stack = []]

def button_add():
    stack

def button_subtract():
    return

def button_multiply():
    return

def button_divide():
    return

def button_enter():
    global num
    ui.delete(0, END)
    ui.insert(0, int(num))

button_7 = Button(root, text = "7", padx = 20, pady= 20, bg="#EEEEEE", command= lambda: button_click(7)).grid(row=1, column = 0)
button_8 = Button(root, text = "8",  padx = 20, pady= 20, bg="#EEEEEE", command= lambda: button_click(8)).grid(row=1, column = 1)
button_9 =  Button(root, text = "9",  padx = 20, pady= 20, bg="#EEEEEE", command= lambda: button_click(9)).grid(row=1, column = 2)

button_4 = Button(root, text = "4", padx = 20, pady= 20, bg="#EEEEEE", command= lambda: button_click(4)).grid(row=2, column = 0)
button_5 = Button(root, text = "5",  padx = 20, pady= 20, bg="#EEEEEE", command= lambda: button_click(5)).grid(row=2, column = 1)
button_6 =  Button(root, text = "6",  padx = 20, pady= 20, bg="#EEEEEE", command= lambda: button_click(6)).grid(row=2, column = 2)

button_1 = Button(root, text = "1", padx = 20, pady= 20, bg="#EEEEEE", command= lambda: button_click(1)).grid(row=3, column = 0)
button_2 = Button(root, text = "2",  padx = 20, pady= 20, bg="#EEEEEE", command= lambda: button_click(2)).grid(row=3, column = 1)
button_3 =  Button(root, text = "3",  padx = 20, pady= 20, bg="#EEEEEE", command= lambda: button_click(3)).grid(row=3, column = 2)

button_0 =  Button(root, text = "0",  padx = 20, pady= 20, bg="#EEEEEE", command= lambda: button_click(0)).grid(row=4, column = 0)
button_clear =  Button(root, text = "Clear",  padx = 85, pady= 20, bg="#FFCBCB", command= button_clear).grid(row=4, column = 1, columnspan=2)

button_add =  Button(root, text = "+",  padx = 20, pady= 20, bg="#EEEEEE", command= button_add).grid(row=5, column = 0)
button_enter =  Button(root, text = "=",  padx = 85, pady= 20, bg="#D4FFCB", command= button_enter).grid(row=5, column = 1, columnspan=2)

button_subtract =  Button(root, text = "-",  padx = 20, pady= 20, bg="#EEEEEE", command= lambda: button_click()).grid(row=6, column = 1)
button_multiply =  Button(root, text = "*",  padx = 20, pady= 20, bg="#EEEEEE", command= lambda: button_click()).grid(row=6, column = 2)
button_divide = Button(root, text = "*",  padx = 20, pady= 20, bg="#EEEEEE", command= lambda: button_click()).grid(row=6, column = 0)


root.mainloop()
