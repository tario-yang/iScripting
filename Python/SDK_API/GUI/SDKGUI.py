"""
	GUI: Quick Checking on SDK's API

	History:
		2014-2-18	0.1		First version
							Notes: Some APIs are not ready.
"""

try:
	import os, sys, time, threading, thread
	import win32com.client, win32api
	import pythoncom
	from Tkinter import *
	from ScrolledText import ScrolledText
	from tkFileDialog import *
except:
	print "Error occurs when importing required modules."
	sys.exit(1)

# Generate GUI
def GenerateGUI():
	# Create Tkinter windows
	# GUI : Workflow
	global wControlPanel, wLiveVideo, wPreference
	wControlPanel = Tk()	# List buttons
	wLiveVideo    = Tk()	# Display Live Window
	wPreference   = Tk()	# Preference Setting dialog

	# Handler of the wLiveVideo
	global hWnd
	hWnd = wLiveVideo.winfo_id()

	# GUI Configuration
	GenerateControlPanel()
	GenerateLiveVideo()
	GeneratePreference()

	# Bind customized event
	wControlPanel.bind("<F11>", lambda x: KillProcess())
	wControlPanel.bind("<F12>", lambda x: OpenDirectory())

	# Trace window's event: DELETE
	wControlPanel.protocol("WM_DELETE_WINDOW", EXITAPP)
	wLiveVideo   .protocol("WM_DELETE_WINDOW", lambda: 0) # No response when trying to close Live Video's window
	wPreference  .protocol("WM_DELETE_WINDOW", PreferenceSettingDialogVisable) # Map the close event to PreferenceSettingDialogVisable
