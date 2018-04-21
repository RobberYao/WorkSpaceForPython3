import logging
from logging.config import fileConfig

fileConfig("../logModule/logging.ini")  # 采用配置文件
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


class loggingConfig:

    def init(self):
        fileConfig("logging.ini")  # 采用配置文件

    def consoleLog(self):
        return logging.getLogger('consoleLogger')

    def fileLog(self):
        # fileConfig("logging.ini")  # 采用配置文件
        return logging.getLogger('fileLogger')


if __name__ == '__main__':
    lc = loggingConfig()
    lc.consoleLog().info('play: ' + filePath3)
    lc.fileLog().info('play: ' + filePath3)
