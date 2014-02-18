"""
	GUI: Quick Checking on SDK's API

	History:
		2014-2-18	0.1		First version
							Notes: Some APIs are not ready.
"""

try:
	import os, sys, datetime, time
	import win32com.client, win32gui, time
	from Tkinter import *
	from ScrolledText import ScrolledText
	from tkFileDialog import *
	import tkMessageBox
except:
	print "Error occurs when importing required modules."
	sys.exit(1)

# Windows' events
def ResetWindow(width, height):
	if width == "480":
		wPreference.geometry("640x236+374+685")
	elif width == "640":
		wPreference.geometry("640x236+374+523")
	wLiveVideo.geometry("%sx%s+369+0" % (width, height))
def EXITAPP():
	objACQSDK_CSDevice.ACQSDK_UnInit()
	wControlPanel.quit()
def WinCallback():
	EXITAPP()

# SDK's API
def ACQSDK_Init(): # OK
	ACQSDK_SetLogPath()
	hWnd = win32gui.FindWindow("TkTopLevel","SDK Testing: Live Video")
	ret = objACQSDK_CSDevice.ACQSDK_Init(hWnd)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_UnInit(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_UnInit()
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_OnUpdateLiveWnd(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_OnUpdateLiveWnd()
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_QueryDeviceInfo(): # OK
	pDeviceInfo = objACQSDK_ASDeviceInfor
	ret = objACQSDK_CSDevice.ACQSDK_QueryDeviceInfo(pDeviceInfo)
	CheckResult(sys._getframe().f_code.co_name, ret)
	if ret == 0:
		try:
			device_type = Device_Type[str(hex(pDeviceInfo.get_device_type())).upper()]
		except:
			device_type = "Not Defined"
		finally:
			Logger("\tDevice Type is %r" % device_type)
		try:
			model_type = Model_Type[str(hex(pDeviceInfo.get_mode_type())).upper()]
		except:
			model_type = "Not Defined"
		finally:
			Logger("\tMode Type is %r" % model_type)
		Logger("\tSerial Number is %r" % pDeviceInfo.get_sn())
		Logger("\tFirmware Version is %r" % pDeviceInfo.get_fw_version())
def ACQSDK_SetHPWorkMode(): # Not implemented
	lWorkMode = int(SetHPWorkMode.get())
	Logger("<%r>" % lWorkMode)
	ret = objACQSDK_CSDevice.ACQSDK_SetHPWorkMode(lWorkMode)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_StartPlay(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_StartPlay()
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_PausePlay(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_PausePlay()
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_StopPlay(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_StopPlay()
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_StartRecord(): # OK
	path = r"./%s.avi" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
	ret = objACQSDK_CSDevice.ACQSDK_StartRecord(path)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_StopRecord(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_StopRecord()
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_Capture(): # OK
	pImageUnit = objACQSDK_ASImageUnit
	ret = objACQSDK_CSDevice.ACQSDK_Capture(pImageUnit)
	CheckResult(sys._getframe().f_code.co_name, ret)
	if ret == 0:
		img = pImageUnit.get_white_image()
		Logger("\tGet white image -> %r" % img)
		Logger("\tSave image -> %r" % pImageUnit.save_image(r"./%s" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S'), img))
		Logger("\tFree image -> %r" % pImageUnit.free_image(img))
		Logger("\tFree unit -> %r" % pImageUnit.free_unit())
def ACQSDK_GetImageData(): # Need callback to trigger
	pImageUnit = objACQSDK_ASImageUnit
	ret = objACQSDK_CSDevice.ACQSDK_GetImageData(pImageUnit)
	CheckResult(sys._getframe().f_code.co_name, ret)
	if ret == 0:
		img = pImageUnit.get_white_image()
		Logger("\tGet white image -> %r" % img)
		Logger("\tSave image -> %r" % pImageUnit.save_image(r"./%s" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S'), img))
		Logger("\tFree image -> %r" % pImageUnit.free_image(img))
		Logger("\tFree unit -> %r" % pImageUnit.free_unit())
def ACQSDK_SetLogPath(): # OK
	path = SetLogPath.get()
	Logger("<%r>" % path)
	ret  = objACQSDK_CSDevice.ACQSDK_SetLogPath(path)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_GetSerialNumber(): # Not Implemented
	length = 8
	ret    = objACQSDK_CSDevice.ACQSDK_GetSerialNumber(length)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_SetSerialNumber(): # Not Implemented
	pSn = SetSerialNumber.get()
	Logger("<%r>" % pSn)
	length = 8
	ret = objACQSDK_CSDevice.ACQSDK_SetSerialNumber(pSn, len)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_GetFirmwareVersion(): # Not Implemented
	length = 10
	ret = objACQSDK_CSDevice.ACQSDK_GetFirmwareVersion(length)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_UpgradeFirmware(): # OK
	pFullPathName = askopenfilename()
	ret = objACQSDK_CSDevice.ACQSDK_UpgradeFirmware(pFullPathName)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_AbortUpgrade(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_AbortUpgrade()
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_UploadFile(): # OK
	pFileName = askopenfilename()
	ret = objACQSDK_CSDevice.ACQSDK_UploadFile(pFileName)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_DownloadFile(): # Not Implemented
	# FW_DOWNLOAD_FILE_ID = {
	# "E_FW_FILE_ID_VERSION"          : 0, # /etc/fs.ver
	# "E_FW_FILE_ID_CALIBRATION_FILE" : 1, # /etc/fs.ver
	# "E_FW_FILE_ID_FW_LOG"           : 2, # /opt/deng.jpg
	# "E_FW_FILE_ID_COUNT"            : 3, # DON'T use this
	# }
	fileID = 0
	pFileName = "."
	ret = objACQSDK_CSDevice.ACQSDK_DownloadFile(fileID, pFileName)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_EnableAutoPowerOn(): # OK
	bEnable = int(EnableAutoPowerOn.get())
	Logger("<%r>" % bEnable)
	ret = objACQSDK_CSDevice.ACQSDK_EnableAutoPowerOn(bEnable)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_GetBrightness(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_GetBrightness()
	CheckResult(sys._getframe().f_code.co_name, ret[0])
	Logger("\t%s" % str(ret))
	if ret[0] == 0:
		Logger("\tCurrent brightness: %r" % ret[1])
		Logger("\tMaximum brightness: %r" % ret[2])
		Logger("\tMinimum brightness: %r" % ret[3])
		Logger("\tDefault brightness: %r" % ret[4])
def ACQSDK_SetBrightness(): # OK
	brightness = int(SetBrightness.get())
	Logger("<%r>" % brightness)
	ret = objACQSDK_CSDevice.ACQSDK_SetBrightness(brightness)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_GetContrast(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_GetContrast()
	CheckResult(sys._getframe().f_code.co_name, ret[0])
	Logger("\t%s" % str(ret))
	if ret[0] == 0:
		Logger("\tCurrent contrast: %r" % ret[1])
		Logger("\tMaximum contrast: %r" % ret[2])
		Logger("\tMinimum contrast: %r" % ret[3])
		Logger("\tDefault contrast: %r" % ret[4])
def ACQSDK_SetContrast(): # OK
	contrast = int(SetContrast.get())
	Logger("<%r>" % contrast)
	ret = objACQSDK_CSDevice.ACQSDK_SetContrast(contrast)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_SetPowerlineFrequency(): # OK
	frequency = int(SetPowerlineFrequency.get())
	Logger("<%r>" % frequency)
	ret = objACQSDK_CSDevice.ACQSDK_SetPowerlineFrequency(frequency)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_GetPowerlineFrequency(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_GetPowerlineFrequency()
	CheckResult(sys._getframe().f_code.co_name, ret[0])
	Logger("\t%s" % str(ret))
	if ret[0] == 0:
		Logger("\tCurrent frequency: %r" % ret[1])
		Logger("\tDefault frequency: %r" % ret[2])
def ACQSDK_EnableAutoPowerOff(): # OK
	bEnable = int(EnableAutoPowerOff.get())
	ret = objACQSDK_CSDevice.ACQSDK_EnableAutoPowerOff(bEnable)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_SetAutoPowerOffTime(): # OK
	secondsCount = int(SetAutoPowerOffTime.get())
	Logger("<%r>" % secondsCount)
	ret = objACQSDK_CSDevice.ACQSDK_SetAutoPowerOffTime(secondsCount)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_EnableStandBy(): # OK
	bEnable = int(EnableStandBy.get())
	Logger("<%r>" % bEnable)
	ret = objACQSDK_CSDevice.ACQSDK_EnableStandBy(bEnable)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_SetStandByTime(): # OK
	secondsCount = int(SetStandByTime.get())
	Logger("<%r>" % secondsCount)
	ret = objACQSDK_CSDevice.ACQSDK_SetStandByTime(secondsCount)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_SetSystemTime(): # OK
	secondsCount = int(SetSystemTime.get())
	Logger("<%r>" % secondsCount)
	ret = objACQSDK_CSDevice.ACQSDK_SetSystemTime(secondsCount)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_SetMirrorFlag(): # OK
	bEnable = int(SetMirrorFlag.get())
	Logger("<%r>" % bEnable)
	ret = objACQSDK_CSDevice.ACQSDK_SetMirrorFlag(bEnable)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_GetMirrorFlag(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_GetMirrorFlag()
	CheckResult(sys._getframe().f_code.co_name, ret[0])
	Logger("\t%s" % str(ret))
	if ret[0] == 0:
		Logger("\tCurrent status: %r" % ret[1])
def ACQSDK_SetRotationFlag(): # Need to check on 0.1.0.3
	rotation = int(SetRotationFlag.get())
	Logger("<%r>" % rotation)
	ret = objACQSDK_CSDevice.ACQSDK_SetRotationFlag(rotation)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_GetRotationFlag(): # OK
	ret = objACQSDK_CSDevice.ACQSDK_GetRotationFlag()
	CheckResult(sys._getframe().f_code.co_name, ret[0])
	Logger("\t%s" % str(ret))
	if ret[0] == 0:
		Logger("\tCurrent status: %r" % ret[1])

# Functions for Logger box
def CheckResult(api, ret):
	if ret != 0 and ret != 1:
		ret = str(hex(ret)).upper()
		Logger("%s -> %r" % (api, ret))
		try:
			retValue = OPERATOR_ERROR[ret]
		except:
			retValue = "NOT DEFINED"
		finally:
			Logger("\t%s -> %s" % (ret, retValue))
	else:
		Logger("%s -> %r" % (api, ret))
def Logger(strLine):
	strLine = "%s\n" % str(strLine)
	txtLogger.insert(INSERT, strLine)
	txtLogger.yview(END)
def CLEANHistory(): txtLogger.delete('1.0', END)

# Class needed by Callback
class SDKEvents():
	def OnHPEvents(self, callback):
		print callback.event_id
		#objACQSDK_SDKCallbackInfo.event_id

# definition: dictionary, "acq_sdk/SDK Document/SDKDef.h"
Device_Type = {
	"0X20001" : "DEV_1500",
	"0X20002" : "DEV_1600",
	"0X20003" : "DEV_1200",
	"0X20004" : "DEV_1650",
	"0X20005" : "DEV_UVC",
	"0X20006" : "DEV_UNDEFINED",
}

Model_Type = {
	"0X30001" : "MODEL_WIRED_DOCK",
	"0X30002" : "MODEL_WIRELESS_ONE",
	"0X30003" : "MODEL_WIRELESS_MANY",
	"0X30004" : "MODEL_DIRECT_WIRED_ONE",
	"0X30005" : "MODEL_UNDEFINED",
}

OPERATOR_ERROR = {
	"0XF0001" : "DEVICE_CONNECTION_FALSE",
	"0XF0002" : "DEVICE_CREATED_FAIL",
	"0XF0003" : "HOST_SERVICE_IP_INVALID",
	"0XF0004" : "HOST_SERVICE_CONNECT_FAILED" ,
	"0XF0005" : "UVC_INIT_INPUT_PARAM_ERR" ,
	"0XF0006" : "UVC_INIT_NO_DEVICE" ,
	"0XF0007" : "UVC_INIT_DEVICE_CMT_ERR",
	"0XF0008" : "UVC_INIT_QUERY_CALLBACK_INTERFACE_FAIL",
	"0XF0009" : "UVC_INIT_CREATE_CALLBACK_INSTANCE_FAIL",
	"0XF000A" : "UVC_INIT_BIND_FILTER_FAIL",
	"0XF000B" : "UVC_INIT_HID_DEVICE_INIT_FAIL",
	"0XF000C" : "UVC_GET_DEVICE_INFOR_BUFF_ERROR",
	"0XF000D" : "LOG_PATH_SET_ERR" ,
	"0XF000E" : "ACQSDK_SENDER_FAIL" ,
	"0XF000F" : "ACQSDK_SENDER_TIMEOUT",
	"0XF0010" : "CAPTURE_INPUT_PARAM_VALUE_ERR",
	"0XF0011" : "CAPTURE_INPUT_PARAM_TYPE_ERR",
	"0XF0012" : "CAPTURE_SAFE_CREATE_NULL",
	"0XF0013" : "CAPTURE_SAFE_ACCESS_ERR",
	"0XF0014" : "CAPTURE_INPUT_DATA_BUFFER_NO_ENOUGH",
	"0XF0015" : "CAPTURE_MEMORY_NOT_ENOUGH_TO_NEW",
	"0XF0016" : "CAPTURE_TIME_OUT_WITH_NO_DATA",
	"0XF0017" : "CAPTURE_SEND_EXTERNAL_FAILED",
	"0XF0018" : "CAPUTRE_FREE_TYPE_ERR",
	"0XF0019" : "RECORD_INPUT_FILE_PATH_ERR",
	"0XF001A" : "RECORD_STARTING_WHILE_DEVICE_REMOVE",
	"0XF001B" : "ACQSDK_ERROR_UPDATE_FAILED",
	"0XF001C" : "ACQSDK_ERROR_UPLOADED_FAILED",
	"0XF001D" : "ACQSDK_ERROR_DOWNLOADED_FAILED",
}

Callback_MsgType = {
	"0X200001" : "DEVICE_USB_PLUG_OUT",
	"0X200002" : "DEVICE_USB_PLUG_IN",
	"0X200003" : "FW_UPGRADE_PERCENT_STATE",
	"0X200004" : "HP_BUTTON_CAPTURE_DOWN",
	"0X200005" : "HP_BUTTON_CAPTURE_UP",
	"0X200006" : "HP_BUTTON_RECORD_DOWN",
	"0X200007" : "HP_BUTTON_RECORD_UP",
	"0X200008" : "HP_BUTTON_UP_DOWN",
	"0X200009" : "HP_BUTTON_UP_UP",
	"0X20000A" : "HP_BUTTON_DOWN_DOWN",
	"0X20000B" : "HP_BUTTON_DOWN_UP",
	"0X20000C" : "HP_POWER_BUTTON_DOWN",
	"0X20000D" : "HP_POWER_BUTTON_UP",
	"0X20000E" : "HP_BUTTON_MODE_SWICH_DOWN",
	"0X20000F" : "HP_BUTTON_MODE_SWICH_UP",
	"0X200010" : "HP_POWER_OFF",
	"0X200011" : "HP_POWER_ON",
	"0X200012" : "HP_TRASMIT_TO_PREVIEW",
	"0X200013" : "HP_TRASMIT_IN_SLEEP",
	"0X200014" : "HP_PLUG_IN_HOLDER",
	"0X200015" : "HP_PLUG_OUT_HOLDER",
	"0X200016" : "HP_FW_UPGRADING",
	"0X200017" : "HP_FW_NORMAL",
	"0X200018" : "EXPORT_IMAGE_DATA_FROM_HP",
	"0X200019" : "MSG_TYPE_UNDEFINED",
}

# ProgID list
ACQSDK_CSDevice_ProgID        = "ACQSDK.CSDevice.1"
ACQSDK_ASImageUnit_ProgID     = "ACQSDK.ASImageUnit.1"
ACQSDK_SDKCallbackInfo_ProgID = "ACQSDK.SDKCallbackInfo.1"
ACQSDK_ASDeviceInfor_ProgID   = "ACQSDK.ASDeviceInfor.1"

# Create COM objects and Event
objACQSDK_CSDevice            = win32com.client.DispatchWithEvents(ACQSDK_CSDevice_ProgID, SDKEvents)
objACQSDK_ASImageUnit         = win32com.client.          Dispatch(ACQSDK_ASImageUnit_ProgID)
objACQSDK_SDKCallbackInfo     = win32com.client.          Dispatch(ACQSDK_SDKCallbackInfo_ProgID)
objACQSDK_ASDeviceInfor       = win32com.client.          Dispatch(ACQSDK_ASDeviceInfor_ProgID)

# Create Tkinter windows
wControlPanel = Tk()	# List buttons
wLiveVideo    = Tk()	# Display Live Window
wPreference   = Tk()	# Preference Setting dialog

# Properties of created windows
#	Panel
wControlPanel.geometry("352x754+5+5")
wControlPanel.title("SDK Testing: Control Panel")
wControlPanel.resizable(width = False, height = False)
#	Live Video
wLiveVideo.geometry("640x480+369+0")
wLiveVideo.title("SDK Testing: Live Video")
wLiveVideo.resizable(width = True, height = True)	# Allow to change the window size
#	Preference Setting
wPreference.geometry("640x236+374+523")
wPreference.title("Preference Setting")
wPreference.resizable(width = False, height = False)

# [Panel]

#	Button Set 1, basic APIs
Label(wControlPanel,  text = "Basic")                                                                               .grid(row = 0,  column = 0)
Button(wControlPanel, text = "Init",               bd = 3, width = 15, height = 1, command = ACQSDK_Init).           grid(row = 1,  column = 0)
Button(wControlPanel, text = "UnInit",             bd = 3, width = 15, height = 1, command = ACQSDK_UnInit)         .grid(row = 2,  column = 0)
Button(wControlPanel, text = "Refresh Live Video", bd = 3, width = 15, height = 1, command = ACQSDK_OnUpdateLiveWnd).grid(row = 3,  column = 0)
Button(wControlPanel, text = "Start Play",         bd = 3, width = 15, height = 1, command = ACQSDK_StartPlay)      .grid(row = 1,  column = 1)
Button(wControlPanel, text = "Pause Play",         bd = 3, width = 15, height = 1, command = ACQSDK_PausePlay)      .grid(row = 2,  column = 1)
Button(wControlPanel, text = "Stop Play",          bd = 3, width = 15, height = 1, command = ACQSDK_StopPlay)       .grid(row = 3,  column = 1)
Button(wControlPanel, text = "Capture Image",      bd = 3, width = 15, height = 1, command = ACQSDK_Capture)        .grid(row = 1,  column = 2)
Button(wControlPanel, text = "Start Record",       bd = 3, width = 15, height = 1, command = ACQSDK_StartRecord)    .grid(row = 2,  column = 2)
Button(wControlPanel, text = "Stop Record",        bd = 3, width = 15, height = 1, command = ACQSDK_StopRecord)     .grid(row = 3,  column = 2)

#	The other APIs
Label(wControlPanel,  text = "Extention")                                                                             .grid(row = 4, column = 0)

#	Buttons Set 2
Label(wControlPanel,  text = "Query & Upgrade")                                                                       .grid(row = 5, column = 1)
Button(wControlPanel, text = "Query Device Info", bd = 3, width = 15, height = 1, command = ACQSDK_QueryDeviceInfo)   .grid(row = 6, column = 0)
Button(wControlPanel, text = "Get FW Version",    bd = 3, width = 15, height = 1, command = ACQSDK_GetFirmwareVersion).grid(row = 7, column = 0)
Button(wControlPanel, text = "Get Serial Number", bd = 3, width = 15, height = 1, command = ACQSDK_GetSerialNumber)   .grid(row = 6, column = 1)
Button(wControlPanel, text = "Set Serial Number", bd = 3, width = 15, height = 1, command = ACQSDK_SetSerialNumber)   .grid(row = 7, column = 1)
Button(wControlPanel, text = "Upgrade FW",        bd = 3, width = 15, height = 1, command = ACQSDK_UpgradeFirmware)   .grid(row = 6, column = 2)
Button(wControlPanel, text = "Abort Upgrade",     bd = 3, width = 15, height = 1, command = ACQSDK_AbortUpgrade)      .grid(row = 7, column = 2)

#	Button Set 3
Label(wControlPanel,  text = "HP Configuration")                                                                          .grid(row = 8,  column = 1)
Button(wControlPanel, text = "Get Brightness",     bd = 3, width = 15, height = 1, command = ACQSDK_GetBrightness)        .grid(row = 9,  column = 0)
Button(wControlPanel, text = "Set Brightness",     bd = 3, width = 15, height = 1, command = ACQSDK_SetBrightness)        .grid(row = 10, column = 0)
Button(wControlPanel, text = "Get Contrast",       bd = 3, width = 15, height = 1, command = ACQSDK_GetContrast)          .grid(row = 11, column = 0)
Button(wControlPanel, text = "Set Contrast",       bd = 3, width = 15, height = 1, command = ACQSDK_SetContrast)          .grid(row = 12, column = 0)
Button(wControlPanel, text = "Get Frequency",      bd = 3, width = 15, height = 1, command = ACQSDK_GetPowerlineFrequency).grid(row = 9,  column = 1)
Button(wControlPanel, text = "Set Frequency",      bd = 3, width = 15, height = 1, command = ACQSDK_SetPowerlineFrequency).grid(row = 10, column = 1)
Button(wControlPanel, text = "Auto Power On",      bd = 3, width = 15, height = 1, command = ACQSDK_EnableAutoPowerOn)    .grid(row = 11, column = 1)
Button(wControlPanel, text = "Auto Power Off",     bd = 3, width = 15, height = 1, command = ACQSDK_EnableAutoPowerOff)   .grid(row = 12, column = 1)
Button(wControlPanel, text = "Enable StandBy",     bd = 3, width = 15, height = 1, command = ACQSDK_EnableStandBy)        .grid(row = 9,  column = 2)
Button(wControlPanel, text = "Set StandBy Time",   bd = 3, width = 15, height = 1, command = ACQSDK_SetStandByTime)       .grid(row = 10, column = 2)
Button(wControlPanel, text = "Set System Time",    bd = 3, width = 15, height = 1, command = ACQSDK_SetSystemTime)        .grid(row = 11, column = 2)
Button(wControlPanel, text = "Set Power Off Time", bd = 3, width = 15, height = 1, command = ACQSDK_SetAutoPowerOffTime)  .grid(row = 12, column = 2)

#	Button Set 4
Label(wControlPanel,  text = "Mirror & Rotation")                                                                             .grid(row = 13, column = 1)
Button(wControlPanel, text = "Get Mirror Flag",   bd = 3, width = 15, height = 1, command = ACQSDK_GetMirrorFlag)             .grid(row = 14, column = 0)
Button(wControlPanel, text = "Set Mirror Flag",   bd = 3, width = 15, height = 1, command = ACQSDK_SetMirrorFlag)             .grid(row = 15, column = 0)
Button(wControlPanel, text = "Get Rotation Flag", bd = 3, width = 15, height = 1, command = ACQSDK_GetRotationFlag)           .grid(row = 14, column = 1)
Button(wControlPanel, text = "Set Rotation Flag", bd = 3, width = 15, height = 1, command = ACQSDK_SetRotationFlag)           .grid(row = 15, column = 1)
#		The following two buttons are added for Rotation APIs
Button(wControlPanel, text = "Set to 640*480",    bd = 3, width = 15, height = 1, command = lambda: ResetWindow("640", "480")).grid(row = 14, column = 2)
Button(wControlPanel, text = "Set to 480*640",    bd = 3, width = 15, height = 1, command = lambda: ResetWindow("480", "640")).grid(row = 15, column = 2)

#	Button Set 5
Label(wControlPanel,  text = "File Operation")                                                              .grid(row = 16, column = 1)
Button(wControlPanel, text = "Upload File",   bd = 3, width = 15, height = 1, command = ACQSDK_UploadFile)  .grid(row = 17, column = 0)
Button(wControlPanel, text = "Download File", bd = 3, width = 15, height = 1, command = ACQSDK_DownloadFile).grid(row = 17, column = 1)

#	Logger
Label(wControlPanel,  text = "Operation History").grid(row = 18, column = 2)
txtLogger = ScrolledText(wControlPanel, bd = 3, width = 46, height = 18)
txtLogger.grid(row = 19, column = 0, columnspan = 3)
#	Button: Clean
Button(wControlPanel, text = "Clean", bd = 3, width = 15, height = 1, command = CLEANHistory).grid(row = 20, column = 0)

#	Button: Exit this script
Button(wControlPanel, text = "Exit", bd = 3, width = 15, height = 1, command = EXITAPP).grid(row = 20, column = 2)

# [Preference Setting]
#	Prefix of each API
Label(wPreference, bd = 3, text = "ACQSDK_").grid(row = 0, sticky = W+S+N)

#	Left Part: Label
Label(wPreference, bd = 3, text = "Set System Time")        .grid(row = 1, column = 0, sticky = E+S+N, ipadx = 11, ipady = 2)
Label(wPreference, bd = 3, text = "Set Log Path")           .grid(row = 2, column = 0, sticky = E+S+N, ipadx = 11, ipady = 2)
Label(wPreference, bd = 3, text = "HP Work Mode")           .grid(row = 3, column = 0, sticky = E+S+N, ipadx = 11, ipady = 2)
Label(wPreference, bd = 3, text = "Set Serial Number")      .grid(row = 4, column = 0, sticky = E+S+N, ipadx = 11, ipady = 2)
Label(wPreference, bd = 3, text = "Set Brightness")         .grid(row = 5, column = 0, sticky = E+S+N, ipadx = 11, ipady = 2)
Label(wPreference, bd = 3, text = "Set Contrast")           .grid(row = 6, column = 0, sticky = E+S+N, ipadx = 11, ipady = 2)
Label(wPreference, bd = 3, text = "Set Powerline Frequency").grid(row = 7, column = 0, sticky = E+S+N, ipadx = 11, ipady = 2)

#	Input: text box
SetSystemTime         = Entry(wPreference, bd = 3, width = 25)
SetLogPath            = Entry(wPreference, bd = 3, width = 25)
HPWorkMode            = Entry(wPreference, bd = 3, width = 25)
SetSerialNumber       = Entry(wPreference, bd = 3, width = 25)
SetBrightness         = Entry(wPreference, bd = 3, width = 25)
SetContrast           = Entry(wPreference, bd = 3, width = 25)
SetPowerlineFrequency = Entry(wPreference, bd = 3, width = 25)

#	Input: Grid Properties
SetSystemTime.        grid(row = 1, column = 1)
SetLogPath           .grid(row = 2, column = 1)
HPWorkMode           .grid(row = 3, column = 1)
SetSerialNumber      .grid(row = 4, column = 1)
SetBrightness        .grid(row = 5, column = 1)
SetContrast          .grid(row = 6, column = 1)
SetPowerlineFrequency.grid(row = 7, column = 1)

#	Input: Default value
SetSystemTime.        insert(0, "0")
SetLogPath.           insert(0, ".")
HPWorkMode.           insert(0, "1")
SetSerialNumber.      insert(0, "ABCD1234")
SetBrightness.        insert(0, "4")
SetContrast.          insert(0, "4")
SetPowerlineFrequency.insert(0, "50")

#	Right Part: Label
Label(wPreference, bd = 3, text = "Auto PowerOn")      .grid(row = 1, column = 2, sticky = E+S+N, ipadx = 11, ipady = 2)
Label(wPreference, bd = 3, text = "Auto Power Off")    .grid(row = 2, column = 2, sticky = E+S+N, ipadx = 11, ipady = 2)
Label(wPreference, bd = 3, text = "Set Power Off Time").grid(row = 3, column = 2, sticky = E+S+N, ipadx = 11, ipady = 2)
Label(wPreference, bd = 3, text = "Enable StandBy")    .grid(row = 4, column = 2, sticky = E+S+N, ipadx = 11, ipady = 2)
Label(wPreference, bd = 3, text = "Set StandBy Time")  .grid(row = 5, column = 2, sticky = E+S+N, ipadx = 11, ipady = 2)
Label(wPreference, bd = 3, text = "Set Mirror Flag")   .grid(row = 6, column = 2, sticky = E+S+N, ipadx = 11, ipady = 2)
Label(wPreference, bd = 3, text = "Set Rotation Flag") .grid(row = 7, column = 2, sticky = E+S+N, ipadx = 11, ipady = 2)

#	Input
EnableAutoPowerOn   = Entry(wPreference, bd = 3, width = 25)
EnableAutoPowerOff  = Entry(wPreference, bd = 3, width = 25)
SetAutoPowerOffTime = Entry(wPreference, bd = 3, width = 25)
EnableStandBy       = Entry(wPreference, bd = 3, width = 25)
SetStandByTime      = Entry(wPreference, bd = 3, width = 25)
SetMirrorFlag       = Entry(wPreference, bd = 3, width = 25)
SetRotationFlag     = Entry(wPreference, bd = 3, width = 25)

#	Input: Grid Properties
EnableAutoPowerOn  .grid(row = 1, column = 3)
EnableAutoPowerOff .grid(row = 2, column = 3)
SetAutoPowerOffTime.grid(row = 3, column = 3)
EnableStandBy      .grid(row = 4, column = 3)
SetStandByTime     .grid(row = 5, column = 3)
SetMirrorFlag      .grid(row = 6, column = 3)
SetRotationFlag    .grid(row = 7, column = 3)

#	Input: Default value
EnableAutoPowerOn  .insert(0, "1")
EnableAutoPowerOff .insert(0, "1")
SetAutoPowerOffTime.insert(0, "3600")
EnableStandBy      .insert(0, "1")
SetStandByTime     .insert(0, "60")
SetMirrorFlag      .insert(0, "1")
SetRotationFlag    .insert(0, "90")

#	Bottom
Label(wPreference, bd = 3, text = "Test Application of UVC Camera SDK, built by ActivePython 2.7 (x86)").grid(row = 8, columnspan = 4, sticky = E+S+N)

# Trace window's event: DELETE
wControlPanel.protocol("WM_DELETE_WINDOW", WinCallback)
wLiveVideo.protocol(   "WM_DELETE_WINDOW", WinCallback)
wPreference.protocol(  "WM_DELETE_WINDOW", WinCallback)

# Wait for message
mainloop()