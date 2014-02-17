# Import required modules
try:
	import os, os.path, sys, time, datetime
	import win32com.client, win32gui, win32con
	from win32con import *
except ImportError:
	GDEF.Logger("Info -> %r" % sys._getframe().f_code.co_filename)
	GDEF.Logger("Error -> One or more required modules are missing!")
	sys.exit(1)

# definition: ProgID of each CoClass
ACQSDK_CSDevice_ProgID               = "ACQSDK.CSDevice.1"
ACQSDK_ASImageUnit_ProgID            = "ACQSDK.ASImageUnit.1"
ACQSDK_SDKCallbackInfo_ProgID        = "ACQSDK.SDKCallbackInfo.1"

# definition: Data source directory for XML files
ACQSDK_TestCaseXML_APIDir            = r"../Configuration/API"
ACQSDK_TestCaseXML_WorkflowDir       = r"../Configuration/Workflow"

# definition: Data source list
ACQSDK_TestCaseXML_List              = r"../Configuration/ACQSDK_TestCaseXML_List.txt"

# definition: Keywords in XML
ACQSDK_TestSummaryTag                = "index"
ACQSDK_TestCase                      = "APIName"
ACQSDK_ExpectedResult                = "Return"
ACQSDK_TestStepTag                   = "Teststep"
ACQSDK_ParameterTag                  = "Parameter"
ACQSDK_ParameterNameTag              = "name"
ACQSDK_ParameterValueTag             = "value"

# definition: Outputs: SDK's log file (ACQSDK_SetLogPath), execution's log and test report.
ACQSDK_OutputDir                     = r"../Output"
ACQSDK_ExecutionLogger               = "ACQSDK_Execution.csv"
ACQSDK_ExecutionReport               = "ACQSDK_TestReport.xml"

# definition: Live Video Window
TestACQSDK_LiveVideo_Window_Class    = "TestACQSDK"
TestACQSDK_LiveVideo_Window_Title    = "TestACQSDK: Live Video Display"
TestACQSDK_LiveVideo_Window_Position = (1,1)
TestACQSDK_LiveVideo_Window_Size     = (640,480)

# definition: dictionary, "acq_sdk/SDK Document/SDKDef.h"
Device_Type = {
	"0X20001" : "DEV_1500",
	"0X20002" : "DEV_1600",
	"0X20003" : "DEV_1200",
	"0X20004" : "DEV_1650",
}

Model_Type = {
	"0x00030001" : "MODEL_WIRED_DOCK",
	"0x00030002" : "MODEL_WIRELESS_ONE",
	"0x00030003" : "MODEL_WIRELESS_MANY",
	"0x00030004" : "MODEL_DIRECT_WIRED_ONE",
	"0x00030005" : "MODEL_UNDEFINED",
}