def GenerateControlPanel():
	#	Panel
	wControlPanel.geometry("+0+0")
	wControlPanel.title("SDK Testing: Control Panel")
	wControlPanel.resizable(width = False, height = False)

	#	Button Set 1, basic APIs
	Label(wControlPanel,  text = "Basic")                                                                            .grid(row = 0,  column = 0, columnspan = 2)
	Button(wControlPanel, text = "Init",               bd = 3, width = 20, height = 1, command = ACQSDK_Init).        grid(row = 1,  column = 0)
	Button(wControlPanel, text = "UnInit",             bd = 3, width = 20, height = 1, command = ACQSDK_UnInit)      .grid(row = 2,  column = 0)
	Button(wControlPanel, text = "Start Play",         bd = 3, width = 20, height = 1, command = ACQSDK_StartPlay)   .grid(row = 1,  column = 1)
	Button(wControlPanel, text = "Stop Play",          bd = 3, width = 20, height = 1, command = ACQSDK_StopPlay)    .grid(row = 2,  column = 1)
	Button(wControlPanel, text = "Start Record",       bd = 3, width = 20, height = 1, command = ACQSDK_StartRecord) .grid(row = 1,  column = 2)
	Button(wControlPanel, text = "Stop Record",        bd = 3, width = 20, height = 1, command = ACQSDK_StopRecord)  .grid(row = 2,  column = 2)
	Button(wControlPanel, text = "Capture",            bd = 3, width = 20, height = 1, command = ACQSDK_Capture)     .grid(row = 3,  column = 1)
	Button(wControlPanel, text = "Get Image Data",     bd = 3, width = 20, height = 1, command = ACQSDK_GetImageData).grid(row = 3,  column = 2)

	#	The other APIs
	# Label(wControlPanel,  text = "Extention").grid(row = 4, column = 0)

	#	Buttons Set 2
	Label(wControlPanel,  text = "Query & Upgrade")                                                                       .grid(row = 5, column = 0, columnspan = 2)
	Button(wControlPanel, text = "Query Device Info", bd = 3, width = 20, height = 1, command = ACQSDK_QueryDeviceInfo)   .grid(row = 6, column = 0)
	Button(wControlPanel, text = "Upgrade FW",        bd = 3, width = 20, height = 1, command = ACQSDK_UpgradeFirmware)   .grid(row = 6, column = 1)
	Button(wControlPanel, text = "Abort Upgrade",     bd = 3, width = 20, height = 1, command = ACQSDK_AbortUpgrade)      .grid(row = 6, column = 2)

	#	Button Set 3
	Label(wControlPanel,  text = "HP Configuration")                                                                          .grid(row = 7,  column = 0, columnspan = 2)
	Button(wControlPanel, text = "Get Brightness",     bd = 3, width = 20, height = 1, command = ACQSDK_GetBrightness)        .grid(row = 8,  column = 0)
	Button(wControlPanel, text = "Set Brightness",     bd = 3, width = 20, height = 1, command = ACQSDK_SetBrightness)        .grid(row = 9,  column = 0)
	Button(wControlPanel, text = "Get Contrast",       bd = 3, width = 20, height = 1, command = ACQSDK_GetContrast)          .grid(row = 10, column = 0)
	Button(wControlPanel, text = "Set Contrast",       bd = 3, width = 20, height = 1, command = ACQSDK_SetContrast)          .grid(row = 11, column = 0)
	Button(wControlPanel, text = "Get Frequency",      bd = 3, width = 20, height = 1, command = ACQSDK_GetPowerlineFrequency).grid(row = 8,  column = 1)
	Button(wControlPanel, text = "Set Frequency",      bd = 3, width = 20, height = 1, command = ACQSDK_SetPowerlineFrequency).grid(row = 9,  column = 1)
	Button(wControlPanel, text = "Auto Power On",      bd = 3, width = 20, height = 1, command = ACQSDK_EnableAutoPowerOn)    .grid(row = 10, column = 1)
	Button(wControlPanel, text = "Auto Power Off",     bd = 3, width = 20, height = 1, command = ACQSDK_EnableAutoPowerOff)   .grid(row = 11, column = 1)
	Button(wControlPanel, text = "Enable StandBy",     bd = 3, width = 20, height = 1, command = ACQSDK_EnableStandBy)        .grid(row = 8,  column = 2)
	Button(wControlPanel, text = "Set StandBy Time",   bd = 3, width = 20, height = 1, command = ACQSDK_SetStandByTime)       .grid(row = 9,  column = 2)
	Button(wControlPanel, text = "Set System Time",    bd = 3, width = 20, height = 1, command = ACQSDK_SetSystemTime)        .grid(row = 10, column = 2)
	Button(wControlPanel, text = "Set Power Off Time", bd = 3, width = 20, height = 1, command = ACQSDK_SetAutoPowerOffTime)  .grid(row = 11, column = 2)

	#	Button Set 4
	Label(wControlPanel,  text = "Mirror & Rotation")                                                                                  .grid(row = 12, column = 0, columnspan = 2)
	Button(wControlPanel, text = "Set Mirror Flag",    bd = 3, width = 20, height = 1, command = ACQSDK_SetMirrorFlag)                 .grid(row = 13, column = 0)
	Button(wControlPanel, text = "Set Rotation Flag",  bd = 3, width = 20, height = 1, command = ACQSDK_SetRotationFlag)               .grid(row = 14, column = 0)
	#		The following two buttons are added for Rotation APIs
	Button(wControlPanel, text = "Set to 640*480",     bd = 3, width = 20, height = 1, command = lambda: ResetLiveVideoWindowSize("640", "480")).grid(row = 13, column = 1)
	Button(wControlPanel, text = "Set to 480*640",     bd = 3, width = 20, height = 1, command = lambda: ResetLiveVideoWindowSize("480", "640")).grid(row = 14, column = 1)
	Button(wControlPanel, text = "Update LiveVideo",   bd = 3, width = 20, height = 1, command = ACQSDK_OnUpdateLiveWnd)               .grid(row = 13, column = 2)

	#	Button Set 5
	Label(wControlPanel,  text = "Factory")                                                                               .grid(row = 15, column = 0, columnspan = 2)
	Button(wControlPanel, text = "Get FW Version",    bd = 3, width = 20, height = 1, command = ACQSDK_GetFirmwareVersion).grid(row = 16, column = 0)
	Button(wControlPanel, text = "Get Serial Number", bd = 3, width = 20, height = 1, command = ACQSDK_GetSerialNumber)   .grid(row = 16, column = 1)
	Button(wControlPanel, text = "Set Serial Number", bd = 3, width = 20, height = 1, command = ACQSDK_SetSerialNumber)   .grid(row = 17, column = 1)
	Button(wControlPanel, text = "Set HP Work Mode",  bd = 3, width = 20, height = 1, command = ACQSDK_SetHPWorkMode)     .grid(row = 17, column = 0)
	Button(wControlPanel, text = "Upload File",       bd = 3, width = 20, height = 1, command = ACQSDK_UploadFile)        .grid(row = 16, column = 2)
	Button(wControlPanel, text = "Download File",     bd = 3, width = 20, height = 1, command = ACQSDK_DownloadFile)      .grid(row = 17, column = 2)

	#	Logger
	Label(wControlPanel,  text = "")                 .grid(row = 18, column = 1)
	Label(wControlPanel,  text = "Operation History").grid(row = 19, column = 1)
	Button(wControlPanel, text = "Increase Height (+1)", bd = 3, width = 20, height = 1, command = lambda: ChangeScrolledTextHeight("INCREASE")).grid(row = 20, column = 1)
	Button(wControlPanel, text = "Decrease Height (-1)", bd = 3, width = 20, height = 1, command = lambda: ChangeScrolledTextHeight("DECREASE")).grid(row = 20, column = 2)
	global pLogger
	pLogger = ScrolledText(wControlPanel, bd = 3, width = 52, height = 16, font = ("Courier", 9))
	wControlPanel_info = WindowState(wControlPanel)
	pLogger.grid(row = 21, column = 0, columnspan = 3)

	#	Button: Clean
	Button(wControlPanel, text = "Clean",  bd = 3, width = 20, height = 1, command = CLEANHistory).grid(row = 22, column = 0)

	#	Button: Exit this script
	Button(wControlPanel, text = "Exit",   bd = 3, width = 20, height = 1, command = EXITAPP)     .grid(row = 22, column = 1)

	#	Button: Control whether Preference Setting Dialog is Visable
	global pPSDV
	pPSDV = Button(wControlPanel, text = "Config >>", bd = 3, width = 20, height = 1, command = PreferenceSettingDialogVisable)
	pPSDV.grid(row = 22, column = 2)
