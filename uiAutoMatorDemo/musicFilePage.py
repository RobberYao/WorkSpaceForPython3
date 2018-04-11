from uiautomator import device as d
import time


# 播放全部音乐
def playAllOfMusic():
    print('start playAllOfMusic...')
    d(resourceId='com.android.music:id/tv_play_all').click()
    print('stop playAllOfMusic...')


# 播放全部音乐
def playRandom():
    print('start playRandom...')
    d(resourceId='com.android.music:id/tv_play_random').click()
    print('stop playRandom...')


# 播放列表中的歌曲
def playMusicFromList(i):
    # i = d(resourceId='com.android.music:id/gridview').info
    print('start playMusicFromList...')
    if i >= 0 and i <= 7:
        d(resourceId='com.android.music:id/icon')[i].click()
    else:
        print('must between 0 to 7 ')
    print('stop playMusicFromList...')
    # sibling(className='android.widget.RelativeLayout')


# 打开音乐文件包
def selectByFolders():
    print('start selectByFolders...')
    d(resourceId='com.android.music:id/tab_item_rl')[0].click()
    print('stop selectByFolders...')


# 必须先执行selectByFolders后再查找文件名
def openMusicPackageByName(packageName):
    print('start openMusicPackageByName...')
    d(text=packageName).click()
    print('stop openMusicPackageByName...')


# 打开收藏
def selectByMyFavorite():
    print('start selectByMyFavorite...')
    d(resourceId='com.android.music:id/tab_item_rl')[1].click()
    print('stop selectByMyFavorite...')


# 按播放次数排序
def selectByPlayTimes():
    print('start selectByPlayTimes...')
    d(resourceId='com.android.music:id/tab_item_rl')[2].click()
    print('stop selectByPlayTimes...')


if __name__ == '__main__':
    # print(d(resourceId='com.android.music:id/gridview').info)
    # print('end...')
    # playAllOfMusic()
    # selectByPlayTimes()
    # selectByMyFavorite()
    # selectByFolders()
    # eval('selectByFolders()')
    # eval('playMusicFromList(1)')
    eval('openMusicPackageByName(\'msc\')')
