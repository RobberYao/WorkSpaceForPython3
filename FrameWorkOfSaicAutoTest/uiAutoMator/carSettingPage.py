from uiautomator import device as d
import time
from FrameWorkOfSaicAutoTest.logModule import loggingConfig

lc = loggingConfig.loggingConfig()

# carSetting页面左边栏向上滑动
def swipeUpLeftItems():
    lc.fileLog().info('start swipeUpLeftItems...')
    d.swipe(100, 560, 100, 100)  # 滑动范围写死
    time.sleep(1)
    lc.fileLog().info('end swipeUpLeftItems...')


# carSetting页面左边栏向下滑动
def swipeDownLeftItems():
    lc.fileLog().info('start swipeDownLeftItems...')
    d.swipe(100, 100, 100, 560)
    time.sleep(1)
    lc.fileLog().info('end swipeDownLeftItems...')


# carSetting页面右边栏向上滑动
def swipeUpRightItems():
    lc.fileLog().info('start swipeUpRightItems...')
    d.swipe(900, 560, 900, 100)  # 滑动范围写死
    time.sleep(1)
    lc.fileLog().info('end swipeUpRightItems...')


# carSetting页面右边栏向下滑动
def swipeDownRightItems():
    lc.fileLog().info('start swipeDownRightItems...')
    d.swipe(900, 100, 900, 560)  # 滑动范围写死
    time.sleep(1)
    lc.fileLog().info('end swipeDownRightItems...')


# **打开蓝牙选项**
def enterBlueToothItem():
    lc.fileLog().info('start enterBlueToothItem...')
    d(text='BLUETOOTH').click()
    time.sleep(1)
    lc.fileLog().info('stop enterBlueToothItem...')


# 点击蓝牙自动连接选项
def clickAutoConnectbutton():
    lc.fileLog().info('start clickAutoConnectbutton...')
    d(className='android.widget.TextView', text='AUTO CONNECT').sibling(
        className='android.widget.CompoundButton').click()
    lc.fileLog().info('stop clickAutoConnectbutton...')


# 点击自动接听选项
def clickAnswerAutoMatically():
    lc.fileLog().info('start clickAnswerAutoMatically...')
    d(className='android.widget.TextView', text='ANSWER AUTOMATICALLY').sibling(
        className='android.widget.CompoundButton').click()
    lc.fileLog().info('stop clickAnswerAutoMatically...')


# **打开声音选项**
def enterVoiceItem():
    lc.fileLog().info('start enterVoiceItem...')
    d(text='VOICE').click()
    time.sleep(1)
    lc.fileLog().info('stop enterVoiceItem...')


# 点击静音
def clickVolumeMute():
    lc.fileLog().info('start clickVolumeMute...')
    d(className='android.widget.CheckBox').click()
    time.sleep(1)
    lc.fileLog().info('stop clickVolumeMute...')


# 设置默认音量
def setDefaultVolumes():
    lc.fileLog().info('start setDefaultVolumes...')
    d(text='DEFAULT VOLUMES').click()
    lc.fileLog().info('start setDefaultVolumes...')


# *点击*设置系统音量[452,235][709,315]
def changeSystemVolume(num):
    lc.fileLog().info('start changeSystemVolume...')
    x_index = 476 + num * 7
    lc.fileLog().info('SystemVolume_x_index... ' + str(x_index) + ' => +' + str(num))
    d.click(x_index, 275)
    # lc.fileLog().info(d(className='android.widget.SeekBar', resourceId='com.imotor.settings:id/seekbar').info)
    lc.fileLog().info('start changeSystemVolume...')


# *点击*设置蓝牙通话音量[452,317][707,397]
def changeBTHFP(num):
    lc.fileLog().info('start changeBTHFP...')
    x_index = 476 + num * 7
    lc.fileLog().info('BTHFP_x_index... ' + str(x_index) + ' => +' + str(num))
    d.click(x_index, 357)
    # lc.fileLog().info(d(className='android.widget.SeekBar', resourceId='com.imotor.settings:id/seekbar').info)
    lc.fileLog().info('start changeBTHFP...')


# 点击OK
def clickOk():
    lc.fileLog().info('start clickOk...')
    d(text='OK').click()
    lc.fileLog().info('stop clickOk...')


# 点击Cancel
def clickCancel():
    lc.fileLog().info('start clickCancel...')
    d(text='Cancel').click()
    lc.fileLog().info('stop clickCancel...')


# 设置语速音量
def setSpeedSoundVolumes():
    lc.fileLog().info('start setSpeedSoundVolumes...')
    d(text='SPEED SOUND VOLUME').click()
    lc.fileLog().info('start setSpeedSoundVolumes...')


