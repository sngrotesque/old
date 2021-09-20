#作者: SN-Grotesque，祝你们用的开心
import random,os,platform
#载入需要的模块

#判断系统并执行对应的清屏命令
if(platform.system()=='Windows'):
    os.system("cls")
elif(platform.system()=='Linux'):
    os.system("clear")
else:
    print("")

print("是否读取上次保存的学生名单？(如未保存过程序可能会退出运行)\n请输入(1.是 / 2.否):",end="")
loadFile=int(input())   #将输入的值存为整型数字供if语句判断

if(loadFile==1):
    print("请输入保存的文件名称:",end="")
    fileName=str(input())
    file=open(fileName,"r") #读取对应文件
    student_list=file.read()    #将读取的文件保存为变量
    
    #将变量从字符串类型转为列表类型
    student_list=student_list.strip('[')
    student_list=student_list.strip(']')
    student_list=student_list.split(',')
    
    print("上次保存的名单为:%s"%student_list)
    
    print("你要选几位同学？(请输入整数数字)\n请输入:",end="")
    s_nubmer=int(input())
    lucky=random.sample(student_list, s_nubmer) #随机选择列表内的某项

    print("被选中的同学是...\n%s"%lucky)   #输出选择结果
    exit()  #退出程序
else:
    print("你选择的是不读取上次保存的文件。")

print("班上一共有多少个学生？(请输入整数数字)\n请输入:",end="")
student=int(input())

print("初始化列表，请稍等...")
student_list=["0" for x in range(0,student)]    #初始化列表(也就是初始化数组)

#将输入的名字分别存到列表内
for x in range(student):
    print("请输入第%d个学生的名字:"%(x+1),end="")
    student_name=str(input())
    student_list[x]=student_name
    
print("是否将学生列表存为文件以便下次使用？(1.是 / 2.否)\n请输入:",end="")
choice=int(input())

if(choice==1):
    print("请输入要保存的文件的名称:",end="")
    fileName=str(input())
    file=open(fileName,"w") #覆盖写入的方式添加文件
    file.write(str(student_list))   #将学生列表转为字符串类型保存
    file.close()    #关闭文件
    print("文件保存成功！")
else:
    print("你选择的是不存为文件。")
    
print("你要选几位同学？(请输入整数数字)\n请输入:",end="")
s_nubmer=int(input())
lucky=random.sample(student_list, s_nubmer) #随机选择列表内的某项

print("被选中的同学是...\n%s"%lucky) #输出被选中的幸运儿
