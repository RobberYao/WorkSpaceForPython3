import xlsxwriter as xlsw
import xlrd
import os
import sys
from BaseClass import fileHandler as fh

folderPath = 'd:/SystemExcel/'
filePath = folderPath + 'systemCollection.xlsx'


# 创建xlsx文件方法
def createExcel(folderPath, filePath):
    if fh.isFolderExit(folderPath) == True:  # 如果文件夹路径存在，继续检查文件是否存在
        if fh.isFileExit(filePath) == True:  # 如果文件存在，不做任何操作
            pass
        else:  # 如果文件不存在，生成一份xlsx
            workbook = xlsw.Workbook(filePath)
            workbook.close()
    else:
        fh.createFolder(folderPath)  # 创建文件夹


# 获取xlsx文件对象
def getFile_Obj(filePath):
    if not os.path.isfile(filePath):
        print('文件路径不存在')
        sys.exit()
    else:
        return xlrd.open_workbook(filePath)  # 返回xlsx文件对象


# 通过文件对象获取首页sheet
def getFirstSheetByFile_Obj(data,num):
    return data.sheets()[num]


if __name__ == '__main__':
    # createExcel()
    data = getFile_Obj(filePath)
    print(data.sheet_by_index(0).nrows)  # 获取总行数
    print(data.sheet_by_index(0).ncols)  # 获取总列数
