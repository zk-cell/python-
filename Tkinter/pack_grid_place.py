#位置摆放的不同方式
import tkinter as tk

window = tk.Tk()
window.geometry('200x200+500+100')

#1.pack的四种位置  ipadx:设置控件中水平方向空白区域的大小
tk.Label(window, text = 'top', bg='yellow').pack(side = 'top', ipadx = 50, ipady = 10)
tk.Label(window, text = 'bottom', bg='yellow').pack(side = 'bottom')
tk.Label(window, text = 'left', bg='yellow').pack(side = 'left')
tk.Label(window, text = 'right', bg='yellow').pack(side = 'right')

#2.place指定坐标放置    anchor:确定坐标原点的位置 n s w e及其组合
tk.Label(window, text = 'place', font = ('Arial', 15), bg='orange').place(x = 80, y = 80, anchor = 'nw')

#grid,按网格布局， 设置row、column等参数

window.mainloop()