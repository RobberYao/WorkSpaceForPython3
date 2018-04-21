from uiautomator import device as d
import time
from FrameWorkOfSaicAutoTest.logModule import loggingConfig

lc = loggingConfig.loggingConfig()

# Settings页面向上滑动
def swipeUp():
    lc.consoleLog().info('start swipeUp...')
    lc.fileLog().info('start swipeUp...')
    d.swipe(200, 550, 200, 180)  # 滑动范围写死
    time.sleep(1)
    lc.consoleLog().info('end swipeUp...')
    lc.fileLog().info('end swipeUp...')


#  Settings页面向下滑动
def swipeDown():
    lc.fileLog().info('start swipeDown...')
    d.swipe(200, 180, 200, 550)
    time.sleep(1)
    lc.fileLog().info('end swipeDown...')


# 打开、关闭wifi
def changeWifiConnection():
    lc.fileLog().info('start changeWifiConnection...')
    d(className='android.widget.TextView', resourceId='com.android.settings:id/title').sibling(
        resourceId='com.android.settings:id/check_status').click()
    # d(className='android.widget.Switch', resourceId='com.android.settings:id/check_status', text='ON').click
    # d(text='ON').click
    time.sleep(1)
    lc.fileLog().info('end changeWifiConnection...')


# 进入wifi连接页面
def enterWifiConnectSetting():
    lc.fileLog().info('start enterWifiConnectSetting...')
    d(text='Wi‑Fi').click()
    time.sleep(1)
    lc.fileLog().info('end enterWifiConnectSetting...')


# 选择wifi名并登录
def loginWifiConnectByUserAndPassword(wifiName, password):
    # wifiName = 'SACO_VIP'
    # Fpassword = 'Cisco123'
    lc.fileLog().info('start loginWifiConnectByUserAndPassword...')
    try:
        d(resourceId='android:id/list', className='android.widget.ListView',
          packageName='com.android.settings').child_by_text(wifiName, text=wifiName).click()
        d(resourceId='com.android.settings:id/password', className='android.widget.EditText').set_text(password)
        d(text='Done').click()
        d(text='Connect').click()
    except:
        lc.fileLog().info(wifiName + 'is not exists')
    time.sleep(1)
    lc.fileLog().info('end loginWifiConnectByUserAndPassword...')


# 进入语言选择界面
def enterLanguageAndInput():
    text = 'Language and input'
    lc.fileLog().info('start enterLanguageAndInput...')
    d(text='Language and input').click()
    time.sleep(1)
    lc.fileLog().info('end enterLanguageAndInput...')


# 选择语言
def chooseLanguage(language):
    languageList = ['English', 'Español', '中文']
    lc.fileLog().info('start enterLanguageAndInput...')
    swipeDown()
    swipeDown()
    d(text='Language').click()
    if language in languageList:
        d(text=language).click()
    else:
        lc.fileLog().info(language + ' is not exists')
    time.sleep(1)
    lc.fileLog().info('end enterLanguageAndInput...')


if __name__ == '__main__':
    # swipeDown()
    # swipeDown()
    # swipeDown()
    # swipeUp()
    # swipeUp()
    # swipeUp()
    # changeWifiConnection()
    # enterWifiConnectSetting()
    # loginWifiConnectByUserAndPassword('SACO_VIP', 'Cisco123')
    # enterLanguageAndInput()
    chooseLanguage('Español')
