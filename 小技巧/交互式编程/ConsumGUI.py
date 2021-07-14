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
        self.uptop()
        
        # threading.Thread(target=self.getposition, args=()).start()        

    def uptop(self):
        try:
            import topwindow
        except:
            sys.path.append(os.path.dirname(os.path.abspath(__file__)))
            import topwindow

        t = topwindow.TopWindow(self)
        t.update()

    @property
    def getposition(self):
        """
        实时获取参数
        不同于实时刷新UI, 获取参数只需要.update()刷新当前实例对象的属性即可
        """
        while True:
            print(self.geometry())
            self.update()
            time.sleep(1)
        
if __name__ == '__main__':        
    m = Mainwindow()
    m.mainloop()