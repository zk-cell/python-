#编写登录窗口
import tkinter as tk
from tkinter import Button, font
from tkinter import messagebox
import json 
'''
json有四个方法：dumps、loads、dump和load。dumps和loads是在内存中转换（python对象和json字符串之间的转换），
而dump和load则是对应于文件的处理。
'''
window = tk.Tk()
window.title('Welcome to ZK Python')
window.geometry('500x300+400+180')
window.config(bg = 'pink')

#加载图片
canvas = tk.Canvas(window, height = 150, width = 500)
image_file = tk.PhotoImage(file = './Tkinter/welcome.gif')
image = canvas.create_image(50,0,anchor = 'nw', image = image_file)
canvas.pack()

# user information
tk.Label(window, text = 'User Name', font = ('黑体',15)).place(x = 50, y = 170)
tk.Label(window, text = 'Password', font = ('黑体',15)).place(x = 50, y = 200)

#输入的用户名，密码储存在变量中   通过set，可以给出用户名默认值（例子）
var_user_name = tk.StringVar()
var_user_name.set('example@python.com')
var_user_password = tk.StringVar()

entry_user_name = tk.Entry(window, width = 40,  textvariable = var_user_name)
entry_user_name.place(x = 150, y = 170)

entry_user_password = tk.Entry(window, width = 40, show = '*', textvariable = var_user_password)
entry_user_password.place(x = 150, y = 200)

#注册、登录功能
def Sign_up():
    #创建注册窗口，利用toplevel
    window_sign_up = tk.Toplevel(window)
    window_sign_up.title('Sign Up Window')
    window_sign_up.geometry('400x180+450+230')

    tk.Label(window_sign_up, text = 'UserName', font = ('黑体',12)).place(x = 20, y = 20)
    tk.Label(window_sign_up, text = 'Password', font = ('黑体',12)).place(x = 20, y = 60)
    tk.Label(window_sign_up, text = 'ConfirmPassword', font = ('黑体',12)).place(x = 20, y = 100)

    new_name = tk.StringVar()
    new_pwd = tk.StringVar()
    new_confirm_pwd = tk.StringVar()
    entry_UserName = tk.Entry(window_sign_up , width = 30,  textvariable = new_name).place(x = 160, y = 20)
    entry_Password = tk.Entry(window_sign_up , width = 30,  textvariable = new_pwd).place(x = 160, y = 60)
    entry_Confirm_Password = tk.Entry(window_sign_up , width = 30,  textvariable = new_confirm_pwd).place(x = 160, y = 100)

    def sign_to_ZK_Python():
        nn = new_name.get()
        np = new_pwd.get()
        ncp = new_confirm_pwd.get()
        with open('./Tkinter/user_info.json','r') as user_file:
            exist_user_info = json.load(user_file)

        if np != ncp:
            messagebox.showerror(title = 'error', message = 'Password and Confirm Password must be the same!')
        elif nn in exist_user_info:
            messagebox.showerror(title = 'error', message = 'This name has already been signed up!')
        elif nn == '':
            messagebox.showerror(title = 'error', message = 'UserName should not be empty!')
        else:
            exist_user_info[nn] = np
            with open('./Tkinter/user_info.json','w') as user_file:
                json.dump(exist_user_info, user_file)
            messagebox.showinfo(title = 'Welcome!', message = 'Signing up successfully!')
            window_sign_up.destroy()
        

    button_confirm_sign_up = tk.Button(window_sign_up, width = 8, height = 1 , text = 'Sign In',\
         bg = 'yellow', font = ('黑体',14), command = sign_to_ZK_Python)
    button_confirm_sign_up.place(x = 160, y = 140)


    window_sign_up.mainloop()

def Login():
    #获得entry变量中的内容
    user_name = var_user_name.get()
    user_password = var_user_password.get()
    #打开数据库
    try:
        with open('./Tkinter/user_info.json','r') as user_file:
            user_info = json.load(user_file)
            #print(type(user_info))
    except FileNotFoundError:
        with open('./Tkinter/user_info.json','w') as user_file:
            #下面user_info是json.dump中所需的标准格式
            user_info = "{'admin' : 'admin'}"
            #print(type(user_info))
            json.dump(user_info, user_file)

    if user_name in user_info:
        #print(type(user_info))
        if user_password == user_info[user_name]:
            messagebox.showinfo(title = "Welcome", message = 'Congratulations! You have successfully Logined in!\n Welcome,'+user_name)
        else:
            messagebox.showerror(title = "error", message = "You password is wrong, please try again!")
    else:
        is_sign_up = messagebox.askyesno(title = 'welcome', message = 'Well, you have not signed up yet, how about do that today?')
        if is_sign_up:
            Sign_up()
    

b1 = tk.Button(window, width = 8, height = 1 , text = 'Login', bg = 'yellow',  \
    font = ('黑体',15), command = Login).place(x = 80, y = 240)
b2 = tk.Button(window, width = 8, height = 1 , text = 'Sign Up', bg = 'yellow', \
    font = ('黑体',15), command = Sign_up).place(x = 330, y = 240)

window.mainloop()