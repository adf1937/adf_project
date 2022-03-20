# -*- coding: utf-8 -*-
import tkinter as tk  # 装载tkinter模块,用于Python3
from tkinter import ttk  # 装载tkinter.ttk模块,用于Python3
from bmservice import *
from bbservice import *
from busevice import *


class home():
    def __init__(self, master=None):
        self.root = master
        self.root.state("zoomed")
        self.createNotebook()

    def createNotebook(self):
        self.nb = ttk.Notebook(self.root)  # 创建Notebook

        self.createBBFrame()
        self.createBMFrame()
        self.createBUFrame()

        self.nb.pack(expand=1, fill="both")
        #self.nb.grid(row=0, column=0)

        self.nb.select(0)  # 选择tab1

    def createBBFrame(self):
        tab = bbservice(self.nb)
        self.nb.add(tab, text='借阅管理')  # 把新选项卡增加到Notebook

    def createBMFrame(self):
        tab = bmservice(self.nb)
        self.nb.add(tab, text='图书管理')

    def createBUFrame(self):
        tab = buservice(self.nb)
        self.nb.add(tab, text='用户管理')


if __name__ == "__main__":
    root = tk.Tk()
    home(root)
    root.mainloop()
