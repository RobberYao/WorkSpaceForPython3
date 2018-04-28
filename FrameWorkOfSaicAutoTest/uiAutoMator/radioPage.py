from uiautomator import device as d
import time
from FrameWorkOfSaicAutoTest.logModule import loggingConfig

lc = loggingConfig.loggingConfig()


# 退出radio页面
def exitRadioPage():
    lc.fileLog().info('start exitRadioPage...')
    d(resourceId='com.clw.fmam:id/imgbtn_exit').click()
    time.sleep(2)
    lc.fileLog().info('stop exitRadioPage...')


# 进入音效设置页面
def enterSoundEffectPage():
    lc.fileLog().info('start enterSoundEffectPage...')
    d(resourceId='com.clw.fmam:id/imgbtn_eq').click()
    time.sleep(2)
    lc.fileLog().info('stop enterSoundEffectPage...')


# 收音机频道刷新（耗时35秒）
def autoSearchChannels():
    lc.fileLog().info('start autoSearchChannel...')
    d(resourceId='com.clw.fmam:id/imgbtn_search').click()
    time.sleep(35)
    lc.fileLog().info('stop autoSearchChannel...')


# 选择偏好页面[700,130]
def selectFavoriteChannels():
    lc.fileLog().info('start selectFavoriteChannels...')
    d.click(700, 130)
    time.sleep(2)
    lc.fileLog().info('stop selectFavoriteChannels...')


# 选择AM页面[830,130]
def selectAmChannels():
    lc.fileLog().info('start selectAmChannels...')
    d.click(830, 130)
    time.sleep(2)
    lc.fileLog().info('stop selectAmChannels...')


# 选择FM页面[940,130]
def selectFmChannels():
    lc.fileLog().info('start selectFmChannels...')
    d.click(940, 130)
    time.sleep(2)
    lc.fileLog().info('stop selectFmChannels...')


# 根据名称选择频道
def selectChannelByName(channelName):
    lc.fileLog().info('start selectChannelByName...')
    try:
        d(className='android.widget.ListView',
          packageName='com.clw.fmam').child_by_text(channelName, text=channelName).click()
        print('==' + channelName)
    except:
        lc.fileLog().info(channelName + 'is not exists')
    time.sleep(1)
    lc.fileLog().info('end selectChannelByName...')


# 根据频道名称设置偏好
def setFavoriteByName(channelName):
    lc.fileLog().info('start setFavoriteByName...')
    try:
        d(className='android.widget.ListView',
          packageName='com.clw.fmam').child_by_text(channelName, text=channelName).sibling(
            resourceId='com.clw.fmam:id/favorite').click()
        print('==' + channelName)
    except:
        lc.fileLog().info(channelName + 'is not exists')
    time.sleep(1)
    lc.fileLog().info('end setFavoriteByName...')


# 指定获取AM调频[522,1620]
def chooseAmChannelByNum(num):
    lc.fileLog().info('start chooseAmChannelByNum...')
    d.click(95 + 3.19 * (num - 522) / 9, 434)
    print('num ===' + str(num))
    lc.fileLog().info('start chooseAmChannelByNum...')


# 指定获取FM调频[87.5,108.0]
def chooseFmChannelByNum(num):
    lc.fileLog().info('start chooseFmChannelByNum...')
    d.click(102.5 + 1.74 * (num - 87.5) / 0.1, 434)
    print('num ===' + str(num))
    lc.fileLog().info('start chooseFmChannelByNum...')


# 向下搜索频道(若无天线，将无限循环搜索)
def searchNextChannel():
    lc.fileLog().info('start searchNextChannel...')
    d(className='android.widget.ImageView', resourceId='com.clw.fmam:id/imgbtn_next').long_click()
    lc.fileLog().info('start searchNextChannel...')


# 向前搜索频道(若无天线，将无限循环搜索)
def searchPerviousChannel():
    lc.fileLog().info('start searchPerviousChannel...')
    d(className='android.widget.ImageView', resourceId='com.clw.fmam:id/imgbtn_previous').long_click()
    lc.fileLog().info('start searchPerviousChannel...')


if __name__ == '__main__':
    # exitRadioPage()
    # enterSoundEffectPage()
    # autoSearchChannels()
    # selectFavoriteChannels()
    # selectAmChannels()
    # selectFmChannels()
    # selectChannelByName('FM 108.0')
    # setFavoriteByName('FM 108.0')
    # chooseAmChannelByNum(1620)
    # chooseFmChannelByNum(97)
    # searchNextChannel()
    searchPerviousChannel()

    pass
