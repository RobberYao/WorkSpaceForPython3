# coding:utf-8
import os
import time
from FrameWorkOfSaicAutoTest.logModule import loggingConfig

lc = loggingConfig.loggingConfig()
listFile = 'D:/mp3File/chinese'
# filePath1 = 'D:/mp3File/chinese/musicVoice/暂停.MP3'
# filePath2 = 'D:/mp3File/chinese/musicVoice/下一首.MP3'
filePath3 = 'D:/mp3File/english/musicVoice/e_g_CloseMusic.mp3'



# 播放语音 使用gplay
def play(fileName):
    lc.consoleLog().info('play :' + fileName)
    lc.fileLog().info('play :' + fileName)
    os.system("gplay " + fileName)
    # os.system("wmplayer " + fileName)
    # os.system("XMP " + fileName)
    lc.consoleLog().info('over ')
    lc.fileLog().info('play :' + fileName)


# 单曲循环
def singlePlay(fileName):
    lc.consoleLog().info('singlePlay :' + fileName)
    while True:
        play(fileName)
        time.sleep(1)


# 播放多个语音
def playListofLoop(ListofLoop):
    # os.listdir(ListofLoop)
    lc.consoleLog().info('playListofLoop :' + str(ListofLoop))
    for lis in ListofLoop:
        play(lis)


# 自定义播放次数
def playTimes(fileName, times):
    for index in range(int(times)):
        play(fileName)
        lc.consoleLog().info('need to play ' + str(times) + ' times： ' + fileName)
        lc.consoleLog().info(' has played ' + str(index + 1) + 'times')


# 固定播放10次
def playTimes_10(fileName):
    for index in range(10):
        play(fileName)
        lc.consoleLog().info('play 10 times :' + fileName + ' has played ' + str(index + 1) + ' times')


# 获取MP3时间长度 返回该MP3耗时+1秒
def getSecondOfMp3(fileName):
    '''
    teg = eyed3.load(fileName)
    teg = TinyTag.get(fileName).duration
    print('MP3 ：' + fileName + 'cost ' + str(teg + 1) + '秒')
    return teg + 1
    '''
    pass


if __name__ == '__main__':
    # list = [filePath1, filePath2]
    # print(os.getcwd())
    # print(list)
    # print(playListofLoop(listFile))
    # loadPath()
    # playTimes(filePath3, 1)
    # play(filePath3)
    # lc.consoleLog().info('play ' + filePath3)
    play(filePath3)
    # playListofLoop(list)
    # while True:
    # singlePlay(filePath2)
