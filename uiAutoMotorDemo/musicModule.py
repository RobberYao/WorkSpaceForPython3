from uiautomator import device as d
import time


# 音乐模块方法

# 播放方式、单曲循环、重复播放（大图标）
def changePlayStatusByLocation():
    d.click(255, 345)
    time.sleep(2)


# 播放上一首歌
def getPreviousSongByLocation():
    d.click(135, 440)
    time.sleep(2)


# 快进
def forward():
    d.long_click(135, 440)
    time.sleep(2)


# 快退
def backOff():
    d.long_click(375, 440)
    time.sleep(2)


# 暂停、播放（封面图）
def changePlayStatusByCover():
    d.click(255, 220)
    time.sleep(2)


# 暂停、播放（功能键）
def changePlayStatusByLocation():
    d.click(255, 440)
    time.sleep(2)


# 播放下一首歌
def getNextSongByLocation():
    d.click(375, 440)
    time.sleep(2)


# 打开音效界面
def enterSoundEffectPage():
    d.click(390, 345)
    time.sleep(2)


# 打开音乐文件界面
def enterMusicFilePage():
    d.click(120, 345)
    time.sleep(2)


if __name__ == '__main__':
    enterMusicFilePage()
