import os
import time
from BaseClass import adbCreateLogFile

# os.system('adb version')
# os.system('adb devices')
# out = os.popen('adb shell "dumpsys activity | grep "mFocusedActivity""').read() #os.popen支持读取操作
# out = os.popen('adb shell "top -m 10 -n 1 -s cpu"').read() #os.popen支持读取操作
# out = os.popen('adb shell "dumpsys activity"')
# print(out)


warningValue = 40


# 获取时间戳
def getlocalTime():
    localTime = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    # print(localTime + '\n');
    return localTime


# function of Get VM
def getVirtual_memory():
    vmStr = os.popen('adb shell "top -n 1 -s cpu"').read()

    return vmStr


def isOverWarningValuse(vmStr):
    splitStr = vmStr.split('IOW')
    tempStr = splitStr[0].replace('\n', '').split(', ')
    user = tempStr[0].replace('%', '').split(' ')
    system = tempStr[1].replace('%', '').split(' ')

    if float(user[1]) >= warningValue or float(system[1]) >= warningValue:  # user 或者 system 是否超过阀值
        print('warning !!!! Stop Running' + user[0] + ' : ' + user[1] + ' ' + system[0] + ' : ' + system[1])
        return True
    else:
        print('As Well ' + user[0] + ' : ' + user[1] + ' ' + system[0] + ' : ' + system[1])
        return False


def reboot():
    os.popen('adb shell "reboot"')


def mainMethod():
    i = 0
    for i in range(0, 999999):
        adbCreateLogFile.createLogFile(adbCreateLogFile.isLogFileExit())
        reboot()
        with open("D:/LogFile/SystemMessage.txt", 'a+') as fo:
            fo.write("[Reboot_Times :" + str(i) + "]")
        print("Reboot_Times :" + str(i))
        print("Start witing")
        time.sleep(300)  # 等待5分钟 300
        adbCreateLogFile.getScreenshot2Local()
        print("Stop witing")
        for k in range(0, 9):
            with open("SystemMessage.txt", 'a+') as fo:
                fo.writelines('\n')
                fo.write("[" + getlocalTime() + "]")
                fo.writelines('\n')
                fo.write(getVirtual_memory())
                fo.writelines('\n')
                if isOverWarningValuse(getVirtual_memory()):
                    pass  # 需要报警停止直接将pass改为return即可
                else:
                    pass
                time.sleep(10)  # 10
                k += 1
        adbCreateLogFile.pullLogFileToLocal()
        i += 1


# 功能：重启车机->等待5分钟->每10秒获取一次Cpu&内存信息保存至本地日志文件->获取车机日志crash.log>>>>
if __name__ == "__main__":
    mainMethod()
