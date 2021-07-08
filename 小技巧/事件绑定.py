# -*- coding: utf-8 -*-
"""
@author: GuoZhengJian

E-mail : 572078547@QQ.COM
"""

import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('PYDict')
        self.geometry(newGeometry="500x500+1+1")
        self.config(background="#19232D")
        self.bind('<Control-KeyPress-w>', self.closewindow)
        self.bind('<Control-KeyPress-f>', self.createframe)

    def closewindow(self, event):
        self.destroy()
        
    def createframe(self, event):
        tk.Frame(self, background='#26579B', height=50).pack(side='bottom', fill='x')

if __name__ == '__main__':
    m = MainWindow()
    m.mainloop()
    
    