from FrameWorkOfSaicAutoTest.logModule import loggingConfig

lc = loggingConfig.loggingConfig()

if __name__ == '__main__':
    lc.fileLog().info('Hello Jenkins')
    print('hello Jenkins')
