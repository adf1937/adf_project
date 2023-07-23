from tkinter import Button as tkButton, Tk, Frame, Label


class ChildFrame(Frame):
    '''
    这是一个建立在Frame之上的子窗口控件
    该子窗口可以嵌入tkinter父窗口，但建议是在窗口而不是在控件中
    子窗口可以移动也可以不移动，通过属性设定来改变子窗口的状态
    需要注意的是，在内嵌子窗口导入控件时，注意起始高度为32

    因为组件限制，ChildFrame只能够实现真正窗口的一小部分功能
    '''

    def __init__(self, root, title_color, title='title', color='#f0f0f0'):
        self.root = root
        super().__init__(root, bg=color)  # 底层
        self.title = title
        self.tc = title_color
        self.titlebar = Frame(self, bg=self.tc)  # 标题栏
        Label(self.titlebar, text=self.title,
              bg=self.tc, fg='white').place(x=5, y=5)
        self.conbar = Frame(self.titlebar, bg=self.tc)
        self.conbar.pack(side='right')  # 工具栏
        self.desb = tkButton(self.conbar, text='×', font=('宋体', 15), bg=self.tc, fg='white',
                             activeforeground='white', activebackground='red', relief='flat', command=self.destroy)
        self.desb.pack(side='right')  # 关闭按钮
        self.desb.bind(
            '<Enter>', lambda event: self.desb.configure(background='red'))
        self.desb.bind('<Leave>', lambda event: self.desb.configure(
            background=self.tc))  # 当鼠标划过时有红色样式
        self.expandb = tkButton(self.conbar, text='□', font=('宋体', 15), fg='white', bg=self.tc,
                                activeforeground='white', activebackground=self.tc, relief='flat', command=self.expandwin)
        self.expandb.pack(side='right')  # 最大化
        self.titlebar.pack(fill='x')
        self.titlebar.bind('<Button-1>', self._startmove, add='+')  # 移动
        self.titlebar.bind('<B1-Motion>', self._movewin, add='+')

    def show(self, x, y, width, height):  # 显示窗口
        self.wd = width
        self.hi = height
        self.oralx = x
        self.oraly = y
        self.place(x=x, y=y, width=width, height=height)

    def destroy(self):  # 销毁窗口
        self.place_forget()

    def _startmove(self, event):  # 记录开始移动的坐标
        self.startx = event.x
        self.starty = event.y

    def _movewin(self, event):  # 移动窗口
        self.place(x=self.winfo_x()+(event.x-self.startx),
                   y=self.winfo_y()+(event.y-self.starty))

    def lockwin(self):  # 禁止窗口移动
        self.titlebar.unbind('<B1-Motion>')

    def activewin(self):  # 允许窗口移动
        self.titlebar.bind('<B1-Motion>', self._movewin, add='+')

    def backexpandwin(self):  # 恢复窗口大小
        self.expandb['text'] = '□'
        self.expandb['command'] = self.expandwin
        self.place(x=self.oralx, y=self.oraly, width=self.wd, height=self.hi)
        self.activewin()

    def expandwin(self):  # 最大化窗口
        # 记录窗口的起始位置
        self.oralx = self.winfo_x()
        self.oraly = self.winfo_y()
        self.root.update()
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        self.place(x=0, y=0, width=w, height=h)
        self.expandb['text'] = '◪'
        self.expandb['command'] = self.backexpandwin
        self.lockwin()  # 最大化不能移动

    def noexpand(self):  # 是否支持放大
        self.expandb.pack_forget()

    def haveexpand(self):  # 支持放大
        self.expandb.pack()


root = Tk()
ChildFrame(root,  '#800080')

root.mainloop()
