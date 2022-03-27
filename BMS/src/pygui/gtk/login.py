from tkinter import *
from home import *
from tkinter import messagebox


class login(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('300x150+888+444')
        self.root.title('登录窗口')
        self.creatlogin()

    def creatlogin(self):
        self.fr1 = Frame(self.root)
        self.fr1.pack()
        self.en1 = Entry(self.fr1)
        self.en1.pack(pady=10, fill=X)
        self.but1 = Button(
            self.fr1, text="输入密码:wb98.com 进入主窗口吧", command=self.ok)
        self.but1.pack(pady=(0, 10))
        self.en1.focus_set()  # 获得焦点

    def ok(self):
        a = self.en1.get()
        if a == 'wb98.com':
            self.fr1.destroy()  # 登录界面卸载
            home(self.root)  # 密码对，就把主窗体模块的界面加载
        else:
            messagebox.showwarning("警告：", "密码错，正确的密码是：wb98.com")
