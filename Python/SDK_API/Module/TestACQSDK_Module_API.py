# Import required modules
try:
    import sys
    import time
    import TestACQSDK_Module_Global_Definition as gDef
    import TestACQSDK_Module_Init_Environment as Init_Env
except ImportError:
    print "Required modules are NOT imported!"
    sys.exit(1)
else:
    print gDef.Output_Header() + "Required modules for API lib are imported.\n"

# Error Code List
ErrorCode = {
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

# Output Result: OK
def TestACQSDK_API_Output(module_name, ret):
    print gDef.Output_Header() + "\t" + "Location:" + str(module_name)
    print gDef.Output_Header() + "\t" + "Output:" + str(ret)

# Output Error Info: OK
def TestACQSDK_API_ErrorInfo(ret):
    if ret == 0:
        print gDef.Output_Header() + "\t" + "Pass"
    else:
        print gDef.Output_Header() + "\t" + "Failure: " + str(hex(ret))
        # Fetch the error information via error code
        if ret != 1:
            try:
                print gDef.Output_Header() + "\t" + ErrorCode[str(hex(ret)).upper()]
            except:
                print gDef.Output_Header() + "\t" + "ErrorCode is NOT defined."
    print
    time.sleep(1)

# API: ACQSDK_Init: OK
def TestACQSDK_API_ACQSDK_Init(objACQSDK_CSDevice_1, para_hWnd):
    Module_Name = sys._getframe().f_code.co_name
    if isinstance(para_hWnd, tuple):
        print gDef.Output_Header() + "\t" + "Multiple test data received: " + str(para_hWnd)
        for i in range(len(para_hWnd)):
            print gDef.Output_Header() + "\t" + "Parameter [" + str(i+1) + "] "
            try:
                ret = objACQSDK_CSDevice_1.ACQSDK_Init(para_hWnd[i])
            except:
                print gDef.Output_Header() + "\t" + "Error happens."
            finally:
                TestACQSDK_API_Output(Module_Name, ret)
                TestACQSDK_API_ErrorInfo(ret)
                TestACQSDK_API_ACQSDK_Uninit(objACQSDK_CSDevice_1, 1)
    else:
        try:
            ret = objACQSDK_CSDevice_1.ACQSDK_Init(para_hWnd)
        except:
        	print gDef.Output_Header() + "\t" + "Error happens."
        finally:
            TestACQSDK_API_Output(Module_Name, ret)
            TestACQSDK_API_ErrorInfo(ret)
            TestACQSDK_API_ACQSDK_Uninit(objACQSDK_CSDevice_1, 1)

# API: ACQSDK_Uninit: OK
def TestACQSDK_API_ACQSDK_Uninit(objACQSDK_CSDevice_1, para_times):
    Module_Name = sys._getframe().f_code.co_name
    print gDef.Output_Header() + "\t" + "Execute " + str(para_times) + "times."
    while para_times > 0:
        try:
            ret = objACQSDK_CSDevice_1.ACQSDK_Uninit()
        except:
            print gDef.Output_Header() + "\t" + "Error happens."
        finally:
            TestACQSDK_API_Output(Module_Name, ret)
            TestACQSDK_API_ErrorInfo(ret)
        para_times-=1
        time.sleep(1)

# API: ACQSDK_QueryDeviceInfo
# def TestACQSDK_API_ACQSDK_QueryDeviceInfo():

# API: ACQSDK_SetHPWorkMode
# def TestACQSDK_API_ACQSDK_SetHPWorkMode():

# API: ACQSDK_StartPlay: OK
def TestACQSDK_API_ACQSDK_StartPlay(objACQSDK_CSDevice_1, para_times, para_hWnd):
    Module_Name = sys._getframe().f_code.co_name
    print gDef.Output_Header() + "\t" + "Execute " + str(para_times) + "times."
    while para_times > 0:
        try:
            ret = objACQSDK_CSDevice_1.ACQSDK_StartPlay()
        except:
            print gDef.Output_Header() + "\t" + "Error happens."
            Init_Env.WaitWindowMessage(para_hWnd)
        finally:
            TestACQSDK_API_Output(Module_Name, ret)
            TestACQSDK_API_ErrorInfo(ret)
        para_times-=1
        time.sleep(1)

# API: ACQSDK_StopPlay: OK
def TestACQSDK_API_ACQSDK_StopPlay(objACQSDK_CSDevice_1, para_times, para_hWnd):
    Module_Name = sys._getframe().f_code.co_name
    print gDef.Output_Header() + "\t" + "Execute " + str(para_times) + "times."
    while para_times > 0:
        try:
            ret = objACQSDK_CSDevice_1.ACQSDK_StopPlay()
        except:
            print gDef.Output_Header() + "\t" + "Error happens."
            Init_Env.WaitWindowMessage(para_hWnd)
        finally:
            TestACQSDK_API_Output(Module_Name, ret)
            TestACQSDK_API_ErrorInfo(ret)
        para_times-=1
        time.sleep(1)

# API: ACQSDK_StartRecordEx: OK
def TestACQSDK_API_ACQSDK_StartRecordEx(objACQSDK_CSDevice_1, para_file_path):
    Module_Name = sys._getframe().f_code.co_name
    if isinstance(para_file_path, tuple):
        print gDef.Output_Header() + "\t" + "Multiple test data received: " + str(para_file_path)
        for i in range(len(para_file_path)):
            print gDef.Output_Header() + "\t" + "Parameter [" + str(i+1) + "] "
            try:
                ret = objACQSDK_CSDevice_1.ACQSDK_StartRecord(para_file_path[i])
            except:
                print gDef.Output_Header() + "\t" + "Error happens."
            finally:
                TestACQSDK_API_Output(Module_Name, ret)
                TestACQSDK_API_ErrorInfo(ret)
    else:
        try:
            ret = objACQSDK_CSDevice_1.ACQSDK_StartRecord(para_file_path)
        except:
            print gDef.Output_Header() + "\t" + "Error happens."
        finally:
            TestACQSDK_API_Output(Module_Name, ret)
            TestACQSDK_API_ErrorInfo(ret)

# API: ACQSDK_StopRecord: OK
def TestACQSDK_API_ACQSDK_StopRecord(objACQSDK_CSDevice_1, para_times):
    Module_Name = sys._getframe().f_code.co_name
    print gDef.Output_Header() + "\t" + "Execute " + str(para_times) + "times."
    while para_times > 0:
        try:
            ret = objACQSDK_CSDevice_1.ACQSDK_StopRecord()
        except:
            print gDef.Output_Header() + "\t" + "Error happens."
        finally:
            TestACQSDK_API_Output(Module_Name, ret)
            TestACQSDK_API_ErrorInfo(ret)
        para_times-=1
        time.sleep(1)

# API: ACQSDK_Capture: OK
def TestACQSDK_API_ACQSDK_Capture(objACQSDK_CSDevice_1, para_lCount):
    Module_Name = sys._getframe().f_code.co_name
    if isinstance(para_lCount, tuple):
        print gDef.Output_Header() + "\t" + "Multiple test data received: " + str(para_lCount)
        for i in range(len(para_lCount)):
            print gDef.Output_Header() + "\t" + "Parameter [" + str(i+1) + "] "
            try:
                ret = objACQSDK_CSDevice_1.ACQSDK_Capture(para_lCount[i])
            except:
                print gDef.Output_Header() + "\t" + "Error happens."
            finally:
                TestACQSDK_API_Output(Module_Name, ret)
                TestACQSDK_API_ErrorInfo(ret)
    else:
        try:
            ret = objACQSDK_CSDevice_1.ACQSDK_Capture(para_lCount)
        except:
            print gDef.Output_Header() + "\t" + "Error happens."
        finally:
            TestACQSDK_API_Output(Module_Name, ret)
            TestACQSDK_API_ErrorInfo(ret)

# API: ACQSDK_CaptureEx
# def TestACQSDK_API_ACQSDK_CaptureEx(objACQSDK_CSDevice_1, para_lCount, para_pImageUnit):

# API: ACQSDK_GetImageData
# def TestACQSDK_API_ACQSDK_GetImageData(objACQSDK_CSDevice_1, para_pImageUnit):

# API: ACQSDK_GetWhiteImage
# def TestACQSDK_API_ACQSDK_GetWhiteImage():

# API: ACQSDK_GetUVImage
# def TestACQSDK_API_ACQSDK_GetUVImage():

# API: ACQSDK_FreeImageUnit
# def TestACQSDK_API_ACQSDK_FreeImageUnit(objACQSDK_CSDevice_1, para_pImageUnit):

# API: ACQSDK_SetLogPathEx
def TestACQSDK_API_ACQSDK_SetLogPathEx(objACQSDK_CSDevice_1, para_path):
    Module_Name = sys._getframe().f_code.co_name
    if isinstance(para_path, tuple):
        print gDef.Output_Header() + "\t" + "Multiple test data received: " + str(para_path)
        for i in range(len(para_path)):
            print gDef.Output_Header() + "\t" + "Parameter [" + str(i+1) + "] " + str(para_path[i])
            try:
                ret = objACQSDK_CSDevice_1.ACQSDK_SetLogPathEx(para_path[i])
            except:
                print gDef.Output_Header() + "\t" + "Error happens."
            finally:
                TestACQSDK_API_Output(Module_Name, ret)
                TestACQSDK_API_ErrorInfo(ret)
    else:
        try:
            ret = objACQSDK_CSDevice_1.ACQSDK_SetLogPathEx(para_path)
        except:
            print gDef.Output_Header() + "\t" + "Error happens."
        finally:
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
