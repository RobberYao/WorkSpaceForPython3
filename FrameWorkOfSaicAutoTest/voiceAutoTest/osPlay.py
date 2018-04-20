# coding:utf-8
import os
import time
from logging.config import fileConfig
from FrameWorkOfSaicAutoTest.LogModule import loggingConfig

listFile = 'D:/mp3File/chinese'
# filePath1 = 'D:/mp3File/chinese/musicVoice/暂停.MP3'
# filePath2 = 'D:/mp3File/chinese/musicVoice/下一首.MP3'
filePath3 = 'D:/mp3File/english/musicVoice/e_g_CloseMusic.mp3'

fileConfig("../LogModule/logging.ini")

fileLog = loggingConfig.fileLog()


class osPlay:

    # 播放语音 使用gplay
    def play(fileName):
        fileLog.info('play :' + fileName)
        os.system("gplay " + fileName)
        # os.system("wmplayer " + fileName)
        # os.system("XMP " + fileName)
        fileLog.info('over ')

    # 单曲循环
    def singlePlay(fileName):
        fileLog.info('singlePlay :' + fileName)
        while True:
            osPlay.play(fileName)
            time.sleep(1)

    # 播放多个语音
    def playListofLoop(ListofLoop):
        # os.listdir(ListofLoop)
        fileLog.info('playListofLoop :' + str(ListofLoop))
        for lis in ListofLoop:
            osPlay.play(lis)

    # 自定义播放次数
    def playTimes(fileName, times):
        for index in range(int(times)):
            osPlay.play(fileName)
            fileLog.info('need to play ' + str(times) + ' times： ' + fileName)
            fileLog.info(' has played ' + str(index + 1) + 'times')

    # 固定播放10次
    def playTimes_10(fileName):
        for index in range(10):
            osPlay.play(fileName)
            fileLog.info('play 10 times :' + fileName + ' has played ' + str(index + 1) + ' times')

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
    osP = osPlay()
    # list = [filePath1, filePath2]
    # print(os.getcwd())
    # print(list)
    # print(playListofLoop(listFile))
    # loadPath()
    # playTimes(filePath3, 1)
    # play(filePath3)
    # fileLog.info('play ' + filePath3)
    osP.play(filePath3)
    # playListofLoop(list)
    # while True:
    # singlePlay(filePath2)
