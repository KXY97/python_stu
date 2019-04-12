#!/usr/bin/python
#-*- coding:utf-8 -*-
from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
def closewindow():
    # 设置提示信息
    messagebox.showinfo(title='哈哈哈哈',message='关不掉吧')
    # 关闭窗口
    # window.destroy()
    return
def love():
    # 创建一个顶级窗口，依赖原始窗口存在
    love = Toplevel(window)
    love.title('太好了')
    love.mainloop()

# 创建一个窗口
window = Tk()
# 命名窗口的标题
window.title('hello啊')
# 设置窗口大小# 设置窗口的位置
window.geometry('500x500+500+100')
# 当用户关闭窗口是时触发
window.protocol('WM_DELETE_WINDOW',closewindow)
# 添加文本标签
label = Label(window,text='o3o o3o o3o',font=('宋体',20))
# 显示标签
label.grid(row=0,column=0,sticky=W)
# # 添加图片控件
# imag = PhotoImage(file='11.png')
# image = Label(window,image=imag)
# image.grid(row=2,columnspan=2)
photo = Image.open('11.png')
phot = ImageTk.PhotoImage(photo)
pho = Label(window,image=phot)
pho.grid(row=2,columnspan=2)
# 添加一个按钮
botten = Button(window,text='同意',width=10,height=3,command=love)
botten.grid(row=2,column=0,sticky=W)
# 显示窗口
window.mainloop()

