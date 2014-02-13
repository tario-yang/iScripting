# Import required module(s)
try:
	import sys
	import TestACQSDK_Module_Global_Definition as GDEF
except ImportError:
	GDEF.Logger("Info -> %r" % sys._getframe().f_code.co_filename)
	GDEF.Logger("Error -> One or more required modules are missing!")
	sys.exit(1)

# Function to record exception, happening while executing API.
def ErrorLogger(module_name):
	GDEF.Logger("Error -> Exception happens when executing %r." % module_name)

def ACQSDK_Init(objACQSDK_CSDevice, hWnd):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_Init(hWnd)
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_UnInit(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_UnInit()
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_OnUpdateLiveWnd(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_OnUpdateLiveWnd()
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_QueryDeviceInfo(objACQSDK_CSDevice, pDeviceInfo):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_QueryDeviceInfo(pDeviceInfo)
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_SetHPWorkMode(objACQSDK_CSDevice, lWorkMode): # Factory Mode requried
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_SetHPWorkMode(lWorkMode)
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_StartPlay(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_StartPlay()
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_PausePlay(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_PausePlay()
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_StopPlay(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_StopPlay()
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_StartRecord(objACQSDK_CSDevice, path):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_StartRecord(path)
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_StopRecord(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_StopRecord()
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_Capture(objACQSDK_CSDevice, pImageUnit): # timeout is 2s; actually, real working time 10ms; Wait until it is done
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_Capture(pImageUnit)
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_GetImageData(objACQSDK_CSDevice, pImageUnit): # timeout is 2s
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_GetImageData(pImageUnit)
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_SetLogPath(objACQSDK_CSDevice, path):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_SetLogPath(path)
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_GetSerialNumber(objACQSDK_CSDevice, len):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_GetSerialNumber(len)
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_SetSerialNumber(objACQSDK_CSDevice, pSn, len):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_SetSerialNumber(pSn, len)
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_GetFirmwareVersion(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_GetFirmwareVersion()
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_UpgradeFirmware(objACQSDK_CSDevice, pFullPathName): # Wait until it is done
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_UpgradeFirmware(pFullPathName)
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_AbortUpgrade(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_AbortUpgrade()
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_UploadFile(objACQSDK_CSDevice, pFileName):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_UploadFile(pFileName)
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_DownloadFile(objACQSDK_CSDevice, fileID, pFileName):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_DownloadFile(fileID, pFileName)
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_EnableAutoPowerOn(objACQSDK_CSDevice, bEnable):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_EnableAutoPowerOn(bEnable)
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_GetBrightness(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_GetBrightness()
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_SetBrightness(objACQSDK_CSDevice, brightness):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_SetBrightness(brightness)
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_GetContrast(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_GetContrast()
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_SetContrast(objACQSDK_CSDevice, contrast):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_SetContrast(contrast)
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_SetPowerlineFrequency(objACQSDK_CSDevice, frequency):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_SetPowerlineFrequency(frequency)
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_GetPowerlineFrequency(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_GetPowerlineFrequency()
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_EnableAutoPowerOff(objACQSDK_CSDevice, bEnable):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_EnableAutoPowerOff(bEnable)
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_SetAutoPowerOffTime(objACQSDK_CSDevice, secondsCount):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_SetAutoPowerOffTime(secondsCount)
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_EnableStandBy(objACQSDK_CSDevice, bEnable):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_EnableStandBy(bEnable)
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_SetStandByTime(objACQSDK_CSDevice, secondsCount):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_SetStandByTime(secondsCount)
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_SetSystemTime(objACQSDK_CSDevice, secondsCount):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_SetSystemTime(secondsCount)
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_SetMirrorFlag(objACQSDK_CSDevice, bEnable):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_SetMirrorFlag(bEnable)
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_GetMirrorFlag(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_GetMirrorFlag()
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_SetRotationFlag(objACQSDK_CSDevice, rotation):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_SetRotationFlag(rotation)
	except:
		ErrorLogger(module_name)
	finally:
		return ret

def ACQSDK_GetRotationFlag(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_GetRotationFlag()
	except:
		ErrorLogger(module_name)
	finally:
		return ret

# Check on local
if __name__ == '__main__':
	print sys._getframe().f_code.co_filename