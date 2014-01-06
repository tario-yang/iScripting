# Import required modules
try:
	import sys
	import os
	import TestACQSDK_Module_Global_Definition as gDef
except ImportError:
	print "Required modules are NOT imported!"
	sys.exit(1)
else:
	print gDef.Output_Header() + "\t" + "Required modules for API lib are imported.\n"

# Error Code List
ErrorCode = {
	"0X20006": "[TEST] DEVICE_CONNECTION_FALSE: Disconnected or Disabled?",
	"0XF0001": "DEVICE_CONNECTION_FALSE",
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
	"0XF0017": "RECORD_STARTING_WHILE_DEVICE_REMOVE"
}

# Output Result
def TestACQSDK_API_Output(module_name, ret):
	print gDef.Output_Header() + "\t" + "Location: " + str(module_name)
	print gDef.Output_Header() + "\t" + "Output:   " + str(ret)

# Output Error Info: ACQSDK API
def TestACQSDK_API_ErrorInfo(ret):
	if ret == 0:
		print gDef.Output_Header() + "\t" + "Pass"
	else:
		print gDef.Output_Header() + "\t" + "Failure: " + str(hex(ret))
		# Fetch the error information via error code
		if ret != 1:
			try:
				print gDef.Output_Header() + "\t" + ErrorCode[str(hex(ret)).upper()]
			except KeyError:
				print gDef.Output_Header() + "\t" + "ErrorCode is NOT defined."
	print "-"*88

# API: ACQSDK_Init
def TestACQSDK_API_ACQSDK_Init(objACQSDK_CSDevice_1, para_hWnd):
	Module_Name = sys._getframe().f_code.co_name
	print gDef.Output_Header() + "\t" + "Received: " + str(para_hWnd)
	try:
		ret = objACQSDK_CSDevice_1.ACQSDK_Init(para_hWnd)
	except:
		pass
	finally:
		try:
			type(eval(str(ret)))
		except NameError:
			print gDef.Output_Header() + "\t" + "Exception happens when executing" + " " + Module_Name
			print gDef.Output_Header() + "\t" + " - There is no output return, ret does not exist!"
			sys.exit(1)
		except TypeError:
			print gDef.Output_Header() + "\t" + "Unexpected Type of ret is received."
		else:
			TestACQSDK_API_Output(Module_Name, ret)
			TestACQSDK_API_ErrorInfo(ret)

# API: ACQSDK_Uninit
def TestACQSDK_API_ACQSDK_UnInit(objACQSDK_CSDevice_1):
	Module_Name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice_1.ACQSDK_UnInit()
	except:
		pass
	finally:
		try:
			type(eval(str(ret)))
		except NameError:
			print gDef.Output_Header() + "\t" + "Exception happens when executing" + " " + Module_Name
			print gDef.Output_Header() + "\t" + " - There is no output return, ret does not exist!"
			sys.exit(1)
		except TypeError:
			print gDef.Output_Header() + "\t" + "Unexpected Type of ret is received."
		else:
			TestACQSDK_API_Output(Module_Name, ret)
			TestACQSDK_API_ErrorInfo(ret)

# API: ACQSDK_QueryDeviceInfo
# def TestACQSDK_API_ACQSDK_QueryDeviceInfo(objACQSDK_CSDevice_1, para_pDeviceInfo):

# API: ACQSDK_SetHPWorkMode
# def TestACQSDK_API_ACQSDK_SetHPWorkMode(objACQSDK_CSDevice_1, para_lWorkMode):

# API: ACQSDK_StartPlay
def TestACQSDK_API_ACQSDK_StartPlay(objACQSDK_CSDevice_1):
	Module_Name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice_1.ACQSDK_StartPlay()
	except:
		pass
	finally:
		try:
			type(eval(str(ret)))
		except NameError:
			print gDef.Output_Header() + "\t" + "Exception happens when executing" + " " + Module_Name
			print gDef.Output_Header() + "\t" + " - There is no output return, ret does not exist!"
			sys.exit(1)
		except TypeError:
			print gDef.Output_Header() + "\t" + "Unexpected Type of ret is received."
		else:
			TestACQSDK_API_Output(Module_Name, ret)
			TestACQSDK_API_ErrorInfo(ret)

# API: ACQSDK_StopPlay
def TestACQSDK_API_ACQSDK_StopPlay(objACQSDK_CSDevice_1):
	Module_Name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice_1.ACQSDK_StopPlay()
	except:
		pass
	finally:
		try:
			type(eval(str(ret)))
		except NameError:
			print gDef.Output_Header() + "\t" + "Exception happens when executing" + " " + Module_Name
			print gDef.Output_Header() + "\t" + " - There is no output return, ret does not exist!"
			sys.exit(1)
		except TypeError:
			print gDef.Output_Header() + "\t" + "Unexpected Type of ret is received."
		else:
			TestACQSDK_API_Output(Module_Name, ret)
			TestACQSDK_API_ErrorInfo(ret)

