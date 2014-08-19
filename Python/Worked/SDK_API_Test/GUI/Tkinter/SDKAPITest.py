'''
    GUI: Quick Checking on SDK's API

    History:
        2014-02-18      0.1       First version
                                    Notes: Some APIs are not ready.
        2014-03-26      0.2       Update new APIs
                                    Notes: Used @Windows7 64bit ENU
        2014-07-23      0.3       Update new APIs, refine code and change UI setting
                                    Notes: Used @Windows7 64bit ENU
        2014-08-01      0.4       Update the name of this script and add serial module
'''



import os, sys, time, datetime, threading
import win32com.client, win32api
import _winreg
import pythoncom
from Tkinter import *
from ScrolledText import ScrolledText
from tkFileDialog import *
from tkMessageBox import *
try:
    sys.path.append(r'../../Module')
    import TestACQSDK_Module_Global_Definition as GD
    import TestACQSDK_Module_Wrapper as SDKAPI
except:
    print 'Expected module files are not imported successfully.'
    sys.exit(1)



# Generate GUI
def GenerateGUI():
    # Create Tkinter windows
    # GUI : Workflow
    global wControlPanel, wLiveVideo, wLogger
    wControlPanel = Tk() # List buttons
    wLiveVideo    = Tk() # Display Live Window
    wLogger       = Tk() # Logger Window

    # Hide all windows at first
    wControlPanel.withdraw()
    wLiveVideo.withdraw()
    wLogger.withdraw()

    # Handler of the wLiveVideo
    global hWnd
    hWnd = wLiveVideo.winfo_id()

    # GUI Configuration
    GenerateLogger()
    GenerateControlPanel()
    GenerateLiveVideo()

    # Bind customized event
    wControlPanel.bind('<F11>', lambda x: KillProcess())
    wControlPanel.bind('<Key>', MonitorKey)
    wLiveVideo   .bind('<F11>', lambda x: KillProcess())
    wLiveVideo   .bind('<Key>', MonitorKey)
    wLogger      .bind('<F11>', lambda x: KillProcess())
    wLogger      .bind('<Key>', MonitorKey)
    wControlPanel.bind('<F12>', lambda x: OpenDirectory())
    wLiveVideo   .bind('<F9>',  lambda x: MirrorPerTime())
    wLiveVideo   .bind('<F10>', lambda x: RotationPerTime())

    # Trace window's event: DELETE
    wControlPanel.protocol('WM_DELETE_WINDOW', EXITAPP)

    # No response when trying to close Live Video's window
    wLiveVideo.protocol('WM_DELETE_WINDOW', lambda: 0)

    # No response when trying to close Logger's window
    wLogger.protocol('WM_DELETE_WINDOW', lambda: 0)
def GenerateControlPanel():
    #    Panel
    wControlPanel.title('SDK Testing: Control Panel')
    wControlPanel.resizable(width = False, height = False)

    #    Add Menu
    MenuBar = Menu(wControlPanel)

    #        Operation
    Operation = Menu(MenuBar, tearoff = 0)
    MenuBar.add_cascade(label = 'Operation', menu = Operation)
    Operation.add_command(label = 'Clean Operation History', command = CLEANHistory)

    if DebugMode == 1:
        Operation.add_command(label = 'Reset Parameter to Default Value', command = ResetDefaultParameter)
        Operation.add_separator()

    Operation.add_command(label = 'Capture Frame from AVI File...', command = ACQSDK_GrabFrameFromMovie)
    Operation.add_separator()
    Operation.add_command(label = 'Reset Window Position', command = ResetWindowPosition)
    Operation.add_separator()
    Operation.add_command(label = 'Exit', command = EXITAPP)

    if DebugMode == 1:
        #        Test Process
        TestProcess = Menu(wControlPanel)
        MenuBar.add_cascade(label = 'Test Process', menu = TestProcess)
        TestProcess.add_command(label = 'Stop Process Testing', command = CleanQueue)
        TestProcess.add_separator()
        TestProcess.add_command(label = 'Brightness -> Increase', command = lambda: BrightnessProcess(0))
        TestProcess.add_command(label = 'Brightness -> Decrease', command = lambda: BrightnessProcess(1))
        TestProcess.add_separator()
        TestProcess.add_command(label = 'Contrast   -> Increase', command = lambda: ContrastProcess(0))
        TestProcess.add_command(label = 'Contrast   -> Decrease', command = lambda: ContrastProcess(1))
        TestProcess.add_separator()
        TestProcess.add_command(label = 'Rotation   -> Once', command = RotationPerTime)
        TestProcess.add_command(label = 'Rotation   -> Process', command = RotationProcess)
        TestProcess.add_separator()
        TestProcess.add_command(label = 'Mirror      -> Once', command = MirrorPerTime)
        TestProcess.add_command(label = 'Mirror      -> Process', command = MirrorProcess)

    #        Help
    HelpMenu = Menu(MenuBar, tearoff = 0)
    MenuBar.add_cascade(label = 'Help', menu = HelpMenu)
    HelpMenu.add_command(label = 'Keyboard Shortcut Keys ', command = lambda: showinfo('', ShortcutsInfo))
    HelpMenu.add_separator()
    HelpMenu.add_command(label = 'ACQSDK.DLL -> Version ', command = lambda: showinfo('', 'ACQSDK.DLL -> {}'.format(ACQSDKDLL_FileVersion())))

    #    Display Menu
    wControlPanel.config(menu = MenuBar)

    #    GUI Definition: Property
    global ButtonWidth, EntryWidth
    ButtonWidth  = 20
    EntryWidth   = 23

    #    Group: Basic
    BasicFrameRow = 0
    BasicFrame = LabelFrame(wControlPanel, text = 'Basic Function', width = 400)
    BasicFrame.grid(row = BasicFrameRow, column = 0, columnspan = 3)
    Button(BasicFrame, text = 'Set Log Path', width = ButtonWidth, command = ACQSDK_SetLogPath).grid(row = BasicFrameRow, column = 0)
    global LogPathInput
    LogPathInput = Entry(BasicFrame, bd = 2, width = EntryWidth*2+2)
    LogPathInput.grid(row = BasicFrameRow, column = 1, columnspan = 2)
    LogPathInput.insert(0, r'{}\Output'.format(os.getcwd()))
    Button(BasicFrame, text = 'Init', width = ButtonWidth, command = ACQSDK_Init).grid(row = BasicFrameRow+1, column = 1)
    Button(BasicFrame, text = 'UnInit', width = ButtonWidth, command = ACQSDK_UnInit).grid(row = BasicFrameRow+1, column = 2)
    Button(BasicFrame, text = 'Start Play', width = ButtonWidth, command = ACQSDK_StartPlay).grid(row = BasicFrameRow+2, column = 1)
    Button(BasicFrame, text = 'Stop Play', width = ButtonWidth, command = ACQSDK_StopPlay).grid(row = BasicFrameRow+2, column = 2)
    Button(BasicFrame, text = 'Pause Play', width = ButtonWidth, command = ACQSDK_PausePlay).grid(row = BasicFrameRow+3, column = 1)
    Button(BasicFrame, text = 'Resume Play', width = ButtonWidth, command = ACQSDK_ResumePlay).grid(row = BasicFrameRow+3, column = 2)
    Button(BasicFrame, text = 'Capture', width = ButtonWidth, command = ACQSDK_SendCaptureCmd).grid(row = BasicFrameRow+4, column = 1)
    Button(BasicFrame, text = 'Start Record', width = ButtonWidth, command = ACQSDK_StartRecord).grid(row = BasicFrameRow+5, column = 1)
    Button(BasicFrame, text = 'Stop Record', width = ButtonWidth, command = ACQSDK_StopRecord).grid(row = BasicFrameRow+5, column = 2)

    #    Firmware Upgrade
    GenerateFirmwareUpgrade(wControlPanel, 20)

    #    Frames for testing
    if DebugMode == 1:
        GenerateQueryInfoFrame(wControlPanel, 40) # Query Information
        GenerateMirrorRotationFrame(wControlPanel, 60) # Mirror and Rotation
        GenerateHPConfigurationFrame4CS1200(wControlPanel, 80) # For CS1200
        GenerateHPConfigurationFrame4CS1500(wControlPanel, 100) # For CS1500
        GenerateHPConfigurationFrame(wControlPanel, 120) # HP Configuration
        ResetDefaultParameter() # Reset All Parameters

    #    Label: Display label
    AuthorLabelRow = 500
    Label(wControlPanel, text = InfoLabel).grid(row = AuthorLabelRow, column = 0, columnspan = 3, sticky = E+N+S)

    #    Set Window Property
    wControlPanel.update()
