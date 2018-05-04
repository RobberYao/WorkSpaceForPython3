#

from FrameWorkOfSaicAutoTest.uiAutoMator import mainPage
import time



if __name__ == '__main__':

    # while True: #无限循环
    i = 0
    for i in range(0, 2):  # 循环1次
        mainPage.swipeBottomLeft()  # 向左滑动导航栏，显示第二页导航栏
        mainPage.enterAppByIndex(295,520)  # 点击蓝牙音乐，蓝牙音乐界面显示
        mainPage.swipeBottomRight()  # 向右滑动导航栏，显示第一页导航栏
        mainPage.enterAppByIndex(295,520)  # 点击本地音乐，本地音乐界面显示
        mainPage.enterAppMenuPage()  # 点击app menu，app menu界面显示
        mainPage.enterBTMusic()  # 点击蓝牙音乐app，蓝牙音乐继续播放

        i + 1
        print('运行 ' + str(i) + ' 次')

    '''
    # eval('mainPage.cleanAllPage()')
'''