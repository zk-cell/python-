#窗体、按钮和标签
import tkinter as tk


#创建窗口，并设置窗口参数
window = tk.Tk()
window.title('朱恺的窗口')
#窗口宽、高
window.geometry('200x100+400+180')

#创建变量，传递动态字符   var.set可以设置var中的字符串
var = tk.StringVar()

#创建window中的标签label
l = tk.Label(window, textvariable = var, bg = 'yellow', font = ('Arial',15), width = 20, height = 2)
l.pack()

#按钮功能
on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        var.set('You hit me！')
        on_hit = True
    else:
        var.set('')
        on_hit = False
#创建按钮
b = tk.Button(window, text = 'hit me', width = 10, height = 2, font = ('TimesNewRoman',15), bg = 'grey', command = hit_me)
b.pack()


window.mainloop()
