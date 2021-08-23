#列表部件
import tkinter as tk

window = tk.Tk()
window.geometry('200x200+500+100')

var1 = tk.StringVar()

l = tk.Label(window, textvariable=var1, bg = 'yellow', font = ('Arial',15), width = 10, height = 2)
l.pack()

def print_selection():
    #listbox中选定的元素:lb.curselection, lb.get获取内容, var.set设值
    content = lb.curselection()
    value = lb.get(content)
    var1.set(value)

b1 = tk.Button(window, text = 'print selection', width = 15, height = 2, command = print_selection)
b1.pack()

#列表部件
var2 = tk.StringVar()
var2.set((11,22,33,44,55,66,77,88,99,111))
lb = tk.Listbox(window, listvariable = var2)
#给listbox加入新的元素
list_items = ['holy', 'shit', '!']
for item in list_items:
    lb.insert('end', item)
#指定位置插入元素
lb.insert(0,'first')
lb.insert(1, 'second')
#删除元素
lb.delete(1)
lb.pack()

window.mainloop()
