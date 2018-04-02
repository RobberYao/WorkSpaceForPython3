import pygame
import sys
import os
import time

fileName1 = 'D:/WorkSpaceForPython3.0/mp3File/music/1.mp3'
fileName2 = 'D:/WorkSpaceForPython3.0/mp3File/music/2.mp3'

# 测试流程行为 暂且不用
pygame.USEREVENT


# 初始化测试行为
def init():
    pygame.init()
    pygame.display.set_mode([480, 320])  # 注意这一句


# 播放指定MP3文件（）
def play():
    pygame.mixer.music.play()
    # time.sleep(time)


def loadMp3(filePath):
    pygame.mixer.music.load(filePath)


def pause():
    pygame.mixer.music.pause()


def pause(time):  # 暂停 time 秒后重启
    pygame.mixer.music.pause()
    time.sleep(time)
    unpause()


def unpause():
    pygame.mixer.music.unpause()


def stop():
    pygame.mixer.music.stop()


if __name__ == '__main__':
    init()
    loadMp3(fileName1)
    play()
    loadMp3(fileName1)
    play()
    # print(play(fileName))
    time.sleep(1666)
    print(pygame.mixer.music.get_pos())
    # print(pygame.mixer.music.get_busy())
