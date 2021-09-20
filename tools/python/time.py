import time
#以年月日时分秒的方式输出当前时间
print(time.strftime("%Y/%m/%d %H:%M:%S",time.localtime()))
#以秒输出当前时间距离1970年1月1日的时间
print(time.time())
