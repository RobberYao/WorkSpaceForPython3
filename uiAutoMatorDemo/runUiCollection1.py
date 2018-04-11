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