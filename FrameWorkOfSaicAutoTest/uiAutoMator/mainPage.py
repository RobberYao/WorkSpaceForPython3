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
    # time.sleep(2)
    print('end enterDataModule...')


# 进入app菜单页面
def enterAppMenuPage():
    home()
    print('start enterAppMenuPage...')
    d.click(510, 520)
    print('end enterAppMenuPage...')


# 进入Music页面中
def enterMusic():
    print('start enterMusic...')
    d(text='Music').click()
    time.sleep(2)
    print('end enterMusic...')


# 进入CarSetting页面中
def enterCarSetting():
    print('start enterCarSetting...')
    d(text='Car Setting').click()
    print('end enterCarSetting...')


# 进入settings页面中
def enterSettings():
    print('start enterSettings...')
    d(text='Settings').click()
    print('stop enterSettings...')


# 底层控件向左滑动
def swipeBottomLeft():
    print('start swipeBottomLeft...')
    d.swipe(890, 530, 130, 530)  # 滑动范围写死
    time.sleep(2)
    print('end swipeBottomLeft...')


# 底层控件向右滑动
def swipeBottomRight():
    print('start swipeBottomRight...')
    d.swipe(130, 530, 890, 530)  # 滑动范围写死
    time.sleep(2)
    print('end swipeBottomRight...')


# app页面向右滑动
def swipeRightInAppMenuPage():
    print('start swipeRightInAppMenuPage...')
    d.swipe(50, 275, 950, 275)  # 滑动范围写死
    time.sleep(2)
    print('end swipeRightInAppMenuPage...')


# app页面向左滑动
def swipeLeftInAppMenuPage():
    print('start swipeLeftInAppMenuPage...')
    d.swipe(950, 275, 50, 275)
    time.sleep(2)
    print('end swipeLeftInAppMenuPage...')


# 通过传入resourceId调用功能
def useMainPageFunction(resourceId):
    print('Start ' + resourceId + ' ...')
    d(resourceId=resourceId).click()
    time.sleep(5)
    print('end ' + resourceId + ' ...')


# 返回上一层
def back():
    print('start back...')
    d.press.back()
    print('stop back...')


# 返回首页
def home():
    print('start home...')
    d.press.home()
    print('start home...')
    time.sleep(1)


# 打开后台页面
def minimization():
    print('start minimization...')
    d.click(210, 30)
    print('stop minimization...')
    time.sleep(1)


# 关闭所有后台页面
def cleanAllPage():
    print('start cleanAllPage...')
    while d(className='android.widget.ImageButton', resourceId='com.android.systemui:id/recents_clear_all').exists:
        print('Page is cleanning')
        d.click(932, 137)
        # d(className='android.widget.ImageButton', resourceId='com.android.systemui:id/recents_clear_all').click
        time.sleep(4)
        '''
        if d(resourceId='com.android.systemui:id/recents_clear_all').exists:
            print('Page is cleanning')
            d(resourceId='com.android.systemui:id/recents_clear_all').click
        else:
            print('Page is not exists,back to homePage')
            home()
        '''
    # home()
    print('stop cleanAllPage...')
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
    # print(d.info)
    # enterAppMenuPage()
    # swipeLeftInAppMenuPage()
    # swipeRightInAppMenuPage()
    # swipeRightInAppMenuPage()
    # enterCarSetting()
    enterSettings()
