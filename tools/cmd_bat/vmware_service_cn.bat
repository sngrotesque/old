@echo off
echo "建议使用管理员权限运行此脚本"
echo "1.启动服务/2.关闭服务"
set /p ff=请输入: 
if /i %ff%==1 (goto 1)
if /i %ff%==2 (goto 2)
:1
net start  VMAuthdService
net start  VMnetDHCP
net start  "VMware NAT Service"
net start  VMUSBArbService
net start  VMwareHostd
echo 执行完成..
pause
exit
:2
net stop  VMAuthdService
net stop  VMnetDHCP
net stop  "VMware NAT Service"
net stop  VMUSBArbService
net stop  VMwareHostd
echo 执行完成..
pause
exit
