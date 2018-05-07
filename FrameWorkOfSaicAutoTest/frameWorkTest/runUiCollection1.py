# ***脚本模版***


from autoSpeechDemo.function import osPlay
from FrameWorkOfSaicAutoTest.uiAutoMator import carSettingPage
from FrameWorkOfSaicAutoTest.uiAutoMator import mainPage
from FrameWorkOfSaicAutoTest.uiAutoMator import musicModule
from FrameWorkOfSaicAutoTest.uiAutoMator import musicFilePage
from FrameWorkOfSaicAutoTest.uiAutoMator import settings
from FrameWorkOfSaicAutoTest.voiceAutoTest import osPlay
from FrameWorkOfSaicAutoTest.logModule import loggingConfig

lc = loggingConfig.loggingConfig()
import time

if __name__ == '__main__':

    filePath3 = 'D:/mp3File/english/musicVoice/e_g_smartMirror.mp3'  # 语音播放音频的路径
    filePath4 = 'D:/mp3File/english/musicVoice/e_g_nextSong.mp3'

    # while True: #无限循环
    i = 1  # 起始次数
    k = 10  # 循环次数（按需求可修改）
    while i <= k:  # 循环10次
        mainPage.minimization()
        mainPage.cleanAllPage()

        mainPage.home()
        osPlay.play(filePath3)
        osPlay.play(filePath4)
        musicModule.enterMusicFilePage()

        mainPage.swipeBottomLeft()
        mainPage.swipeBottomRight()
        mainPage.enterAppMenuPage()

        mainPage.swipeLeftInAppMenuPage()
        mainPage.swipeRightInAppMenuPage()
        mainPage.enterMusic()
        osPlay.playTimes(filePath3, 1)

        osPlay.play('D:/mp3File/english/musicVoice/e_g_nextSong.mp3')

        musicModule.enterMusicFilePage()
        musicFilePage.selectByMyFavorite()
        musicFilePage.selectByPlayTimes()
        musicFilePage.selectByFolders()
        musicFilePage.openMusicPackageByName('msc')
        musicModule.getNextSongByLocation()
        time.sleep(10)
        musicModule.getPreviousSongByLocation()
        time.sleep(10)
        musicModule.backOff()
        musicModule.changePlayStatusByLocation()
        musicModule.forward()
        musicModule.enterSoundEffectPage()
        carSettingPage.changeSoundStyle('100', -6)
        carSettingPage.changeSoundStyle('200', -7)
        carSettingPage.changeSoundStyle('500', -8)
        carSettingPage.changeSoundStyle('1.5K', -9)
        carSettingPage.changeSoundStyle('2.5K', -10)
        carSettingPage.changeSoundStyle('10K', -11)
        carSettingPage.changeSoundStyle('15K', -12)
        carSettingPage.changeSoundStyle('17.5K', -13)
        carSettingPage.changeSoundStyle('60', 5)
        carSettingPage.changeSoundStyle('100', 6)
        carSettingPage.changeSoundStyle('200', 7)
        carSettingPage.changeSoundStyle('500', 8)
        carSettingPage.changeSoundStyle('1.5K', 9)
        carSettingPage.changeSoundStyle('2.5K', 10)
        carSettingPage.changeSoundStyle('10K', 11)
        carSettingPage.changeSoundStyle('15K', 12)
        carSettingPage.changeSoundStyle('17.5K', 13)

        lc.fileLog().info('has run ' + str(i) + ' times')  # 日志文件记录当前运行次数
        print('has run ' + str(i) + ' times')  # 控制台输出当前运行次数
        i = i + 1  # 运行次数累加1
    else:
        lc.fileLog().info('run ' + str(i - 1) + ' times complete ')  # 日志文件记录总运行次数
        print('run ' + str(i - 1) + ' times complete ')  # 控制台输出总运行次数