def GenerateFirmwareUpgrade(master, StartRow):
    #    Group: Firmware Upgrade
    FirmwareUpgradeFrame = LabelFrame(master,  text = 'Firmware Upgrade')
    FirmwareUpgradeFrame.grid(row = StartRow, column = 0, columnspan = 3)
    Button(FirmwareUpgradeFrame, text = 'Query Device', width = ButtonWidth, command = ACQSDK_QueryDeviceInfo).grid(row = StartRow, column = 0)
    Button(FirmwareUpgradeFrame, text = 'Abort Upgrade', width = ButtonWidth, command = ACQSDK_AbortUpgrade).grid(row = StartRow, column = 1)
    Button(FirmwareUpgradeFrame, text = 'Upgrade FW', width = ButtonWidth, command = ACQSDK_UpgradeFirmware).grid(row = StartRow, column = 2)
def GenerateQueryInfoFrame(master, StartRow):
    #    Group: Query Info
    QueryFrame = LabelFrame(master,  text = 'Information Query')
    QueryFrame.grid(row = StartRow, column = 0, columnspan = 3)
    Button(QueryFrame, text = 'Query Device', width = ButtonWidth, command = ACQSDK_QueryDeviceInfo).grid(row = StartRow, column = 0)
    Button(QueryFrame, text = 'Query SDK Version', width = ButtonWidth, command = ACQSDK_GetSDKVersion).grid(row = StartRow, column = 1)
    Button(QueryFrame, text = 'Query Host Version', width = ButtonWidth, command = ACQSDK_GetHostVersion).grid(row = StartRow, column = 2)
    Button(QueryFrame, text = 'Query FW Version', width = ButtonWidth, command = ACQSDK_GetFirmwareVersion).grid(row = StartRow+1, column = 1)
    Button(QueryFrame, text = 'Query FW Status', width = ButtonWidth, command = ACQSDK_GetFwStatus).grid(row = StartRow+1, column = 2)
def GenerateMirrorRotationFrame(master, StartRow):
    #    Group: Mirror and Rotation
    MirrorRotationFrame = LabelFrame(master, text = 'Mirror & Rotation')
    MirrorRotationFrame.grid(row = StartRow, column = 0, columnspan = 3)
    Label(MirrorRotationFrame, text = 'Fetch Setting').grid(row = StartRow, column = 0)
    Label(MirrorRotationFrame, text = 'Apply Setting').grid(row = StartRow, column = 1)
    Label(MirrorRotationFrame, text = ' <- Value').grid(row = StartRow, column = 2)
    Button(MirrorRotationFrame, text = 'Get Mirror Flag', width = ButtonWidth, anchor = W, command = ACQSDK_GetMirrorFlag).grid(row = StartRow+1, column = 0)
    Button(MirrorRotationFrame, text = 'Set Mirror Flag', width = ButtonWidth, anchor = W, command = ACQSDK_SetMirrorFlag).grid(row = StartRow+1, column = 1)
    global MirrorInput
    MirrorInput = Entry(MirrorRotationFrame, bd = 2, width = EntryWidth)
    MirrorInput.grid(row = StartRow+1, column = 2, padx = 3)
    Button(MirrorRotationFrame, text = 'Get Rotation Flag', width = ButtonWidth, anchor = W, command = ACQSDK_GetRotationFlag).grid(row = StartRow+2, column = 0)
    Button(MirrorRotationFrame, text = 'Set Rotation Flag', width = ButtonWidth, anchor = W, command = ACQSDK_SetRotationFlag).grid(row = StartRow+2, column = 1)
    global RotationInput
    RotationInput = Entry(MirrorRotationFrame, bd = 2, width = EntryWidth)
    RotationInput.grid(row = StartRow+2, column = 2, padx = 3)

    #        The following two buttons are added for Rotation APIs
    Button(MirrorRotationFrame, text = 'Set to 640*480', width = ButtonWidth, command = lambda: ResetLiveVideoWindowSize(640, 480)).grid(row = StartRow+3, column = 1)
    Button(MirrorRotationFrame, text = 'Set to 480*640', width = ButtonWidth, command = lambda: ResetLiveVideoWindowSize(480, 640)).grid(row = StartRow+3, column = 2)

    #        Refresh Window and set window size
    Button(MirrorRotationFrame, text = 'Update LiveVideo Size', width = ButtonWidth, command = ChangeLiveVideoSize).grid(row = StartRow+4, column = 1)
    Button(MirrorRotationFrame, text = 'Refresh LiveVideo Window', width = ButtonWidth,    command = ACQSDK_OnUpdateLiveWnd).grid(row = StartRow+4, column = 2)
