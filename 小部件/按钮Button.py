# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 16:25:05 2020

@author: GuoZheng

E-mail : email@guozheng.online
"""

import tkinter as tk

class Top(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Button, Checkbutton, Menubutton, Radiobutton')
        self.iconbitmap("E:\OneDrive\图片\图标\ooopic_1533975397.ico") 
        self.geometry(newGeometry='450x325+-7+0')
        self.config(highlightcolor='#6495ED', highlightbackground='#F8F8FF', highlightthickness=2)
        
        # Widget_Button(self)
        # Widget_checkbutton(self)
        # Widget_radiobutton(self)
        Widget_menubutton(self)
        
class Widget_Button(tk.Frame):
    """
    Tkiner Variable 类教程: https://tkdocs.com/shipman/control-variables.html
    """
    def __init__(self, root):
        super().__init__(root)
        self.config(background='#0fffff')
        self.pack(fill='both', padx=1, pady=1, expand=True)
        
        self.var = tk.StringVar()
        width_len = len(self.var.get())
     
        self.label = tk.Label(self,  width=width_len, textvariable=self.var)
        self.label.pack()
    
        self.entry = tk.Entry(self, textvariable=self.var)
        self.entry.pack(fill='x')
        
        # Button--------------------------------------------------------------
        import time        
        def label_variable():
            for i in range(10):
                time.sleep(0.1) # 注意: 如果循环变换的间隔时间为0, 那么文本就不会变化, 也就是假状的卡死状态
                self.var.set('开始计时%s秒'%i)
                self.label.update()
                print("get()返回值:", self.var.get())
            
        self.button = tk.Button(self, text='开始计时', command=label_variable,)
        self.button.config(bitmap='info', compound='left')
        self.button.pack(fill='x')
        
        def flash_state():
            self.button.config(activebackground="#0000FF", disabledforeground="#FF00FF")
            self.button.flash()
            
        def invoke_state():
            print("invoke()返回值:", self.button.invoke())
            
        tk.Button(self, text='flash(), 状态重绘', command=flash_state).pack(fill='x')
        tk.Button(self, text='invoke()', command=invoke_state).pack(fill='x')
        
 
        from PIL import Image, ImageTk
        """
        注意!!! image 和 imageobj 必须是初始化参数, 也就是必须加上self, 
        如: self.image, self.imageobj, 否则会报错: 图像“ pyimage”不存在!
        (如果图像参数不是初始化参数, 那么只能在每次重启IDE时才能加载出来)
        """
        self.image = Image.open('E:\OneDrive\图片\图标\雪山丛林.jpg')
        self.imageobj = ImageTk.PhotoImage(self.image)
        self.label_image = tk.Label(self, text='asdasd', image=self.imageobj, compound='left')
        self.label_image.pack()
        
class Widget_checkbutton(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.config(background='#0fffff')
        self.pack(fill='both', padx=1, pady=1, expand=True)
        
        self.strvar = tk.StringVar()
        
        width_len = len(self.strvar.get())
        self.label = tk.Label(self,  width=width_len, textvariable=self.strvar)
        self.label.pack()
    
        self.entry = tk.Entry(self, textvariable=self.strvar)
        self.entry.pack(fill='x')
        
        # Checkbutton---------------------------------------------------------
        def get_1():
            print(self.intvar_1.get())
        
        def get_2():
            print(self.strval_2.get())
            
        self.intvar_1 = tk.IntVar()
        self.Checkbutton_1 = tk.Checkbutton(self, text='Checkbutton_1')
        self.Checkbutton_1.config(variable=self.intvar_1, command=get_1)
        self.Checkbutton_1.pack(fill='x')
        self.intvar_1.set(1)
        self.Checkbutton_1.config(indicatoron=False)

        self.strval_2 = tk.StringVar()
        self.Checkbutton_2 = tk.Checkbutton(self, text='Checkbutton_2')
        self.Checkbutton_2.config(variable=self.strval_2, onvalue='YES', offvalue='NO', command=get_2)
        self.Checkbutton_2.pack(fill='x')
        self.strval_2.set("YES")
        self.Checkbutton_2.config(indicatoron=False, offrelief='ridge')
        self.Checkbutton_2.toggle()
        
class Widget_radiobutton(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.config(background='#0fffff')
        self.pack(fill='both', padx=1, pady=1, expand=True)
        
        self.strvar = tk.StringVar()
        
        width_len = len(self.strvar.get())
        self.label = tk.Label(self,  width=width_len, textvariable=self.strvar)
        self.label.pack()
    
        self.entry = tk.Entry(self, textvariable=self.strvar)
        self.entry.pack(fill='x')
        
        # Radiobutton---------------------------------------------------------
        self.intvar = tk.IntVar()
        
        def get_intvar():
            print(self.intvar.get())
        
        self.Radiobutton_1 = tk.Radiobutton(self, text='Radiobutton_1')
        self.Radiobutton_1.config(variable=self.intvar, value=2, command=get_intvar)
        self.Radiobutton_1.pack(fill='x')
        
        self.Radiobutton_2 = tk.Radiobutton(self, text='Radiobutton_2')
        self.Radiobutton_2.config(variable=self.intvar, value=4, command=get_intvar)
        self.Radiobutton_2.pack(fill='x')
        
        self.Radiobutton_3 = tk.Radiobutton(self, text='Radiobutton_3')
        self.Radiobutton_3.config(variable=self.intvar, value=6, command=get_intvar)
        self.Radiobutton_3.pack(fill='x')
        
        self.Radiobutton_1.select()
        
        self.Radiobutton_1.config(indicatoron=False)
        self.Radiobutton_2.config(indicatoron=False)
        self.Radiobutton_3.config(indicatoron=False)
        
class Widget_menubutton(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.config(background='#0fffff')
        self.pack(fill='both', padx=1, pady=1, expand=True)
        
        self.strvar = tk.StringVar()
        
        width_len = len(self.strvar.get())
        self.label = tk.Label(self,  width=width_len, textvariable=self.strvar)
        self.label.pack()
    
        self.entry = tk.Entry(self, textvariable=self.strvar)
        self.entry.pack(fill='x')
        
        # Menubutton---------------------------------------------------------
        def check_return():
            print("程序已经打开")
            
        self.menubutton = tk.Menubutton(self, text='下拉菜单')
        self.menubutton.pack(fill='x')
        
        self.menu = tk.Menu(self.menubutton)
        self.menu.add_checkbutton(label='打开', command=check_return)
        self.menu.add_command(label='退出', command=check_return)
        
        self.menubutton.config(menu=self.menu)


top = Top()
top.mainloop()
# top.update()