"""
    GUI: Quick Checking on SDK's API

    History:
        2014-02-18	0.1		First version
							Notes: Some APIs are not ready.
		2014-03-26	0.2		Update new APIs
"""

import os, sys, time, threading
import win32com.client, win32api, pythoncom
from Tkinter import *
from ScrolledText import ScrolledText
from tkFileDialog import *
from tkMessageBox import *
try:
	sys.path.append(r'../Module')
	import TestACQSDK_Module_Global_Definition as GD
	import TestACQSDK_Module_Wrapper as SDKAPI
except:
	print "Expected module files are not imported successfully."
	#sys.exit(1)

# Generate GUI
def GenerateGUI():
	# Create Tkinter windows
	# GUI : Workflow
	global wControlPanel, wLiveVideo, wLogger
	wControlPanel = Tk()	# List buttons
	wLiveVideo    = Tk()	# Display Live Window
	wLogger       = Tk()    # Logger Window

	# Handler of the wLiveVideo
	global hWnd
	hWnd = wLiveVideo.winfo_id()

	# GUI Configuration
	GenerateControlPanel()
	GenerateLiveVideo()
	GenerateLogger()

	# Bind customized event
	wControlPanel.bind("<F11>", lambda x: KillProcess())
	wLiveVideo   .bind("<F11>", lambda x: KillProcess())
	wLogger      .bind("<F11>", lambda x: KillProcess())
	wControlPanel.bind("<F12>", lambda x: OpenDirectory())

	# Trace window's event: DELETE
	wControlPanel.protocol("WM_DELETE_WINDOW", EXITAPP)
	wLiveVideo   .protocol("WM_DELETE_WINDOW", lambda: 0) # No response when trying to close Live Video's window
	wLogger      .protocol("WM_DELETE_WINDOW", lambda: 0) # No response when trying to close Logger's window