def GenerateLiveVideo():
	#	Live Video
	global wLiveVideo_title
	wLiveVideo_title = "SDK Testing: Live Video"
	wLiveVideo.geometry("%sx%s" % (LiveVideo_Width, LiveVideo_Height))
	wLiveVideo.title("SDK Testing: Live Video")
	wLiveVideo.withdraw()
def GeneratePreference():
	#	Preference Setting
	wPreference.title("Preference Setting")
	wPreference.resizable(width = False, height = False)
	wPreference.withdraw()

	#	Prefix of each API
	pFileVersion = Label(wPreference, bd = 3, text = "ACQSDK.DLL -> %s" % DLL_FileVersion())
	pFileVersion.grid(row = 0, sticky = W+S+N, columnspan = 7)
	pFileVersion.bind("<Button-1>", lambda x: OpenDirectory(ACQSDK_DLL_Dir))

	#	Left Part: Label
	Label(wPreference, bd = 3, text = "Set System Time")  .grid(row = 1, column = 0, sticky = E+S+N, ipadx = 11, ipady = 2)
	Label(wPreference, bd = 3, text = "Set Log Path")     .grid(row = 2, column = 0, sticky = E+S+N, ipadx = 11, ipady = 2)
	Label(wPreference, bd = 3, text = "HP Work Mode")     .grid(row = 3, column = 0, sticky = E+S+N, ipadx = 11, ipady = 2)
	Label(wPreference, bd = 3, text = "Set Serial Number").grid(row = 4, column = 0, sticky = E+S+N, ipadx = 11, ipady = 2)
	Label(wPreference, bd = 3, text = "Set Brightness")   .grid(row = 5, column = 0, sticky = E+S+N, ipadx = 11, ipady = 2)
	Label(wPreference, bd = 3, text = "Set Contrast")     .grid(row = 6, column = 0, sticky = E+S+N, ipadx = 11, ipady = 2)
	Label(wPreference, bd = 3, text = "Set Frequency")    .grid(row = 7, column = 0, sticky = E+S+N, ipadx = 11, ipady = 2)

	#	Input: text box
	global SetSystemTime, SetLogPath, SetHPWorkMode, SetSerialNumber, SetBrightness, SetContrast, SetPowerlineFrequency
	SetSystemTime         = Entry(wPreference, bd = 3, width = 18)
	SetLogPath            = Entry(wPreference, bd = 3, width = 18)
	SetHPWorkMode         = Entry(wPreference, bd = 3, width = 18)
	SetSerialNumber       = Entry(wPreference, bd = 3, width = 18)
	SetBrightness         = Entry(wPreference, bd = 3, width = 18)
	SetContrast           = Entry(wPreference, bd = 3, width = 18)
	SetPowerlineFrequency = Entry(wPreference, bd = 3, width = 18)

	#	Input: Grid Properties
	SetSystemTime.        grid(row = 1, column = 1)
	SetLogPath           .grid(row = 2, column = 1)
	SetHPWorkMode        .grid(row = 3, column = 1)
	SetSerialNumber      .grid(row = 4, column = 1)
	SetBrightness        .grid(row = 5, column = 1)
	SetContrast          .grid(row = 6, column = 1)
	SetPowerlineFrequency.grid(row = 7, column = 1)

	#	Center Part: Label
	Label(wPreference, bd = 3, text = "Auto PowerOn")      .grid(row = 1, column = 2, sticky = E+S+N, ipadx = 11, ipady = 2)
	Label(wPreference, bd = 3, text = "Auto Power Off")    .grid(row = 2, column = 2, sticky = E+S+N, ipadx = 11, ipady = 2)
	Label(wPreference, bd = 3, text = "Set Power Off Time").grid(row = 3, column = 2, sticky = E+S+N, ipadx = 11, ipady = 2)
	Label(wPreference, bd = 3, text = "Enable StandBy")    .grid(row = 4, column = 2, sticky = E+S+N, ipadx = 11, ipady = 2)
	Label(wPreference, bd = 3, text = "Set StandBy Time")  .grid(row = 5, column = 2, sticky = E+S+N, ipadx = 11, ipady = 2)
	Label(wPreference, bd = 3, text = "Set Mirror Flag")   .grid(row = 6, column = 2, sticky = E+S+N, ipadx = 11, ipady = 2)
	Label(wPreference, bd = 3, text = "Set Rotation Flag") .grid(row = 7, column = 2, sticky = E+S+N, ipadx = 11, ipady = 2)

	#	Input
	global EnableAutoPowerOn, EnableAutoPowerOff, SetAutoPowerOffTime, EnableStandBy, SetStandByTime, SetMirrorFlag, SetRotationFlag
	EnableAutoPowerOn   = Entry(wPreference, bd = 3, width = 18)
	EnableAutoPowerOff  = Entry(wPreference, bd = 3, width = 18)
	SetAutoPowerOffTime = Entry(wPreference, bd = 3, width = 18)
	EnableStandBy       = Entry(wPreference, bd = 3, width = 18)
	SetStandByTime      = Entry(wPreference, bd = 3, width = 18)
	SetMirrorFlag       = Entry(wPreference, bd = 3, width = 18)
	SetRotationFlag     = Entry(wPreference, bd = 3, width = 18)

	#	Input: Grid Properties
	EnableAutoPowerOn  .grid(row = 1, column = 3)
	EnableAutoPowerOff .grid(row = 2, column = 3)
	SetAutoPowerOffTime.grid(row = 3, column = 3)
	EnableStandBy      .grid(row = 4, column = 3)
	SetStandByTime     .grid(row = 5, column = 3)
	SetMirrorFlag      .grid(row = 6, column = 3)
	SetRotationFlag    .grid(row = 7, column = 3)

	ResetDefaultParameter()

	#	Right Part: Buttons
	for i in xrange(1,8): eval("Label(wPreference, bd = 3).grid(row = " + str(i) + ", column = 4, ipadx = 5, ipady = 2)")
	Button(wPreference, text = "RESET PARAMETER", width = 21, height = 3, command = TMP_Func1).grid(row = 2, column = 5, rowspan = 2)
	Button(wPreference, text = "START WORKFLOW",  width = 21, height = 1, command = TMP_Func2).grid(row = 5, column = 5)
	Button(wPreference, text = "STOP WORKFLOW",   width = 21, height = 1, command = TMP_Func3).grid(row = 6, column = 5)
	for i in xrange(1,8): eval("Label(wPreference, bd = 3).grid(row = " + str(i) + ", column = 6, ipadx = 5, ipady = 2)")

	#	Bottom
	Label(wPreference, bd = 3, text = "Test Application of UVC Camera SDK, built by ActivePython 2.7 (x86)").grid(row = 8, columnspan = 7, sticky = E+S+N)

