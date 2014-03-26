"""
Test Cases for SDK API Testing
"""

# Import required modules
import os, sys, gc, threading, time
import win32com.client
from Tkinter import *
sys.path.append(r"../Module")
import TestACQSDK_Module_Global_Definition as GD
import TestACQSDK_Module_Wrapper as SDKAPI

# Handler
root_id = Tk().winfo_id()

# Clean Environment
def CleanEnv(objACQSDK_CSDevice):
	SDKAPI.ACQSDK_UnInit(objACQSDK_CSDevice)
	SDKAPI.ACQSDK_Init(objACQSDK_CSDevice, root_id)

# Remove variables
def RemoveObj(var):
	del var
	gc.collect()

# Basic Function
def ACQSDK_Init(hWnd): # hWnd shall be a global variable
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Execute
	if hWnd == "hWnd": hWnd = root_id
	ret = SDKAPI.ACQSDK_Init(objACQSDK_CSDevice, hWnd)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]
def ACQSDK_UnInit():
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ret = SDKAPI.ACQSDK_UnInit(objACQSDK_CSDevice)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]
def ACQSDK_OnUpdateLiveWnd():
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ret = SDKAPI.ACQSDK_OnUpdateLiveWnd(objACQSDK_CSDevice)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]
def ACQSDK_StartPlay():
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ret = SDKAPI.ACQSDK_StartPlay(objACQSDK_CSDevice)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]
def ACQSDK_StopPlay():
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ACQSDK_StartPlay(objACQSDK_CSDevice)
	ret = SDKAPI.ACQSDK_StopPlay(objACQSDK_CSDevice)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]
def ACQSDK_StartRecord(path):
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	SDKAPI.ACQSDK_StartPlay(objACQSDK_CSDevice)
	ret = SDKAPI.ACQSDK_StartRecord(objACQSDK_CSDevice, path)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]
def ACQSDK_StopRecord():
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	SDKAPI.ACQSDK_StartPlay(objACQSDK_CSDevice)
	SDKAPI.ACQSDK_StartRecord(objACQSDK_CSDevice, r"./TestData - %s.avi" % time.strftime('%Y-%m-%d-%H-%M-%S'))
	time.Sleep(3)
	ret = SDKAPI.ACQSDK_StopRecord(objACQSDK_CSDevice)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]
def ACQSDK_Capture(*args):
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	if len(args) == 0: pImageUnit = win32com.client.Dispatch(GD.ACQSDK_ASImageUnit_ProgID)
	else: pImageUnit = args[0]
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	SDKAPI.ACQSDK_StartPlay(objACQSDK_CSDevice)
	ret = SDKAPI.ACQSDK_Capture(objACQSDK_CSDevice, pImageUnit)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]
def ACQSDK_GetImageData(*args):
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	if len(args) == 0: pImageUnit = win32com.client.Dispatch(GD.ACQSDK_ASImageUnit_ProgID)
	else: pImageUnit = args[0]
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	SDKAPI.ACQSDK_StartPlay(objACQSDK_CSDevice)
	ret = SDKAPI.ACQSDK_GetImageData(objACQSDK_CSDevice, pImageUnit)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]
def ACQSDK_SetLogPath(path):
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ret = SDKAPI.ACQSDK_SetLogPath(objACQSDK_CSDevice, path)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]

# Mirror & Rotation
def ACQSDK_SetMirrorFlag(bEnable):
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	SDKAPI.ACQSDK_StartPlay(objACQSDK_CSDevice)
	ret = SDKAPI.ACQSDK_SetMirrorFlag(objACQSDK_CSDevice, bEnable)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]
def ACQSDK_GetMirrorFlag():
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	SDKAPI.ACQSDK_StartPlay(objACQSDK_CSDevice)
	ret = SDKAPI.ACQSDK_GetMirrorFlag(objACQSDK_CSDevice)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]
def ACQSDK_SetRotationFlag(rotation):
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	SDKAPI.ACQSDK_StartPlay(objACQSDK_CSDevice)
	ret = SDKAPI.ACQSDK_SetRotationFlag(objACQSDK_CSDevice, rotation)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]
def ACQSDK_GetRotationFlag():
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	SDKAPI.ACQSDK_StartPlay(objACQSDK_CSDevice)
	ret = SDKAPI.ACQSDK_GetRotationFlag(objACQSDK_CSDevice)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]

# Query
def ACQSDK_QueryDeviceInfo(*args):
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	if len(args) == 0:
		pDeviceInfo = win32com.client.Dispatch(GD.ACQSDK_ASDeviceInfor_ProgID)
	else:
		pDeviceInfo = args[0]
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ret = SDKAPI.ACQSDK_QueryDeviceInfo(objACQSDK_CSDevice, pDeviceInfo)
	RemoveObj(objACQSDK_CSDevice)
	RemoveObj(pDeviceInfo)
	return ret[1]
