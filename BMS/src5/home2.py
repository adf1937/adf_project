# -*- coding: utf-8 -*-
import tkinter as tk  # 装载tkinter模块,用于Python3
from tkinter import ttk  # 装载tkinter.ttk模块,用于Python3


class home():
    def __init__(self, master=None):
        self.root = master
        self.root.state("zoomed")
        self.createnb()

    def createnb(self):
        self.nb = ttk.Notebook(self.root)  # 创建Notebook

        self.tab1 = ttk.Frame(self.nb)            # Create a tab
        self.nb.add(self.tab1, text='第一页')      # Add the tab

        self.createbmpage()

        self.tab2 = ttk.Frame(self.nb)            # Add a second tab
        self.nb.add(self.tab2, text='第二页')      # Make second tab visible

        self.tab3 = ttk.Frame(self.nb)            # Add a third tab
        self.nb.add(self.tab3, text='第三页')      # Make second tab visible

        self.createbupage()

        self.nb.pack(expand=1, fill="both")  # Pack to make visible
        self.nb.select(0)  # 选择tab1

    def createbmpage(self):

        #---------------Tab1控件介绍------------------#
        # We are creating a container tab3 to hold all other widgets
        monty = ttk.LabelFrame(self.tab1, text='控件示范区1')
        monty.grid(column=0, row=0, padx=8, pady=4)

        # Modified Button Click Function

        # Changing our Label
        ttk.Label(monty, text="输入文字:").grid(column=0, row=0, sticky='W')

        # Adding a Textbox Entry widget
        name = tk.StringVar()
        nameEntered = ttk.Entry(monty, width=12, textvariable=name)
        nameEntered.grid(column=0, row=1, sticky='W')

        # Adding a Button
        action = ttk.Button(monty, text="点击之后\n按钮失效",
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

    def createbupage(self):

        #---------------Tab1控件介绍------------------#
        # We are creating a container tab3 to hold all other widgets
        monty = ttk.LabelFrame(self.tab3, text='用户管理')
        monty.grid(column=0, row=0, padx=8, pady=4)

        # Modified Button Click Function

        # Changing our Label
        ttk.Label(monty, text="输入文字:").grid(column=0, row=0, sticky='W')

        # Adding a Textbox Entry widget
        name = tk.StringVar()
        nameEntered = ttk.Entry(monty, width=12, textvariable=name)
        nameEntered.grid(column=0, row=1, sticky='W')

        # Adding a Button
        action = ttk.Button(monty, text="点击之后\n按钮失效",
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


if __name__ == "__main__":
    root = tk.Tk()
    home(root)
    root.mainloop()