# Check DLL's File Version
def DLL_FileVersion():
	try:
		DLL_VerInfo = win32api.GetFileVersionInfo(ACQSDK_DLL, "\\")
		ms = DLL_VerInfo['FileVersionMS']
		ls = DLL_VerInfo['FileVersionLS']
		return "%s.%s.%s.%s" % (win32api.HIWORD(ms),win32api.LOWORD(ms),win32api.HIWORD(ls),win32api.LOWORD(ls))
	except:
		return "NOT FOUND"

# Parameter value: Reset
def ResetDefaultParameter():
	# Clean
	SetSystemTime        .delete(0, END)
	SetLogPath           .delete(0, END)
	SetHPWorkMode        .delete(0, END)
	SetSerialNumber      .delete(0, END)
	SetBrightness        .delete(0, END)
	SetContrast          .delete(0, END)
	SetPowerlineFrequency.delete(0, END)
	EnableAutoPowerOn    .delete(0, END)
	EnableAutoPowerOff   .delete(0, END)
	SetAutoPowerOffTime  .delete(0, END)
	EnableStandBy        .delete(0, END)
	SetStandByTime       .delete(0, END)
	SetMirrorFlag        .delete(0, END)
	SetRotationFlag      .delete(0, END)

	# Input: Default value
	SetSystemTime        .insert(0, str(int(time.time())))
	SetLogPath           .insert(0, "./")
	SetHPWorkMode        .insert(0, "1")
	SetSerialNumber      .insert(0, "ABCD1234")
	SetBrightness        .insert(0, "4")
	SetContrast          .insert(0, "4")
	SetPowerlineFrequency.insert(0, "50")
	EnableAutoPowerOn    .insert(0, "1")
	EnableAutoPowerOff   .insert(0, "1")
	SetAutoPowerOffTime  .insert(0, "3600")
	EnableStandBy        .insert(0, "1")
	SetStandByTime       .insert(0, "60")
	SetMirrorFlag        .insert(0, "1")
	SetRotationFlag      .insert(0, "0")

