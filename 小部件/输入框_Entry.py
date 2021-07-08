# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 09:08:45 2020

@author: GuoZheng

E-mail : email@guozheng.online
"""

import tkinter as tk

class Top(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Entry实现账号密码登陆')
        self.iconbitmap("E:\OneDrive\图片\图标\ooopic_1533975397.ico") 
        self.geometry(newGeometry='450x325+-7+0')
        self.config(highlightcolor='#6495ED', highlightbackground='#F8F8FF', highlightthickness=2)
        
        user_loging(self)

class user_loging(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.config(background='#0fffff')
        self.pack( fill='both', padx=1, pady=1, expand=True)
        padxsetting = 2
        padysetting = 2
        widthsetting = 50
        
        tk.Label(self, text='用户', width=10).grid(padx=padxsetting, pady=padysetting, row=0, column=0)
        tk.Label(self, text='密码', width=10).grid(padx=padxsetting, pady=padysetting, row=1, column=0)
        tk.Label(self, text='其他', width=10).grid(padx=padxsetting, pady=padysetting, row=2, column=0)

        # 用户名输入
        self.user = tk.Entry(self)
        self.user.config(state='normal') #参数[disabled, normal, or readonly]
        self.user.config(insertbackground='#DC143C', #红色
                         selectbackground='#5F9EA0', #绿色
                         selectforeground='#DAA520', #黄色
                         disabledbackground='#000000', #黑色
                         disabledforeground='#DC143C') #红色
        self.user.config(width=widthsetting,
                          insertwidth=10, 
                          insertborderwidth=10,
                          selectborderwidth=10)
        self.user.config(exportselection=1)
        #--------------------------------------------------------------------
        # validate, validatecommand(vcmd), invalidcommand(invcmd)参数使用教程
        def validate_len():
            if len(self.user.get())>3:
                print('输入内容符合规范')
                return True
            else:
                print('错误! 输入内容不符合规范')
                self.user.delete(0, 'end')
                return False
        def validate_false():
            self.toplevel = tk.Toplevel(self)
            self.label = tk.Label(self.toplevel, text='错误! 输入内容不符合规范').pack()
            self.toplevel.pack()
        self.user.config(validate='focusout', validatecommand=validate_len, invalidcommand=validate_false) 
        # self.user.config(validate='focusout', vcmd=validate_len, invcmd=validate_false) 
        #--------------------------------------------------------------------


        # xscrollcommand) #文本超过控件宽度后启动滚动条 (与scrollbar(滚动条)组件相关联, 使用方法参考与scrollbar)
        self.user.grid(padx=padxsetting, pady=padysetting, row=0, column=1)
        
        # -------------------------------------------------------------------
        self.user.insert(0, '请输入用户名称')
        self.user.insert(5, '(账户)')
        self.user.insert('end', ',谢谢')
        self.user.focus_set() 
        self.user.icursor(5) # 需要与self.user.focus_set()一起使用
        print(self.user.index('end'), 'index')  
        print(self.user.xview('end'), 'xview')
        self.user.selection_adjust("end")
        print(self.user.selection_present())
        # self.user.selection_from(5) #?
        self.user.selection_range(2,80)
        self.user.selection_to(6)
        
        # -------------------------------------------------------------------
        
        
        # 密码输入
        self.password = tk.Entry(self, width=widthsetting)
        self.password.config(show='*')
        self.password.grid(padx=padxsetting, pady=padysetting, row=1, column=1)
        
        # 其他输入
        self.other = tk.Entry(self, width=widthsetting)
        self.other.grid(padx=padxsetting, pady=padysetting, row=2, column=1)
        
        # 点击注册并打印输入内容
        self.button = tk.Button(self, text='点击注册')
        self.button.config(width=50, command=self.delete_entry_str)
        self.button.grid(padx=padxsetting, pady=padysetting, row=3, column=1)
        
        # 退出当前Frame框架
        self.quit = tk.Button(self, text='退出')
        self.quit.config(width=10, command=self.destroy)
        self.quit.grid(padx=padxsetting, pady=padysetting, row=3, column=0, sticky='w')
        
    # 获取当前输入的值  
    def get_entry_str(self):
        print('用户:', self.user.get(),
              '密码:', self.password.get(),
              '其他:', self.other.get(),)
    
    # 清空当前输入的值
    def delete_entry_str(self):
        print('用户:', self.user.delete(0, 'end'),
              '密码:', self.password.delete(0, 'end'),
              '其他:', self.other.delete(0, 'end'),)
        


top = Top()
top.mainloop()
# top.update()

