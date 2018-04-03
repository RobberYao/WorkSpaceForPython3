# 解析Json配置文件
import time
import os
import logHandler
from autoSpeechDemo.function import osPlay
from autoSpeechDemo.BaseConfig import filePathConfig as fpConfig

totalDicts = ['languageDict', 'module', 'voice']  # 音频文件索引
runCollectPath = 'D:/WorkSpaceForPython3.0/autoSpeechDemo/AutoCollection/runCollection'
voicePath = 'D:/mp3File'


# 读取runCollection文件（需要执行的自动化测试用例配置文件）
def readReadCollection(fileName):
    file = open(fileName)
    str = ''
    while True:
        line = file.readline()
        if not line:
            break  # 读完跳出
        else:
            str = str + line.replace('\n', '')
    print(str)
    return str


# 循环比较runCollection中关键索引是否存在
def checkIndexWords(context):
    listOfVoicePath = []
    listOfContext = context.split('/')
    # print(listOfContext)
    index = 0
    for index in range(len(listOfContext)):
        # [languageDict=china,repeat=1;moduleDict= music,repeat=1;voice=play,repeat=1]
        context = listOfContext[index]
        print('index : ' + str(index) + ' [' + context + ']')

        languageKey = getLanguageKey(context)  # languageDict
        languageValue = getLanguageValue(context)  # china
        print('语言 ：' + languageKey + ' -> ' + languageValue)
        # languageRepeatTimes = listOfContext[index].split(';')[0].split(',')[1].split('=')[1]  # 1

        moduleKey = getModuleKey(context)  # moduleDict
        moduleValue = getModuleValue(context)  # music

        voiceKey = getVoiceKey(context)  # voice
        voiceValue = getVoiceValue(context)  # play
        voiceRepeatTimes = getRepeatTimes(context)
        correctResponse = getCorrectResponse(context)

        print('模块 ：' + moduleKey + ' -> ' + moduleValue)
        print('音频 ：' + voiceKey + ' -> ' + voiceValue + ' 播放次数 ：' + voiceRepeatTimes + '次')
        print('正确返回答复 ：' + correctResponse)

        if languageKey == 'languageDict':
            if languageValue in fpConfig.languageDict.keys():  # 判断是key是否存在于languageDict中
                print(languageValue + ' in languageDict is ' + fpConfig.languageDict[languageValue])
                if moduleValue == 'musicVoice':  # 语音voice 层校验
                    print('musicVoice ==>')  # musicModule
                    if moduleKey in fpConfig.moduleDict.keys():  # 判断是key是否存在于moduleDict中
                        print(moduleKey + ' in moduleDict')
                        if fpConfig.moduleDict[moduleKey] == 'musicVoice':  # 音乐voice 层校验
                            print('musicVoice ==>')
                            if voiceValue in fpConfig.musicVoice.keys():
                                print(voiceValue + ' in musicVoice is ' + fpConfig.musicVoice[voiceValue])
                                listOfVoicePath.append(
                                    voicePath + '/' + fpConfig.languageDict[languageValue] + '/musicVoice/' + \
                                    fpConfig.musicVoice[
                                        voiceValue] + '=' + voiceRepeatTimes + '=' + correctResponse)  # 拼接音频路径=播放次数=正确返回并保存
                            else:
                                print(voiceValue + ' is not in musicVoice')
                                return
                        else:
                            print('moduleDict中已配置' + fpConfig.moduleDict[moduleValue] + '该层级 但无法找到该层级的内容层级')
                            return
                    else:
                        print('moduleDict中未配置' + moduleKey)
                        return
                elif moduleValue == 'mapVoice':  # 地图voice 层校验 预留
                    print('mapVoice ==>')  #
                    if moduleKey in fpConfig.moduleDict.keys():  # 判断是key是否存在于moduleDict中
                        print(moduleKey + ' in moduleDict')
                        if fpConfig.moduleDict[moduleKey] == 'mapVoice':  # 音乐voice 层校验
                            print('Voice ==>')
                            if voiceValue in fpConfig.mapVoice.keys():
                                print(voiceValue + ' in mapVoice is ' + fpConfig.mapVoice[voiceValue])
                                listOfVoicePath.append(
                                    voicePath + '/' + fpConfig.languageDict[languageValue] + '/mapVoice/' +
                                    fpConfig.mapVoice[
                                        voiceValue] + '=' + voiceRepeatTimes + '=' + correctResponse)  # 拼接音频路径=播放次数=正确返回并保存
                            else:
                                print(voiceValue + ' is not in mapVoice')
                                return
                        else:
                            print('moduleDict中已配置' + fpConfig.moduleDict[moduleValue] + '该层级 但无法找到该层级的内容层级')
                            return
                    else:
                        print('moduleDict中未配置' + moduleKey)
                        return
                elif moduleValue == 'radioVoice':  # 收音机voice 层校验 预留
                    print('radioVoice ==>')  #
                    if moduleKey in fpConfig.moduleDict.keys():  # 判断是key是否存在于moduleDict中
                        print(moduleKey + ' in moduleDict')
                        if fpConfig.moduleDict[moduleKey] == 'radioVoice':  #
                            print('Voice ==>')
                            if voiceValue in fpConfig.radioVoice.keys():
                                print(voiceValue + ' in radioVoice is ' + fpConfig.radioVoice[voiceValue])
                                listOfVoicePath.append(
                                    voicePath + '/' + fpConfig.languageDict[languageValue] + '/radioVoice/' +
                                    fpConfig.radioVoice[
                                        voiceValue] + '=' + voiceRepeatTimes + '=' + correctResponse)  # 拼接音频路径=播放次数=正确返回并保存
                            else:
                                print(voiceValue + ' is not in radioVoice')
                                return
                        else:
                            print('moduleDict中已配置' + fpConfig.moduleDict[moduleValue] + '该层级 但无法找到该层级的内容层级')
                            return
                    else:
                        print('moduleDict中未配置' + moduleKey)
                        return
                elif moduleValue == 'systemVoice':  # 系统voice 层校验 预留
                    print('systemVoice ==>')  #
                    if moduleKey in fpConfig.moduleDict.keys():  # 判断是key是否存在于moduleDict中
                        print(moduleKey + ' in moduleDict')
                        if fpConfig.moduleDict[moduleKey] == 'systemVoice':  #
                            print('Voice ==>')
                            if voiceValue in fpConfig.systemVoice.keys():
                                print(voiceValue + ' in systemVoice is ' + fpConfig.systemVoice[voiceValue])
                                listOfVoicePath.append(
                                    voicePath + '/' + fpConfig.languageDict[languageValue] + '/systemVoice/' +
                                    fpConfig.systemVoice[
                                        voiceValue] + '=' + voiceRepeatTimes + '=' + correctResponse)  # 拼接音频路径=播放次数=正确返回并保存
                            else:
                                print(voiceValue + ' is not in systemVoice')
                                return
                        else:
                            print('moduleDict中已配置' + fpConfig.moduleDict[moduleValue] + '该层级 但无法找到该层级的内容层级')
                            return
                    else:
                        print('moduleDict中未配置' + moduleKey)
                        return
                elif moduleValue == 'controlVoice':  # 车控voice 层校验 预留
                    print('controlVoice ==>')  # control
                    if moduleKey in fpConfig.moduleDict.keys():  # 判断是key是否存在于moduleDict中
                        print(moduleKey + ' in moduleDict')
                        if fpConfig.moduleDict[moduleKey] == 'controlVoice':  #
                            print('Voice ==>')
                            if voiceValue in fpConfig.controlVoice.keys():
                                print(voiceValue + ' in controlVoice is ' + fpConfig.controlVoice[voiceValue])
                                listOfVoicePath.append(
                                    voicePath + '/' + fpConfig.languageDict[languageValue] + '/controlVoice/' +
                                    fpConfig.controlVoice[
                                        voiceValue] + '=' + voiceRepeatTimes + '=' + correctResponse)  # 拼接音频路径=播放次数=正确返回并保存
                            else:
                                print(voiceValue + ' is not in controlVoice')
                                return
                        else:
                            print('moduleDict中已配置' + fpConfig.moduleDict[moduleValue] + '该层级 但无法找到该层级的内容层级')
                            return
                    else:
                        print('moduleDict中未配置' + moduleKey)
                        return
                elif moduleValue == 'telephoneVoice':  # 车控voice 层校验 预留
                    print('telephoneVoice ==>')  # control
                    if moduleKey in fpConfig.moduleDict.keys():  # 判断是key是否存在于moduleDict中
                        print(moduleKey + ' in moduleDict')
                        if fpConfig.moduleDict[moduleKey] == 'telephoneVoice':  #
                            print('Voice ==>')
                            if voiceValue in fpConfig.telephoneVoice.keys():
                                print(voiceValue + ' in telephoneVoice is ' + fpConfig.telephoneVoice[voiceValue])
                                listOfVoicePath.append(
                                    voicePath + '/' + fpConfig.languageDict[languageValue] + '/telephoneVoice/' +
                                    fpConfig.telephoneVoice[
                                        voiceValue] + '=' + voiceRepeatTimes + '=' + correctResponse)  # 拼接音频路径=播放次数=正确返回并保存
                            else:
                                print(voiceValue + ' is not in telephoneVoice')
                                return
                        else:
                            print('moduleDict中已配置' + fpConfig.moduleDict[moduleValue] + '该层级 但无法找到该层级的内容层级')
                            return
                    else:
                        print('moduleDict中未配置' + moduleKey)
                        return
                else:
                    print('moduleDict 下无字段 ：' + moduleValue)
                    return
            else:
                print('languageDict 下无字段 ：' + languageValue)
                return
        else:
            print('请调整索引顺序顺序 ：languageDict > moduleDict > voice languageDict放首位')
            return
    return listOfVoicePath