# Windows' events
def WindowState(objWin): return (objWin.winfo_width(), objWin.winfo_height(), objWin.winfo_x(), objWin.winfo_y())
def ResetWindowPosition(message):
	if message == "origin":
		# wControlPanel
		status = WindowState(wControlPanel)
		width  = status[0]
		height = status[1]
		x      = 0
		y      = 0
	else:
		# wControlPanel
		status = WindowState(wControlPanel)
		width  = status[0]
		height = status[1]
		x      = status[2]
		y      = status[3]

	# wLiveVideo
	x = width + x + 8
	wLiveVideo.geometry("+%s+%s" % (str(x), str(y)))
	wLiveVideo.update()
	# Check status of wLiveVideo
	if wLiveVideo.state() == "withdrawn": wLiveVideo.deiconify()

	# wPreference
	i = WindowState(wLiveVideo)
	j = WindowState(wPreference)
	wPreference.geometry("%sx%s+%s+%s" % (LiveVideo_Width, str(j[1]), str(x), str(int(i[1]) + y + 28)))
	wPreference.update()
def ResetLiveVideoWindowSize(width, height):
	wLiveVideo.geometry("%sx%s" % (width, height))
	ResetWindowPosition("DOIT")
def ChangeScrolledTextHeight(change):
	status = pLogger["height"]
	if change == "INCREASE":
		pLogger.config(height = status + 1)
	if change == "DECREASE":
		pLogger.config(height = status - 1)
def PreferenceSettingDialogVisable():
	if wPreference.state() == "withdrawn":
		wPreference.update()
		wPreference.deiconify()
		pPSDV.config(text = "Config <<")
	elif wPreference.state() == "normal":
		wPreference.update()
		wPreference.withdraw()
		pPSDV.config(text = "Config >>")
def EXITAPP():
	if Initiated == True: objACQSDK_CSDevice.ACQSDK_UnInit()
	wControlPanel.quit()

# Customized events
def OpenDirectory(location = "."):
	if location == ".":
		os.system("explorer.exe %s" % ".")
	elif os.path.exists(location):
		os.system("explorer.exe %s" % location)
	else:
		return
