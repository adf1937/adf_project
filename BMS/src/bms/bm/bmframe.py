# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
from tkinter import ttk
from bm.booktreeview import *
from util.bmsdb import BMSDB


class bmframe():
    def __init__(self,  db: BMSDB, master=None):
        self.nb = master
        self.db = db
        self.tab_bm = ttk.Frame(self.nb)
        self.nb.add(self.tab_bm, text='书籍管理')      # Add the tab
        self.createbmpage()

    def createbmpage(self):
        self.createBookSearchLableFrame()
        self.createBookAddLableFrame()

    def createBookSearchLableFrame(self):

        #---------------Tab1控件介绍------------------#
        # We are creating a container tab3 to hold all other widgets
        monty = ttk.LabelFrame(self.tab_bm, text='书籍查询')
        monty.grid(column=0, row=0, padx=8, pady=4)

        # Adding a Combobox for status
        ttk.Label(monty, text="状态").grid(column=0, row=0, sticky='W')
        self.bkstatus = tk.StringVar()
        bkStatusChosen = ttk.Combobox(
            monty, width=12, textvariable=self.bkstatus)
        bkStatusChosen['values'] = ('所有', '借出', '空闲', '维护')
        bkStatusChosen.grid(column=0, row=1)
        bkStatusChosen.current(0)  # 设置初始显示值，值为元组['values']的下标
        bkStatusChosen.config(state='readonly')  # 设为只读模式

        # Adding Book name
        ttk.Label(monty, text="书名").grid(column=1, row=0, sticky='W')
        # Adding a Textbox Entry widget
        self.bkname = tk.StringVar()
        bknameEntered = ttk.Entry(monty, width=12, textvariable=self.bkname)
        bknameEntered.grid(column=1, row=1, sticky='W')

        # Adding a Textbox borrower.
        ttk.Label(monty, text="借阅者").grid(column=2, row=0, sticky='W')
        self.bkusername = tk.StringVar()
        usernameEntered = ttk.Entry(
            monty, width=12, textvariable=self.bkusername)
        usernameEntered.grid(column=2, row=1, sticky='W')

        # Adding a Button for search
        action = ttk.Button(monty, text="查找",
                            width=10, command=self.search_m)
        action.grid(column=3, row=1, rowspan=2, padx=6)

        # 一次性控制各控件之间的距离
        for child in monty.winfo_children():
            child.grid_configure(padx=3, pady=1)
        # 单独控制个别控件之间的距离

        self.bktreeview = booktreeview(self.tab_bm)

    def search_m(self):
        bkStatus = self.bkstatus.get()
        bkName = self.bkname.get()
        bkUserName = self.bkusername.get()

        res = self.db.searchBook(bkStatus, bkName, bkUserName)
        self.bktreeview.delete()
        self.bktreeview.insert(res)
        print(res)
        pass

    def createBookAddLableFrame(self):

        #---------------Tab1控件介绍------------------#
        # We are creating a container tab3 to hold all other widgets
        monty = ttk.LabelFrame(self.tab_bm, text='书籍添加')
        monty.grid(column=0, row=40, padx=8, pady=4)

        # Adding Book name
        ttk.Label(monty, text="书名").grid(column=0, row=0, sticky='W')
        # Adding a Textbox Entry widget
        self.newbkname = tk.StringVar()
        bknameEntered = ttk.Entry(monty, width=12, textvariable=self.newbkname)
        bknameEntered.grid(column=0, row=1, sticky='W')

        # Adding Book SN
        ttk.Label(monty, text="书号").grid(column=1, row=0, sticky='W')
        # Adding a Textbox Entry widget
        self.newbksn = tk.StringVar()
        bknameEntered = ttk.Entry(monty, width=12, textvariable=self.newbksn)
        bknameEntered.grid(column=1, row=1, sticky='W')

        # Adding Book Comments
        ttk.Label(monty, text="备注").grid(column=2, row=0, sticky='W')
        # Adding a Textbox Entry widget
        self.newbkComments = tk.StringVar()
        bknameEntered = ttk.Entry(
            monty, width=12, textvariable=self.newbkComments)
        bknameEntered.grid(column=2, row=1, sticky='W')

        # Adding a Button for search
        action = ttk.Button(monty, text="添加",
                            width=10, command=self.add_m)
        action.grid(column=3, row=1, rowspan=2, padx=6)

        # 一次性控制各控件之间的距离
        for child in monty.winfo_children():
            child.grid_configure(padx=3, pady=1)
        # 单独控制个别控件之间的距离

    def add_m(self):
        bkname = self.newbkname.get()
        bksn = self.newbksn.get()
        bkcomments = self.newbkComments.get()
        print(bkname + " " + bksn + " " + bkcomments)
        self.db.addBook(bkname, bksn, bkcomments)

        pass
