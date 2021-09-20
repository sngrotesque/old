import requests
import os

os.system("clear")
url="https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=85&provinceId=0&pageSize=1000" #查询的网址

#Headers标头
h={
    "user-agent":"android 8.1.0",
    "cookie":"none"
}

#获取返回的json数据
r=requests.get(url,headers=h).json()

#初始化变量
x=0

while x<1000:
    print("第[%s]期超级大乐透号码为:[%s]"%(r['value']['list'][x]['lotteryDrawNum'],r['value']['list'][x]['lotteryDrawResult']))

    #写入到文件
    file=open("cp_dlt_history.txt","a+")
    file.write("第[%s]期超级大乐透号码为:[%s]\n"%(r['value']['list'][x]['lotteryDrawNum'],r['value']['list'][x]['lotteryDrawResult']))
    file.close()

    x=x+1
