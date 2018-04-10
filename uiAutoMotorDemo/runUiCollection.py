#
from uiAutoMotorDemo import mainPage
from uiAutoMotorDemo import musicModule
from uiAutoMotorDemo import musicFilePage
import time

if __name__ == '__main__':
    eval('mainPage.swipeLeft()')
    eval('mainPage.swipeRight()')
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
    eval('musicModule.changePlayStatusByLocation()')
    eval('musicModule.changePlayStatusByLocation()')