def KillProcess(process = "python.exe"): os.system("TASKKILL /F /IM %s" % process)

# SDK's API
def ACQSDK_Init():
	ACQSDK_SetLogPath()
	ret = objACQSDK_CSDevice.ACQSDK_Init(hWnd)
	CheckResult(sys._getframe().f_code.co_name, ret)
	Initiated = True
def ACQSDK_UnInit():
	ret = objACQSDK_CSDevice.ACQSDK_UnInit()
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_OnUpdateLiveWnd():
	ret = objACQSDK_CSDevice.ACQSDK_OnUpdateLiveWnd()
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_QueryDeviceInfo():
	pDeviceInfo = win32com.client.Dispatch(ACQSDK_ASDeviceInfor_ProgID)
	ret         = objACQSDK_CSDevice.ACQSDK_QueryDeviceInfo(pDeviceInfo)
	CheckResult(sys._getframe().f_code.co_name, ret)
	if ret == 0:
		try:
			index1 = str(hex(pDeviceInfo.get_device_type())).upper()
			device_type = Device_Type[index1]
		except:
			device_type = index1
		finally:
			Logger("\tDevice Type is %r" % device_type)
		try:
			index2 = str(hex(pDeviceInfo.get_mode_type())).upper()
			model_type = Model_Type[index2]
		except:
			model_type = index2
		finally:
			Logger("\tMode Type is %r" % model_type)
		Logger("\tSerial Number is %r" % pDeviceInfo.get_sn())
		Logger("\tFirmware Version is %r" % pDeviceInfo.get_fw_version())
	del pDeviceInfo
def ACQSDK_SetHPWorkMode(): # Not implemented
	lWorkMode = int(SetHPWorkMode.get())
	Logger("<%r>" % lWorkMode)
	ret = objACQSDK_CSDevice.ACQSDK_SetHPWorkMode(lWorkMode)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_StartPlay():
	ret = objACQSDK_CSDevice.ACQSDK_StartPlay()
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_StopPlay():
	ret = objACQSDK_CSDevice.ACQSDK_StopPlay()
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_StartRecord():
	path = r"./%s.avi" % time.strftime('%Y-%m-%d-%H-%M-%S')
	ret = objACQSDK_CSDevice.ACQSDK_StartRecord(path)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_StopRecord():
	ret = objACQSDK_CSDevice.ACQSDK_StopRecord()
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_Capture():
	pImageUnit = win32com.client.Dispatch(ACQSDK_ASImageUnit_ProgID)
	ret        = objACQSDK_CSDevice.ACQSDK_Capture(pImageUnit)
	CheckResult(sys._getframe().f_code.co_name, ret)
	if ret == 0:
		img = pImageUnit.get_white_image()
		Logger("\tImageUnit: %r" % img)
		img_file = time.strftime('%Y-%m-%d-%H-%M-%S')
		save_image_ret = pImageUnit.save_image(r"./%s" % img_file, img)
		CheckResult("ACQSDK_Capture -> Save image", save_image_ret)
		Logger("\t%s.jpg" % img_file)
		CheckResult("ACQSDK_Capture -> Free image", pImageUnit.free_image(img))
		CheckResult("ACQSDK_Capture -> Free unit", pImageUnit.free_unit())
	del pImageUnit
def ACQSDK_GetImageData():
	pImageUnit = win32com.client.Dispatch(ACQSDK_ASImageUnit_ProgID)
	ret = objACQSDK_CSDevice.ACQSDK_GetImageData(pImageUnit)
	CheckResult(sys._getframe().f_code.co_name, ret)
	if ret == 0:
		img = pImageUnit.get_white_image()
		Logger("\tImageUnit: %r" % img)
		CheckResult("ACQSDK_GetImageData -> Save image", pImageUnit.save_image(r"./%s" % time.strftime('%Y-%m-%d-%H-%M-%S'), img))
		CheckResult("ACQSDK_GetImageData -> Free image", pImageUnit.free_image(img))
		CheckResult("ACQSDK_GetImageData -> Free unit", pImageUnit.free_unit())
	del pImageUnit
