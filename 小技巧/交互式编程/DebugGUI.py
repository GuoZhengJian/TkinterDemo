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
        # threading.Thread(target=self.getposition, args=()).start()        

    @property
    def uptop(self):
        """
        实时刷新UI
        后端更改参数, 前端实时更新. 要实现这个方法需要以下思路:
            1) 在循环中使用reload重新加载前端UI模块
            2) 使用.destroy关闭已经加载的前端模块, 使Toplevel中始终只保留一个UI模块
    
        关于importlib.reload:
            在早期的py版本中提供了reload模块用于重新加载模块. 但py3完全删除了这一个功能,
        因为py的C/C++扩展无法以任何方式安全的卸载或重新加载模块. 如果你有类似的需求, 唯
        一的解决办法是重新启动python解释器进程
            通常不鼓励使用此模块, 除非用作调试辅助措施
        """
        try:
            import topwindow
        except:
            sys.path.append(os.path.dirname(os.path.abspath(__file__)))
            import topwindow
            
        while True:
            importlib.reload(topwindow)
            t = topwindow.TopWindow(self)
            t.update()
            time.sleep(1)
            t.destroy()

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