def GenerateHPConfigurationFrame4CS1200(master, StartRow):
    #    Group: Handpiece (CS 1200) Configuration
    HPCS1200ConfigurationFrame = LabelFrame(master, text = 'CS1200 Configuration')
    HPCS1200ConfigurationFrame.grid(row = StartRow, column = 0, columnspan = 3)
    Label(HPCS1200ConfigurationFrame, text = 'Fetch Setting').grid(row = StartRow, column = 0)
    Label(HPCS1200ConfigurationFrame, text = 'Apply Setting').grid(row = StartRow, column = 1)
    Label(HPCS1200ConfigurationFrame, text = ' <- Value').grid(row = StartRow, column = 2)
    Button(HPCS1200ConfigurationFrame, text = 'Get AutoPowerOn Status', width = ButtonWidth, anchor = W, command = ACQSDK_GetEnableAutoPowerOn).grid(row = StartRow+1, column = 0)
    Button(HPCS1200ConfigurationFrame, text = 'Set AutoPowerOn', width = ButtonWidth, anchor = W, command = ACQSDK_EnableAutoPowerOn).grid(row = StartRow+1, column = 1)
    global SetAutoPowerOnInput
    SetAutoPowerOnInput = Entry(HPCS1200ConfigurationFrame, bd = 2, width = EntryWidth)
    SetAutoPowerOnInput.grid(row = StartRow+1, column = 2, padx = 3)
def GenerateHPConfigurationFrame4CS1500(master, StartRow):
    #    Group: Handpiece (CS 1500) Configuration
    HPCS1500ConfigurationFrame = LabelFrame(master, text = 'CS1500 Configuration')
    HPCS1500ConfigurationFrame.grid(row = StartRow, column = 0, columnspan = 3)
    Label(HPCS1500ConfigurationFrame, text = 'Fetch Setting').grid(row = StartRow, column = 0)
    Label(HPCS1500ConfigurationFrame, text = 'Apply Setting').grid(row = StartRow, column = 1)
    Label(HPCS1500ConfigurationFrame, text = ' <- Value').grid(row = StartRow, column = 2)
    Button(HPCS1500ConfigurationFrame, text = 'Get 2Level Capture Status', width = ButtonWidth, anchor = W, command = ACQSDK_Get2LevelCapture).grid(row = StartRow+1, column = 0)
    Button(HPCS1500ConfigurationFrame, text = 'Set 2Level Capture', width = ButtonWidth, anchor = W, command = ACQSDK_Set2LevelCapture).grid(row = StartRow+1, column = 1)
    global Set2LevelCaptureInput
    Set2LevelCaptureInput = Entry(HPCS1500ConfigurationFrame, bd = 2, width = EntryWidth)
    Set2LevelCaptureInput.grid(row = StartRow+1, column = 2, padx = 3)
