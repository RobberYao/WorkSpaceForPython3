from uiautomator import device as d
import time
from FrameWorkOfSaicAutoTest.logModule import loggingConfig

lc = loggingConfig.loggingConfig()


# 拨号0到9
def dialing0To9(num):
    numDict = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }

    lc.fileLog().info('start dialing0To9...')
    d(resourceId='com.android.contacts:id/' + numDict.get(num)).click()
    lc.fileLog().info('stop dialing0To9...')
    time.sleep(2)


# 拨*号
def dialingStarKey():
    lc.fileLog().info('start dialingStar...')
    d(resourceId='com.android.contacts:id/star').click()
    lc.fileLog().info('stop dialingStar...')
    time.sleep(2)


# 拨#号
def dialingPoundKey():
    lc.fileLog().info('start dialingNumberKey...')
    d(resourceId='com.android.contacts:id/pound').click()
    lc.fileLog().info('stop dialingNumberKey...')
    time.sleep(2)


# 删除拨号
def deleteButton():
    lc.fileLog().info('start deleteButton...')
    d(resourceId='com.android.contacts:id/deleteButton').click()
    lc.fileLog().info('stop deleteButton...')
    time.sleep(2)



# 回退
def back():
    lc.fileLog().info('start back...')
    d(resourceId='com.clw.btphone:id/back').click()
    lc.fileLog().info('stop back...')
    time.sleep(2)


# 最近通话记录，坐标暂定为(615, 140)
def recentCalls():
    lc.fileLog().info('start dialingNumberKey...')
    d.click(615, 140)
    lc.fileLog().info('stop dialingNumberKey...')
    time.sleep(2)


# 联系人，坐标暂定为(745, 140)
def contactsList():
    lc.fileLog().info('start contactsList...')
    d.click(745, 140)
    lc.fileLog().info('stop contactsList...')
    time.sleep(2)


# 拨打
def confirm():
    lc.fileLog().info('start confirm...')
    d(resourceId='com.android.contacts:id/dialog_confirm').click()
    lc.fileLog().info('stop confirm...')
    time.sleep(2)


# 取消
def cancel():
    lc.fileLog().info('start cancel...')
    d(resourceId='com.android.contacts:id/dialog_cancel').click()
    lc.fileLog().info('stop cancel...')
    time.sleep(2)


# 挂断电话
def endCall():
    lc.fileLog().info('start endCall...')
    d(resourceId='com.clw.btphone:id/end_call').click()
    lc.fileLog().info('stop endCall...')
    time.sleep(2)


# 静音
def mute():
    lc.fileLog().info('start mute...')
    d(resourceId='com.clw.btphone:id/voice_mute').click()
    lc.fileLog().info('stop mute...')
    time.sleep(2)


# 切换音频通道
def switch():
    lc.fileLog().info('start switch...')
    d(resourceId='com.clw.btphone:id/voice_switch').click()
    lc.fileLog().info('stop switch...')
    time.sleep(2)


# 拨号盘
def dialpad():
    lc.fileLog().info('start dialpad...')
    d(resourceId='com.clw.btphone:id/dialpad').click()
    lc.fileLog().info('stop dialpad...')
    time.sleep(2)


# 根据联系人名称选择拨号
def selectRecentCallsByCallName(callName):
    lc.fileLog().info('start selectRecentCallsByCallName...')
    try:
        d(resourceId='com.android.contacts:id/calls_list', className='android.widget.ListView',
          packageName='com.android.contacts').child_by_text(callName, text=callName).click()
        print('==' + callName)
    except:
        lc.fileLog().info(callName + 'is not exists')
    time.sleep(1)
    lc.fileLog().info('end selectRecentCallsByCallName...')


# 根据电话号码选择拨号
def selectRecentCallsByCallNum(callNum):
    lc.fileLog().info('start selectRecentCallsByCallNum...')
    try:
        d(resourceId='com.android.contacts:id/calls_list', className='android.widget.ListView',
          packageName='com.android.contacts').child_by_text(callNum, text=callNum).click()
        print('==' + callNum)
    except:
        lc.fileLog().info(callNum + 'is not exists')
    time.sleep(1)
    lc.fileLog().info('end selectRecentCallsByCallNum...')


# 根据联系人名称选择拨号
def selectContactsListByCallName(callName):
    lc.fileLog().info('start selectNumberByCallName...')
    try:
        d(resourceId='com.android.contacts:id/main_list', className='android.widget.ListView',
          packageName='com.android.contacts').child_by_text(callName, text=callName).click()
        print('==' + callName)
    except:
        lc.fileLog().info(callName + 'is not exists')
    time.sleep(1)
    lc.fileLog().info('end selectNumberByCallName...')


# 根据联系人电话选择拨号
def selectContactsListByCallNum(callNum):
    lc.fileLog().info('start selectContactsListByCallNum...')
    try:
        d(resourceId='com.android.contacts:id/main_list', className='android.widget.ListView',
          packageName='com.android.contacts').child_by_text(callNum, text=callNum).click()
        print('==' + callNum)
    except:
        lc.fileLog().info(callNum + 'is not exists')
    time.sleep(1)
    lc.fileLog().info('end selectContactsListByCallNum...')


# 拨打按键
def dialButton():
    lc.fileLog().info('start dialButton...')
    d(resourceId='com.android.contacts:id/dialButton').click()
    lc.fileLog().info('stop dialButton...')
    time.sleep(2)







if __name__ == '__main__':
    # dialing0To9(0)
    # dialingStarKey()
    # dialingPoundKey()
    # recentCalls()
    # contactsList()
    selectRecentCallsByCallName('1006')
    # selectContactsListByCallNum('10086')
    pass
