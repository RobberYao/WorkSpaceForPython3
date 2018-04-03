# 该类只适用生成系统cpu、内存消耗excel


from BaseClass import fileHandler as fh
import xlsxwriter as xw
import time
import re

excelFolderPath = 'd:/SystemExcel/'
excelFilePath = excelFolderPath + 'systemCollection.xlsx'
testFile = 'D:/LogFile/SystemMessage.txt'
targetfile = 'D:/LogFile/targetfile.txt'

rebootRowNum = 2  # excel中rebootRowNum行数控制


# 正则获取数字部分
def getNum(str):
    return re.sub('\D', '', str)


if __name__ == '__main__':
    fh.readLineAndSave(testFile, targetfile)  # 第一次过滤日志至从原文件至targetFile
    time.sleep(2)
    workbook = xw.Workbook(excelFilePath)  # 创建xlsx文件
    time.sleep(2)
    worksheet = workbook.add_worksheet('SystemMessage')  # 获取xlsx首页sheet内容(SystemMessage)
    worksheet.write('A1', 'Reboot_Times')  # 设置标题
    worksheet.write('B1', 'System_Time')  # 设置标题
    worksheet.write('C1', 'User(%)')  # 设置标题
    worksheet.write('D1', 'System(%)')  # 设置标题
    # time.sleep(2)

    tgFile = open(targetfile)  # 循环已过滤日志文件
    tgFile.readline()
    while 1:
        line = tgFile.readline()
        if not line:
            break  # 读完跳出
        else:
            if fh.isKeyWordsInStr(line, '[Reboot_Times', ':'):  # 写入重启次数
                worksheet.write('A' + str(rebootRowNum), getNum(line))
                print('Write into ' + 'A' + str(rebootRowNum) + ' : ' + getNum(line))
            else:
                if fh.isKeyWordsInStr(line, '[2018', '-'):  # 写入日期
                    worksheet.write('B' + str(rebootRowNum), line.replace('[', '').replace(']', ''))
                    print('Write into ' + 'B' + str(rebootRowNum) + ' : ' + line)
                else:
                    lineFirst = line.split(', ')  # 逗号分割cpu 内存参数 获得[User 16%, System 11%]
                    User = lineFirst[0].split(' ')  # 用空格符二次分隔参数获得[User, 16%]
                    System = lineFirst[1].split(' ')  # 用空格符二次分隔参数获得[ System, 11%]

                    worksheet.write('C' + str(rebootRowNum), float(User[1].replace('%', '')))  # 去除%保存
                    print('Write into ' + 'C' + str(rebootRowNum) + ' : ' + User[1].replace('%', ''))

                    worksheet.write('D' + str(rebootRowNum), float(System[1].replace('%', '')))  # 去除%保存
                    print('Write into ' + 'D' + str(rebootRowNum) + ' : ' + System[1].replace('%', ''))
                    rebootRowNum += 1  # 行数+1
    workbook.close()
