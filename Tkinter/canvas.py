#画布
import tkinter as tk

window = tk.Tk()
window.geometry('200x200+500+100')

canvas = tk.Canvas(window, bg = 'blue', height = 150, width = 200)
#打开图片文件
image_file = tk.PhotoImage(file = './Tkinter/神奇宝贝.gif')
#摆放图片   anchor:定义0，0点所在方位
image = canvas.create_image(0,0,anchor = 'nw', image = image_file)
#自定义图形
x0,y0,x1,y1 = 50,50,80,80
line = canvas.create_line(x0,y0,x1,y1)
rectangle = canvas.create_rectangle(x0,y0,x1,y1,fill = 'purple')
arc = canvas.create_arc(x0+40,y0+40,x1+40,y1+40,start = 0, extent = 180)
oval = canvas.create_oval(90,50,120,80)
canvas.pack()

def move_rect():
    #使用canvas.move来移动画布中的元素
    canvas.move(rectangle,0,2)
b = tk.Button(window, text = 'move rect', command =  move_rect)
b.pack()

window.mainloop()