# !/usr/bin/python3
# 通过dict来连接各个纬度的映射


# 语言字典 ：中文 、英文
languageDict = {
    'china': 'chinese',
    'english': 'english'
};

# 模块字典 ：
moduleDict = {
    'musicModule': 'musicVoice',
    'mapModule': 'mapVoice',
    'radioModule': 'radioVoice',
    'systemModule': 'systemVoice',
    'controlModule': 'controlVoice',
    'telephoneModule': 'telephoneVoice'
};

# 模块映射功能 ：
# 音乐模块映射方法
musicVoice = {
    'e_g_CloseMusic': 'e_g_CloseMusic.mp3',  #
    'e_g_ItsToLoud': 'e_g_ItsToLoud.mp3',  #
    'e_g_ItsToQuite': 'e_g_ItsToQuite.mp3',
    'e_g_iWantToListenToMusic': 'e_g_iWantToListenToMusic.mp3',
    'e_g_MaxmizeTheVolume': 'e_g_MaxmizeTheVolume.mp3',
    'e_g_MinizeTheVolume': 'e_g_MinizeTheVolume.mp3',  #
    'e_g_Mute': 'e_g_Mute.mp3',
    'e_g_MuteTheLowestVolume': 'e_g_MuteTheLowestVolume.mp3',  #
    'e_g_NEXT': 'e_g_NEXT.mp3',
    'e_g_NextSong': 'e_g_NextSong.mp3',
    'e_g_OpenBluetoothMusic': 'e_g_OpenBluetoothMusic.mp3',
    'e_g_OpenLocalMusic': 'e_g_OpenLocalMusic.mp3',
    'e_g_Pause': 'e_g_Pause.mp3',
    'e_g_PauseMusic': 'e_g_PauseMusic.mp3',
    'e_g_PlayBluetoothMusic': 'e_g_PlayBluetoothMusic.mp3',
    'e_g_PlayLocalMusic': 'e_g_PlayLocalMusic.mp3',
    'e_g_PlayMusic': 'e_g_PlayMusic.mp3',
    'e_g_PlayPreviousSong': 'e_g_PlayPreviousSong.mp3',
    'e_g_PlayRandom': 'e_g_PlayRandom.mp3',
    'e_g_PreviousOne': 'e_g_PreviousOne.mp3',
    'e_g_Stop': 'e_g_Stop.mp3',
    'e_g_TheLowestVolume': 'e_g_TheLowestVolume.mp3',
    'e_g_TurnUpTheVolume': 'e_g_TurnUpTheVolume.mp3',
    'e_g_TurnDownTheVolume': 'e_g_TurnDownTheVolume.mp3',
    'e_g_Unmute': 'e_g_Unmute.mp3',
    'e_m_CloseMusic': 'e_m_CloseMusic.mp3',
    'e_m_GiveMeSomeMusicInUDisk': 'e_m_GiveMeSomeMusicInUDisk',
    'e_m_ItsToLoud': 'e_m_ItsToLoud.mp3',
    'e_m_ItsToQuite': 'e_m_ItsToQuite.mp3',
    'e_m_IWantToListenToMusic': 'e_m_IWantToListenToMusic.mp3',
    'e_m_MaxmizeTheVolume': 'e_m_MaxmizeTheVolume.mp3',
    'e_m_MinmizeTheVolume': 'e_m_MinmizeTheVolume.mp3',
    'e_m_Mute': 'e_m_Mute.mp3',
    'e_m_MuteTheLowestVolume': 'e_m_MuteTheLowestVolume.mp3',
    'e_m_NEXT': 'e_m_NEXT.mp3',
    'e_m_NextSong': 'e_m_NextSong.mp3',
    'e_m_OpenBluetoothMusic': 'e_m_OpenBluetoothMusic.mp3',
    'e_m_OpenLocalMusic': 'e_m_OpenLocalMusic.mp3',
    'e_m_Pause': 'e_m_Pause.mp3',
    'e_m_PauseMusic': 'e_m_PauseMusic.mp3',
    'e_m_PlayBluetoothMusic': 'e_m_PlayBluetoothMusic.mp3',
    'e_m_PlayLocalMusic': 'e_m_PlayLocalMusic.mp3',
    'e_m_PlayMusic': 'e_m_PlayMusic.mp3',
    'e_m_PlayPreviousSong': 'e_m_PlayPreviousSong.mp3',
    'e_m_PlayRandom': 'e_m_PlayRandom.mp3',
    'e_m_PreviousOne': 'e_m_PreviousOne.mp3',
    'e_m_Stop': 'e_m_Stop.mp3',
    'e_m_TheLowestVolume': 'e_m_TheLowestVolume.mp3',
    'e_m_TurnUpTheVolume': 'e_m_TurnUpTheVolume.mp3',
    'e_m_TurnDownTheVolume': 'e_m_TurnDownTheVolume.mp3',
    'e_m_Unmute': 'e_m_Unmute.mp3'
};