def GenerateControlPanel():
	#	Panel
	wControlPanel.geometry("+5+5")
	wControlPanel.title("SDK Testing: Control Panel")
	wControlPanel.resizable(width = False, height = False)

	#	Add Menu
	MenuBar = Menu(wControlPanel)
	#		Operation
	FileOperation = Menu(MenuBar, tearoff = 0)
	MenuBar.add_cascade(label = "File", menu = FileOperation)
	FileOperation.add_checkbutton(label = "Display Operation History Window", command = DisplayOperationHistoryWindow)
	FileOperation.add_command(label = "Reset Parameter to Default Value", command = ResetDefaultParameter)
	FileOperation.add_separator()
	FileOperation.add_command(label = "Exit", command = EXITAPP)
	#		Help
	HelpMenu = Menu(MenuBar, tearoff = 0)
	MenuBar.add_cascade(label = "About", menu = HelpMenu)
	HelpMenu.add_command(label = "ACQSDK.DLL -> Version", command = lambda: showinfo("", "ACQSDK.DLL -> %s" % ACQSDKDLL_FileVersion()))
	#	Display Menu
	wControlPanel.config(menu = MenuBar)

	#	GUI Definition: Property
	ButtonWidth = 22
	EntryWidth = 25

	#	Group: Basic
	BasicFrameRow = 0
	BasicFrame = LabelFrame(wControlPanel, text = "Basic Function", width = 400, padx = 3, pady = 3)
	BasicFrame.grid(row = BasicFrameRow, column = 0, columnspan = 3)
	Button(BasicFrame, text = "Set Log Path",   width = ButtonWidth, command = ACQSDK_SetLogPath)  .grid(row = BasicFrameRow,      column = 0)
	global LogPathInput
	LogPathInput = Entry(BasicFrame, bd = 2, width = EntryWidth*2)
	LogPathInput                                                                                   .grid(row = BasicFrameRow,      column = 1, columnspan = 2)
	Button(BasicFrame, text = "Init",           width = ButtonWidth, command = ACQSDK_Init)        .grid(row = BasicFrameRow + 1,  column = 1)
	Button(BasicFrame, text = "UnInit",         width = ButtonWidth, command = ACQSDK_UnInit)      .grid(row = BasicFrameRow + 1,  column = 2)
	Button(BasicFrame, text = "Start Play",     width = ButtonWidth, command = ACQSDK_StartPlay)   .grid(row = BasicFrameRow + 2,  column = 1)
	Button(BasicFrame, text = "Stop Play",      width = ButtonWidth, command = ACQSDK_StopPlay)    .grid(row = BasicFrameRow + 2,  column = 2)
	Button(BasicFrame, text = "Capture",        width = ButtonWidth, command = ACQSDK_Capture)     .grid(row = BasicFrameRow + 3,  column = 1)
	Button(BasicFrame, text = "Get Image Data", width = ButtonWidth, command = ACQSDK_GetImageData).grid(row = BasicFrameRow + 3,  column = 2)
	Button(BasicFrame, text = "Start Record",   width = ButtonWidth, command = ACQSDK_StartRecord) .grid(row = BasicFrameRow + 4,  column = 1)
	Button(BasicFrame, text = "Stop Record",    width = ButtonWidth, command = ACQSDK_StopRecord)  .grid(row = BasicFrameRow + 4,  column = 2)

	#	Group: Query Info
	QueryFrameRow = 10
	QueryFrame = LabelFrame(wControlPanel,  text = "Information Query", padx = 3, pady = 3)
	QueryFrame.grid(row = QueryFrameRow, column = 0, columnspan = 3)
	Button(QueryFrame, text = "Query Device",      width = ButtonWidth, command = ACQSDK_QueryDeviceInfo)   .grid(row = QueryFrameRow, column = 0)
	Button(QueryFrame, text = "Query SDK Version", width = ButtonWidth, command = ACQSDK_GetSDKVersion)     .grid(row = QueryFrameRow, column = 1)
	Button(QueryFrame, text = "Query FW Version",  width = ButtonWidth, command = ACQSDK_GetFirmwareVersion).grid(row = QueryFrameRow, column = 2)

	#	Group: Firmware Upgrade
	FirmwareUpgradeFrameRow = 20
	FirmwareUpgradeFrame = LabelFrame(wControlPanel,  text = "Firmware Upgrade", padx = 3, pady = 3)
	FirmwareUpgradeFrame.grid(row = FirmwareUpgradeFrameRow, column = 0, columnspan = 3)
	Button(FirmwareUpgradeFrame, text = "Abort Upgrade", width = ButtonWidth, command = ACQSDK_AbortUpgrade)   .grid(row = FirmwareUpgradeFrameRow, column = 0)
	Button(FirmwareUpgradeFrame, text = "Upgrade FW",    width = ButtonWidth, command = ACQSDK_UpgradeFirmware).grid(row = FirmwareUpgradeFrameRow, column = 1)
	Placeholder = Button(FirmwareUpgradeFrame, text = "FW Upgrade Test",   width = ButtonWidth)
	Placeholder.grid(row = FirmwareUpgradeFrameRow, column = 2)
	Placeholder.config(state = "disabled")

	#	Group: Mirror and Rotation
	MirrorRotationFrameRow = 30
	MirrorRotationFrame = LabelFrame(wControlPanel,  text = "Mirror & Rotation", padx = 3, pady = 3)
	MirrorRotationFrame.grid(row = MirrorRotationFrameRow, column = 0, columnspan = 3)
	Label(MirrorRotationFrame, text = "Fetch Setting").grid(row = MirrorRotationFrameRow, column = 0)
	Label(MirrorRotationFrame, text = "Apply Setting").grid(row = MirrorRotationFrameRow, column = 1)
	Label(MirrorRotationFrame, text = " <- Value")    .grid(row = MirrorRotationFrameRow, column = 2)
	Button(MirrorRotationFrame, text = "Get Mirror Flag", width = ButtonWidth, anchor = W, command = ACQSDK_GetMirrorFlag)    .grid(row = MirrorRotationFrameRow + 1, column = 0)
	Button(MirrorRotationFrame, text = "Set Mirror Flag", width = ButtonWidth, anchor = W, command = ACQSDK_SetMirrorFlag)    .grid(row = MirrorRotationFrameRow + 1, column = 1)
	global MirrorInput
	MirrorInput = Entry(MirrorRotationFrame, bd = 2, width = EntryWidth)
	MirrorInput                                                                                                               .grid(row = MirrorRotationFrameRow + 1, column = 2)
	Button(MirrorRotationFrame, text = "Get Rotation Flag", width = ButtonWidth, anchor = W, command = ACQSDK_GetRotationFlag).grid(row = MirrorRotationFrameRow + 2, column = 0)
	Button(MirrorRotationFrame, text = "Set Rotation Flag", width = ButtonWidth, anchor = W, command = ACQSDK_SetRotationFlag).grid(row = MirrorRotationFrameRow + 2, column = 1)
	global RotationInput
	RotationInput = Entry(MirrorRotationFrame, bd = 2, width = EntryWidth)
	RotationInput                                                                                                             .grid(row = MirrorRotationFrameRow + 2, column = 2)
	#		The following two buttons are added for Rotation APIs
	Button(MirrorRotationFrame, text = "Set to 640*480", width = ButtonWidth, command = lambda: ResetLiveVideoWindowSize(640, 480)).grid(row = MirrorRotationFrameRow + 3,  column = 1)
	Button(MirrorRotationFrame, text = "Set to 480*640", width = ButtonWidth, command = lambda: ResetLiveVideoWindowSize(480, 640)).grid(row = MirrorRotationFrameRow + 3,  column = 2)
	#		Refresh Window and set window size
	Button(MirrorRotationFrame, text = "Update LiveVideo Size", width = ButtonWidth, command = ChangeLiveVideoSize)   .grid(row = MirrorRotationFrameRow + 4, column = 1)
	Button(MirrorRotationFrame, text = "Refresh LiveVideo Window",     width = ButtonWidth, command = ACQSDK_OnUpdateLiveWnd).grid(row = MirrorRotationFrameRow + 4, column = 2)

	#	Group: Handpiece Common Configuration
	CommonConfigurationFrameRow = 40
	CommonConfigurationFrame = LabelFrame(wControlPanel,  text = "HP Configuration", padx = 3, pady = 3)
	CommonConfigurationFrame.grid(row = CommonConfigurationFrameRow, column = 0, columnspan = 3)
	Label(CommonConfigurationFrame, text = "Fetch Setting").grid(row = CommonConfigurationFrameRow, column = 0)
	Label(CommonConfigurationFrame, text = "Apply Setting").grid(row = CommonConfigurationFrameRow, column = 1)
	Label(CommonConfigurationFrame, text = " <- Value")    .grid(row = CommonConfigurationFrameRow, column = 2)
	Button(CommonConfigurationFrame, text = "Get Brightness",          width = ButtonWidth, anchor = W, command = ACQSDK_GetBrightness        ).grid(row = CommonConfigurationFrameRow + 1, column = 0, padx = 3)
	Button(CommonConfigurationFrame, text = "Set Brightness",          width = ButtonWidth, anchor = W, command = ACQSDK_SetBrightness        ).grid(row = CommonConfigurationFrameRow + 1, column = 1, padx = 3)
	Button(CommonConfigurationFrame, text = "Get Contrast",            width = ButtonWidth, anchor = W, command = ACQSDK_GetContrast          ).grid(row = CommonConfigurationFrameRow + 2, column = 0, padx = 3)
	Button(CommonConfigurationFrame, text = "Set Contrast",            width = ButtonWidth, anchor = W, command = ACQSDK_SetContrast          ).grid(row = CommonConfigurationFrameRow + 2, column = 1, padx = 3)
	Button(CommonConfigurationFrame, text = "Get Frequency",           width = ButtonWidth, anchor = W, command = ACQSDK_GetPowerlineFrequency).grid(row = CommonConfigurationFrameRow + 3, column = 0, padx = 3)
	Button(CommonConfigurationFrame, text = "Set Frequency",           width = ButtonWidth, anchor = W, command = ACQSDK_SetPowerlineFrequency).grid(row = CommonConfigurationFrameRow + 3, column = 1, padx = 3)
	Button(CommonConfigurationFrame, text = "Get Sleep Status",        width = ButtonWidth, anchor = W, command = ACQSDK_GetEnableSleep       ).grid(row = CommonConfigurationFrameRow + 4, column = 0, padx = 3)
	Button(CommonConfigurationFrame, text = "Set Sleep",               width = ButtonWidth, anchor = W, command = ACQSDK_SetEnableSleep       ).grid(row = CommonConfigurationFrameRow + 4, column = 1, padx = 3)
	Button(CommonConfigurationFrame, text = "Get Sleep Time",          width = ButtonWidth, anchor = W, command = ACQSDK_GetSleepTime         ).grid(row = CommonConfigurationFrameRow + 5, column = 0, padx = 3)
	Button(CommonConfigurationFrame, text = "Set Sleep Time",          width = ButtonWidth, anchor = W, command = ACQSDK_SetSleepTime         ).grid(row = CommonConfigurationFrameRow + 5, column = 1, padx = 3)
	Button(CommonConfigurationFrame, text = "Get AutoPowerOn Status",  width = ButtonWidth, anchor = W, command = ACQSDK_GetEnableAutoPowerOn ).grid(row = CommonConfigurationFrameRow + 6, column = 0, padx = 3)
	Button(CommonConfigurationFrame, text = "Set AutoPowerOn",         width = ButtonWidth, anchor = W, command = ACQSDK_EnableAutoPowerOn    ).grid(row = CommonConfigurationFrameRow + 6, column = 1, padx = 3)
	Button(CommonConfigurationFrame, text = "Get AutoPowerOff Status", width = ButtonWidth, anchor = W, command = ACQSDK_GetEnableAutoPowerOff).grid(row = CommonConfigurationFrameRow + 7, column = 0, padx = 3)
	Button(CommonConfigurationFrame, text = "Set AutoPowerOff",        width = ButtonWidth, anchor = W, command = ACQSDK_EnableAutoPowerOff   ).grid(row = CommonConfigurationFrameRow + 7, column = 1, padx = 3)
	Button(CommonConfigurationFrame, text = "Get AutoPowerOff Time",   width = ButtonWidth, anchor = W, command = ACQSDK_GetAutoPowerOffTime  ).grid(row = CommonConfigurationFrameRow + 8, column = 0, padx = 3)
	Button(CommonConfigurationFrame, text = "Set AutoPowerOff Time",   width = ButtonWidth, anchor = W, command = ACQSDK_SetAutoPowerOffTime  ).grid(row = CommonConfigurationFrameRow + 8, column = 1, padx = 3)
	#		Inputbox
	global BrightnessInput, ContrastInput, FrequencyInput, SetSleepInput, SleepTimeInput, SetAutoPowerOnInput, SetAutoPowerOffInput, AutoPowerOffTimeInput
	BrightnessInput       = Entry(CommonConfigurationFrame, bd = 2, width = EntryWidth)
	ContrastInput         = Entry(CommonConfigurationFrame, bd = 2, width = EntryWidth)
	FrequencyInput        = Entry(CommonConfigurationFrame, bd = 2, width = EntryWidth)
	SetSleepInput         = Entry(CommonConfigurationFrame, bd = 2, width = EntryWidth)
	SleepTimeInput        = Entry(CommonConfigurationFrame, bd = 2, width = EntryWidth)
	SetAutoPowerOnInput   = Entry(CommonConfigurationFrame, bd = 2, width = EntryWidth)
	SetAutoPowerOffInput  = Entry(CommonConfigurationFrame, bd = 2, width = EntryWidth)
	AutoPowerOffTimeInput = Entry(CommonConfigurationFrame, bd = 2, width = EntryWidth)
	BrightnessInput      .grid(row = CommonConfigurationFrameRow + 1, column = 2)
	ContrastInput        .grid(row = CommonConfigurationFrameRow + 2, column = 2)
	FrequencyInput       .grid(row = CommonConfigurationFrameRow + 3, column = 2)
	SetSleepInput        .grid(row = CommonConfigurationFrameRow + 4, column = 2)
	SleepTimeInput       .grid(row = CommonConfigurationFrameRow + 5, column = 2)
	SetAutoPowerOnInput  .grid(row = CommonConfigurationFrameRow + 6, column = 2)
	SetAutoPowerOffInput .grid(row = CommonConfigurationFrameRow + 7, column = 2)
	AutoPowerOffTimeInput.grid(row = CommonConfigurationFrameRow + 8, column = 2)
	#		Reset All Parameters
	ResetDefaultParameter()

	#	Label: Display label
	AuthorLabelRow = 100
	Label(wControlPanel, text = InfoLabel).grid(row = AuthorLabelRow, column = 0, columnspan = 3, sticky = E+N+S)

	#	Set Window Property
	wControlPanel.update()