def ACQSDK_SetLogPath():
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
def ACQSDK_UpgradeFirmware():
	pFullPathName = askopenfilename()
	if pFullPathName != "":
		class FWUpgrade(threading.Thread):
			def __init__(self):
				threading.Thread.__init__(self)
			def run(self):
				self.ret = objACQSDK_CSDevice.ACQSDK_UpgradeFirmware(pFullPathName)
				CheckResult("Firmware Upgrade Thread", self.ret)
		instance = FWUpgrade()
		instance.start()
	elif pFullPathName == "":
		Logger("ACQSDK_UpgradeFirmware -> No File is selected.")
def ACQSDK_AbortUpgrade():
	ret = objACQSDK_CSDevice.ACQSDK_AbortUpgrade()
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_UploadFile():
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
	pFileName = askdirectory()
	ret = objACQSDK_CSDevice.ACQSDK_DownloadFile(fileID, pFileName)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_EnableAutoPowerOn():
	bEnable = int(EnableAutoPowerOn.get())
	Logger("<%r>" % bEnable)
	ret = objACQSDK_CSDevice.ACQSDK_EnableAutoPowerOn(bEnable)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_GetBrightness():
	ret = objACQSDK_CSDevice.ACQSDK_GetBrightness()
	CheckResult(sys._getframe().f_code.co_name, ret[0])
	Logger("\t%s" % str(ret))
	if ret[0] == 0:
		Logger("\tCurrent brightness: %r" % ret[1])
		Logger("\tMaximum brightness: %r" % ret[2])
		Logger("\tMinimum brightness: %r" % ret[3])
		Logger("\tDefault brightness: %r" % ret[4])
def ACQSDK_SetBrightness():
	brightness = int(SetBrightness.get())
	Logger("<%r>" % brightness)
	ret = objACQSDK_CSDevice.ACQSDK_SetBrightness(brightness)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_GetContrast():
	ret = objACQSDK_CSDevice.ACQSDK_GetContrast()
	CheckResult(sys._getframe().f_code.co_name, ret[0])
	Logger("\t%s" % str(ret))
	if ret[0] == 0:
		Logger("\tCurrent contrast: %r" % ret[1])
		Logger("\tMaximum contrast: %r" % ret[2])
		Logger("\tMinimum contrast: %r" % ret[3])
		Logger("\tDefault contrast: %r" % ret[4])
def ACQSDK_SetContrast():
	contrast = int(SetContrast.get())
	Logger("<%r>" % contrast)
	ret = objACQSDK_CSDevice.ACQSDK_SetContrast(contrast)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_SetPowerlineFrequency():
	frequency = int(SetPowerlineFrequency.get())
	Logger("<%r>" % frequency)
	ret = objACQSDK_CSDevice.ACQSDK_SetPowerlineFrequency(frequency)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_GetPowerlineFrequency():
	ret = objACQSDK_CSDevice.ACQSDK_GetPowerlineFrequency()
	CheckResult(sys._getframe().f_code.co_name, ret[0])
	Logger("\t%s" % str(ret))
	if ret[0] == 0:
		Logger("\tCurrent frequency: %r" % ret[1])
		Logger("\tDefault frequency: %r" % ret[2])
def ACQSDK_EnableAutoPowerOff():
	bEnable = int(EnableAutoPowerOff.get())
	Logger("<%r>" % bEnable)
	ret = objACQSDK_CSDevice.ACQSDK_EnableAutoPowerOff(bEnable)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_SetAutoPowerOffTime():
	secondsCount = int(SetAutoPowerOffTime.get())
	Logger("<%r>" % secondsCount)
	ret = objACQSDK_CSDevice.ACQSDK_SetAutoPowerOffTime(secondsCount)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_EnableStandBy():
	bEnable = int(EnableStandBy.get())
	Logger("<%r>" % bEnable)
	ret = objACQSDK_CSDevice.ACQSDK_EnableStandBy(bEnable)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_SetStandByTime():
	secondsCount = int(SetStandByTime.get())
	Logger("<%r>" % secondsCount)
	ret = objACQSDK_CSDevice.ACQSDK_SetStandByTime(secondsCount)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_SetSystemTime():
	secondsCount = int(SetSystemTime.get())
	Logger("<%r>" % secondsCount)
	ret = objACQSDK_CSDevice.ACQSDK_SetSystemTime(secondsCount)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_SetMirrorFlag():
	bEnable = int(SetMirrorFlag.get())
	Logger("<%r>" % bEnable)
	ret = objACQSDK_CSDevice.ACQSDK_SetMirrorFlag(bEnable)
	CheckResult(sys._getframe().f_code.co_name, ret)
