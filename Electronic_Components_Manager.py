# 实现简单的图形化界面，进行电子元件的出入库管理
import tkinter as tk
from tkinter import messagebox
import traceback
import datetime
from pathlib import Path
import tkinter


image1 = None
image_file = None


class ElectronicComponents(tk.Radiobutton):
    """电子元器件类"""
    number = 50  # 继承一个类，多了个number属性
    price = 0  # 继承，增加price属性，默认值0，需要额外一行赋值
    name = ""
    instances = []

    def instance_append(self):
        """在类中添加实例的信息"""
        self.__class__.instances.append(self)
        (filename, line_number, function_name,
         txt) = traceback.extract_stack()[-2]
        self.name = txt[:txt.find('.')].strip()  # 实例的名称

    @classmethod
    def set_alarm_info(cls, warn_text):
        """设置报警信息"""
        count = 0
        for instance in cls.instances:
            if instance.number <= 4:
                count += 1
                warn_text += instance.name + "库存不足5件\n"
        if count:
            warn_text += "请尽快补货。"
        warn_info.set(warn_text)


# 窗口主体
window = tk.Tk()
window.title('仓库管理系统')
window.geometry('960x600')

# 画板主体
canvas = tk.Canvas(window, bg='lightgrey', height=210, width=500)



whole_info = tk.StringVar()  # 按类型查看所有相关元件的标签中的文字
item = tk.StringVar()  # selected显示用
number = tk.StringVar()  # 数量显示用,StringVar类型
infomation = tk.StringVar()  # infomation
warn_info = tk.StringVar()  # 报警信息
value_depot = tk.StringVar()  # 在库元件价值
export_month_str = tk.StringVar()  # 月出库元件总价值
month_consume = tk.StringVar()  # 各类元器件的月消耗量(出库量-入库量)
month_choose = tk.StringVar()  # 选择月份

# 元器件列表
cpu_list = ["Core_i7_9700F", "Core_i9_9980XE",
            "Ryzen_9_3900X", "Ryzen_Threadripper_3990X"]
gra_list = ["RTX_2070", "RTX_2080", "TITAN_RTX", "RX_5700XT"]
scr_list = ["", "", "", ""]
mem_list = ["", "", "", ""]
list = ["RTX_2080", "RTX_2070", "TITAN_RTX", "RX_5700XT", "Core_i7_9700F",
        "Core_i9_9980XE", "Ryzen_9_3900X", "Ryzen_Threadripper_3990X"]

# 选择元器件和数量模块
selected = tk.Label(window, text='', font=('Arial', 12), bg='lightgray',
                    fg='FireBrick', width=54, height=1, relief="ridge", borderwidth=5)
info = tk.Label(window, text='', bg='lightgray', width=70, height=5)
selected.place(x=25, y=25)          # 选择显示位置
info.place(x=25, y=65)          # 简介显示位置


