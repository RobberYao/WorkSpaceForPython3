import os
import re

folderPath = 'd:/SystemExcel/'
filePath = folderPath + 'systemCollection.xlsx'

testFile = 'D:/test.txt'
targetfile = 'D:/mp3File/music/2.mp3'


# 判断文件夹是否存在
def isFolderExit(filePath):
    return os.path.exists(filePath)


# 判断文件是否存在
def isFileExit(filePath):
    return os.path.isfile(filePath)


# 创建文件夹
def createFolder(filePath):
    os.mkdir(filePath)
    if isFolderExit(filePath) == True:
        print('Folder created successfully')
        return True
    else:
        print('Folder created failure')
        return False


# 正则截取[]中内容
def getStrBySquareBrackets(str):
    pattern = re.compile(r'\[(.*?)\]')  # 接取[]内所有内容
    p = pattern.findall(str)[0].replace(" ", "").replace("[", "").replace("]", "")  # 移除空格
    print(p)
    return p


# 行读过滤空行和首字符为空格的整行
def readLineAndSave(testFile, targetfile):
    file = open(testFile)
    while 1:
        line = file.readline()  # 行读
        if not line:
            break  # 读完跳出
        else:
            print(line)
            if isFirstSpaceInStr(line):  # 移除首字符位空的字符串包括空行
                pass
            else:
                if isSpaceRow(line):
                    pass
                else:
                    if isKeyWordsInStr(line, 'User', '+'):  # 移除含User、%号的字符串
                        pass
                    else:
                        with open(targetfile, 'a+') as fo:
                            fo.write(line)
                            # fo.write('\n')
                    pass
    file.close()


# 判断首字符是否是空格
def isFirstSpaceInStr(str):
    return str.startswith(' ')


# 判断是否是空行
def isSpaceRow(str):
    return str.startswith('\n')


# 是否有关键词str1、str2在字符串context中
def isKeyWordsInStr(context, str1, str2):
    if str1 in context and str2 in context:
        return True
    else:
        return False


def getSystemMessage(str):
    pass


# print(re.match(r"([Reboot_Times : 0-9])", str))
# print(re.search("[Reboot_Times :0-9]", str))

if __name__ == '__main__':
    # print(createFolder(folderPath))
    # getStrBySquareBrackets('[Reboot_Times :0]')
    # getStrBySquareBrackets('[2018 - 03 - 21 - 15 - 36 - 48]')
    # print(isFirstSpaceInStr('User 16%, System 11%, IOW 0%, IRQ 0%'))
    ## readLineAndSave(testFile)
    print(isFileExit(targetfile))
