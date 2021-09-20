#-*- coding=utf-8 -*-
# 作者：SN-Grotesque（Author: SN-Grotesque）
#将代码稍微小改一下就可以做双色球的测试了
import random

cp = [1, 4, 14, 16, 19, 3, 4]     #第21051期开奖号码
x=1                                 #x为1

print("需要查看使用手册吗？(y/n)",end="")
yhsc=str(input()).upper()

if yhsc=='Y':

    #os.system("cls")     #Windows
    #os.system("clear")   #Linux
    print(
        "此程序由SN-Grotesque制作，语言为Python3。\n\
        \r此程序中“全年无休”指的是1年开144次奖。\n\
        \r需要多少年才能买到头奖(保留两位小数)。")
    
elif yhsc=='N':
    res = []                            #定义res变量
    while res != cp:
        #os.system("cls")     #Windows
        #os.system("clear")   #Linux

        res_red = random.sample([x for x in range(1, 36)], 5)  # 在35个随机选取5个红球
        res_blue = random.sample([x for x in range(1, 13)], 2)  # 在12个随机选取2个红球

        res_red.sort()  # 对选取的5个红球排序
        res_blue.sort()  # 对选取的2个蓝球排序

        res = res_red + res_blue
        x+=1
    
    print("一共开了%d次，总计花费金额为[%d元]，按照全年无休计算需至少%.2f年才能买到头奖。"%(x,x*2,x/144.00))
