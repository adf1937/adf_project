# -*- coding: utf-8 -*-
import tkinter as tk  # 装载tkinter模块,用于Python3
from tkinter import ttk  # 装载tkinter.ttk模块,用于Python3


class bmservice(ttk.Frame):  # 继承Frame类
    def __init__(self, master=None):
        self.tab = ttk.Frame.__init__(self, master)
        self.root = master
        self.create_bmpage()

    def create_bmpage(self):

        # Changing our Label
        ttk.Label(self.tab, text="输入文字:").grid(column=0, row=0, sticky='W')

        # Adding a Textbox Entry widget
        name = tk.StringVar()
        nameEntered = ttk.Entry(self.tab, width=12, textvariable=name)
        nameEntered.grid(column=0, row=1, sticky='W')

        # Adding a Button
        action = ttk.Button(self.tab, text="点击之后\n按钮失效",
                            width=10, command=self.search_m)
        action.grid(column=2, row=1, rowspan=2, ipady=7)

        ttk.Label(self.tab, text="请选择一本书:").grid(column=1, row=0, sticky='W')

    def search_m():
        pass
