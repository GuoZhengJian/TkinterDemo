# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 15:59:39 2021

@author: 57207
"""

import tkinter as tk
import time

class Mytest(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        
        """
        当出现无法使用Button触发bind时,可以使用如下逻辑实现:
            小部件对象 → 鼠标或按钮绑定bind → 然后在event对象中更改小部件对象的属性或方法
        """
        self.labelframe = tk.LabelFrame(self)
        self.labelframe.pack(side='top', fill='x')
        self.labelframe.config(background='#1abc9c', height=50)
        
        labelconfig = {'activebackground':'#3498db', 'background':'#ffffff', 'anchor':'w', 'state':'normal'}
        
        self.label1 = tk.Label(self.labelframe, text='1')
        self.label2 = tk.Label(self.labelframe, text='Hello Word')
        self.label3 = tk.Label(self.labelframe, text='你好, 世界')
        
        self.label1.place(relx=0, rely=0, relheight=1, relwidth=0.1)
        self.label2.place(relx=0.1, rely=0, relheight=1, relwidth=0.3)
        self.label3.place(relx=0.4, rely=0, relheight=1, relwidth=0.6)

        
        self.label1.config(labelconfig)
        self.label2.config(labelconfig)
        self.label3.config(labelconfig)
        
        self.label1.bind('<Button-1>', self.active_func, add='+')
        self.label2.bind('<Button-1>', self.active_func, add='+')
        self.label3.bind('<Button-1>', self.active_func, add='+')
        
        self.label1.bind('<ButtonRelease-1>', self.disabled_func, add='+')
        self.label2.bind('<ButtonRelease-1>', self.disabled_func, add='+')
        self.label3.bind('<ButtonRelease-1>', self.disabled_func, add='+')
        
    def active_func(self, event):
        event.widget.config(state='active')
        print(event.widget.cget('text'))
        print(event.widget)
        
    def disabled_func(self, event):
        time.sleep(0.1)
        event.widget.config(state='disabled')


if __name__ == '__main__':
    root = tk.Tk()
    root.wm_attributes('-topmost', 1)
    root.title('Mytest')
    root.geometry(newGeometry="566x355+966+0")
    Mytest(root)
    root.mainloop()

