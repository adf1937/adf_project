# -*- coding: utf-8 -*-
from tkinter import *
from home.login import *  # 导入登录模块
from util.bmsdb import *
bmsdb = BMSDB()

root = Tk()
login(bmsdb, root)  # 登录界面类的实例化

root.mainloop()