def GenerateLiveVideo():
	#	Live Video
	wLiveVideo.geometry("%sx%s" % (LiveVideo_Width, LiveVideo_Height))
	wLiveVideo.title("SDK Testing: Live Video")
	wLiveVideo.update()
	wLiveVideo.withdraw()
def GenerateLogger():
	#	Logger
	wLogger.title("Operation History")
	wLogger.geometry("850x700")
	global pLogger
	pLogger = ScrolledText(wLogger, width = 50, height = 30, font = ("Courier New", 10), bg = "grey")
	pLogger.pack(fill = BOTH, expand = 1)
	wLogger.update()
	wLogger.withdraw()

# Windows' events
def WindowState(objWin): return (objWin.winfo_width(), objWin.winfo_height(), objWin.winfo_x(), objWin.winfo_y())
def ResetWindowPosition():
	# wControlPanel
	#status = WindowState(wControlPanel)
	#wControlPanel.geometry("+%d+%d" % (5, (wControlPanel.winfo_screenheight() - status[1])/2))
	#	Check status of wControlPanel
	#if wControlPanel.state() == "withdrawn": wControlPanel.deiconify()
	wControlPanel.geometry("+5+5")

	# wLiveVideo
	status = WindowState(wLiveVideo)
	wLiveVideo.geometry("+%d+%d" % ((wLiveVideo.winfo_screenwidth() - status[0])/2, (wLiveVideo.winfo_screenheight() - status[1])/2))
	wLiveVideo.update()
	#	Check status of wLiveVideo
	if wLiveVideo.state() == "withdrawn": wLiveVideo.deiconify()

	# wLogger
	status = WindowState(wLogger)
	x = (wLogger.winfo_screenwidth() - status[0] - 20)
	wLogger.geometry("+%d+%d" % (x, 0))