def getLanguageKey(context):
    return context.split(';')[0].split(',')[0].split('=')[0]


def getLanguageValue(context):
    return context.split(';')[0].split(',')[0].split('=')[1]


def getModuleKey(context):
    return context.split(';')[1].split(',')[0].split('=')[0]


def getModuleValue(context):
    return context.split(';')[1].split(',')[0].split('=')[1]


def getVoiceKey(context):
    return context.split(';')[2].split(',')[0].split('=')[0]


def getVoiceValue(context):
    return context.split(';')[2].split(',')[0].split('=')[1]


def getRepeatTimes(context):
    repeatTimes = context.split(';')[2].split(',')[1].split('=')[1]
    print('repeatTimes :' + repeatTimes)
    return repeatTimes


def getCorrectResponse(context):
    correctResponse = context.split(';')[2].split(',')[2].split('=')[1]
    print('correctResponse :' + correctResponse)
    return correctResponse


if __name__ == '__main__':
    index = 0
    context = readReadCollection(runCollectPath)  # 获取配置文件音频内容
    list = checkIndexWords(context)  # 校验音频内容正确性并返回可执行性的上下文（数组型）
    for index in range(len(list)):  # 循环执行每条音频文件
        voiceName = list[index].split('=')[0]  # 获取音频文件路径
        voiceRepeatTimes = list[index].split('=')[1]  # 获取执行次数
        voiceCorrectResponse = list[index].split('=')[2]  # 获取正确返回值
        logHandler.cleanFile()  # 预清空车机日志文件
        osPlay.playTimes(voiceName, voiceRepeatTimes)  # 播放音频文件
        time.sleep(6)
        logHandler.pullFile()  # 从车机拉取日志至本地临时文件和保存文件
        logHandler.markResult(voiceCorrectResponse, logHandler.matchVoice(voiceCorrectResponse))  # 匹配车机是否返回预期值并做处理
        logHandler.cleanTempFile()  # 清空本地日志临时文件

    # osPlay.playTimes_10(list[0])