OPERATOR_ERROR = {
	"0X000F0001" : "DEVICE_CONNECTION_FALSE",
	"0X000F0002" : "DEVICE_CREATED_FAIL",
	"0X000F0003" : "HOST_SERVICE_IP_INVALID",
	"0X000F0004" : "HOST_SERVICE_CONNECT_FAILED" ,
	"0X000F0005" : "UVC_INIT_INPUT_PARAM_ERR" ,
	"0X000F0006" : "UVC_INIT_NO_DEVICE" ,
	"0X000F0007" : "UVC_INIT_DEVICE_CMT_ERR",
	"0X000F0008" : "UVC_INIT_QUERY_CALLBACK_INTERFACE_FAIL",
	"0X000F0009" : "UVC_INIT_CREATE_CALLBACK_INSTANCE_FAIL",
	"0X000F000A" : "UVC_INIT_BIND_FILTER_FAIL",
	"0X000F000B" : "UVC_INIT_HID_DEVICE_INIT_FAIL",
	"0X000F000C" : "UVC_GET_DEVICE_INFOR_BUFF_ERROR",
	"0X000F000D" : "LOG_PATH_SET_ERR" ,
	"0X000F000E" : "ACQSDK_SENDER_FAIL" ,
	"0X000F000F" : "ACQSDK_SENDER_TIMEOUT",
	"0X000F0010" : "CAPTURE_INPUT_PARAM_VALUE_ERR",
	"0X000F0011" : "CAPTURE_INPUT_PARAM_TYPE_ERR",
	"0X000F0012" : "CAPTURE_SAFE_CREATE_NULL",
	"0X000F0013" : "CAPTURE_SAFE_ACCESS_ERR",
	"0X000F0014" : "CAPTURE_INPUT_DATA_BUFFER_NO_ENOUGH",
	"0X000F0015" : "CAPTURE_MEMORY_NOT_ENOUGH_TO_NEW",
	"0X000F0016" : "CAPTURE_TIME_OUT_WITH_NO_DATA",
	"0X000F0017" : "CAPTURE_SEND_EXTERNAL_FAILED",
	"0X000F0018" : "CAPUTRE_FREE_TYPE_ERR",
	"0X000F0019" : "RECORD_INPUT_FILE_PATH_ERR",
	"0X000F001A" : "RECORD_STARTING_WHILE_DEVICE_REMOVE",
	"0X000F001B" : "ACQSDK_ERROR_UPDATE_FAILED",
	"0X000F001C" : "ACQSDK_ERROR_UPLOADED_FAILED",
	"0X000F001D" : "ACQSDK_ERROR_DOWNLOADED_FAILED",
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

FW_DOWNLOAD_FILE_ID = {
	"E_FW_FILE_ID_VERSION"          : 0, # /etc/fs.ver
	"E_FW_FILE_ID_CALIBRATION_FILE" : 1, # /etc/fs.ver
	"E_FW_FILE_ID_FW_LOG"           : 2, # /opt/deng.jpg
	"E_FW_FILE_ID_COUNT"            : 3, # DON'T use this
}

# definition: functions and classes
try:
	# Function to return Output Header. The header is a timestamp.
	def Output_Header():
		return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H-%M-%S')

	# Logger related functions
	# 	Function to initiate execution log file
	def InitExecLogger(Dir = ACQSDK_OutputDir, ExecutionLogger = ACQSDK_ExecutionLogger):
		if os.path.isfile(Dir + "/" + ExecutionLogger):
			time.sleep(1)
			os.rename(Dir + "/" + ExecutionLogger, Dir + "/" + Output_Header().replace(" ", "-") + "_" + ExecutionLogger)
		else:
			pass
		f = open(Dir + "/" + ExecutionLogger, "w")
		f.write("Date, Time, Description, Result, Comment\n")
		f.close()

	#	Function to write execution log file
	def WriteLine2ExecLogger(StrLine, Dir = ACQSDK_OutputDir, ExecutionLogger = ACQSDK_ExecutionLogger):
		f = open(Dir + "/" + ExecutionLogger, "a+")
		f.write(Output_Header().replace(" ", ",") + ", %s\n" % StrLine)
		f.close()

	# 	Function to output content to console and execution log
	def Logger(StrLine):
		WriteLine2ExecLogger(StrLine)
		print Output_Header() + "\t%s" % StrLine

	# 	Function to output content to console and execution log file for API/Workflow
	def TEE(module_name, ret, parameter="none", flag = "api", ExecutionLogger = ACQSDK_ExecutionLogger):
		info = "Location: %s; Output: %s; Parameter: %s" % (module_name, ret, parameter)
		result = ""
		errorcode = ""
		if ret == 0:
			result = "Pass"
		else:
			result = "Failure"
			if ret != 1:
				try:
					errorcode = OPERATOR_ERROR[str(hex(ret)).upper()]
				except KeyError:
					errorcode = "Error code is NOT defined."
		if flag == "api":
			info = info + ", %s, %s" % (result, errorcode)
			Logger(info)
			WriteLine2ExecReporter(module_name, result)
		elif flag == "workflow":
			pass

	# Report related functions
	#	Function to initiate execution report
	def InitExecReporter(Dir = ACQSDK_OutputDir, ExecutionReporter = ACQSDK_ExecutionReport):
		if os.path.isfile(Dir + "/" + ExecutionReporter):
			time.sleep(1)
			os.rename(Dir + "/" + ExecutionReporter, Dir + "/" + Output_Header().replace(" ", "-") + "_" + ExecutionReporter)
		f = open(Dir + "/" + ExecutionReporter, "w")
		f.write(r'<?xml version="1.0" encoding="utf-8"?>')
		f.close()

	#	Function to write execution report
	def WriteLine2ExecReporter(testcase, result, flag = "api", Dir = ACQSDK_OutputDir, ExecutionLogger = ACQSDK_ExecutionLogger):
		pass

	# Function of Creating COM Object
	def CreateCOMObject(ProgID): return win32com.client.Dispatch(ProgID)

	# Function of Creating COM Event
	def CreateCOMObjectEvent(ProgID, Event): return win32com.client.DispatchEvents(ProgID,Event)

	# Class of Callback ===> When using multi-thread, this can be invloked to test whether callback works or not.
	class ACQSDK_Callback():
		def OnHPEvents(self, objSDKCallbackInfo):
			return objSDKCallbackInfo.get_event_id()

	# Functions of Window object
	def WndProc(hWnd, msg, wParam, lParam):
		if msg == WM_PAINT:
			hdc,ps = win32gui.BeginPaint(hWnd)
			rect = win32gui.GetClientRect(hWnd)
			win32gui.EndPaint(hWnd,ps)
		if msg == WM_DESTROY:
			win32gui.PostQuitMessage(0)
		return win32gui.DefWindowProc(hWnd, msg, wParam, lParam)
	def WindowObjectCreate():
		objWin = win32gui.WNDCLASS()
		objWin.hbrBackground = COLOR_BTNFACE
		objWin.hCursor = win32gui.LoadCursor(0, IDC_ARROW)
		objWin.hIcon = win32gui.LoadIcon(0, IDI_APPLICATION)
		objWin.lpszClassName = TestACQSDK_LiveVideo_Window_Class
		objWin.lpfnWndProc = WndProc
		reg_objWin = win32gui.RegisterClass(objWin)
		hWnd = win32gui.CreateWindow(
				reg_objWin,
				TestACQSDK_LiveVideo_Window_Title,
				WS_OVERLAPPEDWINDOW,
				TestACQSDK_LiveVideo_Window_Position[0],
				TestACQSDK_LiveVideo_Window_Position[1],
				TestACQSDK_LiveVideo_Window_Size[0],
				TestACQSDK_LiveVideo_Window_Size[1],
				0, 0, 0, None)
		win32gui.ShowWindow(hWnd, SW_SHOWNORMAL)
		time.sleep(1)
		win32gui.UpdateWindow(hWnd)
		win32gui.PumpMessages()
	def WindowObjectKill(hWnd): win32gui.PostMessage(hWnd, win32con.WM_CLOSE, 0, 0)
except:
	Logger(r"Error -> Defined function/class includes error/mistake.")
	sys.exit(1)
else:
	# Display the window when executing directly
	if __name__ == '__main__':
		print sys._getframe().f_code.co_filename
		WindowObjectCreate()
