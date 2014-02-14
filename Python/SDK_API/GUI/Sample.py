"""
	GUI: Quick Checking
"""
import os, sys, datetime, time
import win32com.client, win32gui, time
import Tkinter

def ACQSDK_Init(): # OK
	ACQSDK_SetLogPath()
	hWnd = win32gui.FindWindow("TkTopLevel","SDK Testing: Live Video")
	ret = objACQSDK_CSDevice.ACQSDK_Init(hWnd)
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
def ACQSDK_UnInit(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_UnInit()
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
def ACQSDK_OnUpdateLiveWnd(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_OnUpdateLiveWnd()
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
def ACQSDK_QueryDeviceInfo(): # OK
	pDeviceInfo = objACQSDK_ASDeviceInfor
	ret = objACQSDK_CSDevice.ACQSDK_QueryDeviceInfo(pDeviceInfo)
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
	if ret == 0:
		print "Device Type is '%r'" % pDeviceInfo.get_device_type()
		print "Mode Type is '%r'" % pDeviceInfo.get_mode_type()
		print "Serial Number is '%r'" % pDeviceInfo.get_sn()
		print "Firmware Version is '%r'" % pDeviceInfo.get_fw_version()
def ACQSDK_SetHPWorkMode(): # Not implemented
	lWorkMode = 1
	ret = objACQSDK_CSDevice.ACQSDK_SetHPWorkMode(lWorkMode)
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
def ACQSDK_StartPlay(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_StartPlay()
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
def ACQSDK_PausePlay(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_PausePlay()
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
def ACQSDK_StopPlay(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_StopPlay()
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
def ACQSDK_StartRecord(): # OK
	path = r"./%s.avi" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
	ret = objACQSDK_CSDevice.ACQSDK_StartRecord(path)
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
def ACQSDK_StopRecord(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_StopRecord()
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
def ACQSDK_Capture(): # OK
	pImageUnit = objACQSDK_ASImageUnit
	ret = objACQSDK_CSDevice.ACQSDK_Capture(pImageUnit)
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
	if ret == 0:
		img = pImageUnit.get_white_image()
		print "\tGet white image -> %r" % img
		print "\tSave image -> %r" % pImageUnit.save_image(r"./%s" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S'), img)
		print "\tFree image -> %r" % pImageUnit.free_image(img)
		print "\tFree unit -> %r" % pImageUnit.free_unit()
def ACQSDK_GetImageData(): # Need multithread + callback
	pImageUnit = objACQSDK_ASImageUnit
	ret = objACQSDK_CSDevice.ACQSDK_GetImageData(pImageUnit)
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
def ACQSDK_SetLogPath(): # OK
	path=r"."
	ret = objACQSDK_CSDevice.ACQSDK_SetLogPath(path)
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
def ACQSDK_GetSerialNumber():
	len = 1
	ret = objACQSDK_CSDevice.ACQSDK_GetSerialNumber(len)
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
def ACQSDK_SetSerialNumber():
	pSn, len = 1
	ret = objACQSDK_CSDevice.ACQSDK_SetSerialNumber(pSn, len)
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
def ACQSDK_GetFirmwareVersion(): # ISSUE
	length = 10
	ret = objACQSDK_CSDevice.ACQSDK_GetFirmwareVersion(length)
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
def ACQSDK_UpgradeFirmware():
	pFullPathName = r"."
	ret = objACQSDK_CSDevice.ACQSDK_UpgradeFirmware(pFullPathName)
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
def ACQSDK_AbortUpgrade():
	ret = objACQSDK_CSDevice.ACQSDK_AbortUpgrade()
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
def ACQSDK_UploadFile():
	pFileName = 1
	ret = objACQSDK_CSDevice.ACQSDK_UploadFile(pFileName)
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
def ACQSDK_DownloadFile():
	fileID, pFileName = 1
	ret = objACQSDK_CSDevice.ACQSDK_DownloadFile(fileID, pFileName)
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
def ACQSDK_EnableAutoPowerOn(): # OK, suggest not to use parameter
	bEnable = 1
	ret = objACQSDK_CSDevice.ACQSDK_EnableAutoPowerOn(bEnable)
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
def ACQSDK_GetBrightness(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_GetBrightness()
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
	if ret[0] == 0:
		print "Current brightness: %r" % ret[1]
		print "Maximum brightness: %r" % ret[2]
		print "Minimum brightness: %r" % ret[3]
		print "Default brightness: %r" % ret[4]
def ACQSDK_SetBrightness(): # OK
	brightness = 7
	ret = objACQSDK_CSDevice.ACQSDK_SetBrightness(brightness)
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
def ACQSDK_GetContrast(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_GetContrast()
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
	if ret[0] == 0:
		print "Current contrast: %r" % ret[1]
		print "Maximum contrast: %r" % ret[2]
		print "Minimum contrast: %r" % ret[3]
		print "Default contrast: %r" % ret[4]
def ACQSDK_SetContrast(): # OK
	contrast = 7
	ret = objACQSDK_CSDevice.ACQSDK_SetContrast(contrast)
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
def ACQSDK_SetPowerlineFrequency(): # OK
	frequency = 60
	ret = objACQSDK_CSDevice.ACQSDK_SetPowerlineFrequency(frequency)
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
def ACQSDK_GetPowerlineFrequency(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_GetPowerlineFrequency()
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
	if ret[0] == 0:
		print("Current frequency: %r" % ret[1])
		print("Default frequency: %r" % ret[2])
def ACQSDK_EnableAutoPowerOff(): # OK, suggest not to use parameter
	bEnable = 1
	ret = objACQSDK_CSDevice.ACQSDK_EnableAutoPowerOff(bEnable)
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
def ACQSDK_SetAutoPowerOffTime():
	secondsCount = 1
	ret = objACQSDK_CSDevice.ACQSDK_SetAutoPowerOffTime(secondsCount)
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
def ACQSDK_EnableStandBy():
	bEnable = 1
	ret = objACQSDK_CSDevice.ACQSDK_EnableStandBy(bEnable)
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
def ACQSDK_SetStandByTime():
	secondsCount = 1
	ret = objACQSDK_CSDevice.ACQSDK_SetStandByTime(secondsCount)
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
def ACQSDK_SetSystemTime():
	secondsCount = 1
	ret = objACQSDK_CSDevice.ACQSDK_SetSystemTime(secondsCount)
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
def ACQSDK_SetMirrorFlag():
	bEnable = 1
	ret = objACQSDK_CSDevice.ACQSDK_SetMirrorFlag(bEnable)
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
def ACQSDK_GetMirrorFlag():
	ret = objACQSDK_CSDevice.ACQSDK_GetMirrorFlag()
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
def ACQSDK_SetRotationFlag():
	rotation = 1
	ret = objACQSDK_CSDevice.ACQSDK_SetRotationFlag(rotation)
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)
def ACQSDK_GetRotationFlag():
	ret = objACQSDK_CSDevice.ACQSDK_GetRotationFlag()
	print "%s -> %r" % (sys._getframe().f_code.co_name, ret)

ACQSDK_CSDevice_ProgID        = "ACQSDK.CSDevice.1"
ACQSDK_ASImageUnit_ProgID     = "ACQSDK.ASImageUnit.1"
ACQSDK_SDKCallbackInfo_ProgID = "ACQSDK.SDKCallbackInfo.1"
ACQSDK_ASDeviceInfor_ProgID   = "ACQSDK.ASDeviceInfor.1"
objACQSDK_CSDevice            = win32com.client.Dispatch(ACQSDK_CSDevice_ProgID)
objACQSDK_ASImageUnit         = win32com.client.Dispatch(ACQSDK_ASImageUnit_ProgID)
objACQSDK_SDKCallbackInfo     = win32com.client.Dispatch(ACQSDK_SDKCallbackInfo_ProgID)
objACQSDK_ASDeviceInfor       = win32com.client.Dispatch(ACQSDK_ASDeviceInfor_ProgID)

wControlPanel = Tkinter.Tk()
wLiveVideo    = Tkinter.Tk()

wControlPanel.geometry("353x480+655+0")
wControlPanel.title("SDK Testing: Control Panel")
wLiveVideo.geometry("640x480+0+0")
wLiveVideo.title("SDK Testing: Live Video")

frame_BasicControl = Tkinter.Frame(wControlPanel).grid()

Tkinter.Label(frame_BasicControl, text = "Basic Functions").grid(                                                                           row = 1,  column = 1)
Tkinter.Button(frame_BasicControl, text ="Init",               bd = 3, width = 15, height = 1, command = ACQSDK_Init).grid(                 row = 2,  column = 1)
Tkinter.Button(frame_BasicControl, text ="UnInit",             bd = 3, width = 15, height = 1, command = ACQSDK_UnInit).grid(               row = 3,  column = 1)
Tkinter.Button(frame_BasicControl, text ="Refresh Live Video", bd = 3, width = 15, height = 1, command = ACQSDK_OnUpdateLiveWnd).grid(      row = 4,  column = 1)
Tkinter.Button(frame_BasicControl, text ="Start Play",         bd = 3, width = 15, height = 1, command = ACQSDK_StartPlay).grid(            row = 2,  column = 2)
Tkinter.Button(frame_BasicControl, text ="Pause Play",         bd = 3, width = 15, height = 1, command = ACQSDK_PausePlay).grid(            row = 3,  column = 2)
Tkinter.Button(frame_BasicControl, text ="Stop Play",          bd = 3, width = 15, height = 1, command = ACQSDK_StopPlay).grid(             row = 4,  column = 2)
Tkinter.Button(frame_BasicControl, text ="Capture Image",      bd = 3, width = 15, height = 1, command = ACQSDK_Capture).grid(              row = 2,  column = 3)
Tkinter.Button(frame_BasicControl, text ="Start Record",       bd = 3, width = 15, height = 1, command = ACQSDK_StartRecord).grid(          row = 3,  column = 3)
Tkinter.Button(frame_BasicControl, text ="Stop Record",        bd = 3, width = 15, height = 1, command = ACQSDK_StopRecord).grid(           row = 4,  column = 3)

Tkinter.Label(frame_BasicControl,  text = "Others").grid(                                                                                   row = 6,  column = 1)

Tkinter.Label(frame_BasicControl,  text = "Query & Upgrade").grid(                                                                          row = 7,  column = 2)
Tkinter.Button(frame_BasicControl, text ="Query Device Info",  bd = 3, width = 15, height = 1, command = ACQSDK_QueryDeviceInfo).grid(      row = 8,  column = 1)
Tkinter.Button(frame_BasicControl, text ="?Get FW Version",     bd = 3, width = 15, height = 1, command = ACQSDK_GetFirmwareVersion).grid(   row = 9,  column = 1)
Tkinter.Button(frame_BasicControl, text ="?Get Serial Number",  bd = 3, width = 15, height = 1, command = ACQSDK_GetSerialNumber).grid(      row = 8,  column = 2)
Tkinter.Button(frame_BasicControl, text ="?Set Serial Number",  bd = 3, width = 15, height = 1, command = ACQSDK_SetSerialNumber).grid(      row = 9,  column = 2)
Tkinter.Button(frame_BasicControl, text ="?Upgrade FW",         bd = 3, width = 15, height = 1, command = ACQSDK_UpgradeFirmware).grid(      row = 8,  column = 3)
Tkinter.Button(frame_BasicControl, text ="?Abort Upgrade",      bd = 3, width = 15, height = 1, command = ACQSDK_AbortUpgrade).grid(         row = 9,  column = 3)

Tkinter.Label(frame_BasicControl,  text = "HP Configuration").grid(                                                                         row = 10, column = 2)
Tkinter.Button(frame_BasicControl, text ="Get Brightness",     bd = 3, width = 15, height = 1, command = ACQSDK_GetBrightness).grid(        row = 11, column = 1)
Tkinter.Button(frame_BasicControl, text ="Set Brightness",     bd = 3, width = 15, height = 1, command = ACQSDK_SetBrightness).grid(        row = 12, column = 1)
Tkinter.Button(frame_BasicControl, text ="Get Contrast",       bd = 3, width = 15, height = 1, command = ACQSDK_GetContrast).grid(          row = 13, column = 1)
Tkinter.Button(frame_BasicControl, text ="Set Contrast",       bd = 3, width = 15, height = 1, command = ACQSDK_SetContrast).grid(          row = 14, column = 1)
Tkinter.Button(frame_BasicControl, text ="Get Frequency",      bd = 3, width = 15, height = 1, command = ACQSDK_GetPowerlineFrequency).grid(row = 11, column = 2)
Tkinter.Button(frame_BasicControl, text ="Set Frequency",      bd = 3, width = 15, height = 1, command = ACQSDK_SetPowerlineFrequency).grid(row = 12, column = 2)
Tkinter.Button(frame_BasicControl, text ="Enable Auto On",     bd = 3, width = 15, height = 1, command = ACQSDK_EnableAutoPowerOn).grid(    row = 13, column = 2)
Tkinter.Button(frame_BasicControl, text ="Enable Auto Off",    bd = 3, width = 15, height = 1, command = ACQSDK_EnableAutoPowerOff).grid(   row = 14, column = 2)


wLiveVideo.mainloop()