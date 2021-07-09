# -*- coding: utf-8 -*-
"""
@author: GuoZhengJian

E-mail : 572078547@QQ.COM
"""

import tkinter as tk
import sys, os

class TopWindow(tk.Frame):
    def __init__(self):
        super().__init__()
        self.config(background="#EC7600", height=200)
        self.pack(fill='both')
        
        
if __name__ == '__main__':
    try:
        import mainwindow
    except:
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        import mainwindow
        
    m = mainwindow.Mainwindow()
    m.mainloop()