from uiautomator import device as d
import time
from FrameWorkOfSaicAutoTest.logModule import loggingConfig

lc = loggingConfig.loggingConfig()

# 播放全部音乐
def playAllOfMusic():
    lc.fileLog().info('start playAllOfMusic...')
    d(resourceId='com.android.music:id/tv_play_all').click()
    lc.fileLog().info('stop playAllOfMusic...')


# 播放全部音乐
def playRandom():
    lc.fileLog().info('start playRandom...')
    d(resourceId='com.android.music:id/tv_play_random').click()
    lc.fileLog().info('stop playRandom...')


# 播放列表中的歌曲
def playMusicFromList(i):
    # i = d(resourceId='com.android.music:id/gridview').info
    lc.fileLog().info('start playMusicFromList...')
    if i >= 0 and i <= 7:
        d(resourceId='com.android.music:id/icon')[i].click()
    else:
        lc.fileLog().info('must between 0 to 7 ')
    lc.fileLog().info('stop playMusicFromList...')
    # sibling(className='android.widget.RelativeLayout')


# 打开音乐文件包
def selectByFolders():
    lc.fileLog().info('start selectByFolders...')
    d(resourceId='com.android.music:id/tab_item_rl')[0].click()
    lc.fileLog().info('stop selectByFolders...')


# 必须先执行selectByFolders后再查找文件名
def openMusicPackageByName(packageName):
    lc.fileLog().info('start openMusicPackageByName...')
    d(text=packageName).click()
    lc.fileLog().info('stop openMusicPackageByName...')


# 打开收藏
def selectByMyFavorite():
    lc.fileLog().info('start selectByMyFavorite...')
    d(resourceId='com.android.music:id/tab_item_rl')[1].click()
    lc.fileLog().info('stop selectByMyFavorite...')


# 按播放次数排序
def selectByPlayTimes():
    lc.fileLog().info('start selectByPlayTimes...')
    d(resourceId='com.android.music:id/tab_item_rl')[2].click()
    lc.fileLog().info('stop selectByPlayTimes...')


if __name__ == '__main__':
    # lc.fileLog().info(d(resourceId='com.android.music:id/gridview').info)
    # lc.fileLog().info('end...')
    # playAllOfMusic()
    # selectByPlayTimes()
    # selectByMyFavorite()
    # selectByFolders()
    # eval('selectByFolders()')
    # eval('playMusicFromList(1)')
    eval('openMusicPackageByName(\'msc\')')
