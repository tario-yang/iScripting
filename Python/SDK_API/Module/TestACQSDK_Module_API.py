# Import required modules
try:
	import os, sys
	import TestACQSDK_Module_Init_Environment as INIT
except ImportError:
	print "One or more required modules are missing!"
	sys.exit(1)

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
	"0XF0017": "RECORD_STARTING_WHILE_DEVICE_REMOVE",
}

# Output Result
def TestACQSDK_API_Output(module_name, ret):
	print INIT.Output_Header() + "\t" + "Location: " + str(module_name)
	print INIT.Output_Header() + "\t" + "Output:   " + str(ret)
	if ret == 0:
		print INIT.Output_Header() + "\t" + "Pass"
	else:
		print INIT.Output_Header() + "\t" + "Failure: " + str(hex(ret))
		# Fetch the error information via error code
		if ret != 1:
			try:
				print INIT.Output_Header() + "\t" + ErrorCode[str(hex(ret)).upper()]
			except KeyError:
				print INIT.Output_Header() + "\t" + "ErrorCode is NOT defined."
	print ""

# API: ACQSDK_Init
def TestACQSDK_API_ACQSDK_Init(objACQSDK_CSDevice_1, para_hWnd):
	Module_Name = sys._getframe().f_code.co_name
	print INIT.Output_Header() + "\t" + "Received: " + '"' + str(para_hWnd) + '"'
	try:
		ret = objACQSDK_CSDevice_1.ACQSDK_Init(para_hWnd)
	except:
		pass
	finally:
		try:
			type(eval(str(ret)))
		except NameError:
			print INIT.Output_Header() + "\t" + "Exception happens when executing" + " " + Module_Name
			print INIT.Output_Header() + "\t" + " - There is no output return, ret does not exist!\n"
		except TypeError:
			print INIT.Output_Header() + "\t" + "Unexpected Type of ret is received."
		else:
			TestACQSDK_API_Output(Module_Name, ret)

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
			print INIT.Output_Header() + "\t" + "Exception happens when executing" + " " + Module_Name
			print INIT.Output_Header() + "\t" + " - There is no output return, ret does not exist!\n"
		except TypeError:
			print INIT.Output_Header() + "\t" + "Unexpected Type of ret is received."
		else:
			TestACQSDK_API_Output(Module_Name, ret)

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
			print INIT.Output_Header() + "\t" + "Exception happens when executing" + " " + Module_Name
			print INIT.Output_Header() + "\t" + " - There is no output return, ret does not exist!\n"
		except TypeError:
			print INIT.Output_Header() + "\t" + "Unexpected Type of ret is received."
		else:
			TestACQSDK_API_Output(Module_Name, ret)

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
			print INIT.Output_Header() + "\t" + "Exception happens when executing" + " " + Module_Name
			print INIT.Output_Header() + "\t" + " - There is no output return, ret does not exist!\n"
		except TypeError:
			print INIT.Output_Header() + "\t" + "Unexpected Type of ret is received."
		else:
			TestACQSDK_API_Output(Module_Name, ret)

# API: ACQSDK_StartRecord
def TestACQSDK_API_ACQSDK_StartRecord(objACQSDK_CSDevice_1, para_file_path):
	Module_Name = sys._getframe().f_code.co_name
	print INIT.Output_Header() + "\t" + "Received: " + str(para_file_path)
	try:
		ret = objACQSDK_CSDevice_1.ACQSDK_StartRecordEx(para_file_path)
	except:
		pass
	finally:
		try:
			type(eval(str(ret)))
		except NameError:
			print INIT.Output_Header() + "\t" + "Exception happens when executing" + " " + Module_Name
			print INIT.Output_Header() + "\t" + " - There is no output return, ret does not exist!\n"
		except TypeError:
			print INIT.Output_Header() + "\t" + "Unexpected Type of ret is received."
		else:
			TestACQSDK_API_Output(Module_Name, ret)

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
			print INIT.Output_Header() + "\t" + "Exception happens when executing" + " " + Module_Name
			print INIT.Output_Header() + "\t" + " - There is no output return, ret does not exist!\n"
		except TypeError:
			print INIT.Output_Header() + "\t" + "Unexpected Type of ret is received."
		else:
			TestACQSDK_API_Output(Module_Name, ret)

# API: ACQSDK_SetLogPath
def TestACQSDK_API_ACQSDK_SetLogPath(objACQSDK_CSDevice_1, para_path):
	Module_Name = sys._getframe().f_code.co_name
	print INIT.Output_Header() + "\t" + "Received: " + str(para_path)
	try:
		ret = objACQSDK_CSDevice_1.ACQSDK_SetLogPath(para_path)
	except:
		pass
	finally:
		try:
			print type(eval(str(ret)))
		except NameError:
			print INIT.Output_Header() + "\t" + "Exception happens when executing" + " " + Module_Name
			print INIT.Output_Header() + "\t" + " - There is no output return, ret does not exist!\n"
		except TypeError:
			print INIT.Output_Header() + "\t" + "Unexpected Type of ret is received."
		else:
			TestACQSDK_API_Output(Module_Name, ret)

