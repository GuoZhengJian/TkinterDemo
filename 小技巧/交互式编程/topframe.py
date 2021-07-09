# -*- coding: utf-8 -*-
"""
@author: GuoZhengJian

E-mail : 572078547@QQ.COM
"""

import tkinter as tk
        
class Topframe2(tk.Frame):
    def __init__(self, master=None):
        super().__init__()
        self.config(background='#AD4A4A', height=100)
        self.pack(fill='both')
               
if __name__ == '__main__':
    try:
        import main
    except:
        import sys, os
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        import main
        
    m = main.Mainwindow()
    m.mainloop()