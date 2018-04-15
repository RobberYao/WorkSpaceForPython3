#
from uiAutoMatorDemo import mainPage
from uiAutoMatorDemo import musicModule
from uiAutoMatorDemo import musicFilePage
import time

if __name__ == '__main__':
    while True:
        eval('mainPage.home()')
        eval('mainPage.minimization()')
        eval('mainPage.cleanAllPage()')
        eval('mainPage.swipeBottomLeft()')
        eval('mainPage.swipeBottomRight()')
        eval('mainPage.enterMusicModule()')
        eval('musicModule.getNextSongByLocation()')
        time.sleep(10)
        eval('musicModule.getPreviousSongByLocation()')
        time.sleep(10)
        eval('musicModule.enterMusicFilePage()')
        eval('musicFilePage.selectByMyFavorite()')
        eval('musicFilePage.selectByPlayTimes()')
        eval('musicFilePage.selectByFolders()')
        eval('musicFilePage.openMusicPackageByName(\'msc\')')
        eval('musicModule.getNextSongByLocation()')
        time.sleep(10)
        eval('musicModule.forward()')
        time.sleep(2)
        eval('musicModule.backOff()')
        eval('musicModule.changePlayStatusByLocation()')
        eval('musicModule.changePlayStatusByLocation()')
