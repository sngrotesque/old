@echo off
echo "It is recommended that you run this script with administrator privileges."
echo "1.Start Service / 2.Stop Service"
set /p ff="Please enter:"
if /i %ff%==1 (goto 1)
if /i %ff%==2 (goto 2)
:1
net start  VMAuthdService
net start  VMnetDHCP
net start  "VMware NAT Service"
net start  VMUSBArbService
net start  VMwareHostd
echo "Command execution complete"
pause
exit
:2
net stop  VMAuthdService
net stop  VMnetDHCP
net stop  "VMware NAT Service"
net stop  VMUSBArbService
net stop  VMwareHostd
echo "Command execution complete"
pause
exit
