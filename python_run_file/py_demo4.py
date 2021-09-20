from ctypes import *
'''
#使用ctypes调用kernel32.dll中的函数
#使用ctypes模块可以让Python调用位于动态链接库的函数。
#ctypes模块为Python提供了调用动态链接库中函数的功能。
#使用ctypes模块可以方便地调用由C语言编写的动态链接库，并向其传递参数。
#ctypes模块定义了C语言中的基本数据类型，并且可以实现C语言中的结构体和联合体。
#ctypes模块可以工作在Windows,Linux,Mac OS等多种操作系统，基本上实现了跨平台。
#示例:Windows下调用user32.dll中的MessageBoxA函数。
'''
user32 = windll.LoadLibrary('user32.dll')
user32.MessageBoxA(0, str.encode('Ctypes is so smart!'), str.encode('Ctypes'), 0)
'''
ctype模块中含有的基本类型与C语言类似，下面是几个基本的数据类型的对照:

Ctypes数据类型	C数据类型
c_char	       char
c_short	       short
c_int	         int
c_long	       long
c_float	       float
c_doule	       double
c_void_p	     void *
'''
