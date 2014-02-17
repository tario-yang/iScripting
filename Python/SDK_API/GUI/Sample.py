"""
	GUI: Quick Checking
"""
import os, sys, datetime, time
import win32com.client, win32gui, time
from Tkinter import *
from ScrolledText import ScrolledText
from tkFileDialog import *
import tkMessageBox

def ResetWindow(width, height): wLiveVideo.geometry("%sx%s+368+0" % (width, height))
def EXITAPP():
	objACQSDK_CSDevice.ACQSDK_UnInit()
	wControlPanel.quit()
def WinCallback():
	EXITAPP()

def ACQSDK_Init(): # OK
	ACQSDK_SetLogPath()
	hWnd = win32gui.FindWindow("TkTopLevel","SDK Testing: Live Video")
	ret = objACQSDK_CSDevice.ACQSDK_Init(hWnd)
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
def ACQSDK_UnInit(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_UnInit()
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
def ACQSDK_OnUpdateLiveWnd(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_OnUpdateLiveWnd()
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
def ACQSDK_QueryDeviceInfo(): # OK
	pDeviceInfo = objACQSDK_ASDeviceInfor
	ret = objACQSDK_CSDevice.ACQSDK_QueryDeviceInfo(pDeviceInfo)
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
	if ret == 0:
		Logger("\tDevice Type is '%r'" % pDeviceInfo.get_device_type())
		Logger("\tMode Type is '%r'" % pDeviceInfo.get_mode_type())
		Logger("\tSerial Number is '%r'" % pDeviceInfo.get_sn())
		Logger("\tFirmware Version is '%r'" % pDeviceInfo.get_fw_version())
def ACQSDK_SetHPWorkMode(): # Not implemented
	lWorkMode = 1
	ret = objACQSDK_CSDevice.ACQSDK_SetHPWorkMode(lWorkMode)
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
def ACQSDK_StartPlay(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_StartPlay()
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
def ACQSDK_PausePlay(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_PausePlay()
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
def ACQSDK_StopPlay(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_StopPlay()
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
def ACQSDK_StartRecord(): # OK
	path = r"./%s.avi" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
	ret = objACQSDK_CSDevice.ACQSDK_StartRecord(path)
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
def ACQSDK_StopRecord(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_StopRecord()
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
def ACQSDK_Capture(): # OK
	pImageUnit = objACQSDK_ASImageUnit
	ret = objACQSDK_CSDevice.ACQSDK_Capture(pImageUnit)
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
	if ret == 0:
		img = pImageUnit.get_white_image()
		Logger("\tGet white image -> %r" % img)
		Logger("\tSave image -> %r" % pImageUnit.save_image(r"./%s" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S'), img))
		Logger("\tFree image -> %r" % pImageUnit.free_image(img))
		Logger("\tFree unit -> %r" % pImageUnit.free_unit())
def ACQSDK_GetImageData(): # Need multithread + callback
	pImageUnit = objACQSDK_ASImageUnit
	ret = objACQSDK_CSDevice.ACQSDK_GetImageData(pImageUnit)
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
	if ret == 0:
		img = pImageUnit.get_white_image()
		Logger("\tGet white image -> %r" % img)
		Logger("\tSave image -> %r" % pImageUnit.save_image(r"./%s" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S'), img))
		Logger("\tFree image -> %r" % pImageUnit.free_image(img))
		Logger("\tFree unit -> %r" % pImageUnit.free_unit())
def ACQSDK_SetLogPath(): # OK
	path = r"."
	ret  = objACQSDK_CSDevice.ACQSDK_SetLogPath(path)
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
def ACQSDK_GetSerialNumber(): # ->>> ISSUE
	length = 8
	ret    = objACQSDK_CSDevice.ACQSDK_GetSerialNumber(length)
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
def ACQSDK_SetSerialNumber(): # ->>> ISSUE
	pSn = "ASDF0001"
	length = 8
	ret = objACQSDK_CSDevice.ACQSDK_SetSerialNumber(pSn, len)
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
def ACQSDK_GetFirmwareVersion(): # ->>> ISSUE
	length = 10
	ret = objACQSDK_CSDevice.ACQSDK_GetFirmwareVersion(length)
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
def ACQSDK_UpgradeFirmware():
	pFullPathName = askopenfilename()
	ret = objACQSDK_CSDevice.ACQSDK_UpgradeFirmware(pFullPathName)
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
def ACQSDK_AbortUpgrade():
	ret = objACQSDK_CSDevice.ACQSDK_AbortUpgrade()
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
def ACQSDK_UploadFile():
	pFileName = askopenfilename()
	ret = objACQSDK_CSDevice.ACQSDK_UploadFile(pFileName)
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
def ACQSDK_DownloadFile():
	fileID = 1
	pFileName = "."
	ret = objACQSDK_CSDevice.ACQSDK_DownloadFile(fileID, pFileName)
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
def ACQSDK_EnableAutoPowerOn(): # OK, suggest not to use parameter
	bEnable = 1
	ret = objACQSDK_CSDevice.ACQSDK_EnableAutoPowerOn(bEnable)
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
def ACQSDK_GetBrightness(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_GetBrightness()
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
	if ret[0] == 0:
		Logger("\tCurrent brightness: %r" % ret[1])
		Logger("\tMaximum brightness: %r" % ret[2])
		Logger("\tMinimum brightness: %r" % ret[3])
		Logger("\tDefault brightness: %r" % ret[4])
def ACQSDK_SetBrightness(): # OK
	brightness = 4
	ret = objACQSDK_CSDevice.ACQSDK_SetBrightness(brightness)
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
def ACQSDK_GetContrast(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_GetContrast()
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
	if ret[0] == 0:
		Logger("\tCurrent contrast: %r" % ret[1])
		Logger("\tMaximum contrast: %r" % ret[2])
		Logger("\tMinimum contrast: %r" % ret[3])
		Logger("\tDefault contrast: %r" % ret[4])
def ACQSDK_SetContrast(): # OK
	contrast = 7
	ret = objACQSDK_CSDevice.ACQSDK_SetContrast(contrast)
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
def ACQSDK_SetPowerlineFrequency(): # OK
	frequency = 60
	ret = objACQSDK_CSDevice.ACQSDK_SetPowerlineFrequency(frequency)
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
def ACQSDK_GetPowerlineFrequency(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_GetPowerlineFrequency()
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
	if ret[0] == 0:
		Logger("Current frequency: %r" % ret[1])
		Logger("Default frequency: %r" % ret[2])
def ACQSDK_EnableAutoPowerOff(): # OK, suggest not to use parameter
	bEnable = 1
	ret = objACQSDK_CSDevice.ACQSDK_EnableAutoPowerOff(bEnable)
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
def ACQSDK_SetAutoPowerOffTime(): # OK
	secondsCount = 0
	ret = objACQSDK_CSDevice.ACQSDK_SetAutoPowerOffTime(secondsCount)
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
def ACQSDK_EnableStandBy(): # OK
	bEnable = 1
	ret = objACQSDK_CSDevice.ACQSDK_EnableStandBy(bEnable)
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
def ACQSDK_SetStandByTime(): # OK
	secondsCount = 1000
	ret = objACQSDK_CSDevice.ACQSDK_SetStandByTime(secondsCount)
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
def ACQSDK_SetSystemTime(): # OK
	secondsCount = 1000
	ret = objACQSDK_CSDevice.ACQSDK_SetSystemTime(secondsCount)
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
def ACQSDK_SetMirrorFlag(): # Not Implemented
	bEnable = 1
	ret = objACQSDK_CSDevice.ACQSDK_SetMirrorFlag(bEnable)
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
def ACQSDK_GetMirrorFlag(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_GetMirrorFlag()
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
def ACQSDK_SetRotationFlag(): # Not Implemented
	rotation = 90 # 0, 90, 180, 270
	ret = objACQSDK_CSDevice.ACQSDK_SetRotationFlag(rotation)
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))
def ACQSDK_GetRotationFlag(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_GetRotationFlag()
	Logger("%s -> %r" % (sys._getframe().f_code.co_name, ret))

def Logger(strLine):
	strLine = "%s\n" % strLine
	txtLogger.insert(INSERT, strLine)
def CLEANHistory(): txtLogger.delete('1.0', END)

class SDKEvents():
	def OnHPEvents(self, objACQSDK_SDKCallbackInfo):
		Logger("Parameter data type: %r" % objACQSDK_SDKCallbackInfo)
		objACQSDK_SDKCallbackInfo.get_event_id()

ACQSDK_CSDevice_ProgID        = "ACQSDK.CSDevice.1"
ACQSDK_ASImageUnit_ProgID     = "ACQSDK.ASImageUnit.1"
ACQSDK_SDKCallbackInfo_ProgID = "ACQSDK.SDKCallbackInfo.1"
ACQSDK_ASDeviceInfor_ProgID   = "ACQSDK.ASDeviceInfor.1"

objACQSDK_CSDevice            = win32com.client.DispatchWithEvents(ACQSDK_CSDevice_ProgID, SDKEvents)
objACQSDK_ASImageUnit         = win32com.client.Dispatch(ACQSDK_ASImageUnit_ProgID)
objACQSDK_SDKCallbackInfo     = win32com.client.Dispatch(ACQSDK_SDKCallbackInfo_ProgID)
objACQSDK_ASDeviceInfor       = win32com.client.Dispatch(ACQSDK_ASDeviceInfor_ProgID)

wControlPanel = Tk()
wLiveVideo    = Tk()

wControlPanel.geometry("352x755+5+5")
wControlPanel.title("SDK Testing: Control Panel")
wControlPanel.resizable(width = False, height = False)
wLiveVideo.geometry("640x480+368+0")
wLiveVideo.title("SDK Testing: Live Video")
wLiveVideo.resizable(width = True, height = True)

# Create frame
frame_Controls = Frame(wControlPanel).grid(row = 0, column = 0)

#	Button Set 1
Label(frame_Controls,  text = "Basic").grid(                                                                               row = 0,  column = 0)
#	Buttons
Button(frame_Controls, text = "Init",               bd = 3, width = 15, height = 1, command = ACQSDK_Init).grid(           row = 1,  column = 0)
Button(frame_Controls, text = "UnInit",             bd = 3, width = 15, height = 1, command = ACQSDK_UnInit).grid(         row = 2,  column = 0)
Button(frame_Controls, text = "Refresh Live Video", bd = 3, width = 15, height = 1, command = ACQSDK_OnUpdateLiveWnd).grid(row = 3,  column = 0)
Button(frame_Controls, text = "Start Play",         bd = 3, width = 15, height = 1, command = ACQSDK_StartPlay).grid(      row = 1,  column = 1)
Button(frame_Controls, text = "Pause Play",         bd = 3, width = 15, height = 1, command = ACQSDK_PausePlay).grid(      row = 2,  column = 1)
Button(frame_Controls, text = "Stop Play",          bd = 3, width = 15, height = 1, command = ACQSDK_StopPlay).grid(       row = 3,  column = 1)
Button(frame_Controls, text = "Capture Image",      bd = 3, width = 15, height = 1, command = ACQSDK_Capture).grid(        row = 1,  column = 2)
Button(frame_Controls, text = "Start Record",       bd = 3, width = 15, height = 1, command = ACQSDK_StartRecord).grid(    row = 2,  column = 2)
Button(frame_Controls, text = "Stop Record",        bd = 3, width = 15, height = 1, command = ACQSDK_StopRecord).grid(     row = 3,  column = 2)

#	Button Set 2
Label(frame_Controls,  text = "Extention").grid(                                                                             row = 4, column = 0)
#	Buttons
Label(frame_Controls,  text = "Query & Upgrade").grid(                                                                       row = 5, column = 1)
Button(frame_Controls, text = "Query Device Info", bd = 3, width = 15, height = 1, command = ACQSDK_QueryDeviceInfo).grid(   row = 6, column = 0)
Button(frame_Controls, text = "Get FW Version",    bd = 3, width = 15, height = 1, command = ACQSDK_GetFirmwareVersion).grid(row = 7, column = 0)
Button(frame_Controls, text = "Get Serial Number", bd = 3, width = 15, height = 1, command = ACQSDK_GetSerialNumber).grid(   row = 6, column = 1)
Button(frame_Controls, text = "Set Serial Number", bd = 3, width = 15, height = 1, command = ACQSDK_SetSerialNumber).grid(   row = 7, column = 1)
Button(frame_Controls, text = "Upgrade FW",        bd = 3, width = 15, height = 1, command = ACQSDK_UpgradeFirmware).grid(   row = 6, column = 2)
Button(frame_Controls, text = "Abort Upgrade",     bd = 3, width = 15, height = 1, command = ACQSDK_AbortUpgrade).grid(      row = 7, column = 2)

#	Button Set 3
Label(frame_Controls,  text = "HP Configuration").grid(                                                                          row = 8, column = 1)
#	Buttons
Button(frame_Controls, text = "Get Brightness",     bd = 3, width = 15, height = 1, command = ACQSDK_GetBrightness).grid(        row = 9,  column = 0)
Button(frame_Controls, text = "Set Brightness",     bd = 3, width = 15, height = 1, command = ACQSDK_SetBrightness).grid(        row = 10, column = 0)
Button(frame_Controls, text = "Get Contrast",       bd = 3, width = 15, height = 1, command = ACQSDK_GetContrast).grid(          row = 11, column = 0)
Button(frame_Controls, text = "Set Contrast",       bd = 3, width = 15, height = 1, command = ACQSDK_SetContrast).grid(          row = 12, column = 0)
Button(frame_Controls, text = "Get Frequency",      bd = 3, width = 15, height = 1, command = ACQSDK_GetPowerlineFrequency).grid(row = 9,  column = 1)
Button(frame_Controls, text = "Set Frequency",      bd = 3, width = 15, height = 1, command = ACQSDK_SetPowerlineFrequency).grid(row = 10, column = 1)
Button(frame_Controls, text = "Auto Power On",      bd = 3, width = 15, height = 1, command = ACQSDK_EnableAutoPowerOn).grid(    row = 11, column = 1)
Button(frame_Controls, text = "Auto Power Off",     bd = 3, width = 15, height = 1, command = ACQSDK_EnableAutoPowerOff).grid(   row = 12, column = 1)
Button(frame_Controls, text = "Enable Standby",     bd = 3, width = 15, height = 1, command = ACQSDK_EnableStandBy).grid(        row = 9,  column = 2)
Button(frame_Controls, text = "Set Standby Time",   bd = 3, width = 15, height = 1, command = ACQSDK_SetStandByTime).grid(       row = 10, column = 2)
Button(frame_Controls, text = "Set System Time",    bd = 3, width = 15, height = 1, command = ACQSDK_SetSystemTime).grid(        row = 11, column = 2)
Button(frame_Controls, text = "Set Power Off Time", bd = 3, width = 15, height = 1, command = ACQSDK_SetAutoPowerOffTime).grid(  row = 12, column = 2)

#	Button Set 4
Label(frame_Controls,  text = "Mirror & Rotation").grid(                                                                             row = 13, column = 1)
#	Buttons
Button(frame_Controls, text = "Get Mirror Flag",   bd = 3, width = 15, height = 1, command = ACQSDK_GetMirrorFlag).grid(             row = 14, column = 0)
Button(frame_Controls, text = "Set Mirror Flag",   bd = 3, width = 15, height = 1, command = ACQSDK_SetMirrorFlag).grid(             row = 15, column = 0)
Button(frame_Controls, text = "Get Rotation Flag", bd = 3, width = 15, height = 1, command = ACQSDK_GetRotationFlag).grid(           row = 14, column = 1)
Button(frame_Controls, text = "Set Rotation Flag", bd = 3, width = 15, height = 1, command = ACQSDK_SetRotationFlag).grid(           row = 15, column = 1)
Button(frame_Controls, text = "Set to 640*480",    bd = 3, width = 15, height = 1, command = lambda: ResetWindow("640", "480")).grid(row = 14, column = 2)
Button(frame_Controls, text = "Set to 480*640",    bd = 3, width = 15, height = 1, command = lambda: ResetWindow("480", "640")).grid(row = 15, column = 2)

#	Button Set 5
Label(frame_Controls,  text = "File Operation").grid(                                                              row = 16, column = 1)
#	Buttons
Button(frame_Controls, text = "Upload File",   bd = 3, width = 15, height = 1, command = ACQSDK_UploadFile).grid(  row = 17, column = 0)
Button(frame_Controls, text = "Download File", bd = 3, width = 15, height = 1, command = ACQSDK_DownloadFile).grid(row = 17, column = 1)

#	Logger
Label(frame_Controls,  text = "Operation History").grid(row = 18, column = 2)
#	Use Text
txtLogger = ScrolledText(frame_Controls, bd = 3, width = 46, height = 18)
txtLogger.grid(row = 19, column = 0, columnspan = 3)
#	Button: Clean
Button(frame_Controls, text = "Clean", bd = 3, width = 15, height = 1, command = CLEANHistory).grid(row = 20, column = 0)

#	Button: Exit
Button(frame_Controls, text = "Exit", bd = 3, width = 15, height = 1, command = EXITAPP).grid(row = 20, column = 2)

# Exit event
wControlPanel.protocol("WM_DELETE_WINDOW", WinCallback)
wLiveVideo.protocol("WM_DELETE_WINDOW", WinCallback)

# Wait for message
mainloop()