#pip install pywin32
import win32api

'''
ShellExecute(hwnd, op, file, args, dir, show)
hwnd: 父窗口的句柄，如果没有父窗口，则为0
op : 要运行的操作，为open,print或者为空
file : 要运行的程序，或者打开的脚本
args : 要向程序传递的参数，如果打开的是文件则为空
dir : 程序初始化的目录
show : 是否显示窗口
'''                                                          
win32api.ShellExecute(0, 'open', 'file.exe', '', '', 0)           # 后台执行
win32api.ShellExecute(0, 'open', 'file.exe', '', '', 1)           # 前台打开
win32api.ShellExecute(0, 'open', 'file.exe', 'file', '', 1)      # 打开文件
win32api.ShellExecute(0, 'open', 'host', '', '', 1)   # 打开网页
win32api.ShellExecute(0, 'open', 'D:\\sound.mp3', '', '', 1)         # 播放视频
win32api.ShellExecute(0, 'open', 'D:\\demo.py', '', '', 1)          # 运行程序
