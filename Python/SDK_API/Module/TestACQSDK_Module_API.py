import sys

class TestACQSDK_API:

    # Current API name
    API_NAME = sys._getframe().f_code.co_name

    # Print the return value for each API
    def TestACQSDK_API_Return_Output(ret):
        print "Location:\t" + API_NAME
        print "Output:\t" + str(ret)

    # Print the string for API which is not implemented
    def TestACQSDK_API_Not_Implemented():
        print API_NAME + "is not implemented!\n"

    # API: ACQSDK_Init
    def TestACQSDK_API_ACQSDK_Init(objACQSDK_CSDevice, para_hWnd):
        ret = objACQSDK_CSDevice.ACQSDK_Init(para_hWnd)
        TestACQSDK_API_Return_Output(ret)

    # API: ACQSDK_Uninit
    def TestACQSDK_API_ACQSDK_Uninit(objACQSDK_CSDevice):
        ret = objACQSDK_CSDevice.ACQSDK_Uninit()
        TestACQSDK_API_Return_Output(ret)

    # API: ACQSDK_QueryDeviceInfo
    def TestACQSDK_API_ACQSDK_QueryDeviceInfo(objACQSDK_CSDevice, para_pDeviceInfo):
        TestACQSDK_API_Not_Implemented()

    # API: ACQSDK_SetHPWorkMode
    def TestACQSDK_API_ACQSDK_SetHPWorkMode(objACQSDK_CSDevice, para_lWorkMode):
        TestACQSDK_API_Not_Implemented()

    # API: ACQSDK_StartPlay
    def TestACQSDK_API_ACQSDK_StartPlay(objACQSDK_CSDevice):
        ret = objACQSDK_CSDevice.ACQSDK_StartPlay()
        TestACQSDK_API_Return_Output(ret)

    # API: ACQSDK_StopPlay
    def TestACQSDK_API_ACQSDK_StopPlay(objACQSDK_CSDevice):
        ret = objACQSDK_CSDevice.ACQSDK_StopPlay()
        TestACQSDK_API_Return_Output(ret)

    # API: ACQSDK_StartRecord
    def TestACQSDK_API_ACQSDK_StartRecord(objACQSDK_CSDevice, para_file_path):

    # API: ACQSDK_StopRecord
    def TestACQSDK_API_ACQSDK_StopRecord(objACQSDK_CSDevice):

    # API: ACQSDK_Capture
    def TestACQSDK_API_ACQSDK_Capture(objACQSDK_CSDevice, para_lCount):

    # API: ACQSDK_CaptureEx
    def TestACQSDK_API_ACQSDK_CaptureEx(objACQSDK_CSDevice, para_lCount, para_pImageUnit):

    # API: ACQSDK_GetImageData
    def TestACQSDK_API_ACQSDK_GetImageData(objACQSDK_CSDevice, para_pImageUnit):

    # API: ACQSDK_GetWhiteImage
    def TestACQSDK_API_ACQSDK_GetWhiteImage():
        TestACQSDK_API_Not_Implemented()

    # API: ACQSDK_GetUVImage
    def TestACQSDK_API_ACQSDK_GetUVImage():
        TestACQSDK_API_Not_Implemented()

    # API: ACQSDK_FreeImageUnit
    def TestACQSDK_API_ACQSDK_FreeImageUnit(objACQSDK_CSDevice, para_pImageUnit):

    # API: ACQSDK_SetLogPath
    def TestACQSDK_API_ACQSDK_SetLogPath(objACQSDK_CSDevice, para_path):

    # API: ACQSDK_SetLogPathEx
    def TestACQSDK_API_ACQSDK_SetLogPathEx(objACQSDK_CSDevice, para_path):

    # API: ACQSDK_GetSerialNumber
    def TestACQSDK_API_ACQSDK_GetSerialNumber():
        TestACQSDK_API_Not_Implemented()

    # API: ACQSDK_SetSerialNumber
    def TestACQSDK_API_ACQSDK_SetSerialNumber():
        TestACQSDK_API_Not_Implemented()

    # API: ACQSDK_GetFirmwareVersion
    def TestACQSDK_API_ACQSDK_GetFirmwareVersion():
        TestACQSDK_API_Not_Implemented()

    # API: ACQSDK_StartRecordEx
    def TestACQSDK_API_ACQSDK_StartRecordEx(objACQSDK_CSDevice, para_path):

    # API: ACQSDK_UpgradeFirmware
    def TestACQSDK_API_ACQSDK_UpgradeFirmware():
        TestACQSDK_API_Not_Implemented()

    # API: ACQSDK_SaveImage
    def TestACQSDK_API_ACQSDK_SaveImage(objACQSDK_CSDevice, para_file, para_pImageUnit):

    # API: ACQSDK_SetMsgCallback
    def TestACQSDK_API_ACQSDK_SetMsgCallback(objACQSDK_CSDevice, para_pMsgInfo):
        
    