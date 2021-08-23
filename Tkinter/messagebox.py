#弹窗
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry('200x200+500+100')

def hit_me():
    messagebox.showinfo(title = 'Hi', message = 'This is a message')
    #messagebox.showwarning(title = 'Hi', message = 'this is a warning')
    #messagebox.showerror(title = 'Hi', message = 'Theie is an error in your program!')

    #print(messagebox.askquestion(title = 'Hi', message = '1234') )   #return 'yes' or 'no'
    #print(messagebox.askyesno(title = 'Hi', message = '1234') )       #return 'True' or 'False'
    #print(messagebox.askokcancel(title = 'Hi', message = '1234') )     #return 'True' or 'False'

tk.Button(window, text = 'hit me', command = hit_me).pack()

window.mainloop()