# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 16:25:05 2020

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
        
        All_Variable(self)
        
class All_Variable(tk.Frame):
    """
    Tkiner Variable 类教程: https://tkdocs.com/shipman/control-variables.html
    """
    def __init__(self, root):
        super().__init__(root)
        self.config(background='#0fffff')
        self.pack(fill='both', padx=1, pady=1, expand=True)
        
        self.var = tk.StringVar()
        width_len = len(self.var.get())
     
        self.label = tk.Label(self,  width=width_len, textvariable=self.var)
        self.label.pack()
    
        self.entry = tk.Entry(self, textvariable=self.var)
        self.entry.pack(fill='x')
    
        import time
        def label_variable_1():
            i = 10
            while i>0:
                i -= 1
                time.sleep(0.1)   # 注意: 如果循环变换的间隔时间为0, 那么文本就不会变化, 也就是假状的卡死状态
                # time.sleep(0)     # ERROR: 如果循环变换的间隔时间为0, 那么文本就不会变化, 也就是假状的卡死状态
                self.var.set('倒数计时%s秒'%i)
                self.label.update()
                print(self.var.get())
        
        def label_variable_2():
            for i in range(10):
                time.sleep(0.1)
                self.var.set('开始计时%s秒'%i)
                self.label.update()
                print(self.var.get())
            
        self.button_1 = tk.Button(self, text='倒数计时', command=label_variable_1)
        self.button_1.pack(fill='x')
        
        self.button_2 = tk.Button(self, text='开始计时', command=label_variable_2)
        self.button_2.pack(fill='x')

        
        

        

top = Top()
top.mainloop()
# top.update()