
# -*- coding: utf-8 -*-
import tkinter as tk  # 装载tkinter模块,用于Python3
from tkinter import ttk  # 装载tkinter.ttk模块,用于Python3

root = tk.Tk()  # 创建窗口对象
root.title(string='ttk.Notebook演示')  # 设置窗口标题
root.geometry('400x300+200+200')

job_title = ''
tc = ttk.Notebook(root)


def book_borrow_m():
    global job_title
    global tc
    if job_title != "borrow":
        tabControl = ttk.Notebook(root)  # 创建Notebook
        job_title = "borrow"
        tc = tabControl
        tab1 = tk.Frame(tabControl, bg='blue')  # 增加新选项卡
        tabControl.add(tab1, text='信息窗')  # 把新选项卡增加到Notebook
        tab2 = tk.Frame(tabControl, bg='yellow')
        tabControl.add(tab2, text='综合信息')
        tab3 = tk.Frame(tabControl, bg='green')
        tabControl.add(tab3, text='技术分析')
        tab4 = tk.Frame(tabControl, bg='blue')
        tabControl.add(tab4, text='编写代码')
        tab5 = tk.Frame(tabControl, bg='blue')
        tabControl.add(tab5, text='模拟回测')

        tabControl.pack(expand=1, fill="both")
        tabControl.select(tab1)  # 选择tab1


def book_mnt_m():
    global job_title
    global tc
    if job_title != "mnt":
        tc.destroy()
        tabControl = ttk.Notebook(root)  # 创建Notebook
        job_title = "borrow"
        tc = tabControl

        tab6 = ttk.Frame(tabControl)
        tabControl.add(tab6, text='双色球')
        tab7 = ttk.Frame(tabControl)
        tabControl.add(tab7, text='大乐透')
        tabControl.pack(expand=1, fill="both")
        tabControl.select(tab1)  # 选择tab1
        job_title = "mnt"
        tc = tabControl


menubar = tk.Menu(root)
A = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='图书管理系统', menu=A)
A.add_command(label='借阅', command=book_borrow_m)
A.add_command(label='维护', command=book_mnt_m)
root.config(menu=menubar)

root.mainloop()     # 进入消息循环
