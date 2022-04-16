# coding:utf8
from tkinter import *
from tkinter.constants import *


class APP:
    def __init__(self, master):
        list1 = ["青菜", "白菜", "菠菜", "黄瓜", "青菜", "白菜",
                 "菠菜", "黄瓜", "青菜", "白菜", "菠菜", "黄瓜"]
        frame = Frame(master)
        frame.pack(padx=5, pady=5)

        # 添加一个滚动条Scrollbar,靠右，填充。
        sb = Scrollbar(frame)
        sb.pack(side=RIGHT, fill=Y)

        # listbox 生成列表选框,selectmode设置选择模式，SINGLE单选，EXTENDED多选
        lb = Listbox(frame, width=30, selectmode=EXTENDED,
                     yscrollcommand=sb.set)
        lb.pack(fill=BOTH)
        sb.config(command=lb.yview)

        # insert 添加选项
        for key in list1:
            lb.insert(END, key)

        # 打印所有选项
        print(lb.get(0, END))
        # 删除选中的选项
        b1 = Button(frame, text="删除它", command=lambda x=lb: x.delete(ACTIVE))
        b1.pack(side=LEFT)


root = Tk()
win = APP(root)
root.mainloop()