radioVoice = {
    'e_g_OpenFM97': 'e_g_OpenFM97.mp3',
    'e_g_OpenRadio': 'e_g_OpenRadio.mp3',
    'e_g_PlayFM97': 'e_g_PlayFM97.mp3',
    'e_g_PlayRadio': 'e_g_PlayRadio.mp3',
    'e_g_TuneToFm97': 'e_g_TuneToFm97.mp3',
    'e_m_OpenRadio': 'e_m_OpenRadio.mp3',
    'e_m_playFm97': 'e_m_playFm97.mp3',
    'e_m_PlayRadio': 'e_m_PlayRadio.mp3',
    'e_m_TuneToFm97': 'e_m_TuneToFm97.mp3'
};

mapVoice = {
    'e_g_AvoidMotorway': 'e_g_AvoidMotorway.mp3',
    'e_g_AvoidTollway': 'e_g_AvoidTollway.mp3',
    'e_g_CancelSat-Nav': 'e_g_CancelSat-Nav.mp3',
    'e_g_enlargeTheMap': 'e_g_enlargeTheMap.mp3',
    'e_g_ExitSat-Nav': 'e_g_ExitSat-Nav.mp3',
    'e_g_FinishSat-Nav': 'e_g_FinishSat-Nav.mp3',
    'e_g_iWantToGoNewYork': 'e_g_iWantToGoNewYork.mp3',
    'e_g_iWantToSetHomeAddress': 'e_g_iWantToSetHomeAddress.mp3',
    'e_g_iWantToSetOfficeAddress': 'e_g_iWantToSetOfficeAddress.mp3',
    'e_g_iWantToUseSat-Nav': 'e_g_iWantToUseSat-Nav.mp3',
    'e_g_MaximizeTheMap': 'e_g_MaximizeTheMap.mp3',
    'e_g_MinimizeTheMap': 'e_g_MinimizeTheMap.mp3',
    'e_g_MotorwayFirst': 'e_g_MotorwayFirst.mp3',
    'e_g_OpenAvoidTraffic': 'e_g_OpenAvoidTraffic.mp3',
    'e_g_OpenTheMap': 'e_g_OpenTheMap.mp3',
    'e_g_TakeMeToNwYork': 'e_g_TakeMeToNwYork.mp3',
    'e_g_ZoomOutTheMap': 'e_g_ZoomOutTheMap.mp3',
    'e_m_AvoidMotorway': 'e_m_AvoidMotorway.mp3',
    'e_m_AvoidTollway': 'e_m_AvoidTollway.mp3',
    'e_m_CancelSat-Nav': 'e_m_CancelSat-Nav.mp3',
    'e_m_enlargeTheMap': 'e_m_enlargeTheMap.mp3',
    'e_m_ExitSat-Nav': 'e_m_ExitSat-Nav.mp3',
    'e_m_FinishSat-Nav': 'e_m_FinishSat-Nav.mp3',
    'e_m_iWantToEnlargeTheMapScale': 'e_m_iWantToEnlargeTheMapScale.mp3',
    'e_m_iWantToGoNewYork': 'e_m_iWantToGoNewYork.mp3',
    'e_m_iWantToSetHomeAddress': 'e_m_iWantToSetHomeAddress.mp3',
    'e_m_iWantToSetOfficeAddress': 'e_m_iWantToSetOfficeAddress.mp3',
    'e_m_iWantToTurnOnTheAvoidTollSwitch': 'e_m_iWantToTurnOnTheAvoidTollSwitch',
    'e_m_iWantToUseSat-Nav': 'e_m_iWantToUseSat-Nav.mp3',
    'e_m_MapToMaximize': 'e_m_MapToMaximize.mp3',
    'e_m_MinimizeTheMap': 'e_m_MinimizeTheMap.mp3',
    'e_m_MotorwayFirst': 'e_m_MotorwayFirst.mp3',
    'e_m_OpenAvoidTraffic': 'e_m_OpenAvoidTraffic.mp3',
    'e_m_OpenTheMap': 'e_m_OpenTheMap.mp3',
    'e_m_resizeTheMapBigger': 'e_m_resizeTheMapBigger.mp3',
    'e_m_TakeMeToNwYork': 'e_m_TakeMeToNwYork.mp3',
    'e_m_ZoomOutTheMap': 'e_m_ZoomOutTheMap.mp3'
};
systemVoice = {
    'e_g_Cancel':'e_g_Cancel.mp3',
    'e_g_FirstPage': 'e_g_FirstPage.mp3',
    'e_g_FrontPage': 'e_g_FrontPage.mp3',
    'e_g_Go': 'e_g_Go.mp3',
    'e_g_IDoNotNeedIt.mp3':'e_g_IDoNotNeedIt.mp3',
    'e_g_LastPage': 'e_g_LastPage',
    'e_g_LetUsGo': 'e_g_LetUsGo.mp3',
    'e_g_NEXT': 'e_g_NEXT.mp3',
    'e_g_NextPage': 'e_g_NextPage.mp3',
    'e_g_No':'e_g_No.mp3',
    'e_g_OK': 'e_g_OK.mp3',
    'e_g_Previous': 'e_g_Previous.mp3',
    'e_g_Right': 'e_g_Right.mp3',
    'e_g_SecondPage': 'e_g_SecondPage.mp3',
    'e_g_smartMirror': 'e_g_smartMirror.mp3',
    'e_g_Sure': 'e_g_Sure.mp3',
    'e_g_ThirdPage': 'e_g_ThirdPage.mp3',
    'e_g_Yeah': 'e_g_Yeah.mp3',
    'e_g_Yes': 'e_g_Yes.mp3',
    'e_m_Cancel': 'e_m_Cancel.mp3',
    'e_m_FirstPage': 'e_m_FirstPage.mp3',
    'e_m_FrontPage': 'e_m_FrontPage.mp3',
    'e_m_Go': 'e_m_Go.mp3',
    'e_m_IDoNotNeedIt':'e_m_IDoNotNeedIt.mp3',
    'e_m_LastPage': 'e_m_LastPage.mp3',
    'e_m_LetUsGo': 'e_m_LetUGo.mp3',
    'e_m_Next': 'e_m_Next.mp3',
    'e_m_NextPage': 'e_m_NextPage.mp3',
    'e_m_No':'e_m_No.mp3',
    'e_m_OK': 'e_m_OK.MP3',
    'e_m_previous': 'e_m_previous.mp3',
    'e_m_Right': 'e_m_Right.mp3',
    'e_m_SecondPage': 'e_m_SecondPage.mp3',
    'e_m_smartMirror': 'e_m_smartMirror.mp3',
    'e_m_Sure': 'e_m_Sure.mp3',
    'e_m_ThirdPage': 'e_m_ThirdPage.mp3',
    'e_m_Yes': 'e_m_Yes.mp3'
};