# 选择四种语速音量模式：CLOSE LOW MIDDLE HIGH
def clickSpeedSoundChoose(model):
    lc.fileLog().info('start clickSpeedSoundChoose...')
    if 'CLOSE' == model or 'LOW' == model or 'MIDDLE' == model or 'HIGH' == model:
        lc.fileLog().info('choose model ：' + model)
        d(text=model).click()
    else:
        lc.fileLog().info('* * * * model must be CLOSE|LOW|MIDDLE|HIGH * * * *')
    d(text='SPEED SOUND VOLUME').click()
    lc.fileLog().info('start clickSpeedSoundChoose...')


# 设置来电铃声
def setRingTone():
    lc.fileLog().info('start setRingTone...')
    d(text='RINGTONE').click()
    lc.fileLog().info('stop setRingTone...')


# 选择铃声
def chooseRingTone(ring):
    lastRing = 'Zeta'
    lc.fileLog().info('start chooseNoneRingTone...')
    while True:  # 滑动至顶
        if d(text='None').exists:
            lc.fileLog().info('Top')
            break
        else:
            swipeListViewOfToneDown()
    while d(text=ring).exists is not True:  # 开始往下滑动搜索是否含有此铃声
        if d(text=lastRing).exists:  # 判断是否到最后一首
            lc.fileLog().info(ring + ' is not exists ')
            d(text=ring).click
            break
        else:
            swipeListViewOfToneUp()
    d(text=ring).click()
    lc.fileLog().info('choose...' + ring)
    lc.fileLog().info('stop chooseNoneRingTone...')


# 铃声向上滑动
def swipeListViewOfToneUp():
    lc.fileLog().info('start swipeListViewOfToneUp...')
    d.swipe(500, 420, 500, 160)  # 滑动范围写死
    lc.fileLog().info('stop swipeListViewOfToneUp...')


# 铃声向下滑动
def swipeListViewOfToneDown():
    lc.fileLog().info('start swipeListViewOfToneDown...')
    d.swipe(500, 160, 500, 420)  # 滑动范围写死
    lc.fileLog().info('stop swipeListViewOfToneDown...')


# 设置按键声
def setKeyTone():
    lc.fileLog().info('start setKeyTone...')
    d(text='KEY TONE').click()
    lc.fileLog().info('stop setKeyTone...')


# 选择按键声
def chooseKeyTone(key):
    lastRing = 'KeypressReturn'
    lc.fileLog().info('start chooseKeyTone...')
    while True:  # 滑动至顶
        if d(text='NONE').exists:
            lc.fileLog().info('Top')
            break
        else:
            swipeListViewOfToneDown()
    while d(text=key).exists is not True:  # 开始往下滑动搜索是否含有此铃声
        if d(text=lastRing).exists:  # 判断是否到最后一首
            lc.fileLog().info(key + ' is not exists ')
            d(text=key).click
            break
        else:
            swipeListViewOfToneUp()
    d(text=key).click()
    lc.fileLog().info('choose...' + key)
    lc.fileLog().info('stop chooseKeyTone...')


# 设置音效（不知道为什么这个页面中这个控件的属性于标题一致，所以只能滑动到最下方后取坐标）
def setSoundEffect():
    lc.fileLog().info('start setSoundEffect...')
    swipeUpRightItems()
    swipeUpRightItems()
    d.click(600, 390)
    d(resourceId='android:id/title', text='SOUND EFFECT').click()
    lc.fileLog().info('stop setSoundEffect...')


# 设置音效平衡
def setSoundEqualizer():
    lc.fileLog().info('start setSoundEqualizer...')
    d(text='SOUND EQUALIZER').click()
    lc.fileLog().info('stop setSoundEqualizer...')


# 选择音效模式
def chooseSoundEqualizerItem(style):
    lc.fileLog().info('start chooseSoundEqualizerItem...')
    listOfSoundStyle = ['CUSTOM', 'OFF', 'ROCK', 'POP', 'LIVE', 'DANCE', 'CLASSIC', 'SOFT']
    if style in listOfSoundStyle:
        lc.fileLog().info('change to ' + style)
        d(text=style).click()
    else:
        lc.fileLog().info(style + ' is not exites')
    lc.fileLog().info('stop chooseSoundEqualizerItem...')


# 调整音效传入参数：音轨，校准值
def changeSoundStyle(item, num):
    lc.fileLog().info('start changeSoundStyle...')
    listOfItems = ['60', '100', '200', '500', '1.5K', '2.5K', '10K', '15K', '17.5K']  # 音轨
    x_index = {
        '60': 150,
        '100': 240,
        '200': 330,
        '500': 420,
        '1.5K': 510,
        '2.5K': 600,
        '10K': 690,
        '15K': 780,
        '17.5K': 870
    }  # 音轨对应横坐标、纵坐标[529.3,190.3] 每当11.3 共30档

    if num < -15 or num > 15:  # 参数检验
        lc.fileLog().info('num is not in [-15, 15]')
    else:
        if item in listOfItems:
            x = x_index.get(item)
            y = 190.3 + abs(num - 15) * 11.3  # y轴坐标 其实点位190.3
            lc.fileLog().info('x :' + str(x) + ' y : ' + str(y))  # 点击位置
            d.click(x, y)
        else:
            lc.fileLog().info('item is not exits')
    lc.fileLog().info('stop changeSoundStyle...')


