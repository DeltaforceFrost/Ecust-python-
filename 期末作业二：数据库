# 这个程序用于查找2025年1-4月份规模以上工业企业主要财务指标

import requests
import re 
import openpyxl
import os
import tempfile
from tkinter import *
from tkinter.messagebox import *
import pandas as pd
import sqlite3
import tkinter.ttk
import matplotlib.pyplot as plt





def entrycheck():    # 用于爬取网页的函数，运行结果将一个csv文件保存到桌面上并建立数据库，csv文件仅作为数据转移到数据库的媒介及方便数据整体查看，本身不用作数据处理

    try:
        web='https://www.stats.gov.cn/sj/zxfb/202505/t20250527_1959963.html'
        r=requests.get(web)
        r.encoding=r.apparent_encoding
        data=r.text
        reg='title=".*".*" href="(.*)" target="_blank" data-needdownload="false" needdownload="false" appendix="true">'
        check=re.findall(reg,data)
        filtered_check=[]
        for i in check:
            if i not in filtered_check:
                filtered_check.append(i)
                



        def download_file(url):
            local_filename = os.path.join(tempfile.gettempdir(), url.split('/')[-1])
            with requests.get(url, stream=True) as r:
                r.raise_for_status()
                with open(local_filename, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            return local_filename


        def convert_to_csv(xlsx_path, csv_path):
            df = pd.read_excel(xlsx_path)
            df.to_csv(csv_path, index=False, encoding='utf-8-sig')


        if __name__ == "__main__":
            url = 'https://www.stats.gov.cn/sj/zxfb/202505/'+filtered_check[0]
            xlsx_file_path = download_file(url)
            desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
            csv_file_path = os.path.join(desktop_path, '2025年1-4月份规模以上工业企业主要财务指标.csv')
            convert_to_csv(xlsx_file_path, csv_file_path)

        conn=sqlite3.connect('data.db')
        SQL='drop table if exists information'
        conn.execute(SQL)
        SQL='create table information(项目 text,营业收入金额 float,营业收入同比增长 float,营业成本金额 float,营业成本同比增长 float,利润总额 float,利润总额同比增长 float)'
        conn.execute(SQL)
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
file_name = '2025年1-4月份规模以上工业企业主要财务指标.csv'
file_path = os.path.join(desktop_path, file_name)
with open(file_path, 'r') as fobj:
            alist=fobj.readlines()
        for j in range(6,13):
            i=alist[j]
            i=i.split(',')
            if i[0][:2]=='其中':
                i0=i[0][3:]
                SQL='''insert into information(项目,营业收入金额,营业收入同比增长,营业成本金额,营业成本同比增长,利润总额,利润总额同比增长) 
                    values("%s","%f","%f","%f","%f","%f","%f")'''%(i0,float(i[1]),float(i[2]),float(i[3]),float(i[4]),float(i[5]),float(i[6].strip()))
            else:
                i0=i[0].strip()
                SQL='''insert into information(项目,营业收入金额,营业收入同比增长,营业成本金额,营业成本同比增长,利润总额,利润总额同比增长) 
                    values("%s","%f","%f","%f","%f","%f","%f")'''%(i0,float(i[1]),float(i[2]),float(i[3]),float(i[4]),float(i[5]),float(i[6].strip()))
            conn.execute(SQL)
        conn.commit()
        conn.close()
        showinfo('运行结果','数据表格已经成功获取并保存到你的桌面啦！\n数据库建立成功！')
    except:
        showinfo('运行结果','数据获取失败')





def search():    # 用于查询数据的函数
    try:
        namelist=['采矿业','制造业','电力、热力、燃气及水生产和供应业','国有控股企业','股份制企业','外商及港澳台投资企业','私营企业']
        itemlist=['营业收入金额','营业收入同比增长','营业成本金额','营业成本同比增长','利润总额','利润总额同比增长']
        name=comb1.get()
        item=comb2.current()
        counter=comb2.get()
        if name in namelist and counter in itemlist:
            conn=sqlite3.connect('data.db')
            SQL='''select * from information where 项目="%s"'''%name
            results=list(conn.execute(SQL))
            conn.commit()
            conn.close()
            outcome=results[0][item+1]
            if item==0 or item==2 or item==4:
                E1.delete(0,END)
                E1.insert(END,str(outcome)+'亿元')
            elif item==1 or item==3 or item==5:
                E1.delete(0,END)
                E1.insert(END,str(outcome)+'%')
        else:
            showinfo('错误','请输入正确信息!')
    except:
        showinfo('错误','请先进行数据爬取！')


def draw():    # 用于数据可视化的函数
    try:
        itemlist=['营业收入金额','营业成本金额','利润总额']
        formlist=['折线图','条形图']
        item=comb3.current()
        form=comb4.current()
        items=comb3.get()
        forms=comb4.get()
        if items in itemlist and forms in formlist:
            name=['采矿业','制造业','电力、热力、燃气及水生产和供应业','国有控股企业','股份制企业','外商及港澳台投资企业','私营企业']
            conn=sqlite3.connect('data.db')
            datalist=[]
            for i in range(0,7):
                SQL='''select * from information where 项目="%s"'''%(name[i])
                result=list(conn.execute(SQL))
                datalist.append(result[0][2*item+1])
                plt.rcParams['font.sans-serif']=['SimHei']
                plt.ylabel('亿元')
            if form==0:
                    plt.plot(name,datalist)
                    plt.show()
            elif form==1:
                plt.bar(name,datalist)
                plt.show()
            conn.commit()
            conn.close()
        else:
            showinfo('错误','请输入正确信息!')
    except:
        showinfo('错误','请先进行数据爬取！')



        
# 窗体的设计布局
root=Tk()
root.title('2025年1-4月份工业企业相关指标数据查找')
root.geometry('600x250')
B1=Button(root,bg='red',fg='white',text='数据爬取',command=entrycheck)
B1.place(x=20,y=100)
L1=Label(root,text='我想查询')
L1.place(x=20,y=50)
L2=Label(root,text='的')
L2.place(x=250,y=50)
comb1=tkinter.ttk.Combobox(root,values=['采矿业','制造业','电力、热力、燃气及水生产和供应业','国有控股企业','股份制企业','外商及港澳台投资企业','私营企业'])
comb1.place(x=80,y=50)
comb2=tkinter.ttk.Combobox(root,values=['营业收入金额','营业收入同比增长','营业成本金额','营业成本同比增长','利润总额','利润总额同比增长'])
comb2.place(x=270,y=50)
B2=Button(root,bg='blue',fg='white',text='开始查询',command=search)
B2.place(x=100,y=100)
L2=Label(root,text='查询结果:')
L2.place(x=200,y=100)
E1=Entry(root)
E1.place(x=270,y=100)
L3=Label(root,text='我想绘制各工业企业')
L3.place(x=20,y=150)
comb3=tkinter.ttk.Combobox(root,values=['营业收入金额','营业成本金额','利润总额'])
comb3.place(x=140,y=150)
L4=Label(root,text='的')
L4.place(x=310,y=150)
comb4=tkinter.ttk.Combobox(root,values=['折线图','条形图'])
comb4.place(x=330,y=150)
B2=Button(root,text='开始绘制',command=draw)
B2.place(x=500,y=150)
root.mainloop()