controlVoice = {

    'e_g_Cancel': 'e_g_Cancel.mp3',
    'e_g_CloseAC': 'e_g_CloseAC.mp3',
    'e_g_CloseSunroof': 'e_g_CloseSunroof.mp3',
    'e_g_CloseWindows': 'e_g_CloseWindows.mp3',
    'e_g_DecreaseFanSpeed': 'e_g_DecreaseFanSpeed.mp3',
    'e_g_exitVoiceControl': 'e_g_exitVoiceControl.mp3',
    'e_g_IncreaseFanSpeed': 'e_g_IncreaseFanSpeed.mp3',
    'e_g_OpenAC': 'e_g_OpenAC.mp3',
    'e_g_OpenSunroof': 'e_g_OpenSunroof.mp3',
    'e_g_OpenWindows': 'e_g_OpenWindows.mp3',
    'e_g_Reture': 'e_g_Reture.mp3',
    'e_g_TurenDownTheTemperature': 'e_g_TurenDownTheTemperature.mp3',
    'e_g_TurnUpTheTemperature': 'e_g_TurnUpTheTemperature.mp3',
    'e_m_ IncreaseFanSpeed': 'e_m_ IncreaseFanSpeed.mp3',
    'e_m_Cancel': 'e_m_Cancel.mp3',
    'e_m_CloseAC': 'e_m_CloseAC.mp3',
    'e_m_CloseSunroof': 'e_m_CloseSunroof.mp3',
    'e_m_CloseWindows': 'e_m_CloseWindows.mp3',
    'e_m_DecreaseFanSpeed': 'e_m_DecreaseFanSpeed.mp3',
    'e_m_exitVoiceControl': 'e_m_exitVoiceControl.mp3',
    'e_m_iWantToCloseTheFrontLeftWindow': 'e_m_iWantToCloseTheFrontLeftWindow.mp3',
    'e_m_iWantToOpenTheLeftFrontWindow': 'e_m_iWantToOpenTheLeftFrontWindow.mp3',
    'e_m_OpenAC': 'e_m_OpenAC.mp3',
    'e_m_OpenSunroof': 'e_m_OpenSunroof.mp3',
    'e_m_openTheWindowOfTheMainDrive': 'e_m_openTheWindowOfTheMainDrive.mp3',
    'e_m_OpenWindows': 'e_m_OpenWindows.mp3',
    'e_m_reture': 'e_m_reture.mp3',
    'e_m_TurenDownTheTemperature': 'e_m_TurenDownTheTemperature.mp3',
    'e_m_turnOffTheMainDriveWindow': 'e_m_turnOffTheMainDriveWindow.mp3',
    'e_m_TurnUpTheTemperature': 'e_m_TurnUpTheTemperature.mp3'
};

telephoneVoice = {
    'e_g_CallTom': 'e_g_CallTom.mp3',
    'e_g_HangUp': 'e_g_HangUp.mp3',
    'e_g_iNeedToMakeACall': 'e_g_iNeedToMakeACall.mp3',
    'e_g_PickUpCalls': 'e_g_PickUpCalls.mp3',
    'e_g_RejectPhoeCall': 'e_g_RejectPhoeCall.mp3',
    'e_m_Call3467575': 'e_m_Call3467575.mp3',
    'e_m_CallTom': 'e_m_CallTom.mp3',
    'e_m_HangUp.mp3': 'e_m_HangUp.mp3',
    'e_m_iNeedToMakeACall': 'e_m_iNeedToMakeACall.mp3',
    'e_m_PickUpCalls': 'e_m_PickUpCalls.mp3',
    'e_m_RejectPhoeCall': 'e_m_RejectPhoeCall.mp3'
}

if __name__ == '__main__':
    # print(musicVoice['play'])
    print(mapVoice['e_g_AvoidMotorway'])