def ACQSDK_GetFirmwareVersion():
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ret = SDKAPI.ACQSDK_GetFirmwareVersion(objACQSDK_CSDevice)
	del objACQSDK_CSDevice
	gc.collect()
	return ret[1]
def ACQSDK_GetSDKVersion():
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ret = SDKAPI.ACQSDK_GetSDKVersion(objACQSDK_CSDevice)
	del objACQSDK_CSDevice
	gc.collect()
	return ret[1]

# Configuration

# >> Brightness
def ACQSDK_GetBrightness():
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ret = SDKAPI.ACQSDK_GetBrightness(objACQSDK_CSDevice)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]
def ACQSDK_SetBrightness(brightness):
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ret = SDKAPI.ACQSDK_SetBrightness(objACQSDK_CSDevice, brightness)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]

# >> Contrast
def ACQSDK_GetContrast():
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ret = SDKAPI.ACQSDK_GetContrast(objACQSDK_CSDevice)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]
def ACQSDK_SetContrast(contrast):
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ret = SDKAPI.ACQSDK_SetContrast(objACQSDK_CSDevice, contrast)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]

# >> Powerline Frequency
def ACQSDK_GetPowerlineFrequency():
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ret = SDKAPI.ACQSDK_GetPowerlineFrequency(objACQSDK_CSDevice)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]
def ACQSDK_SetPowerlineFrequency(frequency):
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ret = SDKAPI.ACQSDK_SetPowerlineFrequency(objACQSDK_CSDevice, frequency)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]

# >> Sleep
def ACQSDK_SetEnableSleep(bEnable):
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ret = SDKAPI.ACQSDK_SetEnableSleep(objACQSDK_CSDevice, bEnable)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]
def ACQSDK_GetEnableSleep():
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ret = SDKAPI.ACQSDK_GetEnableSleep(objACQSDK_CSDevice)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]
def ACQSDK_GetSleepTime():
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ret = SDKAPI.ACQSDK_GetSleepTime(objACQSDK_CSDevice)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]
def ACQSDK_SetSleepTime(seconds):
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ret = SDKAPI.ACQSDK_SetSleepTime(objACQSDK_CSDevice, seconds)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]

# >> Auto Power On
def ACQSDK_EnableAutoPowerOn(bEnable):
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ret = SDKAPI.ACQSDK_EnableAutoPowerOn(objACQSDK_CSDevice, bEnable)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]
def ACQSDK_GetEnableAutoPowerOn():
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ret = SDKAPI.ACQSDK_GetEnableAutoPowerOn(objACQSDK_CSDevice)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]

# >> Auto Power Off
def ACQSDK_EnableAutoPowerOff(bEnable):
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ret = SDKAPI.ACQSDK_EnableAutoPowerOff(objACQSDK_CSDevice, bEnable)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]
def ACQSDK_GetEnableAutoPowerOff():
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ret = SDKAPI.ACQSDK_GetEnableAutoPowerOff(objACQSDK_CSDevice)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]
def ACQSDK_GetAutoPowerOffTime():
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ret = SDKAPI.ACQSDK_GetAutoPowerOffTime(objACQSDK_CSDevice)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]
def ACQSDK_SetAutoPowerOffTime(secondsCount):
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ret = SDKAPI.ACQSDK_SetAutoPowerOffTime(objACQSDK_CSDevice, secondsCount)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]

# Firmware
def ACQSDK_UpgradeFirmware(pFullPathName):
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ret = SDKAPI.ACQSDK_UpgradeFirmware(objACQSDK_CSDevice, pFullPathName)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]
def ACQSDK_AbortUpgrade():
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	class FWUpgrade(threading.Thread):
		def __init__(self): threading.Thread.__init__(self)
		def run(self):
			path = r"../TestData/firmware.zip"
			SDKAPI.ACQSDK_UpgradeFirmware(objACQSDK_CSDevice, path)
	instance = FWUpgrade()
	instance.setDaemon(True)
	instance.start()
	time.sleep(3)
	ret = SDKAPI.ACQSDK_AbortUpgrade(objACQSDK_CSDevice)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]

# MFG
def ACQSDK_SetHPWorkMode(lWorkMode):
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ret = SDKAPI.ACQSDK_SetHPWorkMode(objACQSDK_CSDevice, lWorkMode)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]

# >> Serial Number
def ACQSDK_GetSerialNumber():
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ret = SDKAPI.ACQSDK_GetSerialNumber(objACQSDK_CSDevice)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]
def ACQSDK_SetSerialNumber(sn):
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ret = SDKAPI.ACQSDK_SetSerialNumber(objACQSDK_CSDevice, sn)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]

