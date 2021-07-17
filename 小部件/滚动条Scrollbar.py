# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 15:58:50 2020

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
        
        Widget_Listbox(self)
        
class Widget_Listbox(tk.Frame):
    """
    Tkiner Variable 类教程: https://tkdocs.com/shipman/control-variables.html
    """
    def __init__(self, root):
        super().__init__(root)
        self.config(background='#0fffff')
        self.pack(fill='both', padx=1, pady=1, expand=True)
        
        # Scrollbar实例必须在Listbox实例之上, 否则会被listbox抢占空间
        self.yscrollbar = tk.Scrollbar(self, orient='vertical')
        self.yscrollbar.pack(side='left', fill='y')
        self.xscrollbar = tk.Scrollbar(self, orient='horizontal')
        self.xscrollbar.pack(side='bottom', fill='x')
        
        self.listbox = tk.Listbox(self)
        self.listbox.pack(fill='both', expand=True)
        for i in range(100):self.listbox.insert('end', '第%s个选项_哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈'%i)
        
        # .set() 方法是 内容滚动 同时会带动 滚动条滚动 
        self.listbox.config(yscrollcommand = self.yscrollbar.set,
                            xscrollcommand = self.xscrollbar.set)    
        
        # .yview() 方法是 滚动条移动 同时会带动 内容滚动
        self.yscrollbar.config(command=self.listbox.yview)
        self.xscrollbar.config(command=self.listbox.xview)
        
        # .get() 返回当前滑块的位置 (a, b), a值表示当前滑块的顶端或左端的位置，b值表示当前滑块的底端或右端的位置（范围 0.0 ~ 1.0）
        print(self.yscrollbar.get())
        
        
        # 未知用法------------------------------------------------------------
        # self.yscrollbar.delta(deltax=-1, deltay=1)
        # self.yscrollbar.fraction(x=1, y=1)
        # self.yscrollbar.activate("slider")
        # print(self.yscrollbar.identify(x=1, y=2))
        # self.yscrollbar.set(0.0, 0.5)
        
        

top = Top()
top.mainloop()
top.update()