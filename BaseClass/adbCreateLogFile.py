import os
from FunctionClass import rebootAndGetSystemMessage
import time


#os.system('adb root')

#如果日志文件不存在，则创建指定目录下日志文件
def createLogFile(isExit):
    if isExit:
        print('/data/test/crash.log已存在')
    else:
        p = os.popen('adb shell "touch /data/test/crash.log"').read()
        print(p)
        print('Create data/data/test/crash.log Successfully')

#删除目录文件/data/test/
def deletLogFile():
    p=os.popen('adb shell "rm -r /data/test/"')
    if p=='':
        print('Delet /data/test/ Successfully')

#判断crash.log是否存在
def isLogFileExit():
    os.system('adb root')
    p=os.popen('adb shell "find /data/test/crash.log"').read()
    print(p)
    if 'No such' in p:
        print('False')
        return False
    else:
        print('True')
        return True

#截图后pull保存至本地+时间戳命名
def getScreenshot2Local():
    os.system('adb root')
    os.system('adb shell /system/bin/screencap -p /sdcard/screenshot.png')
    time.sleep(8)
    print('waiting screenshot.png')
    os.system('adb pull /sdcard/screenshot.png d:/LogFile')
    time.sleep(8)
    os.rename('d:/LogFile/screenshot.png', 'd:/LogFile/screenshot' + rebootAndGetSystemMessage.getlocalTime() + '.png')



#获取crash.log保存至本地+时间戳命名
def getCrashLogFile2Local():
    os.system('adb root')
    os.system('adb pull /data/test/crash.log d:/LogFile')
    os.rename('d:/LogFile/crash.log', 'd:/LogFile/crash' + rebootAndGetSystemMessage.getlocalTime() + '.log')
    print('crash.log ->' + rebootAndGetSystemMessage.getlocalTime() + '.log')



def getTombstonesFile2Local():
    pass



#将crash日志、tombstones pull到本地后+时间戳命名
def pullLogFileToLocal():
    os.system('adb root')
    os.system('adb pull /data/test/crash.log d:/LogFile')
    os.system('adb pull /data/tombstones d:/logFile')
    os.rename('d:/LogFile/crash.log', 'd:/LogFile/crash' + rebootAndGetSystemMessage.getlocalTime() + '.log')
    os.rename('d:/LogFile/tombstones', 'd:/LogFile/tombstones' + rebootAndGetSystemMessage.getlocalTime())
    print('crash.log ->' + rebootAndGetSystemMessage.getlocalTime() + '.log')
    print('tombstones -> tombstones' + rebootAndGetSystemMessage.getlocalTime())



if __name__ == '__main__':
    #createLogFile(isLogFileExit())
    #pullLogFileToLocal()
    getScreenshot2Local()