def ResetLiveVideoWindowSize(width, height):
	wLiveVideo.geometry("%dx%d" % (width, height))
	wLiveVideo.update()
	ResetWindowPosition()
def ChangeLiveVideoSize():
	status = WindowState(wLiveVideo)
	if status[0] != 640:
		wLiveVideo.geometry("%dx%d" % (status[0], status[0]*0.75))
		wLiveVideo.update()
def DisplayOperationHistoryWindow():
	global DisplayOperationHistoryWindowFlag
	DisplayOperationHistoryWindowFlag = not DisplayOperationHistoryWindowFlag
	if DisplayOperationHistoryWindowFlag == True: wLogger.deiconify()
	elif DisplayOperationHistoryWindowFlag == False: wLogger.withdraw()
def EXITAPP():
	if Initiated == True: objACQSDK_CSDevice.ACQSDK_UnInit()
	wControlPanel.quit()

# Functions for Logger box
def CheckResult(ret):
	print "Result Received -> %r" % (str(ret)) # For Debug
	Logger("%s" % str(ret))
def Logger(strLine):
	global OperationHistoryWindowLineFlag
	if not os.path.isfile("./" + LoggerOutput): open("./" + LoggerOutput, "w").close()
	if OperationHistoryWindowLineFlag > OperationHistoryWindowLineMax:
		CLEANHistory()
		OperationHistoryWindowLineFlag = 0
	strLine = "%s\n" % str(strLine)
	pLogger.insert(END, strLine)
	pLogger.yview(END)
	OperationHistoryWindowLineFlag += 1
	with open("./" + LoggerOutput, "a+") as f: f.write(strLine)
