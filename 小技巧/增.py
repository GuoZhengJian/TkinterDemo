# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 09:09:37 2021

@author: 57207
"""

import tkinter as tk
from src.GUI import test2

user_inp = []

class Myframe(tk.Frame):
    def __init__(self, master=None, task=None):
        super().__init__(master)
        self.master = master
        if not task:
            self.task = []
        else:
            self.task = task
        self.place(relx=0, rely=0, relheight=1, relwidth=1)
            
        self.label = tk.Label(self)
        self.label.pack(side='top', fill='x')
        self.label.config(background='#1abc9c', height=2, text='请在这里输入')
        self.task.append(self.label)

        self.entry = tk.Entry(self, background='#9b59b6')
        self.entry.pack(side='bottom', fill='x')
            
        self.entry.bind('<Return>', self.my_return)
        
    def my_return(self, event):
        user_intput = self.entry.get()
        if user_intput not in [t.cget('text') for t in self.task]:
            self.new_input = tk.Label(self)
            self.new_input.pack(side='top', fill='x')
            self.new_input.config(background='#95a5a6', height=2, text=user_intput)
            self.task.append(self.new_input)
                
        self.entry.delete(0, 'end')
        
if __name__ == '__main__':
    root = tk.Tk()
    root.wm_attributes('-topmost', 1)
    root.title('Mainwindow')
    root.geometry(newGeometry="566x355+966+0")
    Myframe(root)
    root.mainloop()