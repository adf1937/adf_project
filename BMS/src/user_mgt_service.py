from tkinter import *


class UserAddRemoveFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master

        self.create_booksearch()

    def create_AddRemove(self):
        la1 = Label(self, text='这里用户增删除')
        la1.pack()
        en1 = Entry(self)
        en1.pack()


class UserModifyFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master

        self.create_booksearch()

    def create_Modify(self):
        la1 = Label(self, text='这里用户修改')
        la1.pack()
        en1 = Entry(self)
        en1.pack()
