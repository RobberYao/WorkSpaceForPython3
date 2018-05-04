#

from FrameWorkOfSaicAutoTest.uiAutoMator import mainPage
from FrameWorkOfSaicAutoTest.uiAutoMator import bTMusic
import time



if __name__ == '__main__':

    # while True: #无限循环
    i = 0
    for i in range(0, 2):  # 循环1次
        mainPage.enterAppMenuPage()  # app menu界面显示
        mainPage.enterBTMusic()  # 蓝牙音乐界面显示
        time.sleep(2)
        bTMusic.changePlayStatus()  # 暂停
        bTMusic.getBTNextSong()  # 下一首 播放
        time.sleep(2)
        bTMusic.changePlayStatus()  # 暂停
        bTMusic.getBTPerviousSong()  # 回到上一首 播放
        time.sleep(2)

        # 点击下一首3次
        bTMusic.getBTNextSong()
        time.sleep(1)
        bTMusic.getBTNextSong()
        time.sleep(1)
        bTMusic.getBTNextSong()
        time.sleep(1)
        # 点击上一首3次 返回到原先的歌曲播放
        bTMusic.getBTPerviousSong()
        time.sleep(1)
        bTMusic.getBTPerviousSong()
        time.sleep(1)
        bTMusic.getBTPerviousSong()
        time.sleep(1)

        ''' # 暂停播放切换4次，回到播放状态
        bTMusic.changePlayStatus()
        bTMusic.changePlayStatus()
        bTMusic.changePlayStatus()
        bTMusic.changePlayStatus()'''


        # 来回点击下一首/上一首 3次，回到原来歌曲播放
        bTMusic.getBTNextSong()
        bTMusic.getBTPerviousSong()
        bTMusic.getBTNextSong()
        bTMusic.getBTPerviousSong()
        bTMusic.getBTNextSong()
        bTMusic.getBTPerviousSong()


        i + 1
        print('运行 ' + str(i) + ' 次')

    '''
    # eval('mainPage.cleanAllPage()')
'''