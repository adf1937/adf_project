from tkinter import *


class ren(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master

        self.creatren()

    def creatren(self):
        la1 = Label(self, text='这里是人事管理界面')
        la1.pack()
        en1 = Entry(self)
        en1.pack()


class kao(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.creatkao()

    def creatkao(self):
        la1 = Label(self, text='这里是考勤管理界面')
        la1.pack()


class gong(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.creatgong()

    def creatgong(self):
        la1 = Label(self, text='这里是工资管理界面')
        la1.pack()


def about():
    top1 = Toplevel()
    top1.geometry('280x150+950+515')
    top1.title('关于')

    la1 = Label(top1, text='本软件官网: www.wb98.com')
    la1.pack(pady=10)

    but1 = Button(top1, text="  确 定  ", command=top1.destroy)
    but1.pack(side=BOTTOM, pady=10)

    top1.attributes("-toolwindow", 1)  # 无最大化，最小化
    top1.transient()  # 窗口只置顶root之上
    top1.resizable(False, False)  # 不可调节窗体大小
    top1.grab_set()  # 转化模式
    top1.focus_force()  # 得到焦点
