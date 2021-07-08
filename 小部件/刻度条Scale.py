# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 11:00:59 2020

@author: GuoZheng

E-mail : email@guozheng.online
"""

import tkinter as tk

class Top(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Button, Checkbutton, Menubutton, Radiobutton')
        self.iconbitmap("E:\OneDrive\图片\图标\ooopic_1533975397.ico") 
        self.geometry(newGeometry='450x325+-7+0')
        self.config(highlightcolor='#6495ED', highlightbackground='#F8F8FF', highlightthickness=2)
        
        Widget_Scale(self)
        
class Widget_Scale(tk.Frame):
    """
    Tkiner Variable 类教程: https://tkdocs.com/shipman/control-variables.html
    """
    def __init__(self, root):
        super().__init__(root)
        self.config(background='#0fffff')
        self.pack(fill='both', padx=1, pady=1, expand=True)
        
        self.scale = tk.Scale(self)
        self.scale.pack()
        
        self.scale.config(from_=0, to=20, digits=3, resolution=0.01)
        self.scale.config(sliderrelief="sunken")
        self.scale.config(label='我是一个刻度条Scale')
        self.scale.config(showvalue=True)
        self.scale.config(orient="horizontal") # "horizontal"(水平), "vertical"(垂直)
        self.scale.config(length=450)
        self.scale.config(sliderlength=60)
        self.scale.config(tickinterval=5)  # 设置对照刻度，设置的值会按照该值的倍数显示刻度, 如to=20, tickinterval=5, 那么会显示[0, 5, 10, 15, 20]

        print(self.scale.get())
        self.scale.set(5)
        print(self.scale.coords())  # 获得当前滑块的位置对应Scale组件左上角的相对坐标, 如果设置 value 参数，则返回当滑块所在该位置时的相对坐标
        print("当前坐标的小部件是:", self.scale.identify(x=150, y=50))

        # 未知用法-------------------------------------------------------------
        # self.scale.config(bigincrement=0.5)

top = Top()
top.mainloop()
top.update()