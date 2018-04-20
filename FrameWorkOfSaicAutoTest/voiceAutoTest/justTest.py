from FrameWorkOfSaicAutoTest.LogModule import loggingConfig



class test:
    def print(self):
        lc = loggingConfig()
        lc.consoleLog().info('222')

        print('111')


if __name__ == '__main__':
    t = test()
    t.print()
