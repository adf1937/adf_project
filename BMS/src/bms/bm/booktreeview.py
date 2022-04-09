# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
from tkinter import ttk


class booktreeview ():
    def __init__(self,  master=None):
        self.root = master
        self.createtreeview()

    def createtreeview(self):

        columns = ['书名', '书号', '状态', '借阅者', '学号', '时间', '备注']
        self.table = ttk.Treeview(
            master=self.root,  # 父容器
            height=10,  # 表格显示的行数,height行
            columns=columns,  # 显示的列
            show='headings',  # 隐藏首列
        )

        self.table.heading(column='书名',  text='书名',
                           command=lambda: print('书名'))  # 定义表头
        self.table.heading('书号', text='书号', )  # 定义表头
        self.table.heading('状态', text='状态', )  # 定义表头
        self.table.heading('借阅者', text='借阅者', )  # 定义表头
        self.table.heading('学号', text='学号', )  # 定义表头
        self.table.heading('时间', text='时间', )  # 定义表头
        self.table.heading('备注', text='备注', )  # 定义表头

        self.table.column('书名', width=200, minwidth=100, anchor=S)  # 定义列
        self.table.column('书号', width=200, minwidth=100, anchor=S)  # 定义列
        self.table.column('状态', width=50, minwidth=100, anchor=S)  # 定义列
        self.table.column('借阅者', width=50, minwidth=50, anchor=S)  # 定义列
        self.table.column('学号', width=200, minwidth=100, anchor=S)  # 定义列
        self.table.column('时间', width=200, minwidth=100, anchor=S)  # 定义列
        self.table.column('备注', width=400, minwidth=100, anchor=S)  # 定义列

        self.table.grid()

        self.table.bind('<Double-1>', self.modify)

    def insert(self, info: list):

        for index, data in enumerate(info):
            self.table.insert('', END, values=data)  # 添加数据到末尾

    def delete(self):
        obj = self.table.get_children()  # 获取所有对象
        for o in obj:
            self.table.delete(o)  # 删除对象

    def modify(self, event):

        # Set up window
        win = Toplevel()
        win.title("维护书籍信息")
        win.attributes("-toolwindow", True)

        for item in self.table.selection():
            # item = I001
            values = self.table.item(item)["values"]

        ####
        # Set up the window's other attributes and geometry
        ####

        col1Lbl = Label(win, text=self.table.heading(0)["text"])
        col1Ent = Entry(win)
        col1Ent.insert(0, values[0])  # Default is column 1's current value
        col1Lbl.grid(row=0, column=0)
        col1Ent.grid(row=1, column=0)

        col2Lbl = Label(win, text=self.table.heading(1)["text"])
        col2Ent = Entry(win)
        col2Ent.insert(0, values[1])  # Default is column 2's current value
        col2Lbl.grid(row=0, column=1)
        col2Ent.grid(row=1, column=1)

        col3Lbl = Label(win, text=self.table.heading(2)["text"])
        col3Ent = Entry(win)
        col3Ent.insert(0, values[2])  # Default is column 3's current value
        col3Lbl.grid(row=0, column=2)
        col3Ent.grid(row=1, column=2)

        col4Lbl = Label(win, text=self.table.heading(3)["text"])
        col4Ent = Entry(win)
        col4Ent.insert(0, values[3])  # Default is column 3's current value
        col4Lbl.grid(row=0, column=3)
        col4Ent.grid(row=1, column=3)

        col5Lbl = Label(win, text=self.table.heading(4)["text"])
        col5Ent = Entry(win)
        col5Ent.insert(0, values[4])  # Default is column 3's current value
        col5Lbl.grid(row=0, column=4)
        col5Ent.grid(row=1, column=4)

        col6Lbl = Label(win, text=self.table.heading(5)["text"])
        col6Ent = Entry(win)
        col6Ent.insert(0, values[5])  # Default is column 3's current value
        col6Lbl.grid(row=0, column=5)
        col6Ent.grid(row=1, column=5)

        col7Lbl = Label(win, text=self.table.heading(6)["text"])
        col7Txt = Text(win, height=10)
        col7Txt.insert(END, values[6])
        # col7Ent.insert(0, values[6])  # Default is column 3's current value
        col7Lbl.grid(row=2, column=2)
        col7Txt.grid(row=3, column=0, columnspan=6)

        def ConfirmEntry(self, treeView, entry1, entry2, entry3):
            ####
            # Whatever validation you need
            ####

            # Grab the current index in the tree
            currInd = treeView.index(treeView.focus())

            # Remove it from the tree
            DeleteCurrentEntry(treeView)

            # Put it back in with the upated values
            treeView.insert('', currInd, values=(entry1, entry2, entry3))

        def DeleteCurrentEntry(self, treeView):
            curr = treeView.focus()

            if '' == curr:
                return

            treeView.delete(curr)
            return True

        def UpdateThenDestroy(self):
            if ConfirmEntry(self.table, col1Ent.get(), col2Ent.get(), col3Ent.get()):
                win.destroy()

        okButt = Button(win, text="确定修改")
        okButt.bind("<Button-1>", lambda e: self.UpdateThenDestroy())
        okButt.grid(row=4, column=1)

        canButt = Button(win, text="放弃修改")
        canButt.bind("<Button-1>", lambda c: win.destroy())
        canButt.grid(row=4, column=2)

        delButt = Button(win, text="删除记录")
        delButt.bind("<Button-1>", lambda c: win.destroy())
        delButt.grid(row=4, column=4)
