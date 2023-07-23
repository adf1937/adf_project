# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
from home.home import *
from util.bmsdb import *


class login(object):
    def __init__(self, db: BMSDB, master=None):
        self.db = db
        self.root = master  # 定义内部变量root
        self.root.geometry('300x150+888+444')
        self.root.title('图书管理系统')
        self.creatlogin()

    def creatlogin(self):
        self.fr1 = Frame(self.root)
        self.fr1.grid(row=2, column=0, columnspan=2)

        Label(self.fr1, text="用户名：").grid(row=0, column=0)
        Label(self.fr1, text="密  码：").grid(row=1, column=0)
        self.enUser = Entry(self.fr1)
        self.enUser.grid(row=0, column=1)
        self.enPasswd = Entry(self.fr1, show="*")
        self.enPasswd.grid(row=1, column=1)

        #self.enUser.bind_all("<Return>", self.enter)
        #self.enPasswd.bind_all("<Return>", self.enter)
        self.fr1.bind_all("<Return>", self.enter)

        self.but1 = Button(
            self.fr1, text="登录", command=self.submit).grid(row=2, column=1)
        self.enUser.focus_set()  # 获得焦点

    def enter(self, event):
        self.submit()

    def submit(self):
        aUser = self.enUser.get()
        aPasswd = self.enPasswd.get()

        if self.db.checkUser(aUser, aPasswd):
            self.fr1.destroy()  # 登录界面卸载
            home(self.db, self.root)  # 密码对，就把主窗体模块的界面加载
        else:
            messagebox.showwarning("警告：", "用户名或者密码错误，请重试!")
