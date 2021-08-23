#勾选项（多选）
import tkinter as tk

window = tk.Tk()
window.geometry('200x200+500+100')

l = tk.Label(window, text = 'Empty', bg = 'yellow', font = ('Arial',10), width = 30, height = 2)
l.pack()

#value为尺度部件当前所指数值
def print_selection():
    var1_state = var1.get()
    var2_State = var2.get()
    if var1_state ==1 and var2_State ==0:
        l.config(text = f'I love only Python ')
    elif var1_state ==0 and var2_State ==1:
        l.config(text = 'I love only c++')
    elif  var1_state ==1 and var2_State ==1:
        l.config(text = 'I love both')
    else:
        l.config(text = 'I do not love either')

var1 = tk.IntVar()
var2 = tk.IntVar()
#onvalue 选中时将variable设置为1， offvalue 未选中时设置为0
cb1 = tk.Checkbutton(window, text = 'Python', variable = var1, onvalue = 1, offvalue = 0, command = print_selection)
cb1.pack()

cb2 = tk.Checkbutton(window, text = 'C++', variable = var2, onvalue = 1, offvalue = 0, command = print_selection)
cb2.pack()

window.mainloop()
