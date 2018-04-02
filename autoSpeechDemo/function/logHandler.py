# _*_ coding:utf-8 _*_
import os
import re


# 清空文件
def cleanFile():
    # os.system('adb shell echo '' > /data/data/com.saicmotor.voice/files/log.txt')
    os.system('adb shell rm -r /data/data/com.saicmotor.voice/files/log.txt')  # 删除文件
    os.system('adb shell touch /data/data/com.saicmotor.voice/files/log.txt')  # 创建文件


# 将日志文件拉取至本地
def pullFile():
    os.system('adb pull /data/data/com.saicmotor.voice/files/log.txt d:/logFile')

    with open('d:/LogFile/log.txt', 'r', encoding='UTF-8') as log:
        with open('d:/LogFile/logLocal.txt', 'a+', encoding='UTF-8') as logLocal:
            logLocal.write(log.read())  # 从临时文件写入目标文件
            # log.seek(0).truncate()  # 清空临时文件


# 正则匹配关键词
def matchVoice(correctResponse):
    with open('d:/LogFile/log.txt', 'r', encoding='UTF-8') as log:
        context = log.read()
        print('将 ' + correctResponse + ' 与比对 :' + context)
        if correctResponse in context:
            return True
        else:
            return False


# 将匹配结果存入车机日志文件
def markResult(correctResponse, matchResult):
    with open('d:/LogFile/logLocal.txt', 'a+', encoding='UTF-8') as logLocal:
        if matchResult:
            logLocal.write('车机语音测试 ' + correctResponse + ' 匹配成功')
        else:
            logLocal.write('车机语音测试 ' + correctResponse + ' 匹配失败')


# 清空临时文件
def cleanTempFile():
    with open('d:/LogFile/log.txt', 'w', encoding='UTF-8') as log:
        log.truncate()


if __name__ == '__main__':
    '''
    cleanTempFile()
    pullFile()
    cleanTempFile()
    '''
    matchVoice('打开音乐')
    pass
    # cleanFile()