def ACQSDK_SetRotationFlag():
	rotation = int(SetRotationFlag.get())
	Logger("<%r>" % rotation)
	ret = objACQSDK_CSDevice.ACQSDK_SetRotationFlag(rotation)
	CheckResult(sys._getframe().f_code.co_name, ret)

# Class needed by Callback
class SDKEvents():
	def OnHPEvents(self, Callback):
		i = Callback.QueryInterface(pythoncom.IID_IDispatch)
		objSDKCallbackInfo = win32com.client.Dispatch(i)
		EventID = str(hex(objSDKCallbackInfo.get_event_id())).upper()
		Logger(" * Callback -> %s" % EventID)
		try:
			EventID_Value = Callback_MsgType[EventID]
		except:
			EventID_Value = "NOT DEFINED"
		finally:
			Logger("\t%s -> %s" % (EventID, EventID_Value))
		if EventID == "0X200005": ACQSDK_GetImageData()
		if EventID == "0X200003": Logger("\t -> %r" %objSDKCallbackInfo.get_fw_upgrade_percent())

# Class for Workflow
class WorkflowTesting():
	def __init__(self):
		self.Tag = True
		self.thread_s_one = None
		self.thread_s_two = None
	def START(self):
		while True:
			if self.Tag == True:
				if self.thread_s_one is None or self.thread_s_one.isAlive() == False:
					self.thread_s_one = threading.Thread(target = self.Scenario_One, args = (1,1))
					self.thread_s_one.setDaemon(True)
					self.thread_s_one.start()
				if self.thread_s_two is None or self.thread_s_two.isAlive() == False:
					self.thread_s_two = threading.Thread(target = self.Scenario_Two, args = (1,1))
					self.thread_s_two.setDaemon(True)
					self.thread_s_two.start()
			elif self.Tag == False:
				break
		ACQSDK_StopPlay()
		ACQSDK_UnInit()
	def Scenario_One(self, num, delay):
		ACQSDK_Capture()
		time.sleep(1)
	def Scenario_Two(self, num, delay):
		ACQSDK_StartRecord()
		time.sleep(1)
		ACQSDK_StopRecord()

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
	if not os.path.isfile("./" + LoggerOutput): open("./" + LoggerOutput, "w").close()
	strLine = "%s\n" % str(strLine)
	pLogger.insert(END, strLine)
	pLogger.yview(END)
	f = open("./" + LoggerOutput, "a+")
	f.write(strLine)
	f.close()
def CLEANHistory(): pLogger.delete('1.0', END)

# Temporary buttons
def TMP_Func1(): ResetDefaultParameter()
def TMP_Func2():
	ACQSDK_Init()
	time.sleep(1)
	ACQSDK_StartPlay()
	time.sleep(1)
	global instance
	instance = WorkflowTesting()
	instance.START()
def TMP_Func3():
	instance.Tag = False

# >>Body<<

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
ACQSDK_CSDevice_ProgID      = "ACQSDK.CSDevice.1"
ACQSDK_ASImageUnit_ProgID   = "ACQSDK.ASImageUnit.1"
ACQSDK_ASDeviceInfor_ProgID = "ACQSDK.ASDeviceInfor.1"

# Location
ACQSDK_DLL_Dir = "C:\\Program Files (x86)\\Common Files\\Trophy\\Acquisition\\AcqSdk\\"
ACQSDK_DLL     = ACQSDK_DLL_Dir + "ACQSDK.DLL"
LoggerOutput   = "Logger.out.log"

# Generate GUI elements for three window
LiveVideo_Width  = "640"
LiveVideo_Height = "480"
GenerateGUI()

# Flag of Init :: If Init is not executed, EXITAPP function will not execute UnInit.
Initiated = False

# Create COM object and Event
try:
	objACQSDK_CSDevice = win32com.client.DispatchWithEvents(ACQSDK_CSDevice_ProgID, SDKEvents)
except:
	print "Fail to create COM object."

# Event after window has displayed for some time
wControlPanel.after(1000, lambda: ResetWindowPosition("origin"))

# Wait for message
mainloop()