from tkinter import *


class BookSearchFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master

        self.create_booksearch()

    def create_booksearch(self):
        la1 = Label(self, text='这里图书查询界面')
        la1.pack()
        en1 = Entry(self)
        en1.pack()


class BookAddRemoveFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master

        self.create_booksearch()

    def create_AddRemove(self):
        la1 = Label(self, text='这里图书增删除')
        la1.pack()
        en1 = Entry(self)
        en1.pack()


class BookModifyFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master

        self.create_booksearch()

    def create_Modify(self):
        la1 = Label(self, text='这里图书修改')
        la1.pack()
        en1 = Entry(self)
        en1.pack()
