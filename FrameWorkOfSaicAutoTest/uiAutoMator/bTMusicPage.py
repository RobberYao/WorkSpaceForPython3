from uiautomator import device as d
import time
from FrameWorkOfSaicAutoTest.logModule import loggingConfig

lc = loggingConfig.loggingConfig()


# 蓝牙音乐
# 播放下一首歌
def getBTNextSong():
    lc.fileLog().info('start getBTNextSong...')
    d(resourceId='com.clw.btmusic:id/bt_next').click()
    lc.fileLog().info('stop getBTNextSong...')
    time.sleep(2)


# 播放下一首歌
def getBTPerviousSong():
    lc.fileLog().info('start getBTPerviousSong...')
    d(resourceId='com.clw.btmusic:id/bt_pervious').click()
    lc.fileLog().info('stop getBTPerviousSong...')
    time.sleep(2)


# 改变播放状态 播放/暂停
def changePlayStatus():
    lc.fileLog().info('start getBTPerviousSong...')
    d(resourceId='com.clw.btmusic:id/bt_pause').click()
    lc.fileLog().info('stop getBTPerviousSong...')
    time.sleep(2)






