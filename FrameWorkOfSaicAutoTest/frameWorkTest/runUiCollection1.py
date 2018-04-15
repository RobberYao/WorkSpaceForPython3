#
from uiAutoMatorDemo import mainPage
from uiAutoMatorDemo import musicModule
from uiAutoMatorDemo import musicFilePage
from autoSpeechDemo.function import osPlay
import time

if __name__ == '__main__':
    filePath3 = 'D:/mp3File/english/musicVoice/e_g_CloseMusic.mp3'
    # eval('mainPage.home()')
    # eval('mainPage.minimization()')
    osPlay.playTimes(filePath3, 1)
    # eval('mainPage.cleanAllPage()')
