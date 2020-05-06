import tkinter as tk


#窗口主体
window = tk.Tk()
window.title('仓库管理系统')
window.geometry('800x400')

item=tk.StringVar() #selected显示用
number=tk.StringVar() #数量显示用,StringVar类型
infomation=tk.StringVar() #infomation


#选择元器件和数量模块
selected = tk.Label(window,text='',bg='gray',width=15,height=1)
info = tk.Label(window,text='',bg='gray',width=60,height=5)
selected.pack()
info.pack()

def select():
    selected.config(text='已选择'+item.get()+' '+input_number.get()+'个')
#info
def seeinfo2070():
    info.config(text='NVIDIA GeForce RTX 2070必将是你的睿智之选。\n品牌保证严苛品质能够更好的带动和提升电脑的运行性能，\n严苛工艺打造高强度工作下的持久稳定性。')
def seeinfo2080():
    info.config(text='GeForce RTX™ 2080 借助全新 NVIDIA Turing™ 架构，\n带给您难以置信的游戏逼真度、画面渲染速度、更高的能效比以及身临其境的沉浸感，\n这是显卡技术的一次彻底革新。')
#以下为选项模块
RTX2080 = tk.Radiobutton(window, text ='RTX2080', variable = item, value='RTX2080',command=seeinfo2080())
RTX2080.pack()
RTX2070 = tk.Radiobutton(window, text ='RTX2070', variable = item, value='RTX2070',command=seeinfo2070())
RTX2070.pack()
#end
item.set('RTX2080') #设置默认选择为RTX2080
input_number = tk.Entry(window,show=None,textvariable=number)
input_number.pack()
input_number.insert(0,'1') #设置默认数量为1
cofirm = tk.Button(window,text='确定',command=select)
cofirm.pack()



#入库出库
enter = tk.Button(master=window, text='入库', width=15, height=1).pack(side='left')
export = tk.Button(master=window, text='出库',width=15, height=1).pack(side='right')



window.mainloop()