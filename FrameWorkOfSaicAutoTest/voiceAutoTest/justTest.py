from FrameWorkOfSaicAutoTest.LogModule import loggingConfig


def print():
    lc = loggingConfig.loggingConfig()
    lc.consoleLog().info('222')


if __name__ == '__main__':
    print()
