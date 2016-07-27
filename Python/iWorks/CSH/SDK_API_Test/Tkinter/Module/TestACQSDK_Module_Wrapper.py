# Import required module(s)
import sys

# ===================================================== CSDevice =====================================================
# Basic Function

def ACQSDK_Init(objACQSDK_CSDevice, hWnd):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_Init(hWnd)
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

def ACQSDK_UnInit(objACQSDK_CSDevice):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_UnInit()
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

def ACQSDK_OnUpdateLiveWnd(objACQSDK_CSDevice):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_OnUpdateLiveWnd()
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

def ACQSDK_StartPlay(objACQSDK_CSDevice):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_StartPlay()
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

def ACQSDK_StopPlay(objACQSDK_CSDevice):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_StopPlay()
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

def ACQSDK_PausePlay(objACQSDK_CSDevice):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_PausePlay()
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

def ACQSDK_ResumePlay(objACQSDK_CSDevice):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_ResumePlay()
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

def ACQSDK_StartRecord(objACQSDK_CSDevice, path):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_StartRecord(path)
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

def ACQSDK_StopRecord(objACQSDK_CSDevice):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_StopRecord()
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

# def ACQSDK_Capture(objACQSDK_CSDevice, pImageUnit):
#     module_name = sys._getframe().f_code.co_name
    eString = ''
#     try: ret = objACQSDK_CSDevice.ACQSDK_Capture(pImageUnit)
#     except Exception as e:
#        eString = str(e)
#        ret = None
#     finally: return (module_name, ret, eString)

def ACQSDK_SendCaptureCmd(objACQSDK_CSDevice):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_SendCaptureCmd()
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

# def ACQSDK_GetImageData(objACQSDK_CSDevice, pImageUnit):  # timeout is 5s
#     module_name = sys._getframe().f_code.co_name
    eString = ''
#     try: ret = objACQSDK_CSDevice.ACQSDK_GetImageData(pImageUnit)
#     except Exception as e:
#        eString = str(e)
#        ret = None
#     finally: return (module_name, ret, eString)

def ACQSDK_SetLogPath(objACQSDK_CSDevice, path):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_SetLogPath(path)
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

# Mirror & Rotation

def ACQSDK_SetMirrorFlag(objACQSDK_CSDevice, bEnable):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_SetMirrorFlag(bEnable)
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

def ACQSDK_GetMirrorFlag(objACQSDK_CSDevice):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_GetMirrorFlag()
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

def ACQSDK_SetRotationFlag(objACQSDK_CSDevice, rotation):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_SetRotationFlag(rotation)
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

def ACQSDK_GetRotationFlag(objACQSDK_CSDevice):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_GetRotationFlag()
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

# Query

def ACQSDK_QueryDeviceInfo(objACQSDK_CSDevice, pDeviceInfo):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_QueryDeviceInfo(pDeviceInfo)
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

def ACQSDK_GetFirmwareVersion(objACQSDK_CSDevice):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_GetFirmwareVersion()
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

def ACQSDK_GetSDKVersion(objACQSDK_CSDevice):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_GetSDKVersion()
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

# Configuration
# >> Brightness

def ACQSDK_GetBrightness(objACQSDK_CSDevice):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_GetBrightness()
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

def ACQSDK_SetBrightness(objACQSDK_CSDevice, brightness):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_SetBrightness(brightness)
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

# >> Contrast

def ACQSDK_GetContrast(objACQSDK_CSDevice):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_GetContrast()
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

def ACQSDK_SetContrast(objACQSDK_CSDevice, contrast):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_SetContrast(contrast)
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

# >> Powerline Frequency

def ACQSDK_GetPowerlineFrequency(objACQSDK_CSDevice):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_GetPowerlineFrequency()
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

def ACQSDK_SetPowerlineFrequency(objACQSDK_CSDevice, frequency):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_SetPowerlineFrequency(frequency)
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

# >> Sleep

def ACQSDK_SetEnableSleep(objACQSDK_CSDevice, bEnable):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_SetEnableSleep(bEnable)
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

def ACQSDK_GetEnableSleep(objACQSDK_CSDevice):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_GetEnableSleep()
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

def ACQSDK_GetSleepTime(objACQSDK_CSDevice):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_GetSleepTime()
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

def ACQSDK_SetSleepTime(objACQSDK_CSDevice, seconds):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_SetSleepTime(seconds)
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

# >> Auto Power On

def ACQSDK_EnableAutoPowerOn(objACQSDK_CSDevice, bEnable):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_EnableAutoPowerOn(bEnable)
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

def ACQSDK_GetEnableAutoPowerOn(objACQSDK_CSDevice):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_GetEnableAutoPowerOn()
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

# >> Auto Power Off

def ACQSDK_EnableAutoPowerOff(objACQSDK_CSDevice, bEnable):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_EnableAutoPowerOff(bEnable)
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

def ACQSDK_GetEnableAutoPowerOff(objACQSDK_CSDevice):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_GetEnableAutoPowerOff()
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

def ACQSDK_GetAutoPowerOffTime(objACQSDK_CSDevice):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_GetAutoPowerOffTime()
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

def ACQSDK_SetAutoPowerOffTime(objACQSDK_CSDevice, secondsCount):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_SetAutoPowerOffTime(secondsCount)
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

# Firmware

def ACQSDK_UpgradeFirmware(objACQSDK_CSDevice, pFullPathName):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_UpgradeFirmware(pFullPathName)
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

def ACQSDK_AbortUpgrade(objACQSDK_CSDevice):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_AbortUpgrade()
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)


def ACQSDK_GrabFrameFromMovie(objACQSDK_CSDevice, avi_file, bmp_file):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_GrabFrameFromMovie(avi_file, bmp_file)
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

def ACQSDK_GetFwStatus(objACQSDK_CSDevice):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_GetFwStatus()
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

def ACQSDK_GetHostVersion(objACQSDK_CSDevice):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_GetHostVersion()
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

# CS 1500

def ACQSDK_Get2LevelCapture(objACQSDK_CSDevice):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_Get2LevelCapture()
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

def ACQSDK_Set2LevelCapture(objACQSDK_CSDevice, bEnable):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_Set2LevelCapture(bEnable)
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

# MFG
"""
# >> Work Mode
def ACQSDK_SetHPWorkMode(objACQSDK_CSDevice, lWorkMode):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_SetHPWorkMode(lWorkMode)
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)
"""

# >> Serial Number
def ACQSDK_GetSerialNumber(objACQSDK_CSDevice):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_GetSerialNumber()
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

def ACQSDK_SetSerialNumber(objACQSDK_CSDevice, sn):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_SetSerialNumber(sn)
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

# >> File Upload & Download
def ACQSDK_UploadFile(objACQSDK_CSDevice, pFileName):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_UploadFile(pFileName)
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

def ACQSDK_DownloadFile(objACQSDK_CSDevice, fileID, pFileName):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_DownloadFile(fileID, pFileName)
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)

"""
# >> XU
def ACQSDK_MFG_GetXU(objACQSDK_CSDevice, index, value):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_MFG_GetXU(index, value)
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)
def ACQSDK_MFG_SetXU(objACQSDK_CSDevice, index, value, length):
    module_name = sys._getframe().f_code.co_name
    eString = ''
    try: ret = objACQSDK_CSDevice.ACQSDK_MFG_SetXU(index, value, length)
    except Exception as e:
        eString = str(e)
        ret = None
    finally: return (module_name, ret, eString)
"""

# ===================================================== CSDevice =====================================================

# Check on local
if __name__ == '__main__':
    print sys._getframe().f_code.co_filename
