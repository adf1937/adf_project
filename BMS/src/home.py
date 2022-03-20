# -*- coding: utf-8 -*-
import tkinter as tk  # 装载tkinter模块,用于Python3
from tkinter import ttk  # 装载tkinter.ttk模块,用于Python3
from bmservice import *
from bbservice import *
from busevice import *


class home():
    def __init__(self, master=None):
        self.root = master
        w, h = self.root.maxsize()
        self.root.geometry("{}x{}+0+0".format(w, h))
        self.root.resizable(0, 0)
        # self.root.geometry('400x250+888+444')
        self.createNotebook()

    def createNotebook(self):
        self.tabControl = ttk.Notebook(self.root)  # 创建Notebook

        self.createBBPage()
        self.createBMPage()
        self.createBUPage()

        self.tabControl.pack(expand=1, fill="both")
        self.tabControl.select(0)  # 选择tab1

    def createBBPage(self):
        # tab = tk.Frame(self.tabControl, bg='blue')  # 增加新选项卡
        tab = bbservice(self.tabControl)
        self.tabControl.add(tab, text='借阅管理')  # 把新选项卡增加到Notebook

    def createBMPage(self):
        #tab = tk.Frame(self.tabControl, bg='yellow')
        tab = bmservice(self.tabControl)
        self.tabControl.add(tab, text='图书管理')

    def createBUPage(self):
        #tab = tk.Frame(self.tabControl, bg='green')
        tab = buservice(self.tabControl)
        self.tabControl.add(tab, text='用户管理')


if __name__ == "__main__":
    root = tk.Tk()
    home(root)
    root.mainloop()
