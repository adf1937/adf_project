# -*- coding: utf-8 -*-
import tkinter as tk  # 装载tkinter模块,用于Python3
from tkinter import ttk
from bmframe import *
from bbframe import *
from buframe import *


class home():
    def __init__(self, master=None):
        self.root = master
        self.root.state("zoomed")
        self.createnb()

    def createnb(self):
        self.nb = ttk.Notebook(self.root)  # 创建Notebook

        self.bb = bbframe(self.nb)
        self.bm = bmframe(self.nb)
        self.bu = buframe(self.nb)

        self.nb.grid(row=0, column=0)

        self.nb.select(0)  # 选择tab1


if __name__ == "__main__":
    root = tk.Tk()
    home(root)
    root.mainloop()
