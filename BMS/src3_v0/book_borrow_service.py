from tkinter import *


class BookBorrowFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master

        self.create_booksearch()

    def create_booksearch(self):
        la1 = Label(self, text='图书借阅')
        la1.pack()
        en1 = Entry(self)
        en1.pack()


class BookRetrunFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master

        self.create_booksearch()

    def create_AddRemove(self):
        la1 = Label(self, text='图书归还')
        la1.pack()
        en1 = Entry(self)
        en1.pack()


class BookExtendFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master

        self.create_booksearch()

    def create_Modify(self):
        la1 = Label(self, text='图书延期')
        la1.pack()
        en1 = Entry(self)
        en1.pack()
