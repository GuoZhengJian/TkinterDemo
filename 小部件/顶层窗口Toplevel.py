# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 16:27:13 2020

@author: GuoZheng

E-mail : email@guozheng.online
"""

import tkinter as tk

class Top(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('顶层窗口Toplevel')
        self.iconbitmap(bitmap="E:\OneDrive\图片\图标\ooopic_1533975397.ico")
        self.geometry(newGeometry='450x325+-7+0')
        self.config(highlightcolor='#6495ED', highlightbackground='#F8F8FF', highlightthickness=2)
        
        # self.iconify()    # 最小化窗口
        # self.deiconify()  # 显示窗口
        self.resizable(width=False, height=True)
        self.grid(baseWidth=100, baseHeight=100, widthInc=500, heightInc=320)
        print("当前系统的字符串表示", self.frame())
        print("设置和获取焦点模式", self.focusmodel())
        print("设置和获取 wm_colormap_windows 颜色属性", self.colormapwindows())
        
        self.sizefrom(who='user')       # 指定窗口尺寸由“谁”决定
        self.positionfrom(who="user")   # 指定窗口位置由“谁”决定

        print(self.attributes()) # 设置和获取窗口属性
        self.attributes("-alpha", 0.8) # 控制窗口的透明度, 参数1-0
        self.attributes("-disabled",False) # 禁用整个窗口 参数True, False或1,0
        self.attributes("-fullscreen", False) # 全屏显示窗口, 参数True, False或1,0
        self.attributes("-toolwindow", True) # 采用工具窗口的样式, 参数True, False或1,0
        self.attributes("-topmost", True) # 将窗口永远置顶, 参数True, False或1,0
        self.overrideredirect(boolean=False) # 是否隐藏窗口的功能小部件 (功能小部件指的是 标题栏、边框等部件)

        def func_state():
            print('你确定要关闭这个窗口吗')         
        # self.protocol(name="WM_DELETE_WINDOW", func=func_state)  # 窗口被关闭的时候, 将回调函数 func 与相应的规则 name 绑定
        # self.protocol(name="WM_SAVE_YOURSELF", func=func_state)  # 窗口被保存的时候, 将回调函数 func 与相应的规则 name 绑定
        # self.protocol(name="WM_TAKE_FOCU", func=func_state)  # 窗口被保存的时候, 将回调函数 func 与相应的规则 name 绑定

        # 未知用法----------------------------------------------------------------------------------------------
        # self.group() #? 将窗口添加到窗口群中
        # self.iconwindow(pathName=None) #? 设置和获取当窗口图标化（最小化）时的组件窗口
        # self.iconposition(x=None, y=None) #? 设置和获取当窗口图标化（最小化）时的图标位置
        # self.transient() #?  指定为master的临时窗口
        # print(self.client()) #?  设置和获取wm_client_machine(客户机)属性, 如果要删除wm_client_machine属性，赋值为空字符串即可
        # print(self.command()) #? 设置和获取wm_command属性
        # print(self.iconmask(bitmap=None)) #? 设置和获取位图掩码
        

        
top = Top()
top.mainloop()
# top.update()