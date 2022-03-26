# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
from tkinter import ttk


class booktreeview ():
    def __init__(self,  master=None):
        self.root = master
        self.createtreeview()

    def createtreeview(self):

        columns = ['书名', '状态', '借阅者', '学号', '时间', '备注']
        self.table = ttk.Treeview(
            master=self.root,  # 父容器
            height=10,  # 表格显示的行数,height行
            columns=columns,  # 显示的列
            show='headings',  # 隐藏首列
        )

        self.table.heading(column='书名',  text='书名',
                           command=lambda: print('书名'))  # 定义表头
        self.table.heading('状态', text='状态', )  # 定义表头
        self.table.heading('借阅者', text='借阅者', )  # 定义表头
        self.table.heading('学号', text='学号', )  # 定义表头
        self.table.heading('时间', text='时间', )  # 定义表头
        self.table.heading('备注', text='备注', )  # 定义表头

        self.table.column('书名', width=200, minwidth=100, anchor=S)  # 定义列
        self.table.column('状态', width=300, minwidth=100, anchor=S)  # 定义列
        self.table.column('借阅者', width=50, minwidth=50, anchor=S)  # 定义列
        self.table.column('学号', width=300, minwidth=100, anchor=S)  # 定义列
        self.table.column('时间', width=300, minwidth=100, anchor=S)  # 定义列
        self.table.column('备注', width=300, minwidth=100, anchor=S)  # 定义列

        self.table.grid()

    def insert(self, info: list):

        for index, data in enumerate(info):
            self.table.insert('', END, values=data)  # 添加数据到末尾

    def delete(self):
        obj = self.table.get_children()  # 获取所有对象
        for o in obj:
            self.table.delete(o)  # 删除对象
