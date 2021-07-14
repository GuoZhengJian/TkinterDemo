# -*- coding: utf-8 -*-
"""
@author: GuoZhengJian

E-mail : 572078547@QQ.COM
"""

import tkinter as tk
import sys, os

#asdasd
class TopWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.config(background="#EC7600")
        self.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        
        self.F1 = self.addFrame1()
        self.F2 = self.addFrame2()
        
    def addFrame1(self):
        f1 = tk.Frame(self)
        f1.config(background='#1464A0')
        f1.place(relx=0.0, rely=0.0, relheight=0.8, relwidth=0.8)
        return f1
        
    def addFrame2(self):
        f2 = tk.Frame(self.F1)
        f2.config(background='#32414B')
        f2.place(relx=0.0, rely=0.0, relheight=0.6, relwidth=0.6)
        return f2
        
        
if __name__ == '__main__':
    try:
        import mainwindow
    except:
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        import mainwindow
        
    m = mainwindow.Mainwindow()
    m.mainloop()