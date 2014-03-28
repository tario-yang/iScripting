"""
Global Definition for whole SDK testing
"""

# Import required modules
import os, time

# COM
#	definition: ProgID of each CoClass
ACQSDK_CSDevice_ProgID      = "ACQSDK.CSDevice.1"
ACQSDK_ASImageUnit_ProgID   = "ACQSDK.ASImageUnit.1"
ACQSDK_ASDeviceInfor_ProgID = "ACQSDK.ASDeviceInfor.1"

# XML
# 	definition: Data source directory for XML files
ACQSDK_TestCaseXML_APIDir       = r"TestData/InputXML"
# 	definition: Data source list
ACQSDK_TestCaseXML_List         = r"TestData/InputXML/ACQSDK_TestCaseXML_List.txt"
# 	definition: Keywords in XML
ACQSDK_TestSummaryTag    = "index"
ACQSDK_TestCase          = "APIName"
ACQSDK_ExpectedResult    = "Return"
ACQSDK_TestStepTag       = "Teststep"
ACQSDK_ParameterTag      = "Parameter"
ACQSDK_ParameterNameTag  = "name"
ACQSDK_ParameterValueTag = "value"

# definition: Outputs: SDK's log file (ACQSDK_SetLogPath), execution's log.
ACQSDK_OutputDir                = r"Output"
ACQSDK_ExecutionLogger          = "ACQSDK_Execution.csv"

# definition: dictionary, "acq_sdk/SDK Document/SDKDef.h"
Device_Type = {
	"0X20001" : "DEV_1500",
	"0X20002" : "DEV_1600",
	"0X20003" : "DEV_1200",
	"0X20004" : "DEV_1650",
	"0X20005" : "DEV_UVC",
	"0X20006" : "DEV_UNDEFINED", }
Model_Type = {
	"0X30001" : "MODEL_WIRED_DOCK",
	"0X30002" : "MODEL_WIRELESS_ONE",
	"0X30003" : "MODEL_WIRELESS_MANY",
	"0X30004" : "MODEL_DIRECT_WIRED_ONE",
	"0X30005" : "MODEL_UNDEFINED", }
OPERATOR_ERROR = {
	"0XF0001" : "DEVICE_CONNECTION_FALSE",
	"0XF0002" : "DEVICE_CREATED_FAIL",
	"0XF0003" : "HOST_SERVICE_IP_INVALID",
	"0XF0004" : "HOST_SERVICE_CONNECT_FAILED",
	"0XF0005" : "UVC_INPUT_PARAM_ERR",
	"0XF0006" : "UVC_INIT_NO_DEVICE",
	"0XF0007" : "UVC_INIT_DEVICE_CMT_ERR",
	"0XF0008" : "UVC_INIT_QUERY_CALLBACK_INTERFACE_FAIL",
	"0XF0009" : "UVC_INIT_CREATE_CALLBACK_INSTANCE_FAIL",
	"0XF000A" : "UVC_INIT_BIND_FILTER_FAIL",
	"0XF000B" : "UVC_INIT_HID_DEVICE_INIT_FAIL",
	"0XF000C" : "UVC_INIT_XU_INIT_CMD_SEND_TIMEOUT",
	"0XF000D" : "UVC_GET_DEVICE_INFOR_BUFF_ERROR",
	"0XF000E" : "LOG_PATH_SET_ERR",
	"0XF000F" : "ACQSDK_SENDER_FAIL",
	"0XF0010" : "ACQSDK_SENDER_TIMEOUT",
	"0XF0011" : "CAPTURE_INPUT_PARAM_VALUE_ERR",
	"0XF0012" : "CAPTURE_INPUT_PARAM_TYPE_ERR",
	"0XF0013" : "CAPTURE_SAFE_CREATE_NULL",
	"0XF0014" : "CAPTURE_SAFE_ACCESS_ERR",
	"0XF0015" : "CAPTURE_INPUT_DATA_BUFFER_NO_ENOUGH",
	"0XF0016" : "CAPTURE_MEMORY_NOT_ENOUGH_TO_NEW",
	"0XF0017" : "CAPTURE_TIME_OUT_WITH_NO_DATA",
	"0XF0018" : "CAPTURE_SEND_EXTERNAL_FAILED",
	"0XF0019" : "CAPUTRE_FREE_TYPE_ERR",
	"0XF001A" : "RECORD_INPUT_FILE_PATH_ERR",
	"0XF001B" : "RECORD_STARTING_WHILE_DEVICE_REMOVE",
	"0XF001C" : "RECORD_INSUFFICIENT_SPACE_ON_THE_DISK",
	"0XF001D" : "ACQSDK_XU_SET_ERR",
	"0XF001E" : "ACQSDK_XU_GET_ERR",
	"0XF001F" : "ACQSDK_ERROR_UPDATE_FAILED",
	"0XF0020" : "ACQSDK_ERROR_UPLOADED_FAILED",
	"0XF0021" : "ACQSDK_ERROR_DOWNLOADED_FAILED", }
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
	"0X200019" : "MSG_TYPE_UNDEFINED", }

# definition: functions and classes
# 	Function to return Output Header. The header is a timestamp.
def Output_Header(fmt = "%Y-%m-%d-%H-%M-%S"): return time.strftime(fmt,time.localtime())
# 	Function to initiate execution log file
def InitExecLogger(Dir = ACQSDK_OutputDir, ExecutionLogger = ACQSDK_ExecutionLogger):
	if os.path.isfile(Dir + "/" + ExecutionLogger):
		time.sleep(1)
		os.rename(Dir + "/" + ExecutionLogger, Dir + "/" + Output_Header() + "_" + ExecutionLogger)
	else:
		pass
	with open(Dir + "/" + ExecutionLogger, "w") as f: f.write("Date, Time, Description\n")
#	Function to write execution log file
def WriteLine2ExecLogger(StrLine, Dir = ACQSDK_OutputDir, ExecutionLogger = ACQSDK_ExecutionLogger):
	with open(Dir + "/" + ExecutionLogger, "a+") as f:
		f.write(Output_Header("%Y-%m-%d") + "," + Output_Header("%H-%M-%S") + ', "%s"\n' % StrLine)
# 	Function to output content to console and execution log
def Logger(StrLine):
	WriteLine2ExecLogger(StrLine)
	print Output_Header() + "\t%s" % StrLine
