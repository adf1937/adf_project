import tkinter as tk
from tkinter import ttk
from tkinter import *

ws = tk.Tk()
ws.title('PythonGuides')
 ws.geometry('1000x800')
 # ws['bg']='#fb0'
 frame1 = ttk.Frame(ws, borderwidth=5, relief="groove", width=100, height=100)
 frame1.grid(row=0, column=0)
 rame1.propagate(0)
 ttk.Label(frame1, text="Explaining Python Tkinter with an Example", background="green").grid(row=0, column=0)
  
 tv = ttk.Treeview(frame1)
 tv['columns'] = ('Rank', 'Name', 'Badge')
 tv.column('#0', width=0, stretch=tk.NO)
 tv.column('Rank', anchor=tk.CENTER, width=80)
 tv.column('Name', anchor=tk.CENTER, width=80)
 tv.column('Badge', anchor=tk.CENTER, width=80)
 
 tv.heading('#0', text='', anchor=tk.CENTER)
 tv.heading('Rank', text='Id', anchor=tk.CENTER)
 tv.heading('Name', text='rank', anchor=tk.CENTER)
 tv.heading('Badge', text='Badge', anchor=tk.CENTER)
  
 tv.insert(parent='', index=0, iid=0, text='', values=('1', 'Vineet', 'Alpha'))
 tv.insert(parent='', index=1, iid=1, text='', values=('2', 'Anil', 'Bravo'))
 tv.insert(parent='', index=2, iid=2, text='', values=('3', 'Vinod', 'Charlie'))
 tv.insert(parent='', index=3, iid=3, text='', values=('4', 'Vimal', 'Delta'))
 tv.insert(parent='', index=4, iid=4, text='', values=('5', 'Manjeet', 'Echo'))
 tv.grid(row=1, column=0, sticky="W")
  
 
 def update_item():
    selected = tv1.focus()
    print(f'selected={selected}')  # selected=3
    temp = tv1.item(selected, 'values')
    print(f'temp={temp}')  # temp=('Shanti', 'e14', '22000.0')
    sal_up = float(temp[3]) + float(temp[3]) * 0.05
    tv1.item(selected, values=(temp[0], temp[1], temp[2], sal_up))
  
  
  def show_selected():
      print(tv1.selection())
  
  
 def selectmode_none():
     tv1['selectmode'] = "none"
     print("selectmode=none  用户将不会在 Treeview 上看到任何标记,点击数据无显示标记")
  
  
 def selectmode_browse():
     tv1['selectmode'] = "browse"
     print("selectmode=browse  用户将能够在一次选择单个项目")
  
  
  
 def selectmode_extended():
     tv1['selectmode'] = "extended"
     print("selectmode=extended 用户就可以同时选择多个项目（按 shift 键可选择多个项目）")
  
 # 表格数据
 datas = [(0, "vineet", "e11", 1000000.00)
      , (1, "anil", "e12", 120000.00)
      , (2, "ankit", "e13", 41000.00)
      , (3, "Shanti", "e14", 22000.00)
      , (4, "Shanti", "e14", 22000.00)
      , (5, "Shanti", "e14", 22000.00)
      , (6, "Shanti", "e14", 22000.00)
      , (7, "Shanti", "e14", 22000.00)
      , (8, "Shanti", "e14", 22000.00)
      , (9, "Shanti", "e14", 22000.00)
      , (10, "Shanti", "e14", 22000.00)
      , (11, "Shanti", "e14", 22000.00)
           ]
  
 frame2 = ttk.Frame(ws, borderwidth=5, relief="groove", width=300, height=100)
 frame2.grid(row=0, column=1)
 frame2.propagate(0)
  
 sl1 = Scrollbar(frame2)
  
 conten = "How to change Value in Python Tkinter Treeview ,\n Python Tkinter Treeview Scrollbars"
 ttk.Label(frame2, text=conten, background="red").grid(row=0, column=0,columnspan=4)
 columns = ["id", "name", "eid", "Slary"]
 tv1 = ttk.Treeview(frame2
                     , show='headings'
                     , height=5
                     , columns=columns
                     )
  tv1.grid(row=1, column=0,columnspan=4)
  headText = ("id", "name", "eid", "Slary")
  for idx in range(len(columns)):
      tv1.column(columns[idx], width=70, minwidth=70, anchor=tk.CENTER)
      tv1.heading(idx, text=headText[idx])
  
  for i in range(len(datas)):
      tv1.insert(parent='', index=i, iid=i, values=datas[i])
  ttk.Button(frame2, text='Increment Salary', command=update_item).grid(row=2, column=1,columnspan=1)
 # 创建滚动条
 scroll = tk.Scrollbar(frame2, orient="vertical", command=tv1.yview)
 scroll['command'] = tv1.yview
tv1.config(yscrollcommand=scroll.set)  # 将滚动条填充
 scroll.grid(row=1, column=5, sticky=S + W + E + N)
 ttk.Button(frame2, text='Show Selected ', command=show_selected).grid(row=3, column=1,columnspan=1)
 
 ttk.Button(frame2, text='Browse', command=selectmode_browse).grid(row=4, column=0)
 ttk.Button(frame2, text='None', command=selectmode_none).grid(row=4, column=1)
 ttk.Button(frame2, text='Extended', command=selectmode_extended).grid(row=4, column=2)
 
 
 ws.mainloop()