def select():
    """选择与显示"""
    if item.get() == 'RTX_2070':
        RTX2070_image()
        selected.config(text='已选择'+item.get()+' ' +
                        input_number.get()+'个'+'，库存为'+str(RTX_2070.number))
        info.config(
            text='NVIDIA GeForce RTX™ 2070必将是你的睿智之选。\n品牌保证严苛品质能够更好的带动和提升电脑的运行性能，\n严苛工艺打造高强度工作下的持久稳定性。\n')
    elif item.get() == 'RTX_2080':
        RTX2080_image()
        selected.config(text='已选择'+item.get()+' ' +
                        input_number.get()+'个'+'，库存为'+str(RTX_2080.number))
        info.config(
            text='NVIDIA GeForce RTX™ 2080 借助全新 NVIDIA Turing™ 架构，\n带给您难以置信的游戏逼真度、画面渲染速度、更高的能效比以及身临其境的沉浸感，\n这是显卡技术的一次彻底革新。')
    elif item.get() == 'TITAN_RTX':
        TITAN_RTX_image()
        selected.config(text='已选择'+item.get()+' ' +
                        input_number.get()+'个'+'，库存为'+str(TITAN_RTX.number))
        info.config(
            text='NVIDIA TITAN RTX™ 是运行速度超快的 PC 显卡，\n借助屡获殊荣的 Turing™ 架构，给您的 PC 配备 130 Tensor TFLOPs 的性能、\n576 个 Tensor 核心，以及 24 GB 的高速 GDDR6 显存 。')
    elif item.get() == 'RX_5700XT':
        AMD_5700XT_image()
        selected.config(text='已选择'+item.get()+' ' +
                        input_number.get()+'个'+'，库存为'+str(RX_5700XT.number))
        info.config(
            text='RX_5700XT 打破陈规，新的RDNA注入 Radeon RX 5700XT，\n带给你优秀性能和生动逼真的游戏体验，助你掌控全局，体验属于你的强大。')
    elif item.get() == 'Core_i7_9700F':
        i7_image()
        selected.config(text='已选择'+item.get()+' ' +
                        input_number.get()+'个'+'，库存为'+str(Core_i7_9700F.number))
        info.config(
            text='Core i7-9700F處理器屬於後來推出取消內顯的產品,\n運算核心數相對增加，採用14nm製程，\n插槽類型為LGA 1151型，支援2通道DDR4 2666MHz記憶體')
    elif item.get() == 'Ryzen_9_3900X':
        AMD_3900X_image()
        selected.config(text='已选择'+item.get()+' ' +
                        input_number.get()+'个'+'，库存为'+str(Ryzen_9_3900X.number))
        info.config(
            text='AMD 锐龙 9 3900X, 专注性能 为赢而生\n拥有 12 个内核的先进处理器1，为游戏发烧友倾心打造。')
    elif item.get() == 'Ryzen_Threadripper_3990X':
        AMD_3990X_image()
        selected.config(text='已选择'+item.get()+' ' +
                        input_number.get()+'个'+'，库存为'+str(Ryzen_Threadripper_3990X.number))
        info.config(
            text='Ryzen_Threadripper_3990X, 采用64核心、128线程设计，\n基础频率为2.9GHz，最大加速频率高达4.3GHz，\n性能极其强悍，是内容创作者和电脑发烧友们的尖端装备。')
    elif item.get() == 'Core_i9_9980XE':
        i9_image()
        selected.config(text='已选择'+item.get()+' ' +
                        input_number.get()+'个'+'，库存为'+str(Core_i9_9980XE.number))
        info.config(
            text='Core_i9_9980XE, 拥有18核心、36线程，\n采用14nm工艺，升级钎焊，睿频可达单核4.5GHz，\n是畅快游戏和创意实现的坚强后盾')


# 初始化元器件剩余库存
num = [50, 50, 50, 50, 50, 50, 50, 50]
emp = []
my_file = Path("logs.ecm")
if my_file.exists():
    with open("logs.ecm", "r") as f:
        a = reversed(f.readlines())
    for line in a:
        pro = line.split()[1]
        for i in range(len(num)):
            if list[i] == pro and i not in emp:
                num[i] = int(line.split()[-1])
                emp.append(i)
            if len(emp) == len(num):
                break

# 以下为选项模块，可继续增加，使用框架进行分类即可
RTX_2080 = ElectronicComponents(
    window, text='RTX_2080', variable=item, value='RTX_2080')
RTX_2080.price = 5399
RTX_2080.number = num[0]
RTX_2080.instance_append()  # 在类中添加实例的信息
RTX_2080.place(x=800, y=25)          # 选项位置

RTX_2070 = ElectronicComponents(
    window, text='RTX_2070', variable=item, value='RTX_2070')
RTX_2070.price = 3099
RTX_2070.number = num[1]
RTX_2070.instance_append()
RTX_2070.place(x=800, y=55)          # 选项位置

TITAN_RTX = ElectronicComponents(
    window, text='TITAN_RTX', variable=item, value='TITAN_RTX')
TITAN_RTX.price = 21999
TITAN_RTX.number = num[2]
TITAN_RTX.instance_append()
TITAN_RTX.place(x=800, y=85)          # 选项位置

RX_5700XT = ElectronicComponents(
    window, text='RX_5700XT', variable=item, value='RX_5700XT')
RX_5700XT.price = 2999
RX_5700XT.number = num[3]
RX_5700XT.instance_append()
RX_5700XT.place(x=800, y=115)          # 选项位置

Core_i7_9700F = ElectronicComponents(
    window, text='Core_i7_9700F', variable=item, value='Core_i7_9700F')
Core_i7_9700F.price = 4099
Core_i7_9700F.number = num[4]
Core_i7_9700F.instance_append()
Core_i7_9700F.place(x=600, y=25)         # 选项位置

Core_i9_9980XE = ElectronicComponents(
    window, text='Core_i9_9980XE', variable=item, value='Core_i9_9980XE')
Core_i9_9980XE.price = 15999
Core_i9_9980XE.number = num[5]
Core_i9_9980XE.instance_append()
Core_i9_9980XE.place(x=600, y=55)          # 选项位置

Ryzen_9_3900X = ElectronicComponents(
    window, text='Ryzen_9_3900X', variable=item, value='Ryzen_9_3900X')
Ryzen_9_3900X.price = 3999
Ryzen_9_3900X.number = num[6]
Ryzen_9_3900X.instance_append()
Ryzen_9_3900X.place(x=600, y=85)          # 选项位置