# API: ACQSDK_StartRecordEx
def TestACQSDK_API_ACQSDK_StartRecordEx(objACQSDK_CSDevice_1, para_file_path):
	Module_Name = sys._getframe().f_code.co_name
	print gDef.Output_Header() + "\t" + "Received: " + str(para_file_path)
	try:
		ret = objACQSDK_CSDevice_1.ACQSDK_StartRecordEx(para_file_path)
	except:
		pass
	finally:
		try:
			type(eval(str(ret)))
		except NameError:
			print gDef.Output_Header() + "\t" + "Exception happens when executing" + " " + Module_Name
			print gDef.Output_Header() + "\t" + " - There is no output return, ret does not exist!"
			sys.exit(1)
		except TypeError:
			print gDef.Output_Header() + "\t" + "Unexpected Type of ret is received."
		else:
			TestACQSDK_API_Output(Module_Name, ret)
			TestACQSDK_API_ErrorInfo(ret)

# API: ACQSDK_StopRecord
def TestACQSDK_API_ACQSDK_StopRecord(objACQSDK_CSDevice_1):
	Module_Name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice_1.ACQSDK_StopRecord()
	except:
		pass
	finally:
		try:
			type(eval(str(ret)))
		except NameError:
			print gDef.Output_Header() + "\t" + "Exception happens when executing" + " " + Module_Name
			print gDef.Output_Header() + "\t" + " - There is no output return, ret does not exist!"
			sys.exit(1)
		except TypeError:
			print gDef.Output_Header() + "\t" + "Unexpected Type of ret is received."
		else:
			TestACQSDK_API_Output(Module_Name, ret)
			TestACQSDK_API_ErrorInfo(ret)

# API: ACQSDK_CaptureEx
# def TestACQSDK_API_ACQSDK_CaptureEx(objACQSDK_CSDevice_1, para_lCount, para_pImageUnit):

# API: ACQSDK_GetImageData
# def TestACQSDK_API_ACQSDK_GetImageData(objACQSDK_CSDevice_1, para_pImageUnit):

# API: ACQSDK_GetWhiteImage
# def TestACQSDK_API_ACQSDK_GetWhiteImage(objACQSDK_CSDevice_1, para_pImageUnit, para_pWhite):

# API: ACQSDK_GetUVImage
# def TestACQSDK_API_ACQSDK_GetUVImage(objACQSDK_CSDevice_1, para_pImageUnit, para_pUV):

# API: ACQSDK_FreeImageUnit
# def TestACQSDK_API_ACQSDK_FreeImageUnit(objACQSDK_CSDevice_1, para_pImageUnit):

# API: ACQSDK_SetLogPathEx
def TestACQSDK_API_ACQSDK_SetLogPathEx(objACQSDK_CSDevice_1, para_path):
	Module_Name = sys._getframe().f_code.co_name
	print gDef.Output_Header() + "\t" + "Received: " + str(para_path)
	try:
		ret = objACQSDK_CSDevice_1.ACQSDK_SetLogPathEx(para_path)
	except:
		pass
	finally:
		try:
			type(eval(str(ret)))
		except NameError:
			print gDef.Output_Header() + "\t" + "Exception happens when executing" + " " + Module_Name
			print gDef.Output_Header() + "\t" + " - There is no output return, ret does not exist!"
			sys.exit(1)
		except TypeError:
			print gDef.Output_Header() + "\t" + "Unexpected Type of ret is received."
		else:
			TestACQSDK_API_Output(Module_Name, ret)
			TestACQSDK_API_ErrorInfo(ret)

# API: ACQSDK_GetSerialNumber
# def TestACQSDK_API_ACQSDK_GetSerialNumber():

# API: ACQSDK_SetSerialNumber
# def TestACQSDK_API_ACQSDK_SetSerialNumber():

# API: ACQSDK_GetFirmwareVersion
# def TestACQSDK_API_ACQSDK_GetFirmwareVersion():

# API: ACQSDK_UpgradeFirmware
# def TestACQSDK_API_ACQSDK_UpgradeFirmware():

# API: ACQSDK_SaveImage
# def TestACQSDK_API_ACQSDK_SaveImage(objACQSDK_CSDevice_1, para_file, para_pImageUnit):

# API: ACQSDK_SetMsgCallback
# def TestACQSDK_API_ACQSDK_SetMsgCallback(objACQSDK_CSDevice_1, para_pMsgInfo):
