# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 16:30:06 2020

@author: GuoZheng

E-mail : email@guozheng.online
"""
import tkinter as tk

"""
今日单词
"""

class Top(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Spinbox指定值的输入框')
        self.iconbitmap("E:\OneDrive\图片\图标\ooopic_1533975397.ico") 
        self.geometry(newGeometry='450x325+-7+0')
        self.config(highlightcolor='#6495ED', highlightbackground='#F8F8FF', highlightthickness=2)
        
        Widget_Panedwindow(self)

class Widget_Panedwindow(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.config(background='#0fffff')
        self.pack( fill='both', padx=1, pady=1, expand=True)
        
        self.panedwindow = tk.PanedWindow(self)
        self.panedwindow.pack(fill='x')
        
        self.button_1 = tk.Button(self.panedwindow, text='button_1')
        self.panedwindow.add(self.button_1)
        
        self.button_2 = tk.Button(self.panedwindow, text='button_2')
        self.panedwindow.add(self.button_2)
        
        self.button_3 = tk.Button(self.panedwindow, text='button_3')
        self.panedwindow.add(self.button_3)
        
        self.panedwindow.config(proxyrelief='sunken') # [flat, groove, raised, ridge, solid, or sunken]
        self.panedwindow.config()
        # self.panedwindow.config()
        # self.panedwindow.config()
        # self.panedwindow.config()
        # self.panedwindow.config()
        # self.panedwindow.config()

        

top = Top()
top.mainloop()
top.update()