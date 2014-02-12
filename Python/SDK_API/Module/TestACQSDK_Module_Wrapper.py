# Import required module(s)
try:
	import sys
	import TestACQSDK_Module_Global_Definition as GDEF
except ImportError:
	GDEF.Logger("Error -> One or more required modules are missing!")
	sys.exit(1)

def ConfirmResult(module_name, ret, *parameter):
	try:
		print type(eval(str(ret)))
	except NameError:
		GDEF.Logger(r"Error -> Fail to execute " + module_name)
	except TypeError:
		GDEF.Logger(r"Error -> Unexpected Type of ret is received.")
	else:
		if parameter is None:
			GDEF.TEE(module_name, ret)
		else:
			p = ""
			for i in parameter:
				if p == "":
					p = p + "%r" % i
				else:
					p = p + "_%r" % i
			GDEF.TEE(module_name, ret, p)

def ACQSDK_Init(objACQSDK_CSDevice, hWnd):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_Init(hWnd)
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret, hWnd)

def ACQSDK_UnInit(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_UnInit()
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret)

def ACQSDK_OnUpdateLiveWnd(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_OnUpdateLiveWnd()
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret)

def ACQSDK_QueryDeviceInfo(objACQSDK_CSDevice, pDeviceInfo):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_QueryDeviceInfo(pDeviceInfo)
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret, pDeviceInfo)

def ACQSDK_SetHPWorkMode(objACQSDK_CSDevice, lWorkMode): # Factory Mode requried
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_SetHPWorkMode(lWorkMode)
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret, lWorkMode)

def ACQSDK_StartPlay(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_StartPlay()
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret)

def ACQSDK_PausePlay(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_PausePlay()
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret)

def ACQSDK_StopPlay(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_StopPlay()
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret)

def ACQSDK_StartRecord(objACQSDK_CSDevice, path):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_StartRecord(path)
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret, path)

def ACQSDK_StopRecord(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_StopRecord()
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret)

def ACQSDK_Capture(objACQSDK_CSDevice, pImageUnit): # timeout is 2s; actually, real working time 10ms; Wait until it is done
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_Capture(pImageUnit)
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret, pImageUnit)

def ACQSDK_GetImageData(objACQSDK_CSDevice, pImageUnit): # timeout is 2s
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_GetImageData(pImageUnit)
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret, pImageUnit)

def ACQSDK_SetLogPath(objACQSDK_CSDevice, path):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_SetLogPath(path)
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret, path)

def ACQSDK_GetSerialNumber(objACQSDK_CSDevice, len):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_GetSerialNumber(len)
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret, len)

def ACQSDK_SetSerialNumber(objACQSDK_CSDevice, pSn, len):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_SetSerialNumber(pSn, len)
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret, pSn, len)

def ACQSDK_GetFirmwareVersion(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_GetFirmwareVersion()
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret)

def ACQSDK_UpgradeFirmware(objACQSDK_CSDevice, pFullPathName): # Wait until it is done
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_UpgradeFirmware(pFullPathName)
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret, pFullPathName)

def ACQSDK_AbortUpgrade(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_AbortUpgrade()
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret)

def ACQSDK_UploadFile(objACQSDK_CSDevice, pFileName):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_UploadFile(pFileName)
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret, pFileName)

def ACQSDK_DownloadFile(objACQSDK_CSDevice, fileID, pFileName):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_DownloadFile(fileID, pFileName)
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret, fileID, pFileName)

def ACQSDK_EnableAutoPowerOn(objACQSDK_CSDevice, bEnable):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_EnableAutoPowerOn(bEnable)
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret, bEnable)

def ACQSDK_GetBrightness(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_GetBrightness()
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret)

def ACQSDK_SetBrightness(objACQSDK_CSDevice, brightness):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_SetBrightness(brightness)
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret, brightness)

def ACQSDK_GetContrast(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_GetContrast()
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret)

def ACQSDK_SetContrast(objACQSDK_CSDevice, contrast):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_SetContrast(contrast)
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret, contrast)

def ACQSDK_SetPowerlineFrequency(objACQSDK_CSDevice, frequency):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_SetPowerlineFrequency(frequency)
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret, frequency)

def ACQSDK_GetPowerlineFrequency(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_GetPowerlineFrequency()
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret)

def ACQSDK_EnableAutoPowerOff(objACQSDK_CSDevice, bEnable):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_EnableAutoPowerOff(bEnable)
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret, bEnable)

def ACQSDK_SetAutoPowerOffTime(objACQSDK_CSDevice, secondsCount):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_SetAutoPowerOffTime(secondsCount)
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret, secondsCount)

def ACQSDK_EnableStandBy(objACQSDK_CSDevice, bEnable):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_EnableStandBy(bEnable)
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret, bEnable)

def ACQSDK_SetStandByTime(objACQSDK_CSDevice, secondsCount):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_SetStandByTime(secondsCount)
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret, secondsCount)

def ACQSDK_SetSystemTime(objACQSDK_CSDevice, secondsCount):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_SetSystemTime(secondsCount)
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret, secondsCount)

def ACQSDK_SetMirrorFlag(objACQSDK_CSDevice, bEnable):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_SetMirrorFlag(bEnable)
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret, bEnable)

def ACQSDK_GetMirrorFlag(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_GetMirrorFlag()
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret)

def ACQSDK_SetRotationFlag(objACQSDK_CSDevice, rotation):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_SetRotationFlag(rotation)
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret, rotation)

def ACQSDK_GetRotationFlag(objACQSDK_CSDevice):
	module_name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_GetRotationFlag()
	except:
		GDEF.Logger("Error -> Exception happens when executing API.")
	finally:
		ConfirmResult(module_name, ret)