# >> File Upload & Download
def ACQSDK_UploadFile(pFileName):
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ret = SDKAPI.ACQSDK_UploadFile(objACQSDK_CSDevice, pFileName)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]
def ACQSDK_DownloadFile(fileID, pFileName):
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ret = SDKAPI.ACQSDK_DownloadFile(objACQSDK_CSDevice, fileID, pFileName)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]

# >> XU
def ACQSDK_MFG_GetXU(index, value):
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ret = SDKAPI.ACQSDK_MFG_GetXU(objACQSDK_CSDevice, index, value)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]
def ACQSDK_MFG_SetXU(index, value):
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	# Clean
	CleanEnv(objACQSDK_CSDevice)
	# Execute Test
	ret = SDKAPI.ACQSDK_MFG_SetXU(objACQSDK_CSDevice, index, value)
	RemoveObj(objACQSDK_CSDevice)
	return ret[1]

# Exception #1
def ExceptionNotInitiated():
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	pImageUnit         = win32com.client.Dispatch(GD.ACQSDK_ASImageUnit_ProgID)
	pDeviceInfo        = win32com.client.Dispatch(GD.ACQSDK_ASDeviceInfor_ProgID)

	# Precondition
	SDKAPI.ACQSDK_UnInit(objACQSDK_CSDevice)

	# Execute Test
	start = time.time()
	print sys._getframe().f_code.co_name
	print "ACQSDK_OnUpdateLiveWnd -> %r" %       SDKAPI.ACQSDK_OnUpdateLiveWnd(objACQSDK_CSDevice)
	print "ACQSDK_StartPlay -> %r" %             SDKAPI.ACQSDK_StartPlay(objACQSDK_CSDevice)
	print "ACQSDK_StopPlay -> %r" %              SDKAPI.ACQSDK_StopPlay(objACQSDK_CSDevice)
	print "ACQSDK_StartRecord -> %r" %           SDKAPI.ACQSDK_StartRecord(objACQSDK_CSDevice, os.environ.get("tmp") + "\\temp.avi")
	print "ACQSDK_StopRecord -> %r" %            SDKAPI.ACQSDK_StopRecord(objACQSDK_CSDevice)
	print "ACQSDK_Capture -> %r" %               SDKAPI.ACQSDK_Capture(objACQSDK_CSDevice, pImageUnit)
	print "ACQSDK_GetImageData -> %r" %          SDKAPI.ACQSDK_GetImageData(objACQSDK_CSDevice, pImageUnit)
	print "ACQSDK_SetMirrorFlag -> %r" %         SDKAPI.ACQSDK_SetMirrorFlag(objACQSDK_CSDevice, 1)
	print "ACQSDK_GetMirrorFlag -> %r" %         SDKAPI.ACQSDK_GetMirrorFlag(objACQSDK_CSDevice)
	print "ACQSDK_SetRotationFlag -> %r" %       SDKAPI.ACQSDK_SetRotationFlag(objACQSDK_CSDevice, 90)
	print "ACQSDK_GetRotationFlag -> %r" %       SDKAPI.ACQSDK_GetRotationFlag(objACQSDK_CSDevice)
	print "ACQSDK_QueryDeviceInfo -> %r" %       SDKAPI.ACQSDK_QueryDeviceInfo(objACQSDK_CSDevice, pDeviceInfo)
	print "ACQSDK_GetFirmwareVersion -> %r" %    SDKAPI.ACQSDK_GetFirmwareVersion(objACQSDK_CSDevice)
	print "ACQSDK_GetSDKVersion -> %r" %         SDKAPI.ACQSDK_GetSDKVersion(objACQSDK_CSDevice)
	print "ACQSDK_GetBrightness -> %r" %         str(SDKAPI.ACQSDK_GetBrightness(objACQSDK_CSDevice))
	print "ACQSDK_SetBrightness -> %r" %         SDKAPI.ACQSDK_SetBrightness(objACQSDK_CSDevice, 4)
	print "ACQSDK_GetContrast -> %r" %           str(SDKAPI.ACQSDK_GetContrast(objACQSDK_CSDevice))
	print "ACQSDK_SetContrast -> %r" %           SDKAPI.ACQSDK_SetContrast(objACQSDK_CSDevice, 4)
	print "ACQSDK_GetPowerlineFrequency -> %r" % str(SDKAPI.ACQSDK_GetPowerlineFrequency(objACQSDK_CSDevice))
	print "ACQSDK_SetPowerlineFrequency -> %r" % SDKAPI.ACQSDK_SetPowerlineFrequency(objACQSDK_CSDevice, 50)
	print "ACQSDK_SetEnableSleep -> %r" %        SDKAPI.ACQSDK_SetEnableSleep(objACQSDK_CSDevice, 1)
	print "ACQSDK_GetEnableSleep -> %r" %        SDKAPI.ACQSDK_GetEnableSleep(objACQSDK_CSDevice)
	print "ACQSDK_GetSleepTime -> %r" %          SDKAPI.ACQSDK_GetSleepTime(objACQSDK_CSDevice)
	print "ACQSDK_SetSleepTime -> %r" %          SDKAPI.ACQSDK_SetSleepTime(objACQSDK_CSDevice, 60)
	print "ACQSDK_EnableAutoPowerOn -> %r" %     SDKAPI.ACQSDK_EnableAutoPowerOn(objACQSDK_CSDevice, 1)
	print "ACQSDK_GetEnableAutoPowerOn -> %r" %  SDKAPI.ACQSDK_GetEnableAutoPowerOn(objACQSDK_CSDevice)
	print "ACQSDK_EnableAutoPowerOff -> %r" %    SDKAPI.ACQSDK_EnableAutoPowerOff(objACQSDK_CSDevice, 1)
	print "ACQSDK_GetEnableAutoPowerOff -> %r" % SDKAPI.ACQSDK_GetEnableAutoPowerOff(objACQSDK_CSDevice)
	print "ACQSDK_GetAutoPowerOffTime -> %r" %   SDKAPI.ACQSDK_GetAutoPowerOffTime(objACQSDK_CSDevice)
	print "ACQSDK_SetAutoPowerOffTime -> %r" %   SDKAPI.ACQSDK_SetAutoPowerOffTime(objACQSDK_CSDevice, 7200)
	print "ACQSDK_UpgradeFirmware -> %r" %       SDKAPI.ACQSDK_UpgradeFirmware(objACQSDK_CSDevice, r"../Data/firmware.zip")
	print "ACQSDK_AbortUpgrade -> %r" %          SDKAPI.ACQSDK_AbortUpgrade(objACQSDK_CSDevice)
	# print "ACQSDK_SetHPWorkMode -> %r" %       SDKAPI.ACQSDK_SetHPWorkMode
	print "ACQSDK_GetSerialNumber -> %r" %       SDKAPI.ACQSDK_GetSerialNumber(objACQSDK_CSDevice)
	print "ACQSDK_SetSerialNumber -> %r" %       SDKAPI.ACQSDK_SetSerialNumber(objACQSDK_CSDevice, "ABCD1234")
	# print "ACQSDK_UploadFile -> %r" %          SDKAPI.ACQSDK_UploadFile
	# print "ACQSDK_DownloadFile -> %r" %        SDKAPI.ACQSDK_DownloadFile
	# print "ACQSDK_MFG_GetXU -> %r" %           SDKAPI.ACQSDK_MFG_GetXU
	# print "ACQSDK_MFG_SetXU -> %r" %           SDKAPI.ACQSDK_MFG_SetXU
	print "-"*60
	print "Time spent: %r second(s)\n\n" % (time.time() - start)

	# Clean
	RemoveObj(objACQSDK_CSDevice)
	RemoveObj(pImageUnit)
	RemoveObj(pDeviceInfo)

