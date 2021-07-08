# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 15:12:02 2020

@author: GuoZheng

E-mail : email@guozheng.online
"""
import tkinter as tk

class Top(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Listbox')
        self.iconbitmap("E:\OneDrive\图片\图标\ooopic_1533975397.ico")
        self.geometry(newGeometry='450x325+-7+0')
        self.config(highlightcolor='#6495ED', highlightbackground='#F8F8FF', highlightthickness=2)

        Widget_Listbox(self)

class Widget_Listbox(tk.Frame):
    """
    Tkiner Variable 类教程: https://tkdocs.com/shipman/control-variables.html
    """
    def __init__(self, root):
        super().__init__(root)
        self.config(background='#0fffff')
        self.pack(fill='both', padx=1, pady=1, expand=True)

        # Scrollbar实例必须在Listbox实例之上
        self.yscrollbar = tk.Scrollbar(self, orient='vertical', )
        self.yscrollbar.pack(side="left", fill='y')

        self.listbox = tk.Listbox(self)
        self.listbox.pack(fill='both', expand=False)
        for i in range(100):self.listbox.insert("end", "第%s个选择"%i)

        self.listbox.config(selectmode="extended")  # 多选, 鼠标拖动 | Shift+方向键
        self.listbox.config(activestyle="none")         # 无任何样式
        # self.listbox.config(setgrid=True)    # 启动网格控制

        self.yscrollbar.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.yscrollbar.set)

        self.listbox.see(3)     # 调整列表框内选择项目的位置, 使index指定的选择项排到第一个位置
        print(self.listbox.size())
        self.listbox.activate(3)     # ?? 选中指定index索引的选项
        self.listbox.selection_set(1,4)   # 设置选中状态, 范围是first至last, 如果忽略last参数，则只设置first参数指定选项为选中状态
        self.listbox.itemconfig(5, background="#000000",foreground="#FFFFFF")   # 更改指定index行的配置选项, **option配置选项有: background(背景色), foreground(前景色), selectbackground(选中背景色), selectforeground(选中前景色)
        print(self.listbox.itemcget(5, "background"))   # 获得index索引指定选项的"项目值", "项目值"由.itemconfig()方法的**option参数指定
        print(self.listbox.curselection())  # 返回选中选项的序号(从0开始), 如果没有选中任何选项，返回一个空元组
        self.listbox.yview_moveto(fraction=0.01)    # 跟 xview("moveto", fraction) 一样
        # self.listbox.yview("moveto", 0.9)  # 如果第一个参数是 "moveto"，则第二个参数表示滚动到指定的位置：0.0 表示最左端，1.0 表示最右端
        # self.listbox.yview("scroll", 5, "pages")  # 如果第一个参数是 "scroll"，则第二个参数表示滚动的数量，第三个参数表示滚动的单位（可以是 "units" 或 "pages"）
        
        # self.listbox.selection_clear(2,4) # 取消选中状态, 与 .select_clear() 相同

        self.listbox.selection_anchor(index=6)  #在 index 参数的位置下一个锚点，此后你就可以通过 tk.ANCHOR 特殊索引访问
        print(self.listbox.select_anchor(index=6))    # 与 .selection_anchor(index) 相同
        
        print(self.listbox.selection_includes(index=3)) # 返回index索引指定的选项的选中状态, 返回True, False
        print(self.listbox.select_includes(index=3))  # 与 .selection_includes(index) 相同
        print(self.listbox.bbox(index=2))   # 返回给定索引号对应的选项的边框
        

        # 未知用法-----------------------------------------------------------
        # print(self.listbox.nearest(y=1))      #返回与给定参数 y 在垂直坐标上最接近的项目的序号(打印.see()属性的值)
        # self.listbox.scan_mark(x, y)  # 使用鼠标事件操作 Listbox 内容的滚动, 详情参考onenote

top = Top()
# top.mainloop()
top.update()