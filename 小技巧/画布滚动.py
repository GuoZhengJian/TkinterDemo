# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 10:25:01 2021

@author: 57207
"""

import tkinter as tk

class Mytest(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self['background'] = '#ffffff'
        self.place(relx=0, rely=0, relheight=1, relwidth=1)
        
        """
        流程比较复杂, 这里记录
        1) 创建一个画布Canvas
        2) 创建一个容器, 如Frame, 用于方式需要滚动的组件 (因为canvas_window只能放置一个部件)
        3) 创建一个画布窗口canvas_window, 并指定要放置的小工具
        4) 创建一个滚动条Scrollbar
        5) 绑定滚动条
    
        6) 创建一个event, 该event主要用于实时获取画布的可滚动区域, 并通过scrollregion()定义Canvas
        7) 绑定Frame容器对象的键盘事件bind
    
        8) 创建一个鼠标滑轮事件bind, 以实现滑轮滚动画布
        """
        # 1
        self.canvas = tk.Canvas(self, background='#1abc9c') #绿色
        self.canvas.pack(side='right', fill='both', expand=True)
        
        # 2
        self.frame = tk.Frame(self.canvas)

        # 3 (因为create_window没有布局管理属性, 所以当把self.frame放到create_window中是不会显示的, 所以frame也没必要使用布局管理)
        self.canvas.create_window(0, 0, anchor='nw', width=566, window=self.frame)
        
        # 4
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.pack(side='left', fill='y')

        # 5
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.canvas.yview)
        
        # 7
        self.frame.bind("<Configure>",self.region)
        
        # 8
        self.canvas.bind_all("<MouseWheel>", self.mousewheel)
        
        # 其他
        for i in range(20): tk.Label(self.frame, text=i, ).pack(side='top')
        
    # 6
    def region(self, event):
        # 获取画布Canvas的滚动区域, 注意: 是画布Canvas的滚动区域
        bbox = self.canvas.bbox('all')
        self.canvas.config(scrollregion=bbox)
    
    def mousewheel(self, event):
        scroll_int = 0
        if event.delta>0: scroll_int=-1 
        if event.delta<0: scroll_int= 1
        self.canvas.yview('scroll', scroll_int, 'units')
    
if __name__ == '__main__':
    root = tk.Tk()
    root.wm_attributes('-topmost', 1)
    root.title('Mainwindow')
    root.geometry(newGeometry="566x355+966+0")
    Mytest(root)
    root.mainloop()