# Exception #2
def ExceptionInitiated():
	# Create ACQSDK COM object
	objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
	pImageUnit         = win32com.client.Dispatch(GD.ACQSDK_ASImageUnit_ProgID)
	pDeviceInfo        = win32com.client.Dispatch(GD.ACQSDK_ASDeviceInfor_ProgID)

	# Precondition
	SDKAPI.ACQSDK_UnInit(objACQSDK_CSDevice)
	SDKAPI.ACQSDK_Init(objACQSDK_CSDevice, root_id)

	# Execute Test
	start = time.time()
	print sys._getframe().f_code.co_name
	print "ACQSDK_OnUpdateLiveWnd -> %r" %       SDKAPI.ACQSDK_OnUpdateLiveWnd(objACQSDK_CSDevice)
	print "ACQSDK_StopPlay -> %r" %              SDKAPI.ACQSDK_StopPlay(objACQSDK_CSDevice)
	print "ACQSDK_StartRecord -> %r" %           SDKAPI.ACQSDK_StartRecord(objACQSDK_CSDevice, os.environ.get("tmp") + "\\temp.avi")
	print "ACQSDK_StopRecord -> %r" %            SDKAPI.ACQSDK_StopRecord(objACQSDK_CSDevice)
	print "ACQSDK_Capture -> %r" %               SDKAPI.ACQSDK_Capture(objACQSDK_CSDevice, pImageUnit)
	print "ACQSDK_GetImageData -> %r" %          SDKAPI.ACQSDK_GetImageData(objACQSDK_CSDevice, pImageUnit)
	print "-"*60
	print "Time spent: %r second(s)\n\n" % (time.time() - start)

	# Clean
	RemoveObj(objACQSDK_CSDevice)
	RemoveObj(pImageUnit)
	RemoveObj(pDeviceInfo)

# Check on local
if __name__ == '__main__':
	print sys._getframe().f_code.co_filename