#输入框和文本框
import tkinter as tk

window = tk.Tk()
window.geometry('200x200+500+100')

#输入框，这里show使得输入的内容固定为*
e = tk.Entry(window, show = '*')
e.pack()

#e.get获得用户输入的内容;    t.insert('xx', var)将var中内容赋给text，并调整文字插入位置
var = tk.StringVar()
def insert_point():
    var = e.get()
    t.insert('insert', var)
def insert_end():
    var = e.get()
    t.insert('end', var)

b1 = tk.Button(window, text = 'insert point', width = 15, height = 2, command = insert_point )
b1.pack()

b2 = tk.Button(window, text = 'insert end', width = 15, height = 2, command = insert_end )
b2.pack()


#文本框
t = tk.Text(window, height = 2 )
t.pack()




window.mainloop()