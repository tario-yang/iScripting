# Import required module(s)
import sys

# ===================================================== CSDevice =====================================================
# Basic Function
def ACQSDK_Init(objACQSDK_CSDevice, hWnd):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_Init(hWnd)
	except: ret = None
	finally: return (module_name, ret)
def ACQSDK_UnInit(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_UnInit()
	except: ret = None
	finally: return (module_name, ret)
def ACQSDK_OnUpdateLiveWnd(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_OnUpdateLiveWnd()
	except: ret = None
	finally: return (module_name, ret)
def ACQSDK_StartPlay(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_StartPlay()
	except: ret = None
	finally: return (module_name, ret)
def ACQSDK_StopPlay(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_StopPlay()
	except: ret = None
	finally: return (module_name, ret)
def ACQSDK_StartRecord(objACQSDK_CSDevice, path):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_StartRecord(path)
	except: ret = None
	finally: return (module_name, ret)
def ACQSDK_StopRecord(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_StopRecord()
	except: ret = None
	finally: return (module_name, ret)
def ACQSDK_Capture(objACQSDK_CSDevice, pImageUnit): # timeout is 2s; actually, real working time 10ms; Wait until it is done
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_Capture(pImageUnit)
	except: ret = None
	finally: return (module_name, ret)
def ACQSDK_GetImageData(objACQSDK_CSDevice, pImageUnit): # timeout is 2s
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_GetImageData(pImageUnit)
	except: ret = None
	finally: return (module_name, ret)
def ACQSDK_SetLogPath(objACQSDK_CSDevice, path):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_SetLogPath(path)
	except: ret = None
	finally: return (module_name, ret)

# Mirror & Rotation
def ACQSDK_SetMirrorFlag(objACQSDK_CSDevice, bEnable):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_SetMirrorFlag(bEnable)
	except: ret = None
	finally: return (module_name, ret)
def ACQSDK_GetMirrorFlag(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_GetMirrorFlag()
	except: ret = None
	finally: return (module_name, ret)
def ACQSDK_SetRotationFlag(objACQSDK_CSDevice, rotation):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_SetRotationFlag(rotation)
	except: ret = None
	finally: return (module_name, ret)
def ACQSDK_GetRotationFlag(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_GetRotationFlag()
	except: ret = None
	finally: return (module_name, ret)

# Query
def ACQSDK_QueryDeviceInfo(objACQSDK_CSDevice, pDeviceInfo):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_QueryDeviceInfo(pDeviceInfo)
	except: ret = None
	finally: return (module_name, ret)
def ACQSDK_GetFirmwareVersion(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_GetFirmwareVersion()
	except: ret = None
	finally: return (module_name, ret)
def ACQSDK_GetSDKVersion(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_GetSDKVersion()
	except: ret = None
	finally: return (module_name, ret)

# Configuration
# >> Brightness
def ACQSDK_GetBrightness(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_GetBrightness()
	except: ret = None
	finally: return (module_name, ret)
def ACQSDK_SetBrightness(objACQSDK_CSDevice, brightness):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_SetBrightness(brightness)
	except: ret = None
	finally: return (module_name, ret)

# >> Contrast
def ACQSDK_GetContrast(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_GetContrast()
	except: ret = None
	finally: return (module_name, ret)
def ACQSDK_SetContrast(objACQSDK_CSDevice, contrast):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_SetContrast(contrast)
	except: ret = None
	finally: return (module_name, ret)

# >> Powerline Frequency
def ACQSDK_GetPowerlineFrequency(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_GetPowerlineFrequency()
	except: ret = None
	finally: return (module_name, ret)
def ACQSDK_SetPowerlineFrequency(objACQSDK_CSDevice, frequency):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_SetPowerlineFrequency(frequency)
	except: ret = None
	finally: return (module_name, ret)

# >> Sleep
def ACQSDK_SetEnableSleep(objACQSDK_CSDevice, bEnable):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_SetEnableSleep(bEnable)
	except: ret = None
	finally: return (module_name, ret)
def ACQSDK_GetEnableSleep(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_GetEnableSleep()
	except: ret = None
	finally: return (module_name, ret)
def ACQSDK_GetSleepTime(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_GetSleepTime()
	except: ret = None
	finally: return (module_name, ret)
def ACQSDK_SetSleepTime(objACQSDK_CSDevice, seconds):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_SetSleepTime(seconds)
	except: ret = None
	finally: return (module_name, ret)

# >> Auto Power On
def ACQSDK_EnableAutoPowerOn(objACQSDK_CSDevice, bEnable):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_EnableAutoPowerOn(bEnable)
	except: ret = None
	finally: return (module_name, ret)
def ACQSDK_GetEnableAutoPowerOn(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_GetEnableAutoPowerOn()
	except: ret = None
	finally: return (module_name, ret)

# >> Auto Power Off
def ACQSDK_EnableAutoPowerOff(objACQSDK_CSDevice, bEnable):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_EnableAutoPowerOff(bEnable)
	except: ret = None
	finally: return (module_name, ret)
def ACQSDK_GetEnableAutoPowerOff(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_GetEnableAutoPowerOff()
	except: ret = None
	finally: return (module_name, ret)
def ACQSDK_GetAutoPowerOffTime(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_GetAutoPowerOffTime()
	except: ret = None
	finally: return (module_name, ret)
def ACQSDK_SetAutoPowerOffTime(objACQSDK_CSDevice, secondsCount):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_SetAutoPowerOffTime(secondsCount)
	except: ret = None
	finally: return (module_name, ret)

# Firmware
def ACQSDK_UpgradeFirmware(objACQSDK_CSDevice, pFullPathName):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_UpgradeFirmware(pFullPathName)
	except: ret = None
	finally: return (module_name, ret)
def ACQSDK_AbortUpgrade(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_AbortUpgrade()
	except: ret = None
	finally: return (module_name, ret)

"""
# MFG
# >> Work Mode
def ACQSDK_SetHPWorkMode(objACQSDK_CSDevice, lWorkMode):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_SetHPWorkMode(lWorkMode)
	except: ret = None
	finally: return (module_name, ret)

# >> Serial Number
def ACQSDK_GetSerialNumber(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_GetSerialNumber()
	except: ret = None
	finally: return (module_name, ret)
def ACQSDK_SetSerialNumber(objACQSDK_CSDevice, sn):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_SetSerialNumber(sn)
	except: ret = None
	finally: return (module_name, ret)

# >> File Upload & Download
def ACQSDK_UploadFile(objACQSDK_CSDevice, pFileName):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_UploadFile(pFileName)
	except: ret = None
	finally: return (module_name, ret)
def ACQSDK_DownloadFile(objACQSDK_CSDevice, fileID, pFileName):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_DownloadFile(fileID, pFileName)
	except: ret = None
	finally: return (module_name, ret)

# >> XU
def ACQSDK_MFG_GetXU(objACQSDK_CSDevice, index, value):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_MFG_GetXU(index, value)
	except: ret = None
	finally: return (module_name, ret)
def ACQSDK_MFG_SetXU(objACQSDK_CSDevice, index, value):
	module_name = sys._getframe().f_code.co_name
	try: ret = objACQSDK_CSDevice.ACQSDK_MFG_SetXU(index, value)
	except: ret = None
	finally: return (module_name, ret)
"""
# ===================================================== CSDevice =====================================================

# Check on local
if __name__ == '__main__': print sys._getframe().f_code.co_filename