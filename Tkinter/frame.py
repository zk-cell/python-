#框架(相当于窗口中的小窗口)
import tkinter as tk

window = tk.Tk()
window.geometry('200x200+500+100')

tk.Label(window, text = 'on the window').pack()

#主框架
fm = tk.Frame(window)
fm.pack()
#子框架
fm_left = tk.Frame(fm)
fm_right = tk.Frame(fm)
fm_left.pack(side = 'left')
fm_right.pack(side = 'right')

tk.Label(fm_left, text = 'on the fm_left1').pack()
tk.Label(fm_left, text = 'on the fm_left2').pack()
tk.Label(fm_right, text = 'fm_right').pack()

window.mainloop()