def GenerateHPConfigurationFrame(master, StartRow):
    #    Group: Handpiece Common Configuration
    HPCommonConfigurationFrame = LabelFrame(master, text = 'HP Configuration')
    HPCommonConfigurationFrame.grid(row = StartRow, column = 0, columnspan = 3)
    Label(HPCommonConfigurationFrame, text = 'Fetch Setting').grid(row = StartRow, column = 0)
    Label(HPCommonConfigurationFrame, text = 'Apply Setting').grid(row = StartRow, column = 1)
    Label(HPCommonConfigurationFrame, text = ' <- Value').grid(row = StartRow, column = 2)
    Button(HPCommonConfigurationFrame, text = 'Get Brightness', width = ButtonWidth, anchor = W, command = ACQSDK_GetBrightness).grid(row = StartRow+1, column = 0)
    Button(HPCommonConfigurationFrame, text = 'Set Brightness', width = ButtonWidth, anchor = W, command = ACQSDK_SetBrightness).grid(row = StartRow+1, column = 1)
    Button(HPCommonConfigurationFrame, text = 'Get Contrast', width = ButtonWidth, anchor = W, command = ACQSDK_GetContrast).grid(row = StartRow+2, column = 0)
    Button(HPCommonConfigurationFrame, text = 'Set Contrast', width = ButtonWidth, anchor = W, command = ACQSDK_SetContrast).grid(row = StartRow+2, column = 1)
    Button(HPCommonConfigurationFrame, text = 'Get Frequency', width = ButtonWidth, anchor = W, command = ACQSDK_GetPowerlineFrequency).grid(row = StartRow+3, column = 0)
    Button(HPCommonConfigurationFrame, text = 'Set Frequency', width = ButtonWidth, anchor = W, command = ACQSDK_SetPowerlineFrequency).grid(row = StartRow+3, column = 1)
    Button(HPCommonConfigurationFrame, text = 'Get Sleep Status', width = ButtonWidth, anchor = W, command = ACQSDK_GetEnableSleep).grid(row = StartRow+4, column = 0)
    Button(HPCommonConfigurationFrame, text = 'Set Sleep', width = ButtonWidth, anchor = W, command = ACQSDK_SetEnableSleep).grid(row = StartRow+4, column = 1)
    Button(HPCommonConfigurationFrame, text = 'Get Sleep Time', width = ButtonWidth, anchor = W, command = ACQSDK_GetSleepTime).grid(row = StartRow+5, column = 0)
    Button(HPCommonConfigurationFrame, text = 'Set Sleep Time', width = ButtonWidth, anchor = W, command = ACQSDK_SetSleepTime).grid(row = StartRow+5, column = 1)
    Button(HPCommonConfigurationFrame, text = 'Get AutoPowerOff Status', width = ButtonWidth, anchor = W, command = ACQSDK_GetEnableAutoPowerOff).grid(row = StartRow+6, column = 0)
    Button(HPCommonConfigurationFrame, text = 'Set AutoPowerOff', width = ButtonWidth, anchor = W, command = ACQSDK_EnableAutoPowerOff).grid(row = StartRow+6, column = 1)
    Button(HPCommonConfigurationFrame, text = 'Get AutoPowerOff Time', width = ButtonWidth, anchor = W, command = ACQSDK_GetAutoPowerOffTime).grid(row = StartRow+7, column = 0)
    Button(HPCommonConfigurationFrame, text = 'Set AutoPowerOff Time', width = ButtonWidth, anchor = W, command = ACQSDK_SetAutoPowerOffTime).grid(row = StartRow+7, column = 1)

    #        Inputbox
    global BrightnessInput, ContrastInput, FrequencyInput
    global SetSleepInput, SleepTimeInput
    global SetAutoPowerOffInput, AutoPowerOffTimeInput
    BrightnessInput = Entry(HPCommonConfigurationFrame, bd = 2, width = EntryWidth)
    ContrastInput = Entry(HPCommonConfigurationFrame, bd = 2, width = EntryWidth)
    FrequencyInput = Entry(HPCommonConfigurationFrame, bd = 2, width = EntryWidth)
    SetSleepInput = Entry(HPCommonConfigurationFrame, bd = 2, width = EntryWidth)
    SleepTimeInput = Entry(HPCommonConfigurationFrame, bd = 2, width = EntryWidth)
    SetAutoPowerOffInput = Entry(HPCommonConfigurationFrame, bd = 2, width = EntryWidth)
    AutoPowerOffTimeInput = Entry(HPCommonConfigurationFrame, bd = 2, width = EntryWidth)
    BrightnessInput.grid(row = StartRow+1, column = 2, padx = 3)
    ContrastInput.grid(row = StartRow+2, column = 2, padx = 3)
    FrequencyInput.grid(row = StartRow+3, column = 2, padx = 3)
    SetSleepInput.grid(row = StartRow+4, column = 2, padx = 3)
    SleepTimeInput.grid(row = StartRow+5, column = 2, padx = 3)
    SetAutoPowerOffInput.grid(row = StartRow+6, column = 2, padx = 3)
    AutoPowerOffTimeInput.grid(row = StartRow+7, column = 2, padx = 3)
def GenerateLiveVideo():
    #    Live Video
    wLiveVideo.geometry('{}x{}'.format(LiveVideo_Width, LiveVideo_Height))
    wLiveVideo.title('SDK Testing: Live Video')
    wLiveVideo.update()
def GenerateLogger():
    #    Logger
    wLogger.title('Operation History')
    # wLogger.geometry('{}x900'.format(wLogger.winfo_screenwidth()/2))
    wLogger.geometry('778x900')
    global pLogger
    pLogger = ScrolledText(wLogger, width = 50, height = 30, font = ('Courier New', 9), bg = 'grey')
    pLogger.pack(fill = BOTH, expand = 1)
    wLogger.update()



# Customized events
#    Windows' events
def WindowState(objWin): return (objWin.winfo_width(), objWin.winfo_height(), objWin.winfo_x(), objWin.winfo_y())
def ResetWindowPosition(init = None):
    # wControlPanel
    wControlPanel.geometry('+5+5')
    wControlPanel.update()

    #    Check status of wControlPanel
    if wControlPanel.state() == 'withdrawn':
        wControlPanel.deiconify()

    # wLogger
    status = WindowState(wLogger)
    x = (WindowState(wControlPanel)[0]+16)
    wLogger.geometry('+%d+%d' % (x, 0))
    wLogger.update()

    #   Check status of wLogger
    if wLogger.state() == 'withdrawn':
        wLogger.deiconify()

    # wLiveVideo
    status = WindowState(wLiveVideo)
    if init is None:
        wLiveVideo.geometry('+%d+%d' % (wLiveVideo.winfo_screenwidth()-status[0]-16, 0))
    elif init == 0:
        wLiveVideo.geometry('+%d+%d' % (wLiveVideo.winfo_screenwidth()-640-16, 0))
    wLiveVideo.update()

    #   Check status of wLiveVideo
    if wLiveVideo.state() == 'withdrawn':
        wLiveVideo.deiconify()
def ResetLiveVideoWindowSize(width, height):
    wLiveVideo.geometry('%dx%d' % (width, height))
    wLiveVideo.update()
def ChangeLiveVideoSize():
    status = WindowState(wLiveVideo)
    if status[0] != 640:
        wLiveVideo.geometry('%dx%d' % (status[0], status[0] * 0.75))
        wLiveVideo.update()
def EXITAPP():
    if Initiated == True: objACQSDK_CSDevice.ACQSDK_UnInit()
    wControlPanel.quit()

#     Logger's event
def timestamp(): return datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")
def CheckResult(ret):
    print 'Result Received -> %r' % (str(ret))  # For Debug
    Logger('%s' % str(ret))
    if isinstance(ret[1], str) or ret[1] == None:
        return
    elif isinstance(ret[1], tuple):
        retValue = ret[1][0]
    elif isinstance(ret[1], int):
        retValue = ret[1]
    else:
        return
    retValue = hex(retValue)
    if retValue == 0x0 or retValue >= 0xf0000:
        try:
            Logger('\t\tParse Return Value -> {}'.format(GD.OPERATOR_ERROR[str(retValue).upper()]))
        except:
            return
    else:
        return
