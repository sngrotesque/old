import win32process
'''
CreateProcess(appName, cmdLine, proAttr, threadAttr, InheritHandle, CreationFlags, newEnv, currentDir, Attr)
#appName         可执行文件名
#cmdLine         命令行参数
#procAttr        进程安全属性
#threadAttr      线程安全属性
#InheritHandle  继承标志
#CreationFlags  创建标志
#currentDir      进程的当前目录
#Attr             创建程序的属性
'''
win32process.CreateProcess('C:\\Windows\\notepad.exe', '', None, None, 0, win32process.CREATE_NO_WINDOW, None, None, win32process.STARTUPINFO())
'''
结束进程:可以使用win32process.TerminateProcess函数来结束已创建的进程。函数格式如下:
TerminateProcess(handle, exitCode)
#handle 要操作的进程句柄
#exitCode 进程退出代码

或者使用win32event.WaitForSingleObject等待创建的线程结束。函数格式如下:
WaitForSingleObject(handle, milisecond)
#handle : 要操作的进程句柄
#milisecond: 等待的时间,如果为-1,则一直等待.
'''
#示例如下
import win32process
handle = win32process.CreateProcess('C:\\Windows\\notepad.exe', '', None, None, 0, win32process .CREATE_NO_WINDOW, None, None, win32process.STARTUPINFO())            # 打开记事本，获得其句柄
win32process.TerminateProcess(handle[0], 0)                       # 终止进程
#或者
import win32event
handle = win32process.CreateProcess('C:\\Windows\\notepad.exe', '', None, None, 0, win32process.CREATE_NO_WINDOW, None, None, win32process.STARTUPINFO())             # 创建进程获得句柄
win32event.WaitForSingleObject(handle[0], -1)                      # 等待进程结束
