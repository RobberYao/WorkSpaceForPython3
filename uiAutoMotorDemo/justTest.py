from uiautomator import device as d
import unittest


# https://www.cnblogs.com/chenwolong/archive/2017/03/17/uiautomator.html
# link : http://xiaocong.github.io/slides/android-uiautomator-and-python/#/main
def openMusic():
    # d(text='Music').click()
    d(resourceId='com.android.launcher3:id/iv_launcher_music_play').click()


def enterMusic():
    d(resourceId='com.android.launcher3:id/iv_music_normal').click()


def openAutoPlay():
    d(text='AutoPlay').click()


def openSettings():
    d(text='Settings').click()


def openSettingsCh():
    d(text='音乐').click()


def openByIndex():
    d.click(935, 130)


def back():
    d.press.back()


def power():
    d.press.power()


# 点亮屏幕
def screenOn():
    d.screen.on()


# 关闭屏幕
def screenOff():
    d.screen.off()


def wakeUp():
    d.wakeup()


def sleep():
    d.sleep()


def home():
    d.press.home()


def volume_Up():
    d.press.volume_up()


def volume_Down():
    d.press.volume_down()


def volume_Mute():
    d.press.volume_mute()


def swipeLeft():
    d.swipe(100, 100, 1020, 100)


def swipeRight():
    d.swipe(1020, 100, 100, 100)


def screenShot():
    d.screenshot('screenShot.png')


if __name__ == '__main__':
    # d.screen.on()
    openMusic()
    # openByIndex()
    # back()
    # power()
    # openSettings()
    # openByIndex()
    # openSettingsCh()
    # screenOff()
    # wakeUp()
    # sleep()
    # print(d.info)
    # volume_Up()
    # volume_Down()
    # volume_Mute()
    # screenShot()
    # swipeLeft()
    # swipeLeft()
    # swipeRight()
    # openMusic()