def CLEANHistory(): pLogger.delete('1.0', END)


# Customized events
def ACQSDKDLL_FileVersion():
	try:
		DLL_VerInfo = win32api.GetFileVersionInfo(ACQSDK_DLL, "\\")
		ms = DLL_VerInfo['FileVersionMS']
		ls = DLL_VerInfo['FileVersionLS']
		return "%s.%s.%s.%s" % (win32api.HIWORD(ms),win32api.LOWORD(ms),win32api.HIWORD(ls),win32api.LOWORD(ls))
	except:
		return "NOT FOUND"
def ResetDefaultParameter():
	# Clean
	LogPathInput         .delete(0, END)
	MirrorInput          .delete(0, END)
	RotationInput        .delete(0, END)
	BrightnessInput      .delete(0, END)
	ContrastInput        .delete(0, END)
	FrequencyInput       .delete(0, END)
	SetSleepInput        .delete(0, END)
	SleepTimeInput       .delete(0, END)
	SetAutoPowerOnInput  .delete(0, END)
	SetAutoPowerOffInput .delete(0, END)
	AutoPowerOffTimeInput.delete(0, END)

	# Input: Default value
	LogPathInput         .insert(0, "./")
	MirrorInput          .insert(0, "1")
	RotationInput        .insert(0, "90")
	BrightnessInput      .insert(0, "4")
	ContrastInput        .insert(0, "4")
	FrequencyInput       .insert(0, "50")
	SetSleepInput        .insert(0, "0")
	SleepTimeInput       .insert(0, "60")
	SetAutoPowerOnInput  .insert(0, "0")
	SetAutoPowerOffInput .insert(0, "0")
	AutoPowerOffTimeInput.insert(0, "7200")
def OpenDirectory(location = "."):
	if location == ".":
		os.system("explorer.exe %s" % ".")
	elif os.path.exists(location):
		os.system("explorer.exe %s" % location)
	else:
		return
def KillProcess(process = "python.exe"): os.system("TASKKILL /F /IM %s" % process)
def MonitorKey(event): print event.char

# SDK's API
# ===================================================== API =====================================================
# Basic Function
def ACQSDK_Init():
	ret = SDKAPI.ACQSDK_Init(objACQSDK_CSDevice, hWnd)
	CheckResult(ret)
	Initiated = True
def ACQSDK_UnInit():
	ret = SDKAPI.ACQSDK_UnInit(objACQSDK_CSDevice)
	CheckResult(ret)
def ACQSDK_OnUpdateLiveWnd():
	ret = SDKAPI.ACQSDK_OnUpdateLiveWnd(objACQSDK_CSDevice)
	CheckResult(ret)
