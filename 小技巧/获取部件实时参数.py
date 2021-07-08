# -*- coding: utf-8 -*-
"""
@author: GuoZhengJian

E-mail : 572078547@QQ.COM
"""

import tkinter as tk
import time
import threading

class Top(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('实时获取小部件参数')
        self.geometry("%sx%s+%s+%s"%(int(self.winfo_screenheight()/2),
                                     int(self.winfo_screenwidth()/2),
                                     1, 1))
        
        # 用一个子线程来获取参数, 这样主进程的小部件不会卡
        threading.Thread(target=Getconfig().getConfig, args=(self,)).start()
        
        
        
class Getconfig():
    def __init__(self):
        pass
    
    def getConfig(self, master):
        while True:
            print(master.geometry())
            print(master.winfo_screenmmheight(), master.winfo_screenmmwidth())
            print(master.winfo_screenheight(), master.winfo_screenwidth())
            master.update()
            time.sleep(0.1)
        
if __name__ == '__main__':
    t = Top()
    t.mainloop()