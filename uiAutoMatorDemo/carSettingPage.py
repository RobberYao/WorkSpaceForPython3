from uiautomator import device as d
import time


# carSetting页面左边栏向上滑动
def swipeUpLeftItems():
    print('start swipeUpLeftItems...')
    d.swipe(100, 560, 100, 100)  # 滑动范围写死
    time.sleep(1)
    print('end swipeUpLeftItems...')


# carSetting页面左边栏向下滑动
def swipeDownLeftItems():
    print('start swipeDownLeftItems...')
    d.swipe(100, 100, 100, 560)
    time.sleep(1)
    print('end swipeDownLeftItems...')


# carSetting页面右边栏向上滑动
def swipeUpRightItems():
    print('start swipeUpRightItems...')
    d.swipe(900, 560, 900, 100)  # 滑动范围写死
    time.sleep(1)
    print('end swipeUpRightItems...')


# carSetting页面右边栏向下滑动
def swipeDownRightItems():
    print('start swipeDownRightItems...')
    d.swipe(900, 100, 900, 560)  # 滑动范围写死
    time.sleep(1)
    print('end swipeDownRightItems...')


# **打开蓝牙选项**
def enterBlueToothItem():
    print('start enterBlueToothItem...')
    d(text='BLUETOOTH').click()
    time.sleep(1)
    print('stop enterBlueToothItem...')


# 点击蓝牙自动连接选项
def clickAutoConnectbutton():
    print('start clickAutoConnectbutton...')
    d(className='android.widget.TextView', text='AUTO CONNECT').sibling(
        className='android.widget.CompoundButton').click()
    print('stop clickAutoConnectbutton...')


# 点击自动接听选项
def clickAnswerAutoMatically():
    print('start clickAnswerAutoMatically...')
    d(className='android.widget.TextView', text='ANSWER AUTOMATICALLY').sibling(
        className='android.widget.CompoundButton').click()
    print('stop clickAnswerAutoMatically...')


# **打开声音选项**
def enterVoiceItem():
    print('start enterVoiceItem...')
    d(text='VOICE').click()
    time.sleep(1)
    print('stop enterVoiceItem...')


# 点击静音
def clickVolumeMute():
    print('start clickVolumeMute...')
    d(className='android.widget.CheckBox').click()
    time.sleep(1)
    print('stop clickVolumeMute...')


# 设置默认音量
def setDefaultVolumes():
    print('start setDefaultVolumes...')
    d(text='DEFAULT VOLUMES').click()
    print('start setDefaultVolumes...')


# 设置系统音量
def changeSystemVolume():
    print('start changeSystemVolume...')
    print(d(className='android.widget.SeekBar', resourceId='com.imotor.settings:id/seekbar').info)
    print('start changeSystemVolume...')


# 设置蓝牙通话音量
def changeBTHFP():
    pass


if __name__ == '__main__':
    # swipeDownLeftItems()
    # swipeDownLeftItems()
    # swipeUpLeftItems()
    # swipeUpLeftItems()
    # swipeUpRightItems()
    # swipeUpRightItems()
    # swipeDownRightItems()
    # swipeDownRightItems()
    # clickAutoConnectbutton()
    # clickAnswerAutoMatically()
    # clickVolumeMute()
    # setDefaultVolumes()
    changeSystemVolume()
