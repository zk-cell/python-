#菜单
import tkinter as tk

window = tk.Tk()
window.geometry('200x200+500+100')


l = tk.Label(window, text = '', bg = 'yellow')
l.pack()

counter = 0
def do_job():
    global counter
    l.config(text = 'do job'+ str(counter))
    counter += 1
#创建菜单栏
menubar = tk.Menu(window)
menubar.config(bg = 'purple')

filemenu = tk.Menu(menubar, tearoff = 0)
#给filemenu命名
menubar.add_cascade(label = 'File', menu = filemenu)
#给filemenu加上功能
filemenu.add_command(label = 'New', command = do_job)
filemenu.add_command(label = 'Open', command = do_job)
filemenu.add_command(label = 'Save', command = do_job)
#功能之间加分割线     tk.TK().quit是自带功能，退出窗口
filemenu.add_separator()
filemenu.add_command(label = 'Exit', command = window.quit)

#创建filemenu的子菜单
submenu = tk.Menu(filemenu)
#给filemenu命名
filemenu.add_cascade(label = 'Import', menu = filemenu)
#给filemenu加上功能
submenu.add_command(label = 'Sub', command = do_job)

editmenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Edit', menu = editmenu)
editmenu.add_command(label = 'Cut', command = do_job)
editmenu.add_command(label = 'Copy', command = do_job)
editmenu.add_command(label = 'Paste', command = do_job)

#改变window参数，把菜单改成自定义的
window.config(menu = menubar, bg = 'grey')

window.mainloop()