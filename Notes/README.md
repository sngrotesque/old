# 学习IT信息技术时的笔记

> 目录
>>- Python<br>
>> <a href="#py1">Python将16进制与字符串相互转换</a><br>
>> <a href="#py2">Python输出格式总结</a><br>
>> <a href="#py3">Python3的Requests模块，个人使用经验总结</a><br>
>>- Linux<br>
>> <a href="#linux1">Linux将Python脚本至后台运行</a><br>

### <a id="py1">Python将16进制与字符串相互转换</a>

> - 把十六进制的字串转为十进制数字：
> ```python
> print int('ff', 16)
> 255
> ```
> 
> - 把十进制数字转换为以十六进制表示之字串，可调用内置的hex()函数：
> ```python
> print hex(255)   
> 0xff
> ```
> 
> - 调用BinAscii模块其中的b2a_hex()函数，可把以ASCII编码的文字以十六进制表示：
> ```python
> import binascii
> print binascii.b2a_hex('A')   
> 41
> ```
> 
> - 反之也可把以十六进制表示的文字，换成以ASCII编码的文字：
> ```python
> import binascii
> print binascii.a2b_hex('41')
> “A”
> ```

### <a id="py2">Python输出格式总结</a>

> - 这里写下python常用的的print打印函数的输出格式总结，方便自己以后查阅
> ```python
> %(width)s     表示打印字符串
> %d               表示打印数字（十进制打印）
> %(width)f     表示打印浮点小数
> %p               打印地址(用十六进制打印内存地址)
> %c               打印一个字符（或者一个ASCII码，形如：0x31，输出“1”）
> %o               打印无符号整数(八进制)
> %x               无符号整数(十六进制)
> %X              无符号整数(十六进制大写字符)
> 二进制输出可以使用函数：bin（char）来输出二进制
> ```

### <a id="py3">Python3的Requests模块，个人使用经验总结</a>

> - Python3 - Requests
> Install<br>
> pip install requests
```python
#-*- coding:utf-8 -*-
import requests
url="https://www.google.com/"  #此为URL，请加上HTTP协议，示例Google

h={   #请求标头
  "User-Agent":"Devices Name and Version",
  "Cookie":"cookie",
}

data={    #请求数据
  "token":"token",
}

proxy={   #代理使用
  "http":"127.0.0.1:1080",
  "https":"127.0.0.1:1080",
}

r=requests.get(url,headers=h,json=data,proxies=proxy)   #使用GET方式请求上面的所有内容

r=requests.post(url,headers=h,json=data,proxies=proxy)  #使用POST方式请求上面的所有内容

print(r.status_code)  #输出请求状态码
print(r.encode)  #输出文字编码
print(r.text)  #输出请求内容
print(r.json())  #输出请求JSON
print(r.headers)  #输出服务器标头
print(r.content)  #如果是文件，就会输出十六进制的数据内容
```

### <a id="linux1">Linux将Python脚本至后台运行</a>

> - 这段时间想做一些调用Web API的脚本所以就研究了一下
> ```bash
> python test.py > python.log &
> 
> 1、 > 表示把标准输出（STDOUT）重定向到 那个文件，这里重定向到了python.log
> 2、 & 表示在后台执行脚本
> 这样可以到达目的，但是，我们退出shell窗口的时候，必须用exit命令来退出，否则，退出之后，该进程也会随着shell的消失而消失（退出、关闭）
> 在python运行中查看不到输出
> ```
> 因为：python的输出有缓冲，导致python.log3并不能够马上看到输出。
> 使用-u参数，使得python不启用缓冲。
> 所以改正命令，就可以正常使用了
> ```bash
> nohup python -u test.py > out.log 2>&1 &
> ```
