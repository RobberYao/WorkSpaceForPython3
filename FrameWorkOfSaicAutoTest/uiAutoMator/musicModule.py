from uiautomator import device as d
import time
from FrameWorkOfSaicAutoTest.logModule import loggingConfig

lc = loggingConfig.loggingConfig()

# 音乐播放页面功能

# 播放方式、单曲循环、重复播放（小图标）
def changePlayStatus():
    lc.fileLog().info('start changePlayStatus...')
    d.click(255, 345)
    lc.fileLog().info('stop changePlayStatus...')
    time.sleep(2)


# 播放上一首歌
def getPreviousSongByLocation():
    lc.fileLog().info('start getPreviousSongByLocation...')
    d.click(135, 440)
    lc.fileLog().info('stop getPreviousSongByLocation...')
    time.sleep(2)


# 快退
def backOff():
    lc.fileLog().info('start forward...')
    d.long_click(135, 440)
    lc.fileLog().info('stop forward...')
    time.sleep(2)


# 快进
def forward():
    lc.fileLog().info('start backOff...')
    d.long_click(375, 440)
    lc.fileLog().info('stop backOff...')
    time.sleep(2)


# 暂停、播放（封面图）
def changePlayStatusByCover():
    lc.fileLog().info('start changePlayStatusByCover...')
    d.click(255, 220)
    lc.fileLog().info('stop changePlayStatusByCover...')
    time.sleep(2)


# 暂停、播放（功能键）
def changePlayStatusByLocation():
    lc.fileLog().info('start changePlayStatusByLocation...')
    d.click(255, 440)
    lc.fileLog().info('stop changePlayStatusByLocation...')
    time.sleep(2)


# 播放下一首歌
def getNextSongByLocation():
    lc.fileLog().info('start getNextSongByLocation...')
    d.click(375, 440)
    lc.fileLog().info('stop getNextSongByLocation...')
    time.sleep(2)


# 打开音效界面
def enterSoundEffectPage():
    lc.fileLog().info('start enterSoundEffectPage...')
    d.click(390, 345)
    lc.fileLog().info('stop enterSoundEffectPage...')
    time.sleep(2)


# 打开音乐文件界面
def enterMusicFilePage():
    lc.fileLog().info('start enterMusicFilePage...')
    d.click(120, 345)
    lc.fileLog().info('stop enterMusicFilePage...')
    time.sleep(2)


if __name__ == '__main__':
    forward()
    backOff()
