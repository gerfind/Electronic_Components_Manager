import tkinter as tk
from tkinter import messagebox

# 有些代码写的挺屎的，能用就行（安详），如果有更好的实现可以替换


class Electronic_Components(tk.Radiobutton):
    number = 50  # 继承一个类，多了个number属性
    price = 0  # 继承，增加price属性，默认值0，需要额外一行赋值


# 窗口主体
window = tk.Tk()
window.title('仓库管理系统')
window.geometry('800x400')

item = tk.StringVar()  # selected显示用
number = tk.StringVar()  # 数量显示用,StringVar类型
infomation = tk.StringVar()  # infomation


# 选择元器件和数量模块
selected = tk.Label(window, text='', bg='gray', width=30, height=1)
info = tk.Label(window, text='', bg='gray', width=60, height=5)
selected.pack()
info.pack()


def select():
    if item.get() == 'RTX2070':
        selected.config(text='已选择'+item.get()+' ' +
                        input_number.get()+'个'+'，库存为'+str(RTX2070.number))
        info.config(
            text='NVIDIA GeForce RTX 2070必将是你的睿智之选。\n品牌保证严苛品质能够更好的带动和提升电脑的运行性能，\n严苛工艺打造高强度工作下的持久稳定性。')
    elif item.get() == 'RTX2080':
        selected.config(text='已选择'+item.get()+' ' +
                        input_number.get()+'个'+'，库存为'+str(RTX2080.number))
        info.config(
            text='GeForce RTX™ 2080 借助全新 NVIDIA Turing™ 架构，\n带给您难以置信的游戏逼真度、画面渲染速度、更高的能效比以及身临其境的沉浸感，\n这是显卡技术的一次彻底革新。')


# 以下为选项模块
RTX2080 = Electronic_Components(window, text='RTX2080',
                                variable=item, value='RTX2080')
RTX2080.price = 5399
RTX2080.pack()
RTX2070 = Electronic_Components(window, text='RTX2070',
                                variable=item, value='RTX2070')
RTX2070.price = 3099
RTX2070.pack()
# 以上为选项模块，可继续增加，使用框架进行分类即可BV1jW411Y7dL -- P10
item.set('RTX2080')  # 设置默认选择为RTX2080
input_number = tk.Entry(window, show=None, textvariable=number)
input_number.pack()
input_number.insert(0, '1')  # 设置默认数量为1
cofirm = tk.Button(window, text='确定当前选择的器件和数量', command=select)
cofirm.pack()

# 库存系统


def add():
    if item.get() == 'RTX2080':
        RTX2080.number += int(input_number.get())
        messagebox.showinfo(title='提示', message='已经成功入库' +
                            item.get()+input_number.get()+'个')
    elif item.get() == 'RTX2070':
        RTX2070.number += int(input_number.get())
        messagebox.showinfo(title='提示', message='已经成功入库' +
                            item.get()+input_number.get()+'个')


def minus():
    if item.get() == 'RTX2080':
        RTX2080.number -= int(input_number.get())
        messagebox.showinfo(title='提示', message='已经成功出库' +
                            item.get()+input_number.get()+'个')
    elif item.get() == 'RTX2070':
        RTX2070.number -= int(input_number.get())
        messagebox.showinfo(title='提示', message='已经成功出库' +
                            item.get()+input_number.get()+'个')

# 报警系统

# 统计系统，可能需要import datetime


# 入库出库
enter = tk.Button(master=window, text='入库', width=15,
                  height=1, command=add).pack(side='left')
export = tk.Button(master=window, text='出库', width=15,
                   height=1, command=minus).pack(side='right')

window.mainloop()
