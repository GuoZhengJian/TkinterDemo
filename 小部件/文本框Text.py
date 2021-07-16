# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 10:32:36 2021

@author: GuoZheng

E-mail : email@guozheng.online
"""
import tkinter as tk

class Top(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Text文本框')
        self.iconbitmap("E:\OneDrive\图片\图标\ooopic_1533975397.ico") 
        self.geometry(newGeometry='450x325+-7+0')
        self.config(highlightcolor='#6495ED', highlightbackground='#F8F8FF', highlightthickness=2)
        
        Widget_text(self)

class Widget_text(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.config(background='#0fffff')
        self.pack(fill='both', padx=1, pady=1, expand=True)
        
        self.text = tk.Text(self)
        self.text.pack(side='bottom', fill='x')
        self.text.config(height=3)
        
        self.text.insert('insert', 'insert()方法可以在Text文本框中插入文字')
        self.text.tag_add('tag1', '1.0', '2.0')
        self.text.tag_config('tag1', foreground='#FF9FFF', background='#FFFF9F')
        self.text.update_idletasks()
        print(self.text.bbox(index=1.0))
        
        print(self.text.compare(1.0,"==", 2.0))
        self.text.debug(boolean=True)
        
        print(self.text.get('1.0', 'end'))
        



top = Top()
# top.mainloop()
top.update()