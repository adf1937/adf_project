from tkinter import *
from tkinter.ttk import *


def tree_color():  # 表格栏隔行显示不同颜色函数
    items = tree1.get_children()  # 得到根目录所有行的iid
    i = 0  # 初值
    for hiid in items:
        if i/2 != int(i/2):  # 判断奇偶
            tag1 = ''  # 奇数行
        else:
            tag1 = 'even'  # 偶数行
        tree1.item(hiid, tag=tag1)  # 偶数行设为浅蓝色的tag='even'
        i += 1  # 累加1


root = Tk()

#img1 = PhotoImage(file='16-1.png')
#img2 = PhotoImage(file='16-2.png')

tree1 = Treeview(root, columns=('qy', 'dz'))
# 创建树表格组件，栏目有3个：#0, qy, dz

tree1.column('#0', width=120, anchor=CENTER)
tree1.column('qy', width=90, anchor=CENTER)
tree1.column('dz', width=180, anchor=CENTER)
# 定义3个栏目的宽度，对齐方法，宽度是否窗体变化

tree1.heading('#0', text='城市')
tree1.heading('qy', text='区域')
tree1.heading('dz', text='地址')
# 定义3个栏目的表头文字

tree1.insert('', END, text='广州市', values=('海珠区', '阅江中路380号'))
tree1.insert('', END, text='深圳市', values=('南山区', '华侨城侨香路11号'))
tree1.insert('', END, text='东莞市', values=('南城区', '元美东路3号济亨网'))

tree1.insert('', END, text='长沙市', values=('雨花区', '韶山中路108号'))
tree1.insert('', END, text='湘潭市', values=('岳塘区', '书院路42号云峰工作室'))
tree1.insert('', END, text='衡阳市', values=('蒸湘区', '祝融路名都花园B9栋107室'))

tree1.insert('', END, text='长沙市', values=('岳麓区', '梅溪湖路复兴小区709号'))
tree1.insert('', END, text='广州市', values=('白云区', '下塘西路545号'))

tree1.pack(fill=BOTH, expand=True)

# 3.8版要多加的代码------------
# 源码来自wb98.com


def fixed_map(option):
    return [elm for elm in style.map("Treeview", query_opt=option)
            if elm[:2] != ("!disabled", "!selected")]


style = Style()
style.map("Treeview", foreground=fixed_map("foreground"),
          background=fixed_map("background"))
# 3.8版要多加的代码------------

# 定义背景色风格
tree1.tag_configure('even', background='lightblue')  # even标签设定为浅蓝色背景颜色

tree_color()  # 启动程序，根据奇偶行设为不行的背景颜色

tree1.selection_set('I001')  # 默认选中第一项

fr1 = Frame(root)  # 收入3个按钮
fr1.pack(pady=10)


def deljob():  # 真删除
    iid = tree1.selection()
    tree1.delete(iid)
    tree_color()  # 启动程序，根据奇偶行设为不行的背景颜色


def hidejob():  # 假删除，只是隐藏
    global iid1, index1, parent1  # 定义为全局变量
    iid1 = tree1.selection()  # 假删除前，记下选中前的iid
    index1 = tree1.index(iid1)  # 记下假删除行的位置index
    parent1 = tree1.parent(iid1)  # 记下假删除行的父节点
    tree1.detach(iid1)  # 假删除，隐藏
    tree_color()  # 删除及恢复记录后，根据奇偶行重新设置不同行的背景颜色


def showjob():  # 把假删除的记录在原来的位置显示
    global iid1, index1, parent1  # 定义为全局变量
    tree1.selection_set()  # 取消以前的可能选中项
    tree1.move(iid1, parent1, index1)  # 在原来的位置恢复假删除的记录
    tree_color()  # 删除及恢复记录后，根据奇偶行重新设置不同行的背景颜色


but1 = Button(fr1, text="隐藏", command=hidejob)
but1.pack(side=LEFT)
but1 = Button(fr1, text="重现", command=showjob)
but1.pack(side=LEFT)
but1 = Button(fr1, text="彻底删除", command=deljob)
but1.pack(side=LEFT, padx=(20, 0))

root.mainloop()
