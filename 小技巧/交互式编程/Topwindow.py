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
        
        self.inputframe = self.InputFrame()
        self.inputentry = self.InputEntry()
        self.panedwindow = self.OutputPanedWindow()
        
    def InputFrame(self):
        frame = tk.Frame(self)
        frame.config(background="#1464A0")
        frame.place(relx=0.0, rely=0.85, relheight=0.15, relwidth=1.0)
        return frame
        
    def InputEntry(self):
        entry = tk.Entry(self.inputframe)
        entry.config(background='#FFFFFF')
        entry.insert(0, 'print | 打印')
        entry.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        
    def OutputPanedWindow(self):
        paned = tk.PanedWindow(self)
        paned.config(background="#1464A0")
        paned.place(relx=0.0, rely=0.0, relheight=0.8, relwidth=1.0)



    
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
        try:
            import ConsumGUI
        except:
            sys.path.append(os.path.dirname(os.path.abspath(__file__)))
            import ConsumGUI
            
        m = ConsumGUI.Mainwindow()
        m.mainloop()
    
    # debuggui()
    consumgui()
    