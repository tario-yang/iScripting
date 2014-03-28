"""
    GUI: Quick Checking on SDK's API

    History:
        2014-02-18	0.1		First version
							Notes: Some APIs are not ready.
		2014-03-26	0.2		Update new APIs
							Notes: Used @Windows7 64bit ENU
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
	sys.exit(1)

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
	wControlPanel.bind("<Key>", MonitorKey)
	wLiveVideo   .bind("<F11>", lambda x: KillProcess())
	wLiveVideo   .bind("<Key>", MonitorKey)
	wLogger      .bind("<F11>", lambda x: KillProcess())
	wLogger      .bind("<Key>", MonitorKey)
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
	Operation = Menu(MenuBar, tearoff = 0)
	MenuBar.add_cascade(label = "Operation", menu = Operation)
	Operation.add_checkbutton(label = "Hide Operation History Window", command = DisplayOperationHistoryWindow)
	Operation.add_command(label = "Clean Operation History",           command = CLEANHistory)
	Operation.add_command(label = "Reset Parameter to Default Value",  command = ResetDefaultParameter)
	Operation.add_separator()
	Operation.add_command(label = "Reset Window Position",             command = ResetWindowPosition)
	Operation.add_separator()
	Operation.add_command(label = "Exit", command = EXITAPP)
	#		Test Process
	TestProcess = Menu(wControlPanel)
	MenuBar.add_cascade(label = "Test Process", menu = TestProcess)
	TestProcess.add_command(label = "Stop Process Testing", command = CleanQueue)
	TestProcess.add_separator()
	TestProcess.add_command(label = "Brightness -> Increase", command = lambda: BrightnessProcess(0))
	TestProcess.add_command(label = "Brightness -> Decrease", command = lambda: BrightnessProcess(1))
	TestProcess.add_separator()
	TestProcess.add_command(label = "Contrast   -> Increase", command = lambda: ContrastProcess(0))
	TestProcess.add_command(label = "Contrast   -> Decrease", command = lambda: ContrastProcess(1))
	TestProcess.add_separator()
	TestProcess.add_command(label = "Rotation   -> Once",     command = RotationPerTime)
	TestProcess.add_command(label = "Rotation   -> Process",  command = RotationProcess)
	TestProcess.add_separator()
	TestProcess.add_command(label = "Mirror     -> Once",     command = MirrorPerTime)
	TestProcess.add_command(label = "Mirror     -> Process",  command = MirrorProcess)
	TestProcess.add_separator()
	TestProcess.add_command(label = "Workflow",               command = Workflow)
	#		Help
	HelpMenu = Menu(MenuBar, tearoff = 0)
	MenuBar.add_cascade(label = "Help", menu = HelpMenu)
	HelpMenu.add_command(label = " Keyboard Shortcut Keys", command = lambda: showinfo("", ShortcutsInfo))
	HelpMenu.add_separator()
	HelpMenu.add_command(label = "ACQSDK.DLL -> Version",   command = lambda: showinfo("", "ACQSDK.DLL -> %s" % ACQSDKDLL_FileVersion()))
	#	Display Menu
	wControlPanel.config(menu = MenuBar)

	#	GUI Definition: Property
	ButtonWidth = 20
	EntryWidth = 23

	#	Group: Basic
	BasicFrameRow = 0
	BasicFrame = LabelFrame(wControlPanel, text = "Basic Function", width = 400)
	BasicFrame.grid(row = BasicFrameRow, column = 0, columnspan = 3)
	Button(BasicFrame, text = "Set Log Path",   width = ButtonWidth, command = ACQSDK_SetLogPath)  .grid(row = BasicFrameRow,      column = 0)
	global LogPathInput
	LogPathInput = Entry(BasicFrame, bd = 2, width = EntryWidth*2 + 2)
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
	QueryFrame = LabelFrame(wControlPanel,  text = "Information Query")
	QueryFrame.grid(row = QueryFrameRow, column = 0, columnspan = 3)
	Button(QueryFrame, text = "Query Device",      width = ButtonWidth, command = ACQSDK_QueryDeviceInfo)   .grid(row = QueryFrameRow, column = 0)
	Button(QueryFrame, text = "Query SDK Version", width = ButtonWidth, command = ACQSDK_GetSDKVersion)     .grid(row = QueryFrameRow, column = 1)
	Button(QueryFrame, text = "Query FW Version",  width = ButtonWidth, command = ACQSDK_GetFirmwareVersion).grid(row = QueryFrameRow, column = 2)

	#	Group: Firmware Upgrade
	FirmwareUpgradeFrameRow = 20
	FirmwareUpgradeFrame = LabelFrame(wControlPanel,  text = "Firmware Upgrade")
	FirmwareUpgradeFrame.grid(row = FirmwareUpgradeFrameRow, column = 0, columnspan = 3)
	Button(FirmwareUpgradeFrame, text = "Abort Upgrade", width = ButtonWidth, command = ACQSDK_AbortUpgrade)   .grid(row = FirmwareUpgradeFrameRow, column = 0)
	Button(FirmwareUpgradeFrame, text = "Upgrade FW",    width = ButtonWidth, command = ACQSDK_UpgradeFirmware).grid(row = FirmwareUpgradeFrameRow, column = 1)
	Placeholder = Button(FirmwareUpgradeFrame, text = "FW Upgrade Test",   width = ButtonWidth)
	Placeholder.grid(row = FirmwareUpgradeFrameRow, column = 2)
	Placeholder.config(state = "disabled")

	#	Group: Mirror and Rotation
	MirrorRotationFrameRow = 30
	MirrorRotationFrame = LabelFrame(wControlPanel,  text = "Mirror & Rotation")
	MirrorRotationFrame.grid(row = MirrorRotationFrameRow, column = 0, columnspan = 3)
	Label(MirrorRotationFrame, text = "Fetch Setting").grid(row = MirrorRotationFrameRow, column = 0)
	Label(MirrorRotationFrame, text = "Apply Setting").grid(row = MirrorRotationFrameRow, column = 1)
	Label(MirrorRotationFrame, text = " <- Value")    .grid(row = MirrorRotationFrameRow, column = 2)
	Button(MirrorRotationFrame, text = "Get Mirror Flag", width = ButtonWidth, anchor = W, command = ACQSDK_GetMirrorFlag)         .grid(row = MirrorRotationFrameRow + 1, column = 0)
	Button(MirrorRotationFrame, text = "Set Mirror Flag", width = ButtonWidth, anchor = W, command = ACQSDK_SetMirrorFlag)         .grid(row = MirrorRotationFrameRow + 1, column = 1)
	global MirrorInput
	MirrorInput = Entry(MirrorRotationFrame, bd = 2, width = EntryWidth)
	MirrorInput                                                                                                                    .grid(row = MirrorRotationFrameRow + 1, column = 2, padx = 3)
	Button(MirrorRotationFrame, text = "Get Rotation Flag", width = ButtonWidth, anchor = W, command = ACQSDK_GetRotationFlag)     .grid(row = MirrorRotationFrameRow + 2, column = 0)
	Button(MirrorRotationFrame, text = "Set Rotation Flag", width = ButtonWidth, anchor = W, command = ACQSDK_SetRotationFlag)     .grid(row = MirrorRotationFrameRow + 2, column = 1)
	global RotationInput
	RotationInput = Entry(MirrorRotationFrame, bd = 2, width = EntryWidth)
	RotationInput                                                                                                                  .grid(row = MirrorRotationFrameRow + 2, column = 2, padx = 3)
	#		The following two buttons are added for Rotation APIs
	Button(MirrorRotationFrame, text = "Set to 640*480", width = ButtonWidth, command = lambda: ResetLiveVideoWindowSize(640, 480)).grid(row = MirrorRotationFrameRow + 3, column = 1)
	Button(MirrorRotationFrame, text = "Set to 480*640", width = ButtonWidth, command = lambda: ResetLiveVideoWindowSize(480, 640)).grid(row = MirrorRotationFrameRow + 3, column = 2)
	#		Refresh Window and set window size
	Button(MirrorRotationFrame, text = "Update LiveVideo Size",        width = ButtonWidth, command = ChangeLiveVideoSize)         .grid(row = MirrorRotationFrameRow + 4, column = 1)
	Button(MirrorRotationFrame, text = "Refresh LiveVideo Window",     width = ButtonWidth, command = ACQSDK_OnUpdateLiveWnd)      .grid(row = MirrorRotationFrameRow + 4, column = 2)

	#	Group: Handpiece Common Configuration
	CommonConfigurationFrameRow = 40
	CommonConfigurationFrame = LabelFrame(wControlPanel,  text = "HP Configuration")
	CommonConfigurationFrame.grid(row = CommonConfigurationFrameRow, column = 0, columnspan = 3)
	Label(CommonConfigurationFrame, text = "Fetch Setting").grid(row = CommonConfigurationFrameRow, column = 0)
	Label(CommonConfigurationFrame, text = "Apply Setting").grid(row = CommonConfigurationFrameRow, column = 1)
	Label(CommonConfigurationFrame, text = " <- Value")    .grid(row = CommonConfigurationFrameRow, column = 2)
	Button(CommonConfigurationFrame, text = "Get Brightness",          width = ButtonWidth, anchor = W, command = ACQSDK_GetBrightness        ).grid(row = CommonConfigurationFrameRow + 1, column = 0)
	Button(CommonConfigurationFrame, text = "Set Brightness",          width = ButtonWidth, anchor = W, command = ACQSDK_SetBrightness        ).grid(row = CommonConfigurationFrameRow + 1, column = 1)
	Button(CommonConfigurationFrame, text = "Get Contrast",            width = ButtonWidth, anchor = W, command = ACQSDK_GetContrast          ).grid(row = CommonConfigurationFrameRow + 2, column = 0)
	Button(CommonConfigurationFrame, text = "Set Contrast",            width = ButtonWidth, anchor = W, command = ACQSDK_SetContrast          ).grid(row = CommonConfigurationFrameRow + 2, column = 1)
	Button(CommonConfigurationFrame, text = "Get Frequency",           width = ButtonWidth, anchor = W, command = ACQSDK_GetPowerlineFrequency).grid(row = CommonConfigurationFrameRow + 3, column = 0)
	Button(CommonConfigurationFrame, text = "Set Frequency",           width = ButtonWidth, anchor = W, command = ACQSDK_SetPowerlineFrequency).grid(row = CommonConfigurationFrameRow + 3, column = 1)
	Button(CommonConfigurationFrame, text = "Get Sleep Status",        width = ButtonWidth, anchor = W, command = ACQSDK_GetEnableSleep       ).grid(row = CommonConfigurationFrameRow + 4, column = 0)
	Button(CommonConfigurationFrame, text = "Set Sleep",               width = ButtonWidth, anchor = W, command = ACQSDK_SetEnableSleep       ).grid(row = CommonConfigurationFrameRow + 4, column = 1)
	Button(CommonConfigurationFrame, text = "Get Sleep Time",          width = ButtonWidth, anchor = W, command = ACQSDK_GetSleepTime         ).grid(row = CommonConfigurationFrameRow + 5, column = 0)
	Button(CommonConfigurationFrame, text = "Set Sleep Time",          width = ButtonWidth, anchor = W, command = ACQSDK_SetSleepTime         ).grid(row = CommonConfigurationFrameRow + 5, column = 1)
	Button(CommonConfigurationFrame, text = "Get AutoPowerOn Status",  width = ButtonWidth, anchor = W, command = ACQSDK_GetEnableAutoPowerOn ).grid(row = CommonConfigurationFrameRow + 6, column = 0)
	Button(CommonConfigurationFrame, text = "Set AutoPowerOn",         width = ButtonWidth, anchor = W, command = ACQSDK_EnableAutoPowerOn    ).grid(row = CommonConfigurationFrameRow + 6, column = 1)
	Button(CommonConfigurationFrame, text = "Get AutoPowerOff Status", width = ButtonWidth, anchor = W, command = ACQSDK_GetEnableAutoPowerOff).grid(row = CommonConfigurationFrameRow + 7, column = 0)
	Button(CommonConfigurationFrame, text = "Set AutoPowerOff",        width = ButtonWidth, anchor = W, command = ACQSDK_EnableAutoPowerOff   ).grid(row = CommonConfigurationFrameRow + 7, column = 1)
	Button(CommonConfigurationFrame, text = "Get AutoPowerOff Time",   width = ButtonWidth, anchor = W, command = ACQSDK_GetAutoPowerOffTime  ).grid(row = CommonConfigurationFrameRow + 8, column = 0)
	Button(CommonConfigurationFrame, text = "Set AutoPowerOff Time",   width = ButtonWidth, anchor = W, command = ACQSDK_SetAutoPowerOffTime  ).grid(row = CommonConfigurationFrameRow + 8, column = 1)
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
	BrightnessInput         .grid(row = CommonConfigurationFrameRow + 1, column = 2, padx = 3)
	ContrastInput           .grid(row = CommonConfigurationFrameRow + 2, column = 2, padx = 3)
	FrequencyInput          .grid(row = CommonConfigurationFrameRow + 3, column = 2, padx = 3)
	SetSleepInput           .grid(row = CommonConfigurationFrameRow + 4, column = 2, padx = 3)
	SleepTimeInput          .grid(row = CommonConfigurationFrameRow + 5, column = 2, padx = 3)
	SetAutoPowerOnInput     .grid(row = CommonConfigurationFrameRow + 6, column = 2, padx = 3)
	SetAutoPowerOffInput    .grid(row = CommonConfigurationFrameRow + 7, column = 2, padx = 3)
	AutoPowerOffTimeInput   .grid(row = CommonConfigurationFrameRow + 8, column = 2, padx = 3)
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
	wLogger.geometry("600x800")
	global pLogger
	pLogger = ScrolledText(wLogger, width = 50, height = 30, font = ("Courier New", 10), bg = "grey")
	pLogger.pack(fill = BOTH, expand = 1)
	wLogger.update()
	wLogger.withdraw()

# Customized events
#	Windows' events
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
	x = (wLogger.winfo_screenwidth() - status[0] - 16)
	wLogger.geometry("+%d+%d" % (x, 0))
	wLogger.update()
	if wLogger.state() == "withdrawn": wLogger.deiconify()
def ResetLiveVideoWindowSize(width, height):
	wLiveVideo.geometry("%dx%d" % (width, height))
	wLiveVideo.update()
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
# 	Logger's event
def CheckResult(ret):
	print "Result Received -> %r" % (str(ret)) # For Debug
	Logger("%s" % str(ret))
	if isinstance(ret[1], str) or ret[1] == None: return
	elif isinstance(ret[1], tuple): retValue = ret[1][0]
	elif isinstance(ret[1], int): retValue = ret[1]
	else: return
	retValue = hex(retValue)
	if retValue >= 0xf0001:
		try: Logger("\tError -> %s" % GD.OPERATOR_ERROR[str(retValue).upper()])
		except: return
	else: return
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
#	Others
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
	LogPathInput         .insert(0, "./Output")
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
def OpenDirectory(location = r"."):
	if location == r".":            os.system(r"explorer.exe %s" % ".")
	elif os.path.exists(location):  os.system(r"explorer.exe %s" % location)
	else:                           return
def KillProcess(process = "python.exe"): os.system("TASKKILL /F /IM %s" % process)
def MonitorKey(event):
	if event.char == "c": ACQSDK_Capture()
	if event.char == "r": ACQSDK_StartRecord()
	if event.char == "R": ACQSDK_StopRecord()

# ========== SDK's API ==========
# Start
#	Basic Function
def ACQSDK_Init():
	global Initiated
	ret = SDKAPI.ACQSDK_Init(objACQSDK_CSDevice, hWnd)
	Initiated = True
	CheckResult(ret)
def ACQSDK_UnInit():
	global Initiated
	ret = SDKAPI.ACQSDK_UnInit(objACQSDK_CSDevice)
	Initiated = False
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
	path = LogPathInput.get()
	Logger("Received Parameter -> %r" % path)
	path = r"%s/%s.avi" % (path, time.strftime('%Y-%m-%d-%H-%M-%S'))
	ret = SDKAPI.ACQSDK_StartRecord(objACQSDK_CSDevice, path)
	CheckResult(ret)
def ACQSDK_StopRecord():
	ret = SDKAPI.ACQSDK_StopRecord(objACQSDK_CSDevice)
	CheckResult(ret)
def ACQSDK_Capture():
	if Initiated == True:
		class SWCapture(threading.Thread):
			def __init__(self, path):
				threading.Thread.__init__(self)
				self.path = path
			def run(self):
				self.pImageUnit = win32com.client.Dispatch(GD.ACQSDK_ASImageUnit_ProgID)
				self.ret        = SDKAPI.ACQSDK_Capture(objACQSDK_CSDevice, self.pImageUnit)
				CheckResult(self.ret)
				if self.ret[1] == 0:
					self.img = self.pImageUnit.get_white_image()
					Logger(" >> ACQSDK_Capture -> get_white_image: %r" % self.img)
					self.img_file = time.strftime('%Y-%m-%d-%H-%M-%S') + "_%s" % self.getName()
					self.save_image_ret = self.pImageUnit.save_image(r"%s/%s" % (self.path, self.img_file), self.img)
					Logger(" >> ACQSDK_Capture -> save_image: %r, %s" % (self.save_image_ret, self.getName()))
					Logger(" >> ACQSDK_Capture -> free_image: %r" % self.pImageUnit.free_image(self.img))
					Logger(" >> ACQSDK_Capture -> free_unit:  %r" % self.pImageUnit.free_unit())
				del self.pImageUnit
		path = LogPathInput.get()
		Logger("Received Parameter -> %r" % path)
		instance = SWCapture(path)
		instance.setDaemon(True)
		instance.start()
	else:
		pImageUnit = win32com.client.Dispatch(GD.ACQSDK_ASImageUnit_ProgID)
		ret        = SDKAPI.ACQSDK_Capture(objACQSDK_CSDevice, pImageUnit)
		CheckResult(ret)
def ACQSDK_GetImageData():
	if Initiated == True:
		class HWCapture(threading.Thread):
			def __init__(self, path):
				threading.Thread.__init__(self)
				self.path = path
			def run(self):
				self.pImageUnit = win32com.client.Dispatch(GD.ACQSDK_ASImageUnit_ProgID)
				self.ret        = SDKAPI.ACQSDK_GetImageData(objACQSDK_CSDevice, self.pImageUnit)
				CheckResult(self.ret)
				if self.ret[1] == 0:
					self.img = self.pImageUnit.get_white_image()
					Logger(" >> ACQSDK_GetImageData -> get_white_image: %r" % self.img)
					self.img_file = time.strftime('%Y-%m-%d-%H-%M-%S') + "_%s" % self.getName()
					self.save_image_ret = self.pImageUnit.save_image(r"%s/%s" % (self.path, self.img_file), self.img)
					Logger(" >> ACQSDK_GetImageData -> save_image: %r, %s" % (self.save_image_ret, self.getName()))
					Logger(" >> ACQSDK_GetImageData -> free_image: %r" % self.pImageUnit.free_image(self.img))
					Logger(" >> ACQSDK_GetImageData -> free_unit:  %r"  % self.pImageUnit.free_unit())
				del self.pImageUnit
		path = LogPathInput.get()
		Logger("Received Parameter -> %r" % path)
		instance = HWCapture(path)
		#instance.setDaemon(True)
		instance.start()
	else:
		pImageUnit = win32com.client.Dispatch(GD.ACQSDK_ASImageUnit_ProgID)
		ret        = SDKAPI.ACQSDK_GetImageData(objACQSDK_CSDevice, pImageUnit)
		CheckResult(ret)
def ACQSDK_SetLogPath():
	path = LogPathInput.get()
	Logger("Received Parameter -> %r" % path)
	ret  = SDKAPI.ACQSDK_SetLogPath(objACQSDK_CSDevice, path)
	CheckResult(ret)
#	Mirror & Rotation
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
#	Query
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
#	Configuration
#	>> Brightness
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
#	>> Contrast
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
#	>> Powerline Frequency
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
#	>> Sleep
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
#	>> Auto Power On
def ACQSDK_EnableAutoPowerOn():
	bEnable = int(SetAutoPowerOnInput.get())
	Logger("Received Parameter -> %r" % bEnable)
	ret = SDKAPI.ACQSDK_EnableAutoPowerOn(objACQSDK_CSDevice, bEnable)
	CheckResult(ret)
def ACQSDK_GetEnableAutoPowerOn():
	ret = SDKAPI.ACQSDK_GetEnableAutoPowerOn(objACQSDK_CSDevice)
	CheckResult(ret)
#	>> Auto Power Off
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
#	Firmware
def ACQSDK_UpgradeFirmware():
	pFullPathName = askopenfilename()
	if pFullPathName != "":
		class FWUpgrade(threading.Thread):
			def __init__(self):
				threading.Thread.__init__(self)
			def run(self):
				self.ret = SDKAPI.ACQSDK_UpgradeFirmware(objACQSDK_CSDevice, pFullPathName)
				CheckResult(self.ret)
		instance = FWUpgrade()
		instance.start()
	elif pFullPathName == "":
		Logger("ACQSDK_UpgradeFirmware -> No File is selected.")
def ACQSDK_AbortUpgrade():
	ret = SDKAPI.ACQSDK_AbortUpgrade(objACQSDK_CSDevice)
	CheckResult(ret)
# End
# ========== SDK's API ==========

# Callback Class -> CSDevice
class SDKEvents():
	def OnHPEvents(self, Callback):
		i = Callback.QueryInterface(pythoncom.IID_IDispatch)
		objSDKCallbackInfo = win32com.client.Dispatch(i)
		self.EventID = str(hex(objSDKCallbackInfo.get_event_id())).upper()
		self.EventState = "*** SDK Callback -> %s" % self.EventID
		try:     self.EventID_Value = GD.Callback_MsgType[self.EventID]
		except:  self.EventID_Value = "NOT DEFINED"
		if self.EventID == "0X200005": ACQSDK_GetImageData()
		if self.EventID == "0X200003":
			self.percent = objSDKCallbackInfo.get_fw_upgrade_percent()
			self.EventID_Value = self.EventID_Value + " -> %d%%" % self.percent
		Logger("\t%s -> %s" % (self.EventState, self.EventID_Value))

# ========== Test Process ==========
# Begin
def CleanQueue():
	global EventQueue
	EventQueue = []
def BrightnessProcess(typeid):
	#0: "INCREASE"
	#1: "DECREASE":
	global EventQueue
	if   typeid == 0: sequence = [1,2,3,4,5,6,7]
	elif typeid == 1: sequence = [7,6,5,4,3,2,1]
	else: return
	for i in sequence:
		EventQueue.append(("LOGGER", "Change Brightness to %d" % i))
		EventQueue.append(("ACQSDK_SetBrightness", i))
def ContrastProcess(typeid):
	#0: "INCREASE"
	#1: "DECREASE":
	global EventQueue
	if   typeid == 0: sequence = [1,2,3,4,5,6,7]
	elif typeid == 1: sequence = [7,6,5,4,3,2,1]
	else: return
	for i in sequence:
		EventQueue.append(("LOGGER", "Change Contrast to %d" % i))
		EventQueue.append(("ACQSDK_SetContrast", i))
def RotationPerTime():
	global EventQueue
	ret = SDKAPI.ACQSDK_GetRotationFlag(objACQSDK_CSDevice)
	if   ret[1] == 0:
		EventQueue.append(("LOGGER", "Change Rotation to 90"))
		EventQueue.append(("ACQSDK_SetRotationFlag", 90))
	elif ret[1] == 1:
		EventQueue.append(("LOGGER", "Change Rotation to 180"))
		EventQueue.append(("ACQSDK_SetRotationFlag", 180))
	elif ret[1] == 2:
		EventQueue.append(("LOGGER", "Change Rotation to 270"))
		EventQueue.append(("ACQSDK_SetRotationFlag", 270))
	elif ret[1] == 3:
		EventQueue.append(("LOGGER", "Change Rotation to 0"))
		EventQueue.append(("ACQSDK_SetRotationFlag", 0))
	else: Logger("\t<-> GUI Callback -> Fail to fetch Rotation Flag...")
def RotationProcess():
	global EventQueue
	EventQueue.append(("LOGGER", "Change Rotation to 90"))
	EventQueue.append(("ACQSDK_SetRotationFlag", 90))
	EventQueue.append(("LOGGER", "Change Rotation to 180"))
	EventQueue.append(("ACQSDK_SetRotationFlag", 180))
	EventQueue.append(("LOGGER", "Change Rotation to 270"))
	EventQueue.append(("ACQSDK_SetRotationFlag", 270))
	EventQueue.append(("LOGGER", "Change Rotation to 0"))
	EventQueue.append(("ACQSDK_SetRotationFlag", 0))
def MirrorPerTime():
	global EventQueue
	ret = SDKAPI.ACQSDK_GetMirrorFlag(objACQSDK_CSDevice)
	if   ret[1] == 0:
		EventQueue.append(("LOGGER", "Change Mirror to 1"))
		EventQueue.append(("ACQSDK_SetMirrorFlag", 1))
	elif ret[1] == 1:
		EventQueue.append(("LOGGER", "Change Mirror to 0"))
		EventQueue.append(("ACQSDK_SetMirrorFlag", 0))
def MirrorProcess():
	global EventQueue
	for i in [1,2]:
		EventQueue.append(("LOGGER", "Change Mirror to 1"))
		EventQueue.append(("ACQSDK_SetMirrorFlag", 1))
		EventQueue.append(("LOGGER", "Change Mirror to 0"))
		EventQueue.append(("ACQSDK_SetMirrorFlag", 0))
def Workflow(): pass
	# Workflow shall be,
	# Init
	# StartPlay
	# >>Loop: times?
	# Capture
	# StartRecord
	# Capture
	# StopRecord
	# >>LoopDone

def WorkflowMonitor(): pass
	# Make the Workflow work as loop type
def MessageQueue():
	global EventQueue
	if len(EventQueue) != 0:
		cmd = EventQueue[0]
		if   cmd[0] == "ACQSDK_SetBrightness":
			SDKAPI.ACQSDK_SetBrightness(objACQSDK_CSDevice, cmd[1])
			time.sleep(2)
		elif cmd[0] == "ACQSDK_SetContrast":
			SDKAPI.ACQSDK_SetContrast(objACQSDK_CSDevice, cmd[1])
			time.sleep(2)
		elif cmd[0] == "ACQSDK_SetRotationFlag":
			if   cmd[1] == 0  or cmd[1] == 180: ResetLiveVideoWindowSize(640, 480)
			elif cmd[1] == 90 or cmd[1] == 270: ResetLiveVideoWindowSize(480, 640)
			SDKAPI.ACQSDK_OnUpdateLiveWnd(objACQSDK_CSDevice)
			SDKAPI.ACQSDK_SetRotationFlag(objACQSDK_CSDevice, cmd[1])
			time.sleep(3)
		elif cmd[0] == "ACQSDK_SetMirrorFlag":
			SDKAPI.ACQSDK_SetMirrorFlag(objACQSDK_CSDevice, cmd[1])
			time.sleep(2)
		elif cmd[0] == "LOGGER":
			Logger("\t<-> GUI Callback -> %s" % cmd[1])
			time.sleep(1)
		EventQueue.pop(0) # Ignore action which is not defined
	wControlPanel.after(100, MessageQueue)
# End
# ========== Test Process ==========

# >>Body<<
# Location
try:     ACQSDK_DLL_Dir = os.environ.get("CommonProgramFiles(x86)") + "\\Trophy\\Acquisition\\AcqSdk\\"
except:  ACQSDK_DLL_Dir = os.environ.get("CommonProgramFiles") + "\\Trophy\\Acquisition\\AcqSdk\\"
finally: ACQSDK_DLL     = ACQSDK_DLL_Dir + "ACQSDK.DLL"

# Logger: Output file's name
LoggerOutput = r"./Output/AcqTaurus_GUIOperationLogger.log"

# Flag of Init :: If Init is not executed, EXITAPP function will not execute UnInit.
Initiated = False

# Flag of Operation History Window
#	Display
DisplayOperationHistoryWindowFlag = True
#	Line Number
OperationHistoryWindowLineFlag = 0    # 0: Not Display by default
OperationHistoryWindowLineMax  = 3000 # If number is more than 3000, clean the content in window

# Information Label
InfoLabel     = "Test Application of UVC Camera SDK built by ActivePython 2.7 (x86)"
ShortcutsInfo = """
        c\tCapture
        r\tStart Record
        R\tStop Record
"""

# Generate GUI elements for three window
#	Size of Live Video window
LiveVideo_Width  = "640"
LiveVideo_Height = "480"
#	Generate GUI
GenerateGUI()

# Create COM object and Event
try: objACQSDK_CSDevice = win32com.client.DispatchWithEvents(GD.ACQSDK_CSDevice_ProgID, SDKEvents)
except: print "Fail to create COM object."

# Event Queue
EventQueue = []

# Event after window has displayed
wControlPanel.after(500,  ResetWindowPosition)
wControlPanel.after(1000, MessageQueue)

# Display GUI and wait message
mainloop()
