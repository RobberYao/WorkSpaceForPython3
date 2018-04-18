import logging
from logging.config import fileConfig

fileConfig("../logging.conf")  # 采用配置文件
filePath3 = 'D:/mp3File/english/musicVoice/e_g_CloseMusic.mp3'
# create logger


'''
# "application" code
logger1.debug("debug message")
logger1.info("info message")
logger1.warn("warn message")
logger1.error("error message")
logger1.critical("critical message")
'''


def consoleLog():
    fileConfig("logging.conf")  # 采用配置文件
    return logging.getLogger('consoleLogger')


def fileLog():
    fileConfig("logging.conf")  # 采用配置文件
    return logging.getLogger('fileLogger')


if __name__ == '__main__':
    consoleLog().info('play: ' + filePath3)
    fileLog().info('play: ' + filePath3)