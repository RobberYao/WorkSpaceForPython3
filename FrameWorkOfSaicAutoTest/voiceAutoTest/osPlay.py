import os
import time
# import eyed3
# from tinytag import TinyTag
from autoSpeechDemo.BaseConfig.filePathConfig import musicVoice as mv

listFile = 'D:/mp3File/chinese'
filePath1 = 'D:/mp3File/chinese/musicVoice/暂停.MP3'
filePath2 = 'D:/mp3File/chinese/musicVoice/下一首.MP3'
filePath3 = 'D:/mp3File/english/musicVoice/e_g_CloseMusic.mp3'


# 播放语音 使用gplay
def play(fileName):
    print('play :' + fileName)
    os.system("gplay " + fileName)
    # os.system("wmplayer " + fileName)
    # os.system("XMP " + fileName)
    print('over ')


# 单曲循环
def singlePlay(fileName):
    print('singlePlay :' + fileName)
    while True:
        play(fileName)
        time.sleep(1)


# 播放多个语音
def playListofLoop(ListofLoop):
    # os.listdir(ListofLoop)
    print('playListofLoop :' + str(ListofLoop))
    for lis in ListofLoop:
        play(lis)


# 自定义播放次数
def playTimes(fileName, times):
    for index in range(int(times)):
        play(fileName)
        print('需播放 ' + str(times) + ' 次： ' + fileName)
        print(' 已播放 ' + str(index + 1) + '次')


# 固定播放10次
def playTimes_10(fileName):
    for index in range(10):
        play(fileName)
        print('播放10次： ' + fileName + ' 已播放' + str(index + 1) + ' time')


# 获取MP3时间长度 返回该MP3耗时+1秒
def getSecondOfMp3(fileName):
    '''
    teg = eyed3.load(fileName)
    teg = TinyTag.get(fileName).duration
    print('MP3 ：' + fileName + 'cost ' + str(teg + 1) + '秒')
    return teg + 1
    '''
    pass


''' 
def loadPath():
    print(mm['play'])
'''

if __name__ == '__main__':
    # list = [filePath1, filePath2]
    # print(os.getcwd())
    # print(list)
    # print(playListofLoop(listFile))
    # loadPath()
    playTimes(filePath3, 1)

    # playListofLoop(list)
    # while True:
    # singlePlay(filePath2)
