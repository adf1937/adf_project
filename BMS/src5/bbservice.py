# -*- coding: utf-8 -*-
import tkinter as tk  # 装载tkinter模块,用于Python3
from tkinter import ttk  # 装载tkinter.ttk模块,用于Python3


class bbservice(tk.Frame):  # 继承Frame类
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.root = master

        self.create_bbpage()

    def create_bbpage(self):
        la1 = tk.Label(self, text='这里图书借阅界面')
        la1.pack()
        en1 = tk.Entry(self)
        en1.pack()
