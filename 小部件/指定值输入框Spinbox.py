# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 21:21:14 2020

@author: Guozheng
"""

import tkinter as tk

"""
今日单词
    format 格式; 格式化
    increment [数] 增量；增加
    readonly 只读的
"""

class Top(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Spinbox指定值的输入框')
        self.iconbitmap("E:\OneDrive\图片\图标\ooopic_1533975397.ico") 
        self.geometry(newGeometry='450x325+-7+0')
        self.config(highlightcolor='#6495ED', highlightbackground='#F8F8FF', highlightthickness=2)
        
        Widget_Spinbox(self)

class Widget_Spinbox(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.config(background='#0fffff')
        self.pack( fill='both', padx=1, pady=1, expand=True)
        padxsetting = 2
        padysetting = 2
        widthsetting = 50
        
        self.spinbox = tk.Spinbox(self)
        self.spinbox.pack()
        
        self.spinbox.config(buttonuprelief="groove") # groove, raised, ridge, solid, or sunken
        self.spinbox.config(wrap=True) # [Spinbox widget: 是否开启内容循环显示(参数: True or False)]
        self.spinbox.config(from_=0, to=10, increment=0.5) # 指定当用户每次点击调节箭头的时候增加或减少多少; 例如 from_=1, to=10, increment=0.5，那么每次用户点击调节箭头的时候，输入框中的数字增加或减少0.5
        self.spinbox.config(format="%10.4f") # 使用该选项设置选择数值的样式(from_ 和 to 指定范围，用户自行输入的不算), 例如 format='%10.4f' 表示显示的数值占 10 位，小数点后保留 4 位
        self.spinbox.config(values=("张三", "李四", "王五", "马六")) # 指定Spinbox的预设值, 提供两个方法限定用户输入的内容，一种是通过 from_ 和 to 选项设置范围，另一种则是将可选值以元组的形式赋值给 values 选项, 例如 values= ("小新", "风间", "正男", "妮妮", "阿呆") 则允许用户在这 5个字符串中选择
        print(self.spinbox.bbox(index=2))  # 返回index索引指定的字符所在的矩形范围, 返回格式为(x1, y1, x2, y2)
        # self.spinbox.config(state="readonly", readonlybackground="#99FFFF") # 设置当 Spinbox 处于 "readonly" 状态下的背景颜色
       
        self.spinbox.selection("from", 2) # ('from', index) 设置选中范围的起始位置是 index 指定的值
        self.spinbox.selection("to", 2) # ('to', index) 设置选中范围的结束位置是 index 参数指定的值
        self.spinbox.selection("range",0, 2) # ('range', start, end)设置选中范围是 statr 到 end 参数之间的值
        
        self.spinbox.selection_element(element='buttonup') # "设置"或"获取"选择范围, 如果指定 element 参数: 设置选择的范围(参数:buttonup(按下上边按钮) or buttondown(按下下边按钮)), 如果不指定参数,则是获取当前的选择范围
        
        # 未知用法-------------------------------------------------------------
        # self.spinbox.selection_get()


top = Top()
top.mainloop()
top.update()