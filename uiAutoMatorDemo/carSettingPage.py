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


# *点击*设置系统音量[452,235][709,315]
def changeSystemVolume(num):
    print('start changeSystemVolume...')
    x_index = 476 + num * 7
    print('SystemVolume_x_index... ' + str(x_index) + ' => +' + str(num))
    d.click(x_index, 275)
    # print(d(className='android.widget.SeekBar', resourceId='com.imotor.settings:id/seekbar').info)
    print('start changeSystemVolume...')


# *点击*设置蓝牙通话音量[452,317][707,397]
def changeBTHFP(num):
    print('start changeBTHFP...')
    x_index = 476 + num * 7
    print('BTHFP_x_index... ' + str(x_index) + ' => +' + str(num))
    d.click(x_index, 357)
    # print(d(className='android.widget.SeekBar', resourceId='com.imotor.settings:id/seekbar').info)
    print('start changeBTHFP...')


# 点击OK
def clickOk():
    print('start clickOk...')
    d(text='OK').click()
    print('stop clickOk...')


# 点击Cancel
def clickCancel():
    print('start clickCancel...')
    d(text='Cancel').click()
    print('stop clickCancel...')


# 设置语速音量
def setSpeedSoundVolumes():
    print('start setSpeedSoundVolumes...')
    d(text='SPEED SOUND VOLUME').click()
    print('start setSpeedSoundVolumes...')


# 选择四种语速音量模式：CLOSE LOW MIDDLE HIGH
def clickSpeedSoundChoose(model):
    print('start clickSpeedSoundChoose...')
    if 'CLOSE' == model or 'LOW' == model or 'MIDDLE' == model or 'HIGH' == model:
        print('choose model ：' + model)
        d(text=model).click()
    else:
        print('* * * * model must be CLOSE|LOW|MIDDLE|HIGH * * * *')
    d(text='SPEED SOUND VOLUME').click()
    print('start clickSpeedSoundChoose...')


# 设置来电铃声
def setRingTone():
    print('start setRingTone...')
    d(text='RINGTONE').click()
    print('stop setRingTone...')


# 选择铃声
def chooseRingTone(ring):
    lastRing = 'Zeta'
    print('start chooseNoneRingTone...')
    while True:  # 滑动至顶
        if d(text='None').exists:
            print('Top')
            break
        else:
            swipeListViewOfToneDown()
    while d(text=ring).exists is not True:  # 开始往下滑动搜索是否含有此铃声
        if d(text=lastRing).exists:  # 判断是否到最后一首
            print(ring + ' is not exists ')
            d(text=ring).click
            break
        else:
            swipeListViewOfToneUp()
    d(text=ring).click()
    print('choose...' + ring)
    print('stop chooseNoneRingTone...')


# 铃声向上滑动
def swipeListViewOfToneUp():
    print('start swipeListViewOfToneUp...')
    d.swipe(500, 420, 500, 160)  # 滑动范围写死
    print('stop swipeListViewOfToneUp...')


# 铃声向下滑动
def swipeListViewOfToneDown():
    print('start swipeListViewOfToneDown...')
    d.swipe(500, 160, 500, 420)  # 滑动范围写死
    print('stop swipeListViewOfToneDown...')


# 设置按键声
def setKeyTone():
    print('start setKeyTone...')
    d(text='KEY TONE').click()
    print('stop setKeyTone...')


# 选择按键声
def chooseKeyTone(key):
    lastRing = 'KeypressReturn'
    print('start chooseKeyTone...')
    while True:  # 滑动至顶
        if d(text='NONE').exists:
            print('Top')
            break
        else:
            swipeListViewOfToneDown()
    while d(text=key).exists is not True:  # 开始往下滑动搜索是否含有此铃声
        if d(text=lastRing).exists:  # 判断是否到最后一首
            print(key + ' is not exists ')
            d(text=key).click
            break
        else:
            swipeListViewOfToneUp()
    d(text=key).click()
    print('choose...' + key)
    print('stop chooseKeyTone...')


# 设置音效（不知道为什么这个页面中这个控件的属性于标题一致，所以只能滑动到最下方后取坐标）
def setSoundEffect():
    print('start setSoundEffect...')
    swipeUpRightItems()
    swipeUpRightItems()
    d.click(600, 390)
    d(resourceId='android:id/title', text='SOUND EFFECT').click()
    print('stop setSoundEffect...')


# 设置音效
def setSoundEqualizer():
    print('start setSoundEqualizer...')
    d(text='SOUND EQUALIZER').click()
    print('stop setSoundEqualizer...')


# 选择音效模式
def chooseSoundEqualizerItem(style):
    print('start chooseSoundEqualizerItem...')
    listOfSoundStyle = ['CUSTOM', 'OFF', 'ROCK', 'POP', 'LIVE', 'DANCE', 'CLASSIC', 'SOFT']
    if style in listOfSoundStyle:
        print('change to ' + style)
        d(text=style).click()
    else:
        print(style + ' is not exites')
    print('stop chooseSoundEqualizerItem...')


# 调整音效传入参数：音轨，校准值
def changeSoundStyle(item, num):
    print('start changeSoundStyle...')
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
        print('num is not in [-15, 15]')
    else:
        if item in listOfItems:
            x = x_index.get(item)
            y = 190.3 + abs(num - 15) * 11.3  # y轴坐标 其实点位190.3
            print('x :' + str(x) + ' y : ' + str(y))  # 点击位置
            d.click(x, y)
        else:
            print('item is not exits')
    print('stop changeSoundStyle...')


# 设置响度
def setLoudness():
    print('start setLoudness...')
    d(text='LOUDNESS').click()
    print('stop setLoudness...')


# 设置响度音效
def chooseLoudnessEffect():
    print('start chooseLoudnessEffect...')
    d(text='LOUDNESS EFFECT').click()
    print('stop chooseLoudnessEffect...')


# 设置高频补偿
def chooseHighBoost():
    print('start chooseHighBoost...')
    d(text='HIGH BOOST').click()
    print('stop chooseHighBoost...')


# 设置响度音效值y[]
def changeLoundnessValue(num):
    print('start setLoundnessValue...')
    if num < -15 or num > 0:  # 参数检验
        print('num is not in [-15, 0]')
    else:
        x = 860 + num * 28
        y = 295.5  # y轴坐标 其实点位295.5
        print('x :' + str(x) + ' y : ' + str(y))  # 点击位置
        d.click(x, y)
    print('stop setLoundnessValue...')


# 设置中心频率
def setCenterFrequency(frequency):
    print('start setCenterFrequency...')
    if frequency in ['FLAT', '400HZ', '800HZ', '2400HZ']:
        d(text='CENTER FREQUENCY').click()
        d(text=frequency).click()
    else:
        print(frequency + ' is not exites')
    print('stop setCenterFrequency...')


# 设置亮度
def setDisplay(num):
    print('start setDisplay...')
    d(text='DISPLAY').click()
    d(text='BACKLIGHT BRIGHTNESS').click()
    x = 259 + num * 28
    y = 340.5
    d.click(x, y)
    print('print [' + str(x) + ', ' + str(y) + ']')
    print('stop setDisplay...')


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