Ryzen_Threadripper_3990X = ElectronicComponents(
    window, text='Ryzen_Threadripper_3990X', variable=item, value='Ryzen_Threadripper_3990X')
Ryzen_Threadripper_3990X.price = 29999
Ryzen_Threadripper_3990X.number = num[7]
Ryzen_Threadripper_3990X.instance_append()
Ryzen_Threadripper_3990X.place(x=600, y=115)          # 选项位置

item.set('RTX_2080')  # 设置默认选择为RTX_2080
input_number = tk.Entry(window, show=None, textvariable=number)
input_number.place(x=600, y=205, width=175)         # 出入库数量输入框位置
input_number.insert(0, '1')  # 设置默认数量为1
cofirm = tk.Button(window, text='确定当前选择的器件和数量', command=select)
cofirm.place(x=600, y=165, width=175)          # 确认选择按钮位置


# 库存系统
def add():
    """入库"""
    ins = input_number.get()
    try:
        # 输入的数据不是正整数
        if int(ins) <= 0:
            messagebox.showinfo(title='提示', message='请确认输入的数据是正整数。')
        # 成功入库
        else:
            eval(item.get()).number += int(ins)
            import_time(item.get(), int(ins), eval(item.get()).number)
            messagebox.showinfo(title='提示', message='已经成功入库 ' +
                                                    item.get() + ' ' + input_number.get() + '个')
    # 数据不合法
    except ValueError:
        messagebox.showinfo(title='提示', message='请输入合法数据。')

    ElectronicComponents.set_alarm_info("")
    select()


def minus():
    """出库"""
    out = input_number.get()

    try:
        # 出库数量超过库存数量
        if int(out) > eval(item.get()).number:
            messagebox.showinfo(title='提示', message='出库数量超过库存数量，请确认后重新输入。')
        # 输入的数据不是正整数
        elif int(out) <= 0:
            messagebox.showinfo(title='提示', message='请确认输入的数据是正整数。')
        # 成功出库
        else:
            eval(item.get()).number -= int(out)
            export_time(item.get(), int(out), eval(item.get()).number)
            messagebox.showinfo(title='提示', message='已经成功出库 ' +
                                                    item.get() + ' ' + input_number.get()+'个')
    # 数据不合法
    except ValueError:
        messagebox.showinfo(title='提示', message='请输入合法数据。')

    ElectronicComponents.set_alarm_info("")
    select()


# 报警系统
warn = tk.Label(window, textvariable=warn_info, fg='Red')
warn.place(x=25, y=175)           # 警告出现位置


# 按照不同类型查看相关元器件
def gra_info():
    """查看所有显卡信息"""
    global whole_info  # 按类型查看所有相关元件的标签中的文字
    whole_info_str = ""
    for component in gra_list:
        whole_info_str = whole_info_str + component + \
            " 库存为： " + str(eval(component).number) + " 个。\n"
    whole_info.set(whole_info_str)


def cpu_info():
    """查看所有CPU信息"""
    global whole_info  # 按类型查看所有相关元件的标签中的文字
    whole_info_str = ""
    for component in cpu_list:
        whole_info_str = whole_info_str + component + \
            " 库存为： " + str(eval(component).number) + " 个。\n"
    whole_info.set(whole_info_str)


gra_button = tk.Button(window, text="查看所有显卡信息", command=gra_info)
gra_button.place(x=600, y=245)          # 查看显卡信息按钮位置
cpu_button = tk.Button(window, text="查看所有CPU信息", command=cpu_info)
cpu_button.place(x=800, y=245)          # 查看CPU信息按钮位置
info_label = tk.Label(window, textvariable=whole_info)
info_label.place(x=600, y=285)          # 全部信息显示位置

# 统计系统


def depot_value():
    """在库元器件总价值"""
    global value_depot
    value_depot_str = ""
    value_whole = 0
    for component in cpu_list + gra_list:
        value_whole += eval(component).price * eval(component).number
    value_depot_str = "在库元器件总价值为 ：" + str(value_whole) + "元。\n"
    value_depot.set(value_depot_str)


value_depot_button = tk.Button(window, text="查看在库元器件总价值", command=depot_value)
value_depot_button.place(x=600, y=385)          # 总价值按钮位置
value_depot_label = tk.Label(window, textvariable=value_depot)
value_depot_label.place(x=600, y=420)          # 价值显示位置


# 记录入库时间
def import_time(str1, quantity, rest):
    file1 = open("logs.ecm", "a", 1)
    im_time = datetime.datetime.now()
    file1.write("I: "+str1+"  "+str(quantity)+"  " +
                datetime.datetime.ctime(im_time)+" "+str(rest)+"\n")
    file1.close()

