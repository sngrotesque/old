import os

nowpath=os.getcwd()
nowpath_file=os.listdir(os.getcwd())

print("当前目录为[ %s ]"%nowpath)

x=0
while x<len(nowpath_file):
    print(nowpath_file[x])
    x=x+1
    
exit()
