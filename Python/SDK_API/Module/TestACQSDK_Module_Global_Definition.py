# Import required modules
try:
	import os, os.path, sys, time, datetime
	import win32com.client, win32gui, win32con
	from win32con import *
except ImportError:
	print "One or more required modules are missing!"
	sys.exit(1)

# ProgID of each CoClass
ACQSDK_CSDevice_ProgID        = "ACQSDK.CSDevice.1"
ACQSDK_ASImageUnit_ProgID     = "ACQSDK.ASImageUnit.1"
ACQSDK_SDKCallbackInfo_ProgID = "ACQSDK.SDKCallbackInfo.1"

# Data Source: XML
ACQSDK_TestCaseXML_SingleAPI = r"../Configuration/TestACQSDK_Test_Case_SingleAPI.XML"
ACQSDK_TestCaseXML_Workflow  = r"../Configuration/TestACQSDK_Test_Case_Workflow.XML"

# Outputs: SDK's log file (ACQSDK_SetLogPath), execution's log and test report.
ACQSDK_OutputDir       = r"../Output"
ACQSDK_ExecutionLogger = "ACQSDK_Execution.log"
ACQSDK_ExecutionReport = "ACQSDK_TestReport.xml"

# definition: Live Video Window
TestACQSDK_LiveVideo_Window_Class    = "TestACQSDK"
TestACQSDK_LiveVideo_Window_Title    = "TestACQSDK: Live Video Display"
TestACQSDK_LiveVideo_Window_Position = (1,1)
TestACQSDK_LiveVideo_Window_Size     = (640,480)

# definition: dictionary, Error Code List
ErrorCode = {
	"0X20006": "[TEST] DEVICE_CONNECTION_FALSE: Disconnected or Disabled?", # Event
	"0XF0001": "DEVICE_CONNECTION_FALSE",                                   # Return
	"0XF0002": "DEVICE_CREATED_FAIL",
	"0XF0003": "HOST_SERVICE_IP_INVALID",
	"0XF0004": "HOST_SERVICE_CONNECT_FAILED",
	"0XF0005": "UVC_INIT_INPUT_PARAM_ERR",
	"0XF0006": "UVC_INIT_NO_DEVICE",
	"0XF0007": "UVC_INIT_DEVICE_CMT_ERR",
	"0XF0008": "UVC_INIT_BIND_FILTER_FAIL",
	"0XF0009": "UVC_GET_DEVICE_INFOR_BUFF_ERROR",
	"0XF000A": "LOG_PATH_SET_ERR",
	"0XF000B": "ACQSDK_SENDER_FAIL",
	"0XF000C": "ACQSDK_SENDER_TIMEOUT",
	"0XF000D": "CAPTURE_INPUT_PARAM_VALUE_ERR",
	"0XF000E": "CAPTURE_INPUT_PARAM_TYPE_ERR",
	"0XF000F": "CAPTURE_SAFE_CREATE_NULL",
	"0XF0010": "CAPTURE_SAFE_ACCESS_ERR",
	"0XF0011": "CAPTURE_INPUT_DATA_BUFFER_NO_ENOUGH",
	"0XF0012": "CAPTURE_MEMORY_NOT_ENOUGH_TO_NEW",
	"0XF0013": "CAPTURE_TIME_OUT_WITH_NO_DATA",
	"0XF0014": "CAPTURE_SEND_EXTERNAL_FAILED",
	"0XF0015": "CAPUTRE_FREE_TYPE_ERR",
	"0XF0016": "RECORD_INPUT_FILE_PATH_ERR",
	"0XF0017": "RECORD_STARTING_WHILE_DEVICE_REMOVE",
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
		open(Dir + "/" + ExecutionLogger, "w").close()

	#	Function to write execution log file
	def WriteLine2ExecLogger(StrLine, Dir = ACQSDK_OutputDir, ExecutionLogger = ACQSDK_ExecutionLogger):
		f = open(Dir + "/" + ExecutionLogger, "a+")
		f.write(Output_Header().replace(" ", ",") + "," + StrLine + "\n")
		f.close()

	# 	Function to output content to console and execution log
	def Logger(StrLine):
		WriteLine2ExecLogger(StrLine)
		print Output_Header() + "\t" + StrLine

	# 	Function to output content to console and execution log file for API/Workflow
	def TEE(module_name, parameter, ret, type = 1, ExecutionLogger = ACQSDK_ExecutionLogger):
		info = "Location: " + str(module_name) + "; Parameter: " + str(parameter) + "; Output: " + str(ret)
		if ret == 0:
			result = "Pass"
		else:
			result = "Failure"
			# Fetch the error information via error code
			if ret != 1:
				try:
					errorcode = ErrorCode[str(hex(ret)).upper()]
				except KeyError:
					errorcode = "Error code is NOT defined."
		if type == 1: # if api
			Logger(info)
			Logger(result)
			Logger(errorcode)
			WriteLine2ExecReporter(module_name, result)
		elif type == 2: # if workflow
			pass

	# Report related functions
	#	Function to initiate execution report
	def InitExecReporter(Dir = ACQSDK_OutputDir, ExecutionReporter = ACQSDK_ExecutionReport):
		if os.path.isfile(Dir + "/" + ExecutionReporter):
			time.sleep(1)
			os.rename(Dir + "/" + ExecutionReporter, Dir + "/" + Output_Header().replace(" ", "-") + "_" + ExecutionReporter)
		f = open(Dir + "/" + ExecutionReporter, "w")
		f.write(r"<?xml version="1.0" encoding="utf-8"?>")
		f.close()

	#	Function to write execution report
	def WriteLine2ExecReporter(testcase, result, Dir = ACQSDK_OutputDir, ExecutionLogger = ACQSDK_ExecutionLogger):
		pass

	# Function of Creating COM Object
	def CreateCOMObject(ProgID):
		return win32com.client.Dispatch(ProgID)

	# Function of Creating COM Event
	def CreateCOMObjectEvent(ProgID, Event):
		return win32com.client.DispatchEvents(ProgID,Event)

	# Class of Callback
	# [Placeholder]

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
	def WindowObjectKill(hWnd):
		win32gui.PostMessage(hWnd, win32con.WM_CLOSE, 0, 0)
except:
	print "Defined function/class includes error/mistake."
	sys.exit(1)
else:
	print Output_Header() + "\t" + "Initiated."

# Display the window when executing directly
if __name__ == '__main__':
	WindowObjectCreate()
