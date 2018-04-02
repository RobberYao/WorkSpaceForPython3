# coding=utf-8
import time
import os
import configparser as cf
import sys
import getopt
import random
import platform


class Speech_test:

    def __init__(self):
        pass

    # 获取config配置文件
    def getConfig(self):

        # print(type(cf.sections()))

        for section in cf.sections():
            print()
            section
            print()
            type(cf.options(section))
            for option in cf.options(section):
                print()
                option

    def getSections(self, cf):
        return cf.sections()

    def getSystem(self):
        return platform.system()

    def getOptions(self, cf, section):
        return cf.options(section)

    def getPlayList(self):
        cur_path = os.getcwd()
        speech_source_path = os.path.join(cur_path, "speech_source")
        if len(os.listdir(speech_source_path)) == 0:
            print("----------------------------------------------------------------------------------")
            print("Attention Please: speech_source is empty, please input audio file to this forder")
            print("----------------------------------------------------------------------------------")
            sys.exit(1)
        return os.listdir(speech_source_path)

    def doPlay(self, s):
        cur_path = os.getcwd()
        speech_source_path = os.path.join(cur_path, "speech_source")
        source_path = os.path.join(speech_source_path, s)
        if os.path.exists(source_path) is not True:
            return

        sys_platform = self.getSystem()
        if sys_platform in "Linux":
            play_tool = "play"
        else:
            play_tool = "gplay"
        play_cmd = play_tool + " " + source_path
        print('-------------------------------------------------------')
        print('   Start to play:' + s)
        print('-------------------------------------------------------')
        os.system(play_cmd)

    def shuffle_play(self, rp_number):
        for i in range(0, int(rp_number)):
            for source in self.getPlayList():
                self.doPlay(source)

    def random_play(self, rp_number):
        playList = self.getPlayList()
        for i in range(0, int(rp_number)):
            for i in range(0, len(playList)):
                random_value = random.randint(0, len(playList) - 1)
                self.doPlay(playList[random_value])

    def singlePlay(self, rp_number, source):
        for i in range(0, int(rp_number)):
            self.doPlay(source)

    def play(self, rp_type, rp_number, rp_source):
        self.getSystem()
        if "shu" in rp_type:
            self.shuffle_play(rp_number)
        elif "rand" in rp_type:
            self.random_play(rp_number)
        elif "sin" in rp_type:
            self.singlePlay(rp_number, rp_source)


def Usage():
    print('speech_test.py usage:')
    print('-h,--help:			print() help message.')
    print('-v, --version:			 print() script version')
    print(
        '--type:				test type you want, you can set shuffle, random or single, once single is selected, source is needed ')
    print('--repeat:			repeat times you want')
    print('--source:			single play audio name, only type is random used')
    print('-------------------------------------------------------------------')
    print('Use Method:')
    print('    !!!Please first to put all audio files into speech_source forder')
    print('    shuffle play command:')
    print('        python speech_test.py --type shuffle --repeat 3')
    print('    random play command:')
    print('        python speech_test.py --type random --repeat 3')
    print('    single audio play command:')
    print('        python speech_test.py --type single --repeat 3 --source navi.mp3')
    print('-------------------------------------------------------------------')


def Version():
    print('PyTest.py 1.0.0.0.1')


def ParseParm(opts):
    rp_type = ""
    rp_number = 0
    rp_source = ""
    for o, a in opts:
        if o in ('-h', '--help'):
            Usage()
            sys.exit(1)
        elif o in ('-v', '--version'):
            Version()
            sys.exit(0)
        elif o in ('--type',):
            rp_type = a
            print("Tester, Your test repeat_type is: " + rp_type)

        elif o in ('--repeat',):
            rp_number = a
            print("Tester, Your test repeat number is: " + rp_number)

        elif o in ('--source',):
            rp_source = a
            print("Tester, Your test audio source is: " + rp_source)

        else:
            print('unhandled option')

            sys.exit(3)

    return rp_type, rp_number, rp_source


def main():
    try:
        #opts, args = getopt.getopt(sys.argv[1:], 'hv:', ['type=', 'repeat=', 'source='])

        opts, args = getopt.getopt(sys.argv[1:], 'hv:', ['shuffle', '1', '打开音乐.wma'])
    except getopt.GetoptError as err:
        print((str(err)))
        Usage()
        sys.exit(2)

    if len(sys.argv) == 1:
        Usage()
        sys.exit(2)

    repeat_type, repeat_number, repeate_source = ParseParm(opts)

    playsource = Speech_test()
    playsource.play(repeat_type, repeat_number, repeate_source)


if __name__ == '__main__':
    # speechtest = SPEECH_TEST()

    # cf = ConfigParser.ConfigParser()
    # path = 'config.conf'
    # cf.read(path)

    # print() speechtest.getSections(cf)
    # print() args
    main()

    """for section in speechtest.getSections(cf):
        print() speechtest.getOptions(cf, section)

    cur_path = os.getcwd()
    speech_source_path = os.path.join(cur_path, "speech_source")
    for s in os.listdir(speech_source_path):
        source_path = os.path.join(speech_source_path, s)
        play_cmd = "play " + source_path
        os.system(play_cmd)"""