def ACQSDK_StartPlay():
	ret = SDKAPI.ACQSDK_StartPlay(objACQSDK_CSDevice)
	CheckResult(ret)
def ACQSDK_StopPlay():
	ret = SDKAPI.ACQSDK_StopPlay(objACQSDK_CSDevice)
	CheckResult(ret)
def ACQSDK_StartRecord():
	path = r"./%s.avi" % time.strftime('%Y-%m-%d-%H-%M-%S')
	ret = SDKAPI.ACQSDK_StartRecord(objACQSDK_CSDevice, path)
	CheckResult(ret)
def ACQSDK_StopRecord():
	ret = SDKAPI.ACQSDK_StopRecord(objACQSDK_CSDevice)
	CheckResult(ret)
def ACQSDK_Capture():
	class SWCapture(threading.Thread):
		def __init__(self): threading.Thread.__init__(self)
		def run(self):
			self.pImageUnit = win32com.client.Dispatch(GD.ACQSDK_ASImageUnit_ProgID)
			self.ret        = SDKAPI.ACQSDK_Capture(objACQSDK_CSDevice, self.pImageUnit)
			CheckResult(self.ret)
			if self.ret[1] == 0:
				self.img = self.pImageUnit.get_white_image()
				Logger(" >> ACQSDK_Capture -> get_white_image: %r" % self.img)
				self.img_file = time.strftime('%Y-%m-%d-%H-%M-%S')
				self.save_image_ret = self.pImageUnit.save_image(r"./%s" % self.img_file, self.img)
				Logger(" >> ACQSDK_Capture -> save_image:\t%r" % self.save_image_ret, )
				Logger(" >> ACQSDK_Capture -> free_image:\t%r" % self.pImageUnit.free_image(self.img))
				Logger(" >> ACQSDK_Capture -> free_unit:\t%r"  % self.pImageUnit.free_unit())
			del self.pImageUnit
	instance = SWCapture()
	instance.setDaemon(True)
	instance.start()
def ACQSDK_GetImageData():
	class HWCapture(threading.Thread):
		def __init__(self): threading.Thread.__init__(self)
		def run(self):
			self.pImageUnit = win32com.client.Dispatch(GD.ACQSDK_ASImageUnit_ProgID)
			self.ret        = SDKAPI.ACQSDK_GetImageData(objACQSDK_CSDevice, self.pImageUnit)
			CheckResult(self.ret)
			if self.ret[1] == 0:
				self.img = self.pImageUnit.get_white_image()
				Logger(" >> ACQSDK_GetImageData -> get_white_image: %r" % self.img)
				self.img_file = time.strftime('%Y-%m-%d-%H-%M-%S')
				self.save_image_ret = self.pImageUnit.save_image(r"./%s" % self.img_file, self.img)
				Logger(" >> ACQSDK_GetImageData -> save_image:\t%r" % self.save_image_ret, )
				Logger(" >> ACQSDK_GetImageData -> free_image:\t%r" % self.pImageUnit.free_image(self.img))
				Logger(" >> ACQSDK_GetImageData -> free_unit:\t%r"  % self.pImageUnit.free_unit())
			del self.pImageUnit
	instance = HWCapture()
	instance.setDaemon(True)
	instance.start()
def ACQSDK_SetLogPath():
	path = str(LogPathInput.get())
	Logger("Received Parameter -> %r" % path)
	ret  = SDKAPI.ACQSDK_SetLogPath(objACQSDK_CSDevice, path)
	CheckResult(ret)

# Mirror & Rotation
def ACQSDK_SetMirrorFlag():
	bEnable = int(MirrorInput.get())
	Logger("Received Parameter -> %r" % bEnable)
	ret = SDKAPI.ACQSDK_SetMirrorFlag(objACQSDK_CSDevice, bEnable)
	CheckResult(ret)
def ACQSDK_GetMirrorFlag():
	ret = SDKAPI.ACQSDK_GetMirrorFlag(objACQSDK_CSDevice)
	CheckResult(ret)
def ACQSDK_SetRotationFlag():
	rotation = int(RotationInput.get())
	Logger("Received Parameter -> %r" % rotation)
	ret = SDKAPI.ACQSDK_SetRotationFlag(objACQSDK_CSDevice, rotation)
	CheckResult(ret)
def ACQSDK_GetRotationFlag():
	ret = SDKAPI.ACQSDK_GetRotationFlag(objACQSDK_CSDevice)
	CheckResult(ret)