def Logger(strLine):
    global EventQueue
    EventQueue.append(
        ('LoggerWin', '[%s] %s\n' % (time.strftime('%H:%M:%S'), str(strLine))))
def CLEANHistory(): pLogger.delete('1.0', END)
def ACQSDKDLL_FileVersion():
    try:
        DLL_VerInfo = win32api.GetFileVersionInfo(ACQSDK_DLL, '\\')
        ms = DLL_VerInfo['FileVersionMS']
        ls = DLL_VerInfo['FileVersionLS']
        return '{}.{}.{}.{}'.format(win32api.HIWORD(ms), win32api.LOWORD(ms), win32api.HIWORD(ls), win32api.LOWORD(ls))
    except:
        return 'NOT FOUND'
def ResetDefaultParameter():
    # Clean
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
    Set2LevelCaptureInput.delete(0, END)

    # Input: Default value
    MirrorInput          .insert(0, '1')
    RotationInput        .insert(0, '90')
    BrightnessInput      .insert(0, '4')
    ContrastInput        .insert(0, '4')
    FrequencyInput       .insert(0, '50')
    SetSleepInput        .insert(0, '0')
    SleepTimeInput       .insert(0, '60')
    SetAutoPowerOnInput  .insert(0, '0')
    SetAutoPowerOffInput .insert(0, '0')
    AutoPowerOffTimeInput.insert(0, '7200')
    Set2LevelCaptureInput.insert(0, '0')
def OpenDirectory(location = r'.'):
    if location == r'.':
        os.system(r'explorer.exe %s' % '.')
    elif os.path.exists(location):
        os.system(r'explorer.exe %s' % location)
    else:
        return
def KillProcess(process = 'python.exe'): os.system('TASKKILL /F /IM {}'.format(process))
def MonitorKey(event):
    if event.char == 'c': ACQSDK_SendCaptureCmd()
    if event.char == 'r': ACQSDK_StartRecord()
    if event.char == 'R': ACQSDK_StopRecord()



# ========== SDK's API ==========
# Start
#    Basic Function
def ACQSDK_Init():
    global Initiated
    ret = SDKAPI.ACQSDK_Init(objACQSDK_CSDevice, hWnd)
    if ret[1] == 0:
        Initiated = True
    CheckResult(ret)
def ACQSDK_UnInit():
    global Initiated
    ret = SDKAPI.ACQSDK_UnInit(objACQSDK_CSDevice)
    if ret[1] == 0: Initiated = False
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
def ACQSDK_PausePlay():
    ret = SDKAPI.ACQSDK_PausePlay(objACQSDK_CSDevice)
    CheckResult(ret)
def ACQSDK_ResumePlay():
    ret = SDKAPI.ACQSDK_ResumePlay(objACQSDK_CSDevice)
    CheckResult(ret)
def ACQSDK_StartRecord():
    path = LogPathInput.get()
    Logger('Received Parameter -> {}'.format(path))
    path = r'%s/%s.avi' % (path, timestamp())
    ret = SDKAPI.ACQSDK_StartRecord(objACQSDK_CSDevice, path)
    CheckResult(ret)
def ACQSDK_StopRecord():
    ret = SDKAPI.ACQSDK_StopRecord(objACQSDK_CSDevice)
    CheckResult(ret)
def ACQSDK_SendCaptureCmd():
    if Initiated == True:
        class SWCapture(threading.Thread):
            def __init__(self):
                threading.Thread.__init__(self)
            def run(self):
                self.ret = SDKAPI.ACQSDK_SendCaptureCmd(objACQSDK_CSDevice)
                CheckResult(self.ret)
        instance = SWCapture()
        instance.setDaemon(False)
        instance.start()
    else:
        ret = SDKAPI.ACQSDK_SendCaptureCmd(objACQSDK_CSDevice)
        CheckResult(ret)
def ACQSDK_SetLogPath():
    path = LogPathInput.get()
    Logger('Received Parameter -> {}'.format(path))
    ret = SDKAPI.ACQSDK_SetLogPath(objACQSDK_CSDevice, path)
    CheckResult(ret)

#    Mirror & Rotation
def ACQSDK_SetMirrorFlag():
    bEnable = int(MirrorInput.get())
    Logger('Received Parameter -> {}'.format(bEnable))
    ret = SDKAPI.ACQSDK_SetMirrorFlag(objACQSDK_CSDevice, bEnable)
    CheckResult(ret)
    del ret
    ret = SDKAPI.ACQSDK_GetMirrorFlag(objACQSDK_CSDevice)
    CheckResult(ret)
def ACQSDK_GetMirrorFlag():
    ret = SDKAPI.ACQSDK_GetMirrorFlag(objACQSDK_CSDevice)
    CheckResult(ret)
def ACQSDK_SetRotationFlag():
    rotation = int(RotationInput.get())
    Logger('Received Parameter -> {}'.format(rotation))
    ret = SDKAPI.ACQSDK_SetRotationFlag(objACQSDK_CSDevice, rotation)
    CheckResult(ret)
    del ret
    ret = SDKAPI.ACQSDK_GetRotationFlag(objACQSDK_CSDevice)
    CheckResult(ret)
def ACQSDK_GetRotationFlag():
    ret = SDKAPI.ACQSDK_GetRotationFlag(objACQSDK_CSDevice)
    CheckResult(ret)

#    Query
def ACQSDK_QueryDeviceInfo():
    pDeviceInfo = win32com.client.Dispatch(GD.ACQSDK_ASDeviceInfor_ProgID)
    ret = SDKAPI.ACQSDK_QueryDeviceInfo(
        objACQSDK_CSDevice, pDeviceInfo)
    CheckResult(ret)
    if ret[1] == 0:
        try:
            index1 = str(hex(pDeviceInfo.get_device_type())).upper()
            device_type = GD.Device_Type[index1]
        except:
            device_type = index1
        finally:
            Logger('\t\tACQSDK_QueryDeviceInfo -> get_device_type: ({}, {})'.format(index1, device_type))
        try:
            index2 = str(hex(pDeviceInfo.get_mode_type())).upper()
            model_type = GD.Model_Type[index2]
        except:
            model_type = index2
        finally:
            Logger('\t\tACQSDK_QueryDeviceInfo -> get_mode_type: ({}, {})'.format(index2, model_type))
        Logger('\t\tACQSDK_QueryDeviceInfo -> get_sn: {}'.format(pDeviceInfo.get_sn()))
        Logger('\t\tACQSDK_QueryDeviceInfo -> get_fw_version: {}'.format(pDeviceInfo.get_fw_version()))
    del pDeviceInfo
