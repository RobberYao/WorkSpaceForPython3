# !/usr/bin/python3
# 通过dict来连接各个纬度的映射

# 语言字典 ：中文 、英文
languageDict = {
    'china': 'chinese',
    'english': 'english',
    'spanish': 'spanish'
};

# 功能
functionDict = {
    'com': 'commonButten',

};

# 通用按键（上层&下层控件）映射
commonButten = {
    'home': [50, 30],
    'back': [130, 30],
    'minimization': [210, 30],
    'message': [870, 35],
    'map': [140, 520],
    'music': [300, 520],
    'menu': [510, 520],
    'telephone': [710, 520],
    'radio': [870, 520]
};

# 主页面控件
mainPage = {
    'changeMusicStatus': 'ainPage.changeMusicStatus()',
    'enterMusicModule': 'ainPage.enterMusicModule()',
    'enterDataModule': 'ainPage.enterDataModule()',
    'swipeLeft': 'mainPage.swipeLeft()',

}
