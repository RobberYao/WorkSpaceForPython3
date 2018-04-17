from uiautomator import device as d
import time


# Settings页面向上滑动
def swipeUp():
    print('start swipeUp...')
    d.swipe(200, 550, 200, 180)  # 滑动范围写死
    time.sleep(1)
    print('end swipeUp...')


#  Settings页面向下滑动
def swipeDown():
    print('start swipeDown...')
    d.swipe(200, 180, 200, 550)
    time.sleep(1)
    print('end swipeDown...')


# 打开、关闭wifi
def changeWifiConnection():
    print('start changeWifiConnection...')
    d(className='android.widget.TextView', resourceId='com.android.settings:id/title').sibling(
        resourceId='com.android.settings:id/check_status').click()
    # d(className='android.widget.Switch', resourceId='com.android.settings:id/check_status', text='ON').click
    # d(text='ON').click
    time.sleep(1)
    print('end changeWifiConnection...')


# 进入wifi连接页面
def enterWifiConnectSetting():
    print('start enterWifiConnectSetting...')
    d(text='Wi‑Fi').click()
    time.sleep(1)
    print('end enterWifiConnectSetting...')


# 选择wifi名并登录
def loginWifiConnectByUserAndPassword(wifiName, password):
    # wifiName = 'SACO_VIP'
    # Fpassword = 'Cisco123'
    print('start loginWifiConnectByUserAndPassword...')
    try:
        d(resourceId='android:id/list', className='android.widget.ListView',
          packageName='com.android.settings').child_by_text(wifiName, text=wifiName).click()
        d(resourceId='com.android.settings:id/password', className='android.widget.EditText').set_text(password)
        d(text='Done').click()
        d(text='Connect').click()
    except:
        print(wifiName + 'is not exists')
    time.sleep(1)
    print('end loginWifiConnectByUserAndPassword...')


# 进入语言选择界面
def enterLanguageAndInput():
    text = 'Language and input'
    print('start enterLanguageAndInput...')
    d(text='Language and input').click()
    time.sleep(1)
    print('end enterLanguageAndInput...')


# 选择语言
def chooseLanguage(language):
    languageList = ['English', 'Español', '中文']
    print('start enterLanguageAndInput...')
    swipeDown()
    swipeDown()
    d(text='Language').click()
    if language in languageList:
        d(text=language).click()
    else:
        print(language + ' is not exists')
    time.sleep(1)
    print('end enterLanguageAndInput...')


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
