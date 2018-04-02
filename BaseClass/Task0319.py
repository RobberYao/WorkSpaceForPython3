#-*- coding: utf-8 -*-
import time
import psutil
import re
import subprocess


ISOTIMEFORMAT='%Y%m%d%H%M%S'
filename= "SystemMessage" + re.sub(r'[^0-9]','',   str(time.strftime(ISOTIMEFORMAT))) + '.txt'

def getlocalTime():
    localTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #print(localTime + '\n');
    return localTime

#function of Get VM
def getVirtual_memory():
    vmStr = str(psutil.virtual_memory())
    print(vmStr + '\n')
    return vmStr

#function of Get cpuTime
def getCpu_time():
    cpuStr = str(psutil.cpu_times(percpu=False))
    print(cpuStr + '\n')
    return cpuStr
#function of getCpu_percent
def getCpu_percent():
    cpuPercentStr = " CPU: " + str(psutil.cpu_percent()) + "%"
    return cpuPercentStr


#function of Get cpu count
def getCpu_Count():
    print("     Cpu_Count: " + str(psutil.cpu_count(logical=False)))
    return "    CPU:" + str(psutil.cpu_count(logical=False))


def mainMethod():
    for i in range(0,9):
        with open("SystemMessage.txt",'a+') as fo:
            fo.write(getlocalTime() + " Virtual Memory  " + getVirtual_memory())
            fo.writelines('\n')
            fo.write(getlocalTime() + " Cpu Times  " + getCpu_time())
            fo.writelines('\n')
            fo.write(getlocalTime() + " Cpu Utilization  " + getCpu_percent())
            fo.writelines('\n')
            time.sleep(1)
        i += 1



if __name__ == "__main__":
    mainMethod()