def ACQSDK_GetFirmwareVersion():
    ret = SDKAPI.ACQSDK_GetFirmwareVersion(objACQSDK_CSDevice)
    CheckResult(ret)
def ACQSDK_GetSDKVersion():
    ret = SDKAPI.ACQSDK_GetSDKVersion(objACQSDK_CSDevice)
    CheckResult(ret)
def ACQSDK_GetHostVersion():
    ret = SDKAPI.ACQSDK_GetHostVersion(objACQSDK_CSDevice)
    CheckResult(ret)
def ACQSDK_GetFwStatus():
    ret = SDKAPI.ACQSDK_GetFwStatus(objACQSDK_CSDevice)
    CheckResult(ret)

#    Configuration
#    >> Brightness
def ACQSDK_GetBrightness():
    ret = SDKAPI.ACQSDK_GetBrightness(objACQSDK_CSDevice)
    CheckResult(ret)
    if ret[1][0] == 0:
        Logger('\t\tCurrent brightness: {}'.format(ret[1][1]))
        Logger('\t\tMaximum brightness: {}'.format(ret[1][2]))
        Logger('\t\tMinimum brightness: {}'.format(ret[1][3]))
        Logger('\t\tDefault brightness: {}'.format(ret[1][4]))
def ACQSDK_SetBrightness():
    brightness = int(BrightnessInput.get())
    Logger('Received Parameter -> {}'.format(brightness))
    ret = SDKAPI.ACQSDK_SetBrightness(objACQSDK_CSDevice, brightness)
    CheckResult(ret)
    del ret
    ret = SDKAPI.ACQSDK_GetBrightness(objACQSDK_CSDevice)
    CheckResult(ret)

#    >> Contrast
def ACQSDK_GetContrast():
    ret = SDKAPI.ACQSDK_GetContrast(objACQSDK_CSDevice)
    CheckResult(ret)
    if ret[1][0] == 0:
        Logger('\t\tCurrent contrast: {}'.format(ret[1][1]))
        Logger('\t\tMaximum contrast: {}'.format(ret[1][2]))
        Logger('\t\tMinimum contrast: {}'.format(ret[1][3]))
        Logger('\t\tDefault contrast: {}'.format(ret[1][4]))
def ACQSDK_SetContrast():
    contrast = int(ContrastInput.get())
    Logger('Received Parameter -> {}'.format(contrast))
    ret = SDKAPI.ACQSDK_SetContrast(objACQSDK_CSDevice, contrast)
    CheckResult(ret)
    del ret
    ret = SDKAPI.ACQSDK_GetContrast(objACQSDK_CSDevice)
    CheckResult(ret)

#    >> Powerline Frequency
def ACQSDK_GetPowerlineFrequency():
    ret = SDKAPI.ACQSDK_GetPowerlineFrequency(objACQSDK_CSDevice)
    CheckResult(ret)
    if ret[1][0] == 0:
        Logger('\t\tCurrent frequency: {}'.format(ret[1][1]))
        Logger('\t\tDefault frequency: {}'.format(ret[1][2]))
def ACQSDK_SetPowerlineFrequency():
    frequency = int(FrequencyInput.get())
    Logger('Received Parameter -> {}'.format(frequency))
    ret = SDKAPI.ACQSDK_SetPowerlineFrequency(objACQSDK_CSDevice, frequency)
    CheckResult(ret)
    del ret
    ret = SDKAPI.ACQSDK_GetPowerlineFrequency(objACQSDK_CSDevice)
    CheckResult(ret)

#    >> Sleep
def ACQSDK_SetEnableSleep():
    bEnable = int(SetSleepInput.get())
    Logger('Received Parameter -> {}'.format(bEnable))
    ret = SDKAPI.ACQSDK_SetEnableSleep(objACQSDK_CSDevice, bEnable)
    CheckResult(ret)
    del ret
    ret = SDKAPI.ACQSDK_GetEnableSleep(objACQSDK_CSDevice)
    CheckResult(ret)
def ACQSDK_GetEnableSleep():
    ret = SDKAPI.ACQSDK_GetEnableSleep(objACQSDK_CSDevice)
    CheckResult(ret)
def ACQSDK_GetSleepTime():
    ret = SDKAPI.ACQSDK_GetSleepTime(objACQSDK_CSDevice)
    CheckResult(ret)
def ACQSDK_SetSleepTime():
    seconds = int(SleepTimeInput.get())
    Logger('Received Parameter -> {}'.format(seconds))
    ret = SDKAPI.ACQSDK_SetSleepTime(objACQSDK_CSDevice, seconds)
    CheckResult(ret)
    del ret
    ret = SDKAPI.ACQSDK_GetSleepTime(objACQSDK_CSDevice)
    CheckResult(ret)

#    >> Auto Power Off
def ACQSDK_EnableAutoPowerOff():
    bEnable = int(SetAutoPowerOffInput.get())
    Logger('Received Parameter -> {}'.format(bEnable))
    ret = SDKAPI.ACQSDK_EnableAutoPowerOff(objACQSDK_CSDevice, bEnable)
    CheckResult(ret)
    del ret
    ret = SDKAPI.ACQSDK_GetEnableAutoPowerOff(objACQSDK_CSDevice)
    CheckResult(ret)
def ACQSDK_GetEnableAutoPowerOff():
    ret = SDKAPI.ACQSDK_GetEnableAutoPowerOff(objACQSDK_CSDevice)
    CheckResult(ret)
def ACQSDK_GetAutoPowerOffTime():
    ret = SDKAPI.ACQSDK_GetAutoPowerOffTime(objACQSDK_CSDevice)
    CheckResult(ret)