# 设置响度
def setLoudness():
    lc.fileLog().info('start setLoudness...')
    d(text='LOUDNESS').click()
    lc.fileLog().info('stop setLoudness...')


# 设置响度音效
def chooseLoudnessEffect():
    lc.fileLog().info('start chooseLoudnessEffect...')
    d(text='LOUDNESS EFFECT').click()
    lc.fileLog().info('stop chooseLoudnessEffect...')


# 设置高频补偿
def chooseHighBoost():
    lc.fileLog().info('start chooseHighBoost...')
    d(text='HIGH BOOST').click()
    lc.fileLog().info('stop chooseHighBoost...')


# 设置响度音效值范围[-15,0]
def changeLoundnessValue(num):
    lc.fileLog().info('start setLoundnessValue...')
    if num < -15 or num > 0:  # 参数检验
        lc.fileLog().info('num is not in [-15, 0]')
    else:
        x = 860 + num * 28
        y = 295.5  # y轴坐标 其实点位295.5
        lc.fileLog().info('x :' + str(x) + ' y : ' + str(y))  # 点击位置
        d.click(x, y)
    lc.fileLog().info('stop setLoundnessValue...')


# 设置中心频率
def setCenterFrequency(frequency):
    lc.fileLog().info('start setCenterFrequency...')
    if frequency in ['FLAT', '400HZ', '800HZ', '2400HZ']:
        d(text='CENTER FREQUENCY').click()
        d(text=frequency).click()
    else:
        lc.fileLog().info(frequency + ' is not exites')
    lc.fileLog().info('stop setCenterFrequency...')


# 设置亮度范围[0, 19]
def setDisplay(num):
    lc.fileLog().info('start setDisplay...')
    d(text='DISPLAY').click()
    d(text='BACKLIGHT BRIGHTNESS').click()
    x = 259 + num * 28
    y = 340.5
    d.click(x, y)
    lc.fileLog().info('lc.fileLog().info [' + str(x) + ', ' + str(y) + ']')
    lc.fileLog().info('stop setDisplay...')


if __name__ == '__main__':
    # chooseLoudnessEffect()
    # chooseHighBoost()
    # setCenterFrequency('FLAT')
    clickCancel()
    setDisplay(19)
    clickOk()

    # changeLoundnessValue(0)
# chooseSoundEqualizerItem('CUSTOM')
# chooseSoundEqualizerItem('OFF')
# chooseSoundEqualizerItem('ROCK')
# chooseSoundEqualizerItem('POP')
# chooseSoundEqualizerItem('LIVE')
# chooseSoundEqualizerItem('DANCE')
#
#    changeSoundStyle('60', -5)
#
# changeSoundStyle('100', -6)
# changeSoundStyle('200', -7)
# changeSoundStyle('500', -8)
# changeSoundStyle('1.5K', -9)
# changeSoundStyle('2.5K', -10)
# changeSoundStyle('10K', -11)
# changeSoundStyle('15K', -12)
# changeSoundStyle('17.5K', -13)

# changeSoundStyle('60', 5)
# changeSoundStyle('100', 6)
# changeSoundStyle('200', 7)adb
# changeSoundStyle('500', 8)
# changeSoundStyle('1.5K', 9)
# changeSoundStyle('2.5K', 10)
# changeSoundStyle('10K', 11)
# changeSoundStyle('15K', 12)
# changeSoundStyle('17.5K', 13)

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
# changeSystemVolume(15)
# changeBTHFP(15)
# clickOk()
# clickCancel()
# setSpeedSoundVolumes()
# time.sleep(1)
# clickSpeedSoundChoose('close')
# time.sleep(1)
# setSpeedSoundVolumes()
# time.sleep(1)
# clickSpeedSoundChoose('LOW')
# time.sleep(1)
# setSpeedSoundVolumes()
# time.sleep(1)
# clickSpeedSoundChoose('MIDDLE')
# time.sleep(1)
# setSpeedSoundVolumes()
# time.sleep(1)
# clickSpeedSoundChoose('HIGH')
# time.sleep(1)
# setRingTone()
# setKeyTone()
# chooseNoneRingTone('Backroad')
# clickOk()
# time.sleep(1)
# swipeListViewOfToneUp()
# time.sleep(1)
# swipeListViewOfToneDown()
# setSoundEffect()
# setSoundEqualizer()
# chooseKeyTone('KeypressDelete')
# clickCancel()
