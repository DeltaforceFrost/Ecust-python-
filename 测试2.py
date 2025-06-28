#引入库
import tkinter
import math
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog

# 定义全局变量
data = []
ans = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
tdata = 0

# 定义函数‘引用’，用于读取指定文件
def index(x):
    x = x.strip('"\' ')
    try:
        with open(x, 'r', encoding='GB2312') as text:
            relist = []
            lines = text.readlines()
            for i in lines:
                i = i.strip()
                if i.isdigit():
                    relist.append(float(i))
        return relist
    except FileNotFoundError:
        tkinter.messagebox.showerror("提示", "文件未找到")
        return []

# 定义中间函数，防止按钮按后不传递变量直接返回结果
def indexchange():
    text = en1.get()
    if text == '':
        tkinter.messagebox.showinfo('提示', '未输入内容')
    else:
        global data
        data = index(text)

# 定义函数‘均值’，用于计算所读取数据的均值
def average():
    if not data:
        tkinter.messagebox.showinfo('提示', '未查找到数据')
    else:
        tdata = sum(data) / len(data)
        text = '均值为%.2f\n' % tdata
        te1.insert(tkinter.END, text + '\n')
        te1.see(tkinter.END)

# 定义函数‘中位数’，用于计算数据的中位数
def mid():
    if not data:  # 检查 data 是否为空
        tkinter.messagebox.showinfo('提示', '未查找到数据')
    else:
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 != 0:
            tdata = sorted_data[n // 2]
        else:
            tdata = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        text = '中位数为%.2f\n' % tdata
        te1.insert(tkinter.END, text + '\n')
        te1.see(tkinter.END)

# 定义函数‘相对偏差’，用于计算数据的相对偏差
def limit():
    if not data:
        tkinter.messagebox.showinfo('提示', '未查找到数据')
    else:
        avg = sum(data) / len(data)
        relist = [f"{((i - avg) / avg) * 100:.2f}%" for i in data]
        text = f"各数据相对偏差为: {', '.join(relist)}"
        te1.insert(tkinter.END, text + '\n')
        te1.see(tkinter.END)

# 定义函数‘变异系数’，用于判断数据是否可信
def evolution():
    if not data:
        tkinter.messagebox.showinfo('提示', '未查找到数据')
    else:
        avg = sum(data) / len(data)
        variance = sum((i - avg) ** 2 for i in data) / len(data)
        std_dev = math.sqrt(variance)
        coef_variation = (std_dev / avg) * 100
        text = '变异系数为%.2f%%\n' % coef_variation
        te1.insert(tkinter.END, text + '\n')
        te1.see(tkinter.END)

# 定义函数‘清空’，用于清空文本数据
def clear():
    te1.delete(1.0, tkinter.END)
    text='数据已清空'
    te1.insert(tkinter.END, text + '\n')
# 定义函数‘说明书’，用于向用户介绍功能
def readme():
    win2 = tkinter.Toplevel(win)
    win2.geometry("200x200")
    te2 = tkinter.Text(win2, font=14, fg='red', bg='gray', width=20, height=20, wrap=tkinter.WORD)
    te2.pack(fill=tkinter.BOTH, expand=True)
    text = '说明书\n1. 通过在框内输入文件路径可以自动读取文件数据\n2. 之后可以选择窗体下方的各项功能按钮得出想要的数据分析结果\n3. 未录入数据会提示错误'
    te2.insert(tkinter.END, text)
    te2.config(state=tkinter.DISABLED)

# 窗体构建
win = tkinter.Tk()
win.title('数据处理')
win.geometry('470x320')

bt1 = tkinter.Button(win, text='读取文件', command=indexchange, font=("Arial", 12))
bt1.place(x=10, y=40)

lb1 = tkinter.Label(win, text='输入文件名', bg='gray', font=("Arial", 12))
lb1.place(x=10, y=10)

en1 = tkinter.Entry(win, bd=1, width=50)
en1.place(x=150, y=10)

te1 = tkinter.Text(win, font=10, width=25, height=20)
te1.place(x=800, y=0)

bt2 = tkinter.Button(win, text='计算均值', fg='blue', command=average, font=("Arial", 14))
bt2.place(x=0, y=460)

bt3 = tkinter.Button(win, text='计算相对偏差', fg='blue', command=limit, font=("Arial", 14))
bt3.place(x=200, y=460)

bt4 = tkinter.Button(win, text='计算中位数', fg='blue', command=mid, font=("Arial", 14))
bt4.place(x=400, y=460)

bt5 = tkinter.Button(win, text='计算变异系数', fg='blue', command=evolution, font=("Arial", 14))
bt5.place(x=600, y=460)

bt6 = tkinter.Button(win, text='清空文本', fg='blue', command=clear, font=("Arial", 14))
bt6.place(x=800, y=460)

bt7 = tkinter.Button(win, text='说明书', fg='blue', command=readme, font=('Arial', 14))
bt7.place(x=1000, y=460)

win.mainloop()