def ACQSDK_SetAutoPowerOffTime():
    secondsCount = int(AutoPowerOffTimeInput.get())
    Logger('Received Parameter -> {}'.format(secondsCount))
    ret = SDKAPI.ACQSDK_SetAutoPowerOffTime(objACQSDK_CSDevice, secondsCount)
    CheckResult(ret)
    del ret
    ret = SDKAPI.ACQSDK_GetAutoPowerOffTime(objACQSDK_CSDevice)
    CheckResult(ret)

#    Firmware
def ACQSDK_UpgradeFirmware():
    pFullPathName = askopenfilename()
    if pFullPathName != '':
        class FWUpgrade(threading.Thread):
            def __init__(self, pFullPathName):
                threading.Thread.__init__(self)
                self.pFullPathName = pFullPathName
            def run(self):
                self.ret = SDKAPI.ACQSDK_UpgradeFirmware(objACQSDK_CSDevice, self.pFullPathName)
                CheckResult(self.ret)
        instance = FWUpgrade(pFullPathName)
        instance.setDaemon(False)
        instance.start()
    elif pFullPathName == '':
        Logger('ACQSDK_UpgradeFirmware -> No ZIP File is selected.')
def ACQSDK_AbortUpgrade():
    ret = SDKAPI.ACQSDK_AbortUpgrade(objACQSDK_CSDevice)
    CheckResult(ret)

#    Get Frame from AVI file
def ACQSDK_GrabFrameFromMovie():
    avi_file = askopenfilename()
    if avi_file != '':
        avi_file = avi_file.replace('/', '\\')
        bmp_file = avi_file+'.GrabFrame.bmp'
        ret = SDKAPI.ACQSDK_GrabFrameFromMovie(objACQSDK_CSDevice, avi_file, bmp_file)
        CheckResult(ret)
    elif avi_file == '':
        Logger('ACQSDK_GrabFrameFromMovie -> No AVI File is selected.')

#    CS1200
def ACQSDK_EnableAutoPowerOn():
    bEnable = int(SetAutoPowerOnInput.get())
    Logger('Received Parameter -> {}'.format(bEnable))
    ret = SDKAPI.ACQSDK_EnableAutoPowerOn(objACQSDK_CSDevice, bEnable)
    CheckResult(ret)
    del ret
    ret = SDKAPI.ACQSDK_GetEnableAutoPowerOn(objACQSDK_CSDevice)
    CheckResult(ret)
def ACQSDK_GetEnableAutoPowerOn():
    ret = SDKAPI.ACQSDK_GetEnableAutoPowerOn(objACQSDK_CSDevice)
    CheckResult(ret)

#    CS1500
def ACQSDK_Get2LevelCapture():
    ret = SDKAPI.ACQSDK_Get2LevelCapture(objACQSDK_CSDevice)
    CheckResult(ret)
def ACQSDK_Set2LevelCapture():
    bEnable = int(Set2LevelCaptureInput.get())
    Logger('Received Parameter -> {}'.format(bEnable))
    ret = SDKAPI.ACQSDK_Set2LevelCapture(objACQSDK_CSDevice, bEnable)
    CheckResult(ret)
    del ret
    ret = SDKAPI.ACQSDK_Get2LevelCapture(objACQSDK_CSDevice)
    CheckResult(ret)

# ========== SDK's API ==========



# ========== Test Process ==========
# Begin
def CleanQueue():
    global EventQueue
    EventQueue = []
def BrightnessProcess(typeid):
    # 0: 'INCREASE'
    # 1: 'DECREASE':
    global EventQueue
    if typeid == 0:
        sequence = [1, 2, 3, 4, 5, 6, 7]
    elif typeid == 1:
        sequence = [7, 6, 5, 4, 3, 2, 1]
    else:
        return
    for i in sequence:
        EventQueue.append(('ProcessTest', 'Change Brightness to %d' % i))
        EventQueue.append(('ACQSDK_SetBrightness', i))
def ContrastProcess(typeid):
    # 0: 'INCREASE'
    # 1: 'DECREASE':
    global EventQueue
    if typeid == 0:
        sequence = [1, 2, 3, 4, 5, 6, 7]
    elif typeid == 1:
        sequence = [7, 6, 5, 4, 3, 2, 1]
    else:
        return
    for i in sequence:
        EventQueue.append(('ProcessTest', 'Change Contrast to %d' % i))
        EventQueue.append(('ACQSDK_SetContrast', i))
def RotationPerTime():
    global EventQueue
    ret = SDKAPI.ACQSDK_GetRotationFlag(objACQSDK_CSDevice)
    if ret[1] == 0:
        EventQueue.append(('ProcessTest', 'Change Rotation to 90'))
        EventQueue.append(('ACQSDK_SetRotationFlag', 90))
    elif ret[1] == 90:
        EventQueue.append(('ProcessTest', 'Change Rotation to 180'))
        EventQueue.append(('ACQSDK_SetRotationFlag', 180))
    elif ret[1] == 180:
        EventQueue.append(('ProcessTest', 'Change Rotation to 270'))
        EventQueue.append(('ACQSDK_SetRotationFlag', 270))
    elif ret[1] == 270:
        EventQueue.append(('ProcessTest', 'Change Rotation to 0'))
        EventQueue.append(('ACQSDK_SetRotationFlag', 0))
    else:
        Logger('\t<-> GUI Callback -> Fail to fetch Rotation Flag...')
def RotationProcess():
    global EventQueue
    EventQueue.append(('ProcessTest', 'Change Rotation to 90'))
    EventQueue.append(('ACQSDK_SetRotationFlag', 90))
    EventQueue.append(('ProcessTest', 'Change Rotation to 180'))
    EventQueue.append(('ACQSDK_SetRotationFlag', 180))
    EventQueue.append(('ProcessTest', 'Change Rotation to 270'))
    EventQueue.append(('ACQSDK_SetRotationFlag', 270))
    EventQueue.append(('ProcessTest', 'Change Rotation to 0'))
    EventQueue.append(('ACQSDK_SetRotationFlag', 0))
