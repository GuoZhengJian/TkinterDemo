# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 15:25:53 2021

@author: 57207
"""

import tkinter as tk

class Top(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.place(relx=0, rely=0, relheight=1, relwidth=1)
        Topframe(self)
        Topentry(self)

# 核心在于需要一个全局的容器序列
label_text = []

# 展示的Frame
class Topframe(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.config({'background':'#ecf0f1', 'borderwidth':0})
        self.place(relx=0, rely=0, relheight=0.85, relwidth=1)

        self.label = tk.Label(self, text='展示标签', background='#a4b0be')
        self.label.pack(side='top', fill='x')
        
        for i in label_text:
            new_label = tk.Label(self, text=i, background='#a4b0be')
            new_label.pack(side='top', fill='x')

# 用户输入的Frame 
class Topentry(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.config({'background':'#57606f', 'borderwidth':0})
        self.place(relx=0, rely=0.85, relheight=0.15, relwidth=1)
        
        self.entry = tk.Entry(self, background='#a4b0be')
        self.entry.pack(fill='both', expand=True)
        self.entry.bind('<Return>', self.put_func)
        
    def put_func(self, event):
        args = self.entry.get()
        self.entry.delete(0, 'end')

        label_text.append(args)
        Topframe().update()
        
        
if __name__ == '__main__':
    root = tk.Tk()
    root.wm_attributes('-topmost', 1)
    root.title('Mainwindow')
    root.geometry(newGeometry="566x355+966+0")
    Top(root)
    root.mainloop()