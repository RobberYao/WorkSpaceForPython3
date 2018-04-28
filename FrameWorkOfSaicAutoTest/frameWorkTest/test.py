#
from autoSpeechDemo.function import osPlay
from FrameWorkOfSaicAutoTest.uiAutoMator import carSettingPage
from FrameWorkOfSaicAutoTest.uiAutoMator import mainPage
from FrameWorkOfSaicAutoTest.uiAutoMator import musicModule
from FrameWorkOfSaicAutoTest.uiAutoMator import musicFilePage
from FrameWorkOfSaicAutoTest.uiAutoMator import settings
from FrameWorkOfSaicAutoTest.voiceAutoTest import osPlay
import time

if __name__ == '__main__':
    filePath3 = 'D:/mp3File/english/musicVoice/e_g_smartMirror.mp3'  # 语音播放音频的路径
    filePath4 = 'D:/mp3File/english/musicVoice/e_g_nextSong.mp3'
    # while True: #无限循环
    i = 0

    mainPage.enterAppMenuPage()
    mainPage.enterCarSetting()
    carSettingPage.enterVoiceItem()# **打开声音选项**
    carSettingPage.clickVolumeMute() # 点击静音
    carSettingPage.clickVolumeMute()
    carSettingPage.clickSpeedSoundChoose('CLOSE')
    carSettingPage.clickSpeedSoundChoose('CLOSE')

    carSettingPage.chooseRingTone('zeta')
    time.sleep(1)
    carSettingPage.chooseRingTone('zeta')
    carSettingPage.chooseRingTone('xxx')
    carSettingPage.chooseRingTone('zecccta')
    carSettingPage.chooseRingTone('www')
    carSettingPage.clickOk()