def MirrorPerTime():
    global EventQueue
    ret = SDKAPI.ACQSDK_GetMirrorFlag(objACQSDK_CSDevice)
    if ret[1] == 0:
        EventQueue.append(('ProcessTest', 'Change Mirror to 1'))
        EventQueue.append(('ACQSDK_SetMirrorFlag', 1))
    elif ret[1] == 1:
        EventQueue.append(('ProcessTest', 'Change Mirror to 0'))
        EventQueue.append(('ACQSDK_SetMirrorFlag', 0))
def MirrorProcess():
    global EventQueue
    for i in [1, 2]:
        EventQueue.append(('ProcessTest', 'Change Mirror to 1'))
        EventQueue.append(('ACQSDK_SetMirrorFlag', 1))
        EventQueue.append(('ProcessTest', 'Change Mirror to 0'))
        EventQueue.append(('ACQSDK_SetMirrorFlag', 0))
def MessageQueue():
    global EventQueue
    if len(EventQueue) != 0:
        cmd = EventQueue[0]
        if cmd[0] == 'ACQSDK_SetBrightness':
            SDKAPI.ACQSDK_SetBrightness(objACQSDK_CSDevice, cmd[1])
            time.sleep(2)
        elif cmd[0] == 'ACQSDK_SetContrast':
            SDKAPI.ACQSDK_SetContrast(objACQSDK_CSDevice, cmd[1])
            time.sleep(2)
        elif cmd[0] == 'ACQSDK_SetRotationFlag':
            if cmd[1] == 0 or cmd[1] == 180:
                ResetLiveVideoWindowSize(640, 480)
            elif cmd[1] == 90 or cmd[1] == 270:
                ResetLiveVideoWindowSize(480, 640)
            SDKAPI.ACQSDK_OnUpdateLiveWnd(objACQSDK_CSDevice)
            SDKAPI.ACQSDK_SetRotationFlag(objACQSDK_CSDevice, cmd[1])
            time.sleep(1)
        elif cmd[0] == 'ACQSDK_SetMirrorFlag':
            SDKAPI.ACQSDK_SetMirrorFlag(objACQSDK_CSDevice, cmd[1])
            time.sleep(1)
        elif cmd[0] == 'ProcessTest':
            strOutput = ' '*4+'@>-->- ProcessTest -> %s\n' % cmd[1]
            pLogger.insert(END, strOutput)
            pLogger.yview(END)
            with open('./'+LoggerOutput, 'a+') as f:
                f.write(strOutput)
        elif cmd[0] == 'LoggerWin':
            pLogger.insert(END, cmd[1])
            pLogger.yview(END)
            with open('./'+LoggerOutput, 'a+') as f:
                f.write(cmd[1])
        EventQueue.pop(0)  # Ignore action which is not defined
    wControlPanel.after(20, MessageQueue)
# End
# ========== Test Process ==========



# Callback Class -> CSDevice
class SDKEvents():
    def OnHPEvents(self, Callback):
        i = Callback.QueryInterface(pythoncom.IID_IDispatch)
        objSDKCallbackInfo = win32com.client.Dispatch(i)
        self.EventID = str(hex(objSDKCallbackInfo.get_event_id())).upper()
        self.EventState = '*** SDK Callback -> %s' % self.EventID
        try:
            self.EventID_Value = GD.Callback_MsgType[self.EventID]
        except:
            self.EventID_Value = 'NOT DEFINED'
        #if self.EventID == '0X200005':
        #    ACQSDK_SendCaptureCmd()
        if self.EventID == '0X200003':
            self.percent = objSDKCallbackInfo.get_fw_upgrade_percent()
            self.EventID_Value = self.EventID_Value+' -> %d%%' % self.percent
        Logger('\t%s -> %s' % (self.EventState, self.EventID_Value))
    def OnSDKImageDataCallback(self, t, buffer):
        self.path = LogPathInput.get()
        Logger('\t*** SDK Image Callback -> Get image type, {}'.format(t))
        Logger('\t*** SDK Image Callback -> Save to "{}"'.format(self.path))
        try:
            with open('{}\{}.jpg'.format(self.path, timestamp()), 'wb') as f:
                f.write(buffer)
        except:
            Logger('\t*** SDK Image Callback -> Failure on saving.')
        else:
            Logger('\t*** SDK Image Callback -> Saved.')

# >>Body<<
# Location
try:
    ACQSDK_DLL_Dir = os.environ.get('CommonProgramFiles(x86)')+'\\Trophy\\Acquisition\\AcqSdk\\'
except:
    ACQSDK_DLL_Dir = os.environ.get('CommonProgramFiles')+'\\Trophy\\Acquisition\\AcqSdk\\'
finally:
    ACQSDK_DLL = ACQSDK_DLL_Dir+'ACQSDK.DLL'

# Logger
#    Output file's name
LoggerOutput = r'./Output/AcqTaurus_GUIOperationLogger.log'
try:
    if not os.path.isfile('./'+LoggerOutput):
        open(LoggerOutput, 'w').close()  # Create log file is not exist.
except:
    print 'WARN: No Execution Log file generated.'

# Flag of Init :: If Init is not executed, EXITAPP function will not
# execute UnInit.
Initiated = False

# Information Label
InfoLabel = 'Test Application of UVC Camera SDK built by ActivePython 2.7 (x86)'
ShortcutsInfo = '''
    F9\tMirror
    F10\tRotation
    c\tCapture
    r\tStart Record
    R\tStop Record
'''

# Run Mode
DebugMode = 1

# Generate GUI elements for three window
#    Size of Live Video window
LiveVideo_Width  = 640
LiveVideo_Height = 480

#    Generate GUI
GenerateGUI()

# Create COM object and Event
try:
    objACQSDK_CSDevice = win32com.client.DispatchWithEvents(GD.ACQSDK_CSDevice_ProgID, SDKEvents)
except:
    print 'Fail to create COM object.'

# Event Queue
EventQueue = []

# Event after window has displayed
wControlPanel.after(500, lambda: ResetWindowPosition(0))
wControlPanel.after(20, MessageQueue)

# Display GUI and wait message
mainloop()
