# -*- coding: utf-8 -*-
"""
@author: GuoZhengJian

E-mail : 572078547@QQ.COM
"""
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import tkinter as tk
import threading
import importlib
import time

class Mainwindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry(newGeometry="566x355+963+27")
        threading.Thread(target=self.upTop, args=()).start()
        
    @property
    def upTop(self):
        try:
            import topframe
        except:
            import sys, os
            sys.path.append(os.path.dirname(os.path.abspath(__file__)))
            import topframe
            
        while True:
            importlib.reload(topframe)
            t = topframe.Topframe2()
            t.update()
            time.sleep(0.2)
            t.destroy()