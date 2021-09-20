#-*- coding=utf-8 -*-
# 作者：SN-Grotesque（Author: SN-Grotesque）

import os
import requests
import time

url="https://www.lottery.gov.cn/tz_kj.json"
h={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0","Cookie":"None",}
json_r=requests.get(url,headers=h).json()
r=str(json_r)

#os.system("clear")   #Linux
#os.system("cls")     #Windows

print("欢迎进入SN-Grotesque编写的查询体彩开奖号码的程序\n0.退出\n")
print("请输入: ",end="")
int_u_input=input()
u_input=str(int_u_input)

while(u_input!='0'):
    os.system("cls")     #Windows
    print("当前时间: ",time.ctime())
    print("您是想查看体彩哪种彩票的开奖结果?")
    print("1.大乐透\n2.排列三\n3.排列五\n4.七星彩\n0.退出\n")
    print("请输入: ",end="")
    int_u_input=input()
    u_input=str(int_u_input)


    if u_input=='1':
        os.system("cls")     #Windows
        print("当前时间: ",time.ctime())
        print("这是 %s 期大乐透开奖号码: %s"%(r[1233:1238],r[1085:1128]))
        time.sleep(10)
        os.system("cls")     #Windows
    elif u_input=='2':
        os.system("cls")     #Windows
        print("当前时间: ",time.ctime())
        print("这是 %s 期排列三开奖号码: %s"%(r[358:363],r[237:254]))
        time.sleep(5)
        os.system("cls")     #Windows
    elif u_input=='3':
        os.system("cls")     #Windows
        print("当前时间: ",time.ctime())
        print("这是 %s 期排列五开奖号码: %s"%(r[787:792],r[657:682]))
        time.sleep(5)
        os.system("cls")     #Windows
    elif u_input=='4':
        os.system("cls")     #Windows
        print("当前时间: ",time.ctime())
        print("这是 %s 期七星彩开奖号码: %s"%(r[1673:1678],r[1532:1568]))
        time.sleep(10)
        os.system("cls")     #Windows
    elif u_input!='1' and u_input!='2' and u_input!='3' and u_input!='4' and u_input!='0':
        os.system("cls")     #Windows
        print("请输入正确的值！")
        time.sleep(5)
        os.system("cls")     #Windows
        

os.system("cls")     #Windows
print("好的，再见！")

exit()
