#选择按钮
import tkinter as tk

window = tk.Tk()
window.geometry('200x200+500+100')

var = tk.StringVar()
var.set(None)

l = tk.Label(window, text = 'Empty', bg = 'yellow', font = ('Arial',10), width = 30, height = 2)
l.pack()

def print_selection():
    #l.config 改变label的参数, var.get:获取var中的值A/B/C
    l.config(text = 'You have selected '+ var.get() )
#选中该选项时时，将var赋值为'A'
rb1 = tk.Radiobutton(window, text = 'option A', variable = var, value = 'A', command = print_selection)
rb1.pack()

rb2 = tk.Radiobutton(window, text = 'option B', variable = var, value = 'B', command = print_selection)
rb2.pack()

rb3 = tk.Radiobutton(window, text = 'option C', variable = var, value = 'C', command = print_selection)
rb3.pack()

def cancel_selection():
    var.set(None)
    l.config(text = 'You have canceled everything.')
b = tk.Button(window, text = 'Cancel Selection',width = 15, height = 3, bg = 'grey', command = cancel_selection)
b.pack()

window.mainloop()
