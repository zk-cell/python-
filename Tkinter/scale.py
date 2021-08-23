#尺度部件
import tkinter as tk

window = tk.Tk()
window.geometry('200x200+500+100')

l = tk.Label(window, text = 'Empty', bg = 'yellow', font = ('Arial',10), width = 30, height = 2)
l.pack()

#value为尺度部件当前所指数值
def print_selection(value):
    l.config(text = 'You have selected '+ value)

'''scale: label名字，from_/to取值范围 orient方向 length像素长度 tickinterval数轴间隔 resolution分辨率 
show把尺度部件值显示出来:True/1显示；False/0不显示'''
s = tk.Scale(window, label = 'try me', from_ = 5, to = 11, orient = tk.HORIZONTAL, length = 200,\
    showvalue = 1, tickinterval = 3, resolution = 0.01, command = print_selection)
s.pack()


window.mainloop()
