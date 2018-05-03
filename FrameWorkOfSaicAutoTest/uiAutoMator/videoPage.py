from uiautomator import device as d
import time
from FrameWorkOfSaicAutoTest.logModule import loggingConfig

lc = loggingConfig.loggingConfig()


# 点击屏幕
def clickScreen():
    lc.fileLog().info('start clickScreen...')
    d.click(700, 220)
    time.sleep(2)
    lc.fileLog().info('end clickScreen...')


# 退出视频
def back():
    lc.fileLog().info('start back...')
    d.click(845, 45)
    time.sleep(2)
    lc.fileLog().info('end back...')


# 页面向右滑动
def swipeLeft():
    lc.fileLog().info('start swipeLeft...')
    d.swipe(100, 300, 700, 300)  # 滑动范围写死
    time.sleep(2)
    lc.fileLog().info('end swipeLeft...')


# 页面向左滑动
def swipeRight():
    lc.fileLog().info('start swipeRight...')
    d.swipe(700, 300, 100, 300)  # 滑动范围写死
    time.sleep(2)
    lc.fileLog().info('end swipeRight...')


# 根据视频名称选择播放视频
def selectVideoByName(videoName):
    lc.fileLog().info('start selectVideoByName...')
    try:
        d(resourceId='com.clw.video:id/main_list', className='android.widget.ListView',
          packageName='com.clw.video').child_by_text(videoName, text=videoName).click()
        print('==' + videoName)
    except:
        lc.fileLog().info(videoName + 'is not exists')
    time.sleep(1)
    lc.fileLog().info('end selectVideoByName...')


# 点击右上角图标打开右边播放栏
def clickUpperRightCornerOpenRightList():
    lc.fileLog().info('start clickUpperRightCornerOpenRightList...')
    d.click(945, 45)
    time.sleep(2)
    lc.fileLog().info('end clickUpperRightCornerOpenRightList...')


# 点击右侧长条图标打开右边播放栏
def clickRightCornerOpenRightList():
    lc.fileLog().info('start clickRightCornerOpenRightList...')
    d.click(1000, 300)
    time.sleep(2)
    lc.fileLog().info('end clickRightCornerOpenRightList...')


# 滑动打开右边播放栏
def swipeOpenRightList():
    lc.fileLog().info('start swipeOpenRightList...')
    d.swipe(950, 300, 730, 300)  # 滑动范围写死
    time.sleep(2)
    lc.fileLog().info('end swipeOpenRightList...')


# 滑动关闭右边播放栏
def swipeCloseRightList():
    lc.fileLog().info('start swipeCloseRightList...')
    d.swipe(730, 300, 950, 300)  # 滑动范围写死
    time.sleep(2)
    lc.fileLog().info('end swipeCloseRightList...')


# 点击中央大图片改变播放状态
def changeVideoStatusByBigIcon():
    lc.fileLog().info('start changeVideoStatusByBigIcon...')
    d.click(515, 300)
    time.sleep(2)
    lc.fileLog().info('end changeVideoStatusByBigIcon...')


# 点击左下小图片改变播放状态
def changeVideoStatusByBigIcon():
    lc.fileLog().info('start changeVideoStatusByBigIcon...')
    d.click(140, 575)
    time.sleep(2)
    lc.fileLog().info('end changeVideoStatusByBigIcon...')


# 播放下个视频
def getNextVideo():
    lc.fileLog().info('start getNextVideo...')
    d.click(215, 575)
    lc.fileLog().info('stop getNextVideo...')
    time.sleep(2)


# 播放上个视频
def getPerviousVideo():
    lc.fileLog().info('start getPerviousVideo...')
    d.click(70, 575)
    lc.fileLog().info('stop getPerviousVideo...')
    time.sleep(2)


# 静音/关闭静音
def videoMute():
    lc.fileLog().info('start videoMute...')
    d.click(950, 575)
    lc.fileLog().info('stop videoMute...')
    time.sleep(2)


if __name__ == '__main__':
    # swipeLeft()
    # swipeRight()
    # swipeRight()
    # swipeRight()
    # swipeLeft()
    #
    # selectVideoByName('01. 维密秀2016.mp4')
    #
    # selectVideoByName('02. 极清展示—烤鸭.mp4')
    pass
