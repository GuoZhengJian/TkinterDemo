# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 17:27:39 2020

@author: GuoZheng

E-mail : email@guozheng.online
"""

class Top(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Spinbox指定值的输入框')
        self.iconbitmap("E:\OneDrive\图片\图标\ooopic_1533975397.ico") 
        self.geometry(newGeometry='450x325+-7+0')
        self.config(highlightcolor='#6495ED', highlightbackground='#F8F8FF', highlightthickness=2)
        
        Widget_Spinbox(self)

class Widget_Menu(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.config(background='#0fffff')
        self.pack( fill='both', padx=1, pady=1, expand=True)
        
        
top = Top()
top.mainloop()
top.update()