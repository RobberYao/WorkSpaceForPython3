from uiautomator import device as d
import time


# 音乐模块方法

# 播放方式、单曲循环、重复播放（大图标）
def changePlayStatusByLocation():
    print('start changePlayStatusByLocation...')
    d.click(255, 345)
    print('stop changePlayStatusByLocation...')
    time.sleep(2)


# 播放上一首歌
def getPreviousSongByLocation():
    print('start getPreviousSongByLocation...')
    d.click(135, 440)
    print('stop getPreviousSongByLocation...')
    time.sleep(2)


# 快退
def backOff():
    print('start forward...')
    d.long_click(135, 440)
    print('stop forward...')
    time.sleep(2)


# 快进
def forward():
    print('start backOff...')
    d.long_click(375, 440)
    print('stop backOff...')
    time.sleep(2)


# 暂停、播放（封面图）
def changePlayStatusByCover():
    print('start changePlayStatusByCover...')
    d.click(255, 220)
    print('stop changePlayStatusByCover...')
    time.sleep(2)


# 暂停、播放（功能键）
def changePlayStatusByLocation():
    print('start changePlayStatusByLocation...')
    d.click(255, 440)
    print('stop changePlayStatusByLocation...')
    time.sleep(2)


# 播放下一首歌
def getNextSongByLocation():
    print('start getNextSongByLocation...')
    d.click(375, 440)
    print('stop getNextSongByLocation...')
    time.sleep(2)


# 打开音效界面
def enterSoundEffectPage():
    print('start enterSoundEffectPage...')
    d.click(390, 345)
    print('stop enterSoundEffectPage...')
    time.sleep(2)


# 打开音乐文件界面
def enterMusicFilePage():
    print('start enterMusicFilePage...')
    d.click(120, 345)
    print('stop enterMusicFilePage...')
    time.sleep(2)


if __name__ == '__main__':
    forward()
    backOff()
