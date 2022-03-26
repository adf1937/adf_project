# -*- coding: utf-8 -*-
import tkinter as tk  # 装载tkinter模块,用于Python3
from tkinter import ttk  # 装载tkinter.ttk模块,用于Python3


class buframe():
    def __init__(self,  master=None):
        self.nb = master

        self.tab_bu = ttk.Frame(self.nb)            # Add a third tab
        self.nb.add(self.tab_bu, text='用户管理')      # Make second tab visible
        self.createbupage()

    def createbupage(self):

        #---------------Tab1控件介绍------------------#
        # We are creating a container tab3 to hold all other widgets
        monty = ttk.LabelFrame(self.tab_bu, text='用户添加')
        monty.grid(column=0, row=0, padx=8, pady=4)

        # Modified Button Click Function

        # Changing our Label
        ttk.Label(monty, text="用户名").grid(column=0, row=0, sticky='W')

        # Adding a Textbox Entry widget
        name = tk.StringVar()
        nameEntered = ttk.Entry(monty, width=12, textvariable=name)
        nameEntered.grid(column=1, row=0, sticky='W')

        # Changing our Label
        ttk.Label(monty, text="密码").grid(column=0, row=1, sticky='W')

        # Adding a Textbox Entry widget
        name = tk.StringVar()
        nameEntered = ttk.Entry(monty, width=12, textvariable=name)
        nameEntered.grid(column=1, row=1, sticky='W')

        # Adding a Button
        action = ttk.Button(monty, text="添加",
                            width=10, command=self.clickMe)
        action.grid(column=3, row=2, rowspan=2, ipady=7, sticky='N')

        # 一次性控制各控件之间的距离
        for child in monty.winfo_children():
            child.grid_configure(padx=3, pady=1)
        # 单独控制个别控件之间的距离
        action.grid(column=2, row=1, rowspan=2, padx=6)

    def clickMe(self):
        pass

    def search_m(self):
        pass