# Query
def ACQSDK_QueryDeviceInfo():
	pDeviceInfo = win32com.client.Dispatch(GD.ACQSDK_ASDeviceInfor_ProgID)
	ret         = SDKAPI.ACQSDK_QueryDeviceInfo(objACQSDK_CSDevice, pDeviceInfo)
	CheckResult(ret)
	if ret[1] == 0:
		try:
			index1 = str(hex(pDeviceInfo.get_device_type())).upper()
			device_type = GD.Device_Type[index1]
		except:
			device_type = index1
		finally:
			Logger(" >> ACQSDK_QueryDeviceInfo -> get_device_type: (%r, %r)" % (index1, device_type))
		try:
			index2 = str(hex(pDeviceInfo.get_mode_type())).upper()
			model_type = GD.Model_Type[index2]
		except:
			model_type = index2
		finally:
			Logger(" >> ACQSDK_QueryDeviceInfo -> get_mode_type: (%r, %r)" % (index2, model_type))
		Logger(" >> ACQSDK_QueryDeviceInfo -> get_sn: %r" % pDeviceInfo.get_sn())
		Logger(" >> ACQSDK_QueryDeviceInfo -> get_fw_version: %r" % pDeviceInfo.get_fw_version())
	del pDeviceInfo
def ACQSDK_GetFirmwareVersion():
	ret = SDKAPI.ACQSDK_GetFirmwareVersion(objACQSDK_CSDevice)
	CheckResult(ret)
def ACQSDK_GetSDKVersion():
	ret = SDKAPI.ACQSDK_GetSDKVersion(objACQSDK_CSDevice)
	CheckResult(ret)

# Configuration
# >> Brightness
def ACQSDK_GetBrightness():
	ret = SDKAPI.ACQSDK_GetBrightness(objACQSDK_CSDevice)
	CheckResult(ret)
	if ret[1][0] == 0:
		Logger("\tCurrent brightness: %r" % ret[1][1])
		Logger("\tMaximum brightness: %r" % ret[1][2])
		Logger("\tMinimum brightness: %r" % ret[1][3])
		Logger("\tDefault brightness: %r" % ret[1][4])
def ACQSDK_SetBrightness():
	brightness = int(BrightnessInput.get())
	Logger("Received Parameter -> %r" % brightness)
	ret = SDKAPI.ACQSDK_SetBrightness(objACQSDK_CSDevice, brightness)
	CheckResult(ret)

# >> Contrast
def ACQSDK_GetContrast():
	ret = SDKAPI.ACQSDK_GetContrast(objACQSDK_CSDevice)
	CheckResult(ret)
	if ret[1][0] == 0:
		Logger("\tCurrent contrast: %r" % ret[1][1])
		Logger("\tMaximum contrast: %r" % ret[1][2])
		Logger("\tMinimum contrast: %r" % ret[1][3])
		Logger("\tDefault contrast: %r" % ret[1][4])
def ACQSDK_SetContrast():
	contrast = int(ContrastInput.get())
	Logger("Received Parameter -> %r" % contrast)
	ret = SDKAPI.ACQSDK_SetContrast(objACQSDK_CSDevice, contrast)
	CheckResult(ret)

# >> Powerline Frequency
def ACQSDK_GetPowerlineFrequency():
	ret = SDKAPI.ACQSDK_GetPowerlineFrequency(objACQSDK_CSDevice)
	CheckResult(ret)
	if ret[1][0] == 0:
		Logger("\tCurrent frequency: %r" % ret[1][1])
		Logger("\tDefault frequency: %r" % ret[1][2])
def ACQSDK_SetPowerlineFrequency():
	frequency = int(FrequencyInput.get())
	Logger("Received Parameter -> %r" % frequency)
	ret = SDKAPI.ACQSDK_SetPowerlineFrequency(objACQSDK_CSDevice, frequency)
	CheckResult(ret)

# >> Sleep
def ACQSDK_SetEnableSleep():
	bEnable = int(SetSleepInput.get())
	Logger("Received Parameter -> %r" % bEnable)
	ret = SDKAPI.ACQSDK_SetEnableSleep(objACQSDK_CSDevice, bEnable)
	CheckResult(ret)
def ACQSDK_GetEnableSleep():
	ret = SDKAPI.ACQSDK_GetEnableSleep(objACQSDK_CSDevice)
	CheckResult(ret)
def ACQSDK_GetSleepTime():
	ret = SDKAPI.ACQSDK_GetSleepTime(objACQSDK_CSDevice)
	CheckResult(ret)
def ACQSDK_SetSleepTime():
	seconds = int(SleepTimeInput.get())
	Logger("Received Parameter -> %r" % seconds)
	ret = SDKAPI.ACQSDK_SetSleepTime(objACQSDK_CSDevice, seconds)
	CheckResult(ret)

