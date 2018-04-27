from uiautomator import device as d
import time
from FrameWorkOfSaicAutoTest.logModule import loggingConfig

lc = loggingConfig.loggingConfig()


# link : http://xiaocong.github.io/slides/android-uiautomator-and-python/#/main
# 主页面方法


# 播放、暂停音乐
def changeMusicStatus():
    # d(text='Music').click()
    lc.fileLog().info('start changeMusicStatus...')
    d(resourceId='com.android.launcher3:id/iv_launcher_music_play').click()
    time.sleep(1)
    lc.fileLog().info('end changeMusicStatus...')


# 进入音乐页面
def enterMusicModule():
    lc.fileLog().info('start enterMusicModule...')
    d(resourceId='com.android.launcher3:id/iv_music_normal').click()
    time.sleep(1)
    lc.fileLog().info('end enterMusicModule...')


# 进入日期设置页面
def enterDataModule():
    lc.fileLog().info('start enterDataModule...')
    d(resourceId='com.android.launcher3:id/clock').click()
    # time.sleep(2)
    lc.fileLog().info('end enterDataModule...')


# 进入app菜单页面
def enterAppMenuPage():
    home()
    lc.fileLog().info('start enterAppMenuPage...')
    d.click(510, 520)
    lc.fileLog().info('end enterAppMenuPage...')


# 进入Music页面中
def enterMusic():
    lc.fileLog().info('start enterMusic...')
    d(text='Music').click()
    time.sleep(2)
    lc.fileLog().info('end enterMusic...')


# 进入CarSetting页面中
def enterCarSetting():
    lc.fileLog().info('start enterCarSetting...')
    d(text='Car Setting').click()
    lc.fileLog().info('end enterCarSetting...')


# 进入settings页面中
def enterSettings():
    lc.fileLog().info('start enterSettings...')
    d(text='Settings').click()
    lc.fileLog().info('stop enterSettings...')


# 进入蓝牙音乐页面中
def enterBTMusic():
    lc.fileLog().info('start enterBTMusic...')
    d(text='BT-Music').click()
    lc.fileLog().info('stop enterBTMusic...')


# 底层控件向左滑动
def swipeBottomLeft():
    lc.fileLog().info('start swipeBottomLeft...')
    d.swipe(890, 530, 130, 530)  # 滑动范围写死
    time.sleep(2)
    lc.fileLog().info('end swipeBottomLeft...')


# 底层控件向右滑动
def swipeBottomRight():
    lc.fileLog().info('start swipeBottomRight...')
    d.swipe(130, 530, 890, 530)  # 滑动范围写死
    time.sleep(2)
    lc.fileLog().info('end swipeBottomRight...')


# app页面向右滑动
def swipeRightInAppMenuPage():
    lc.fileLog().info('start swipeRightInAppMenuPage...')
    d.swipe(50, 275, 950, 275)  # 滑动范围写死
    time.sleep(2)
    lc.fileLog().info('end swipeRightInAppMenuPage...')


# app页面向左滑动
def swipeLeftInAppMenuPage():
    lc.fileLog().info('start swipeLeftInAppMenuPage...')
    d.swipe(950, 275, 50, 275)
    time.sleep(2)
    lc.fileLog().info('end swipeLeftInAppMenuPage...')


# 通过传入resourceId调用功能
def useMainPageFunction(resourceId):
    lc.fileLog().info('Start ' + resourceId + ' ...')
    d(resourceId=resourceId).click()
    time.sleep(5)
    lc.fileLog().info('end ' + resourceId + ' ...')


# 返回上一层
def back():
    lc.fileLog().info('start back...')
    d.press.back()
    lc.fileLog().info('stop back...')


# 返回首页
def home():
    lc.fileLog().info('start home...')
    d.press.home()
    lc.fileLog().info('start home...')
    time.sleep(1)


# 打开后台页面
def minimization():
    lc.fileLog().info('start minimization...')
    d.click(210, 30)
    lc.fileLog().info('stop minimization...')
    time.sleep(1)


# 关闭所有后台页面
def cleanAllPage():
    lc.fileLog().info('start cleanAllPage...')
    while d(className='android.widget.ImageButton', resourceId='com.android.systemui:id/recents_clear_all').exists:
        lc.fileLog().info('Page is cleanning')
        d.click(932, 137)
        # d(className='android.widget.ImageButton', resourceId='com.android.systemui:id/recents_clear_all').click
        time.sleep(4)
        '''
        if d(resourceId='com.android.systemui:id/recents_clear_all').exists:
            lc.fileLog().info('Page is cleanning')
            d(resourceId='com.android.systemui:id/recents_clear_all').click
        else:
            lc.fileLog().info('Page is not exists,back to homePage')
            home()
        '''
    # home()
    lc.fileLog().info('stop cleanAllPage...')
    time.sleep(1)


if __name__ == '__main__':
    # eval('back()')
    # eval('swipeLeft()')
    # resourceId = 'com.android.launcher3:id/iv_launcher_music_play'
    # swipeLeft()
    # swipeRight()
    # enterDataModule()
    # useMainPageFunction(resourceId)
    # home()
    # minimization()
    # cleanAllPage()
    # lc.fileLog().info(d.info)
    # enterAppMenuPage()
    # swipeLeftInAppMenuPage()
    # swipeRightInAppMenuPage()
    # swipeRightInAppMenuPage()
    # enterCarSetting()
    enterSettings()
