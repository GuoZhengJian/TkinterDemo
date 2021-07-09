# -*- coding: utf-8 -*-
"""
@author: GuoZhengJian

E-mail : 572078547@QQ.COM
"""

import tkinter as tk
import threading
import time
import importlib
import sys, os

class Mainwindow(tk.Tk):
    """
    当mainwindow.py运行后, 在topwindow.py内更改部件参数并保存(不是运行, 是Ctrl+W保存),
    即可看到UI的实时变化.
    
    或者你可以直接在topwindow.py内更改部件参数并运行, 即可看到UI的实时变化.
    """
    def __init__(self):
        super().__init__()
        self.wm_attributes('-topmost', 1)
        self.title('Mainwindow')
        self.geometry(newGeometry="566x355+966+0")
        threading.Thread(target=self.uptop, args=()).start()
        
    @property
    def uptop(self):
        try:
            import topwindow
        except:
            sys.path.append(os.path.dirname(os.path.abspath(__file__)))
            import topwindow
            
        while True:
            importlib.reload(topwindow)
            t = topwindow.TopWindow(self)
            t.update()
            time.sleep(0.5)
            t.destroy()

        
if __name__ == '__main__':        
    m = Mainwindow()
    m.mainloop()