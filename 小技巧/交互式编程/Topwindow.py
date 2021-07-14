# -*- coding: utf-8 -*-
"""
@author: GuoZhengJian

E-mail : 572078547@QQ.COM
"""

import tkinter as tk
import sys, os

class TopWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.config(background="#EC7600")
        self.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        
        self.frame1 = self.Frame1()
        self.frame2 = self.Frame2()
        self.frame3 = self.Frame3()
        
    def Frame1(self):
        f = tk.Frame(self)
        f.config(background="#19232D")
        f.place(relx=0.0, rely=0.0, relheight=0.9, relwidth=0.9)
        return f
    
    def Frame2(self):
        f = tk.Frame(self.frame1)
        f.config(background="#1464A0")
        f.place(relx=0.1, rely=0.1, relheight=0.9, relwidth=0.9)
        return f
        
    def Frame3(self):
        f = tk.Frame(self.frame2)
        f.config(background="#FFFFFF")
        f.place(relx=0.0, rely=0.0, relheight=0.9, relwidth=0.9)
        return f
    
if __name__ == '__main__':
    def debuggui():
        try:
            import DebugGUI
        except:
            sys.path.append(os.path.dirname(os.path.abspath(__file__)))
            import DebugGUI
        m = DebugGUI.Mainwindow()
        m.mainloop()
        
    def consumgui():
        root = tk.Tk()
        root.wm_attributes('-topmost', 1)
        root.title('Mainwindow')
        root.geometry(newGeometry="566x355+966+0")
        TopWindow(root)
        root.mainloop()
    
    debuggui()
    # consumgui()
    