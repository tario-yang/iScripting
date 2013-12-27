# Import required modules
try:
    import os
    import sys
    sys.path.append(os.getcwd() + "\\Module")
    import time
    import win32com.client
    import win32gui
    import TestACQSDK_Module_Global_Definition as gDef
    import TestACQSDK_Module_Init_Environment as Init_Env
    import TestACQSDK_Module_API as API
except ImportError:
    print "Required modules are NOT imported!"
    sys.exit(1)
else:
    print gDef.Output_Header() + "ACQSDK single API test process starts."
    print gDef.Output_Header() + "\t" + "Required modules are imported."

### Test: ACQSDK_Init
def TestACQSDK_Test_Case_API_ACQSDK_Init():
    """
    _test_data = (
        #_test_window,
        #win32gui.FindWindow("Shell_TrayWnd",""),
        None
        #1.0,
        #0,
        #-1,
        #100L,
        #"str"
    )
    """
    _test_data = 0

    API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_data)

### Test: ACQSDK_Uninit
def TestACQSDK_Test_Case_API_ACQSDK_Uninit(para_times):
    API.TestACQSDK_API_ACQSDK_Uninit(_test_object, para_times)

### Test: ACQSDK_StartPlay
def TestACQSDK_Test_Case_API_ACQSDK_StartPlay(para_times):
    API.TestACQSDK_API_ACQSDK_StartPlay(_test_object, para_times)

### Test: ACQSDK_StopPlay
def TestACQSDK_Test_Case_API_ACQSDK_StopPlay(para_times):
    API.TestACQSDK_API_ACQSDK_StopPlay(_test_object, para_times)

### Test: ACQSDK_SetLogPath
def TestACQSDK_API_ACQSDK_SetLogPath():
    _test_data = (
        r"file:///C:/",
        r"file:///C:/test_SetLogPathEx.log",
        r"file://localhost/C:/",
        r"file://localhost/C:/test_SetLogPathEx.log",
        r".",
        r"./test_SetLogPathEx.log",
        r"./Log",
        r"./Log/test_SetLogPathEx.log",
        r"./LogEx",
        r"./LogEx/test_SetLogPathEx.log",
        r"C://",
        r"C://Windows",
        None,
        1.0,
        0,
        -1,
        100L,
        "string"
    )
    API.TestACQSDK_API_ACQSDK_SetLogPath(_test_object, _test_data)

### Test: ACQSDK_SetLogPathEx
def TestACQSDK_API_ACQSDK_SetLogPathEx():
    _test_data = (
        r"file:///C:/",
        r"file:///C:/test_SetLogPathEx.log",
        r"file://localhost/C:/",
        r"file://localhost/C:/test_SetLogPathEx.log",
        r".",
        r"./test_SetLogPathEx.log",
        r"./Log",
        r"./Log/test_SetLogPathEx.log",
        r"./LogEx",
        r"./LogEx/test_SetLogPathEx.log",
        r"C:\\",
        r"C:\\Windows",
        None,
        1.0,
        0,
        -1,
        100L,
        "string"
    )
    API.TestACQSDK_API_ACQSDK_SetLogPathEx(_test_object, _test_data)

### Test Object
_test_object = Init_Env.objACQSDK_CSDevice_1
_test_window = Init_Env.WindowObjectCreate()

### Execution
TestACQSDK_API_ACQSDK_SetLogPathEx()
TestACQSDK_Test_Case_API_ACQSDK_Init()
TestACQSDK_Test_Case_API_ACQSDK_StartPlay(1)