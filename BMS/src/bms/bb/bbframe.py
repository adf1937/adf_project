# -*- coding: utf-8 -*-
import tkinter as tk  # 装载tkinter模块,用于Python3
from tkinter import ttk  # 装载tkinter.ttk模块,用于Python3
from util.bmsdb import *


class bbframe():
    def __init__(self, db: BMSDB,  master=None):
        self.nb = master
        self.tab_bb = ttk.Frame(self.nb)
        self.nb.add(self.tab_bb, text='借阅管理')      # Add the tab
        self.createbbpage()

    def createbbpage(self):

        #---------------Tab1控件介绍------------------#
        # We are creating a container tab3 to hold all other widgets
        monty = ttk.LabelFrame(self.tab_bb, text='书籍借还')
        monty.grid(column=0, row=0, padx=8, pady=4)

        # Changing our Label
        ttk.Label(monty, text="书名").grid(column=0, row=0, sticky='W')

        # Adding a Textbox Entry widget
        name = tk.StringVar()
        nameEntered = ttk.Entry(monty, width=12, textvariable=name)
        nameEntered.grid(column=0, row=1, sticky='W')

        # Adding a Button
        action = ttk.Button(monty, text="借阅",
                            width=10, command=self.clickMe)
        action.grid(column=2, row=1, rowspan=2, ipady=7)

        ttk.Label(monty, text="请选择一本书:").grid(column=1, row=0, sticky='W')

        # Adding a Combobox
        book = tk.StringVar()
        bookChosen = ttk.Combobox(monty, width=12, textvariable=book)
        bookChosen['values'] = ('平凡的世界', '亲爱的安德烈', '看见', '白夜行')
        bookChosen.grid(column=1, row=1)
        bookChosen.current(0)  # 设置初始显示值，值为元组['values']的下标
        bookChosen.config(state='readonly')  # 设为只读模式

        # 一次性控制各控件之间的距离
        for child in monty.winfo_children():
            child.grid_configure(padx=3, pady=1)
        # 单独控制个别控件之间的距离
        action.grid(column=2, row=1, rowspan=2, padx=6)

    def clickMe(self):
        pass
