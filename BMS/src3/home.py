from tkinter import *
from job import ren, kao, gong, about


class home():
    def __init__(self, master=None):
        self.root = master
        self.root.geometry('400x250+888+444')
        self.jobtxt = ''  # 用这个变量记下窗体的标题
        self.createPage()

    def createPage(self):

        menubar = Menu(self.root)
        A = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='图书借还管理', menu=A)
        A.add_command(label='借书', command=self.book_borrow_m)
        A.add_command(label='还书', command=self.book_return_m)
        A.add_command(label='延期', command=self.book_extend_m)
        A.add_command(label='关于', command=about)
        A.add_command(label='退出', command=self.root.destroy)

        A = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='图书维护管理', menu=A)
        A.add_command(label='图书查询', command=self.book_search_m)
        A.add_command(label='图书增删', command=self.book_addremove_m)
        A.add_command(label='图书修改', command=self.book_modify_m)
        A.add_command(label='关于', command=about)
        A.add_command(label='退出', command=self.root.destroy)

        A = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='用户管理', menu=A)
        A.add_command(label='用户维护', command=self.user_maintainence_m)
        A.add_command(label='关于', command=about)
        A.add_command(label='退出', command=self.root.destroy)

        self.root.config(menu=menubar)

        self.welcome()

    def welcome(self):
        pass

    def book_borrow_m(self):  # 执行人员管理菜单
        if self.jobtxt != '图书借阅管理':  # 根据窗体标题来决定否则执行这个菜单功能
            if self.jobtxt == '图书维护管理':  # 如果要切换，就先根据窗体标签把现在的框架卸载掉
                self.kaopage.destroy()
            if self.jobtxt == '用户管理':  # 如果要切换，就先根据窗体标签把现在的框架卸载掉
                self.gongpage.destroy()

            self.renpage = ren(self.root)  # 调用job.py的ren类，显示图书借阅管理界面
            self.renpage.pack()
            self.root.title('图书借阅管理')
            self.jobtxt = '图书借阅管理'  # 记下窗体标题

    def book_return_m(self):  # 执行图书维护管理菜单
        if self.jobtxt != '图书维护管理':
            if self.jobtxt == '图书借阅管理':
                self.renpage.destroy()
            if self.jobtxt == '用户管理':
                self.gongpage.destroy()

            self.kaopage = kao(self.root)
            self.kaopage.pack()
            self.root.title('图书维护管理')
            self.jobtxt = '图书维护管理'

    def book_extend_m(self):  # 执行图书维护管理菜单
        if self.jobtxt != '图书维护管理':
            if self.jobtxt == '图书借阅管理':
                self.renpage.destroy()
            if self.jobtxt == '用户管理':
                self.gongpage.destroy()

            self.kaopage = kao(self.root)
            self.kaopage.pack()
            self.root.title('图书维护管理')
            self.jobtxt = '图书维护管理'

    def about(self):  # 调用job.py里的about函数，弹出窗体
        about()

    def book_search_m(self):
        pass

    def book_addremove_m(self):
        pass

    def book_modify_m(self):
        pass

    def user_maintainence_m(self):
        pass


if __name__ == "__main__":
    root = Tk()
    home(root)
    root.mainloop()
    pass
