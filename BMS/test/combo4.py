
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
from tkinter import ttk


win = Tk()


tupBkStatus = ("空闲", "借出", "损坏", "丢失", "维护")
srcBkStatus = "借出"
try:
    idx = tupBkStatus.index(srcBkStatus)
except:
    idx = 4

cbValue = tk.StringVar()  # 窗体自带的文本，新建一个值
cbValue.set("借出")
cbBookStatus = ttk.Combobox(win, textvariable=cbValue)  # 初始化
cbBookStatus["values"] = tupBkStatus
# cbBookStatus.current(idx)  #
# cbBookStatus.current(2)
lblBookStatus = Label(win, text="test")
lblBookStatus.grid(row=0, column=2)
cbBookStatus.grid(row=1, column=2)


win.mainloop()