# >> Auto Power On
def ACQSDK_EnableAutoPowerOn():
	bEnable = int(SetAutoPowerOnInput.get())
	Logger("Received Parameter -> %r" % bEnable)
	ret = SDKAPI.ACQSDK_EnableAutoPowerOn(objACQSDK_CSDevice, bEnable)
	CheckResult(ret)
def ACQSDK_GetEnableAutoPowerOn():
	ret = SDKAPI.ACQSDK_GetEnableAutoPowerOn(objACQSDK_CSDevice)
	CheckResult(ret)

# >> Auto Power Off
def ACQSDK_EnableAutoPowerOff():
	bEnable = int(SetAutoPowerOffInput.get())
	Logger("Received Parameter -> %r" % bEnable)
	ret = SDKAPI.ACQSDK_EnableAutoPowerOff(objACQSDK_CSDevice, bEnable)
	CheckResult(ret)
def ACQSDK_GetEnableAutoPowerOff():
	ret = SDKAPI.ACQSDK_GetEnableAutoPowerOff(objACQSDK_CSDevice)
	CheckResult(ret)
def ACQSDK_GetAutoPowerOffTime():
	ret = SDKAPI.ACQSDK_GetAutoPowerOffTime(objACQSDK_CSDevice)
	CheckResult(ret)
def ACQSDK_SetAutoPowerOffTime():
	secondsCount = int(AutoPowerOffTimeInput.get())
	Logger("Received Parameter -> %r" % secondsCount)
	ret = SDKAPI.ACQSDK_SetAutoPowerOffTime(objACQSDK_CSDevice, secondsCount)
	CheckResult(ret)

# Firmware
def ACQSDK_UpgradeFirmware():
	pFullPathName = askopenfilename()
	if pFullPathName != "":
		class FWUpgrade(threading.Thread):
			def __init__(self):
				threading.Thread.__init__(self)
			def run(self):
				self.ret = SDKAPI.ACQSDK_UpgradeFirmware(objACQSDK_CSDevice, pFullPathName)
				CheckResult("Firmware Upgrade Thread", self.ret)
		instance = FWUpgrade()
		instance.start()
	elif pFullPathName == "":
		Logger("ACQSDK_UpgradeFirmware -> No File is selected.")
def ACQSDK_AbortUpgrade():
	ret = SDKAPI.ACQSDK_AbortUpgrade(objACQSDK_CSDevice)
	CheckResult(ret)

# ===================================================== API =====================================================

# Callback Class -> CSDevice
class SDKEvents():
	def OnHPEvents(self, Callback):
		i = Callback.QueryInterface(pythoncom.IID_IDispatch)
		objSDKCallbackInfo = win32com.client.Dispatch(i)
		self.EventID = str(hex(objSDKCallbackInfo.get_event_id())).upper()
		self.EventState = " * Callback -> %s" % self.EventID
		try:
			self.EventID_Value = GD.Callback_MsgType[self.EventID]
		except:
			self.EventID_Value = "NOT DEFINED"
		finally:
			Logger("\t%s -> %s" % (self.EventState, self.EventID_Value))
		if self.EventID == "0X200005": ACQSDK_GetImageData()
		if self.EventID == "0X200003": Logger("\t -> %r" % objSDKCallbackInfo.get_fw_upgrade_percent())

# >>Body<<
# Location
try:
	ACQSDK_DLL_Dir = os.environ.get("CommonProgramFiles(x86)") + "\\Trophy\\Acquisition\\AcqSdk\\"
except:
	ACQSDK_DLL_Dir = os.environ.get("CommonProgramFiles") + "\\Trophy\\Acquisition\\AcqSdk\\"
finally:
	ACQSDK_DLL     = ACQSDK_DLL_Dir + "ACQSDK.DLL"

# Logger
LoggerOutput = "Logger.out.log"

# Flag of Init :: If Init is not executed, EXITAPP function will not execute UnInit.
Initiated = False

# Flag of Operation History Window
#	Display
DisplayOperationHistoryWindowFlag = False
#	Line Number
OperationHistoryWindowLineFlag = 0
OperationHistoryWindowLineMax  = 2000

# Information Label
InfoLabel = "Test Application of UVC Camera SDK built by ActivePython 2.7 (x86)"

# Generate GUI elements for three window
LiveVideo_Width  = "640"
LiveVideo_Height = "480"
GenerateGUI()

# Create COM object and Event
try: objACQSDK_CSDevice = win32com.client.DispatchWithEvents(GD.ACQSDK_CSDevice_ProgID, SDKEvents)
except: print "Fail to create COM object."

# Event after window has displayed for some time
wControlPanel.after(500, lambda: ResetWindowPosition())

# Wait for message
mainloop()