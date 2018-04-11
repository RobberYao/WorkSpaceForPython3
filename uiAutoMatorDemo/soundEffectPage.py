from uiautomator import device as d
import time


# 选择自定义音效
def getTomEffect():
    print('start getTomEffect...')
    d(resourceId='com.imotor.settings:id/bt0').click()
    print('stop getTomEffect...')
    # time.sleep(2)


# 选择关闭音效
def getOffEffect():
    print('start getOffEffect...')
    d(resourceId='com.imotor.settings:id/bt1').click()
    print('stop getOffEffect...')
    # time.sleep(2)


# 选择摇滚音效
def getRockEffect():
    print('start getRockEffect...')
    d(resourceId='com.imotor.settings:id/bt2').click()
    print('stop getRockEffect...')
    # time.sleep(2)


# 选择流行音效
def getPopEffect():
    print('start getPopEffect...')
    d(resourceId='com.imotor.settings:id/bt3').click()
    print('stop getPopEffect...')
    # time.sleep(2)


# 选择现场音效
def getLiveEffect():
    print('start getLiveEffect...')
    d(resourceId='com.imotor.settings:id/bt4').click()
    print('stop getLiveEffect...')
    # time.sleep(2)


# 选择舞曲音效
def getDanceEffect():
    print('start getDanceEffect...')
    d(resourceId='com.imotor.settings:id/bt5').click()
    print('stop getDanceEffect...')
    # time.sleep(2)


# 选择古典音效
def getClassionEffect():
    print('start getClassionEffect...')
    d(resourceId='com.imotor.settings:id/bt6').click()
    print('stop getClassionEffect...')
    # time.sleep(2)


# 选择柔和音效
def getSoftEffect():
    print('start getSoftEffect...')
    d(resourceId='com.imotor.settings:id/bt7').click()
    print('stop getSoftEffect...')
    # time.sleep(2)


def getEffectByName():
    print('start getEffectByName...')
    i = d(text='60').sibling(resourceId='com.imotor.settings:id/seekbar').info
    print('stop getEffectByName...' + str(i))


if __name__ == '__main__':
    # getTomEffect()
    # getOffEffect()
    # getRockEffect()
    # getPopEffect()
    # getLiveEffect()
    # getDanceEffect()
    # getClassionEffect()
    # getSoftEffect()
    # getOffEffect()
    getEffectByName()
