# -*- coding: utf-8 -*-
"""
@author: GuoZhengJian

E-mail : 572078547@QQ.COM
"""
import tkinter as tk
import threading
import importlib
import time

class Mainwindow(tk.Tk):
    """
    当main.py运行后, 在Topwindow.py内更改部件参数并保存(不是运行, 是Ctrl+W保存),
    即可看到UI的实时变化
    """
    def __init__(self):
        super().__init__()
        self.wm_attributes('-topmost',1)
        self.geometry(newGeometry="566x355+963+27")
        threading.Thread(target=self.upTop, args=()).start()
        
    @property
    def upTop(self):
        try:
            import Topwindow
        except:
            import sys, os
            sys.path.append(os.path.dirname(os.path.abspath(__file__)))
            import Topwindow
            
        while True:
            # 重新载入Topwindow模块
            importlib.reload(Topwindow)
            t = Topwindow.Top()
            t.update()
            time.sleep(0.2)
            t.destroy()
            

if __name__ == '__main__':
    m = Mainwindow()
    m.mainloop()