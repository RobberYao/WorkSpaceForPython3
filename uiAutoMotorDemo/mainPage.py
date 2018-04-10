from uiautomator import device as d
import time


# link : http://xiaocong.github.io/slides/android-uiautomator-and-python/#/main
# 主页面方法


# 播放、暂停音乐
def changeMusicStatus():
    # d(text='Music').click()
    print('start changeMusicStatus...')
    d(resourceId='com.android.launcher3:id/iv_launcher_music_play').click()
    time.sleep(1)
    print('end changeMusicStatus...')


# 进入音乐页面
def enterMusicModule():
    print('start enterMusicModule...')
    d(resourceId='com.android.launcher3:id/iv_music_normal').click()
    time.sleep(1)
    print('end enterMusicModule...')


# 进入日期设置页面
def enterDataModule():
    print('start enterDataModule...')
    d(resourceId='com.android.launcher3:id/clock').click()
    #time.sleep(2)
    print('end enterDataModule...')


# 底层控件向左滑动
def swipeLeft():
    print('start swipeLeft...')
    d.swipe(890, 530, 130, 530)  # 滑动范围写死
    time.sleep(2)
    print('end swipeLeft...')


# 底层控件向右滑动
def swipeRight():
    print('start swipeRight...')
    d.swipe(130, 530, 890, 530)  # 滑动范围写死
    time.sleep(2)
    print('end swipeRight...')


# 通过传入resourceId调用功能
def useMainPageFunction(resourceId):
    print('Start ' + resourceId + ' ...')
    d(resourceId=resourceId).click()
    time.sleep(5)
    print('end ' + resourceId + ' ...')


def back():
    d.press.back()


if __name__ == '__main__':
    eval('back()')
    eval('swipeLeft()')
    # resourceId = 'com.android.launcher3:id/iv_launcher_music_play'
    # swipeLeft()
    # swipeRight()
    # enterDataModule()
    # useMainPageFunction(resourceId)