# 记录出库时间


def export_time(str1, quantity, rest):
    ex_time = datetime.datetime.now()
    file1 = open("logs.ecm", "a", 1)
    file1.write("E: "+str1+"  "+str(quantity)+"  " +
                datetime.datetime.ctime(ex_time)+" "+str(rest)+"\n")
    file1.close()


notice = tk.Label(window, text='请输入要查看的月份', bg='lightgray',
                  width=15, height=1, relief="ridge")
notice.place(x=600, y=450, width=255)          # 月份提示文本位置
input_month = tk.Entry(window, show=None, textvariable=month_choose)
input_month.place(x=600, y=485, width=255)          # 月份输入框位置
input_month.insert(0, '1')  # 设置默认月份为1
month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May',
              'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

# 每月出库元器件的总价值以及各类元器件的月消耗量(出库量-入库量)


def export_month():
    month = month_list[int(input_month.get())-1]
    out = [0, 0, 0, 0, 0, 0, 0, 0]
    join = [0, 0, 0, 0, 0, 0, 0, 0]
    if my_file.exists():
        with open("logs.ecm", "r") as f:
            b = f.readlines()
        for line in b:
            pro = line.split()[1]
            if line.split()[4] == month and line.split()[0] == "E:":
                for i in range(len(out)):
                    if list[i] == pro:
                        out[i] += int(line.split()[2])
            elif line.split()[4] == month and line.split()[0] == "I:":
                for i in range(len(out)):
                    if list[i] == pro:
                        join[i] += int(line.split()[2])
    global export_month_str
    month_str = ""
    month_consume_str = ""
    month_value = 0
    for i, component in enumerate(list):
        month_value += eval(component).price * out[i]
        month_consume_str = month_consume_str + component + ' ' + \
            input_month.get() + "月消耗量为：" + str(out[i] - join[i]) + " 个。\n"
    month_str = input_month.get() + "月份出库元器件的总价值为 ：" + str(month_value) + "元。\n"
    export_month_str.set(month_str)
    month_consume.set(month_consume_str)


export_month_button = tk.Button(
    window, text="查看当前月份出库元器件的总价值及\n各类元器件的月消耗量(出库量-入库量)", command=export_month)
export_month_button.place(x=600, y=520, width=255)          # 月份确定按钮位置
export_month_label = tk.Label(window, textvariable=export_month_str)
export_month_label.place(x=275, y=175)          # 月份出库价值显示位置
month_consume_label = tk.Label(window, textvariable=month_consume)
month_consume_label.place(x=275, y=200)          # 月份出库内容显示位置

# 入库出库
enter = tk.Button(master=window, text='入库', width=15,
                  height=1, command=add).place(x=800, y=165, width=107)          # 入库按钮位置
export = tk.Button(master=window, text='出库', width=15,
                   height=1, command=minus).place(x=800, y=205, width=107)          # 出库按钮位置

# 图标
# 2080


def RTX2080_image():
    global image1
    global image_file
    image_file = tk.PhotoImage(file='2080.gif')
    image1 = canvas.create_image(0, 0, anchor='nw', image=image_file)
# 2070


def RTX2070_image():
    global image1
    global image_file
    image_file = tk.PhotoImage(file='2070.gif')
    image1 = canvas.create_image(0, 0, anchor='nw', image=image_file)
#


def AMD_5700XT_image():
    global image1
    global image_file
    image_file = tk.PhotoImage(file='5700XT.gif')
    image1 = canvas.create_image(0, 0, anchor='nw', image=image_file)


def AMD_3900X_image():
    global image1
    global image_file
    image_file = tk.PhotoImage(file='3900X.gif')
    image1 = canvas.create_image(0, 0, anchor='nw', image=image_file)


def AMD_3990X_image():
    global image1
    global image_file
    image_file = tk.PhotoImage(file='3990X.gif')
    image1 = canvas.create_image(0, 0, anchor='nw', image=image_file)


def TITAN_RTX_image():
    global image1
    global image_file
    image_file = tk.PhotoImage(file='Titan2.gif')
    image1 = canvas.create_image(0, 0, anchor='nw', image=image_file)


def i9_image():
    global image1
    global image_file
    image_file = tk.PhotoImage(file='9980XE.gif')
    image1 = canvas.create_image(0, 0, anchor='nw', image=image_file)


def i7_image():
    global image1
    global image_file
    image_file = tk.PhotoImage(file='9400F.gif')
    image1 = canvas.create_image(0, 0, anchor='nw', image=image_file)


canvas.place(x=20, y=360)
window.mainloop()
