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
        menubar.add_cascade(label='操作', menu=A)
        A.add_command(label='人事管理', command=self.gotoren)
        A.add_command(label='考勤管理', command=self.gotokao)
        A.add_command(label='工资管理', command=self.gotogong)
        # A.add_command(label='关于',command=self.about)
        A.add_command(label='关于', command=about)
        A.add_command(label='退出', command=self.root.destroy)

        self.root.config(menu=menubar)

        self.gotoren()

    def gotoren(self):  # 执行人员管理菜单
        if self.jobtxt != '人事管理':  # 根据窗体标题来决定否则执行这个菜单功能
            if self.jobtxt == '考勤管理':  # 如果要切换，就先根据窗体标签把现在的框架卸载掉
                self.kaopage.destroy()
            if self.jobtxt == '工资管理':  # 如果要切换，就先根据窗体标签把现在的框架卸载掉
                self.gongpage.destroy()

            self.renpage = ren(self.root)  # 调用job.py的ren类，显示人事管理界面
            self.renpage.pack()
            self.root.title('人事管理')
            self.jobtxt = '人事管理'  # 记下窗体标题

    def gotokao(self):  # 执行考勤管理菜单
        if self.jobtxt != '考勤管理':
            if self.jobtxt == '人事管理':
                self.renpage.destroy()
            if self.jobtxt == '工资管理':
                self.gongpage.destroy()

            self.kaopage = kao(self.root)
            self.kaopage.pack()
            self.root.title('考勤管理')
            self.jobtxt = '考勤管理'

    def gotogong(self):  # 执行工资管理菜单
        if self.jobtxt != '工资管理':
            if self.jobtxt == '考勤管理':
                self.kaopage.destroy()
            if self.jobtxt == '人事管理':
                self.renpage.destroy()

            self.gongpage = gong(self.root)
            self.gongpage.pack()
            self.root.title('工资管理')
            self.jobtxt = '工资管理'

    def about(self):  # 调用job.py里的about函数，弹出窗体
        about()
