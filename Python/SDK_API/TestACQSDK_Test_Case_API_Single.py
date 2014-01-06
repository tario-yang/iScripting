"""
This set is to test each ACQSDK API with following policy,
 - within a minimum combination
 - single
 - with different parameter
"""

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
	print gDef.Output_Header() + "\t" + "Required modules are imported.\n"
	_test_object  = Init_Env.objACQSDK_CSDevice_1
	_test_window  = Init_Env.WindowObjectCreate()
	_test_log_dir = r"./Log"

### Test: ACQSDK_Init
def TestACQSDK_Test_Case_API_ACQSDK_Init():
	Module_Name = sys._getframe().f_code.co_name

	### ### +

	_test_data = (
		_test_window,
		win32gui.FindWindow("Shell_TrayWnd",""),
		None,
		1.0,
		0,
		-1,
		100L,
		"str"
	)

	print Module_Name + " :: " + "Test Case #" + "1"
	if isinstance(_test_data, tuple):
		for i in range(len(_test_data)):
			API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_data[i])
			time.sleep(1)
			API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
			time.sleep(1)
	else:
		print "Incorrect format of test data (shall be tuple)."

	_test_data = 10

	print Module_Name + " :: " + "Test Case #" + "2"
	while _test_data > 0 :
		API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_data)
		time.sleep(1)
		_test_data-=1
	API.TestACQSDK_API_ACQSDK_UnInit(_test_object)

	### ### -
"""
	_test_data = 5

	print Module_Name + " :: " + "Exception Test Case #" + "1"
	while _test_data > 0 :
		gDef.USBCameraDisable()
		API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_data)
		gDef.USBCameraEnable()
		_test_data-=1

	print Module_Name + " :: " + "Exception Test Case #" + "2"
	gDef.USBCameraDisable()
	while _test_data > 0 :
		API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_data)
		_test_data-=1
	gDef.USBCameraEnable()
"""
### Test: ACQSDK_Uninit
def TestACQSDK_Test_Case_API_ACQSDK_Uninit():
	Module_Name = sys._getframe().f_code.co_name

	### ### +

	_test_data = 10

	print Module_Name + " :: " + "Test Case #" + "1"
	while _test_data > 0 :
		API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_window)
		time.sleep(1)
		API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
		time.sleep(1)
		_test_data-=1

	_test_data = 10

	print Module_Name + " :: " + "Test Case #" + "2"
	while _test_data > 0 :
		API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
		time.sleep(1)
		_test_data-=1

	### ### -
"""
	_test_data = 5

	print Module_Name + " :: " + "Exception Test Case #" + "1"
	while _test_data > 0 :
		gDef.USBCameraDisable()
		API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
		gDef.USBCameraEnable()
		_test_data-=1
"""
### Test: ACQSDK_StartPlay
def TestACQSDK_Test_Case_API_ACQSDK_StartPlay():
	Module_Name = sys._getframe().f_code.co_name

	### ### +

	_test_data = 10

	print Module_Name + " :: " + "Test Case #" + "1"
	while _test_data > 0 :
		API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_window)
		time.sleep(1)
		API.TestACQSDK_API_ACQSDK_StartPlay(_test_object)
		time.sleep(5)
		API.TestACQSDK_API_ACQSDK_StopPlay(_test_object)
		time.sleep(1)
		API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
		time.sleep(1)
		_test_data-=1

	_test_data = 10

	print Module_Name + " :: " + "Test Case #" + "2"
	while _test_data > 0 :
		API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_window)
		time.sleep(1)
		API.TestACQSDK_API_ACQSDK_StartPlay(_test_object)
		time.sleep(5)
		API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
		time.sleep(1)
		_test_data-=1

	_test_data = 10

	print Module_Name + " :: " + "Test Case #" + "3"
	API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_window)
	time.sleep(1)
	while _test_data > 0 :
		API.TestACQSDK_API_ACQSDK_StartPlay(_test_object)
		time.sleep(5)
		API.TestACQSDK_API_ACQSDK_StopPlay(_test_object)
		time.sleep(1)
		_test_data-=1
	API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
	time.sleep(1)

	_test_data = 10

	print Module_Name + " :: " + "Test Case #" + "4"
	while _test_data > 0 :
		API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_window)
		time.sleep(1)
		API.TestACQSDK_API_ACQSDK_StartPlay(_test_object)
		time.sleep(5)
		API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
		time.sleep(1)
		_test_data-=1

	_test_data = 10

	print Module_Name + " :: " + "Test Case #" + "5"
	API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_window)
	time.sleep(1)
	while _test_data > 0 :
		API.TestACQSDK_API_ACQSDK_StartPlay(_test_object)
		time.sleep(5)
		_test_data-=1
	API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
	time.sleep(1)

	### ### -

	_test_data = 5

	print Module_Name + " :: " + "Exception Test Case #" + "1"
	while _test_data > 0 :
		API.TestACQSDK_API_ACQSDK_StartPlay(_test_object)
		time.sleep(5)
		_test_data-=1
"""
	_test_data = 5

	print Module_Name + " :: " + "Exception Test Case #" + "2"
	API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_window)
	time.sleep(1)
	gDef.USBCameraDisable()
	while _test_data > 0 :
		API.TestACQSDK_API_ACQSDK_StartPlay(_test_object)
		time.sleep(5)
		_test_data-=1
	gDef.USBCameraEnable()
"""
### Test: ACQSDK_StopPlay
def TestACQSDK_Test_Case_API_ACQSDK_StopPlay():
	Module_Name = sys._getframe().f_code.co_name

	### ### +

	_test_data = 10

	print Module_Name + " :: " + "Test Case #" + "1"
	while _test_data > 0 :
		API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_window)
		time.sleep(1)
		API.TestACQSDK_API_ACQSDK_StartPlay(_test_object)
		time.sleep(5)
		API.TestACQSDK_API_ACQSDK_StopPlay(_test_object)
		time.sleep(1)
		API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
		time.sleep(1)
		_test_data-=1

	print Module_Name + " :: " + "Test Case #" + "2"
	API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_window)
	time.sleep(1)
	while _test_data > 0 :
		API.TestACQSDK_API_ACQSDK_StartPlay(_test_object)
		time.sleep(5)
		API.TestACQSDK_API_ACQSDK_StopPlay(_test_object)
		time.sleep(1)
		_test_data-=1
	API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
	time.sleep(1)

	print Module_Name + " :: " + "Test Case #" + "3"
	API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_window)
	time.sleep(1)
	API.TestACQSDK_API_ACQSDK_StartPlay(_test_object)
	time.sleep(5)
	while _test_data > 0 :
		API.TestACQSDK_API_ACQSDK_StopPlay(_test_object)
		time.sleep(1)
		_test_data-=1
	API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
	time.sleep(1)

	print Module_Name + " :: " + "Test Case #" + "3"
	API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_window)
	time.sleep(1)
	while _test_data > 0 :
		API.TestACQSDK_API_ACQSDK_StopPlay(_test_object)
		time.sleep(1)
		_test_data-=1
	API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
	time.sleep(1)

	### ### -

	_test_data = 5

	print Module_Name + " :: " + "Exception Test Case #" + "1"
	while _test_data > 0 :
		API.TestACQSDK_API_ACQSDK_StopPlay(_test_object)
		time.sleep(5)
		_test_data-=1
"""
	_test_data = 5

	print Module_Name + " :: " + "Exception Test Case #" + "2"
	API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_window)
	time.sleep(1)
	API.TestACQSDK_API_ACQSDK_StartPlay(_test_object)
	time.sleep(5)
	gDef.USBCameraDisable()
	while _test_data > 0 :
		API.TestACQSDK_API_ACQSDK_StopPlay(_test_object)
		time.sleep(5)
		_test_data-=1
	gDef.USBCameraEnable()
"""
### Test: ACQSDK_SetLogPathEx
def TestACQSDK_Test_Case_API_ACQSDK_SetLogPathEx():
	Module_Name = sys._getframe().f_code.co_name

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

	print Module_Name + " :: " + "Test Case #" + "1"
	if isinstance(_test_data, tuple):
		for i in range(len(_test_data)):
			API.TestACQSDK_API_ACQSDK_SetLogPathEx(_test_object, _test_data[i])
			time.sleep(1)
	else:
		print "Incorrect format of test data (shall be tuple)."

	print Module_Name + " :: " + "Test Case #" + "2"
	if isinstance(_test_data, tuple):
		for i in range(len(_test_data)):
			API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_window)
			time.sleep(1)
			API.TestACQSDK_API_ACQSDK_SetLogPathEx(_test_object, _test_data[i])
			time.sleep(1)
			API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
			time.sleep(1)
	else:
		print "Incorrect format of test data (shall be tuple)."

	print Module_Name + " :: " + "Test Case #" + "3"
	if isinstance(_test_data, tuple):
		for i in range(len(_test_data)):
			API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
			time.sleep(1)
			API.TestACQSDK_API_ACQSDK_SetLogPathEx(_test_object, _test_data)
			time.sleep(1)
	else:
		print "Incorrect format of test data (shall be tuple)."

### Test: ACQSDK_StartRecordEx
def TestACQSDK_Test_Case_API_ACQSDK_StartRecordEx():
	Module_Name = sys._getframe().f_code.co_name

	### ### +

	_test_data = (
		r"file:///C:/",
		r"file:///C:/test_SetLogPathEx.avi",
		r"file://localhost/C:/",
		r"file://localhost/C:/test_SetLogPathEx.avi",
		r".",
		r"./test_SetLogPathEx.avi",
		r"./Log",
		r"./Log/test_SetLogPathEx.avi",
		r"./LogEx",
		r"./LogEx/test_SetLogPathEx.avi",
		r"C://",
		r"C://Windows",
		None,
		1.0,
		0,
		-1,
		100L,
		"string"
	)

	print Module_Name + " :: " + "Test Case #" + "1"
	if isinstance(_test_data, tuple):
		for i in range(len(_test_data)):
			API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_window)
			time.sleep(1)
			API.TestACQSDK_API_ACQSDK_StartPlay(_test_object)
			time.sleep(1)
			API.TestACQSDK_API_ACQSDK_StartRecordEx(_test_object, _test_data[i])
			time.sleep(5)
			API.TestACQSDK_API_ACQSDK_StopRecord(_test_object)
			time.sleep(1)
			API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
			time.sleep(1)
	else:
		print "Incorrect format of test data (shall be tuple)."

	print Module_Name + " :: " + "Test Case #" + "2"
	if isinstance(_test_data, tuple):
		for i in range(len(_test_data)):
			API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_window)
			time.sleep(1)
			API.TestACQSDK_API_ACQSDK_StartPlay(_test_object)
			time.sleep(1)
			API.TestACQSDK_API_ACQSDK_StartRecordEx(_test_object, _test_data[i])
			time.sleep(5)
			API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
			time.sleep(1)
	else:
		print "Incorrect format of test data (shall be tuple)."

	print Module_Name + " :: " + "Test Case #" + "3"
	API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_window)
	time.sleep(1)
	API.TestACQSDK_API_ACQSDK_StartPlay(_test_object)
	time.sleep(1)
	if isinstance(_test_data, tuple):
		for i in range(len(_test_data)):
			API.TestACQSDK_API_ACQSDK_StartRecordEx(_test_object, _test_data[i])
			time.sleep(5)
			API.TestACQSDK_API_ACQSDK_StopRecord(_test_object)
			time.sleep(1)
	else:
		print "Incorrect format of test data (shall be tuple)."
	API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
	time.sleep(1)

	print Module_Name + " :: " + "Test Case #" + "4"
	API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_window)
	time.sleep(1)
	API.TestACQSDK_API_ACQSDK_StartPlay(_test_object)
	time.sleep(1)
	if isinstance(_test_data, tuple):
		for i in range(len(_test_data)):
			API.TestACQSDK_API_ACQSDK_StartRecordEx(_test_object, _test_data[i])
			time.sleep(5)
	else:
		print "Incorrect format of test data (shall be tuple)."
	API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
	time.sleep(1)

	### ### -

	_test_data = "."

	print Module_Name + " :: " + "Exception Test Case #" + "1"
	for i in [1,2,3,4,5]:
		API.TestACQSDK_API_ACQSDK_StartRecordEx(_test_object, _test_data)
		time.sleep(5)

	print Module_Name + " :: " + "Exception Test Case #" + "2"
	for i in [1,2,3,4,5]:
		API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_window)
		time.sleep(1)
		API.TestACQSDK_API_ACQSDK_StartRecordEx(_test_object, _test_data)
		time.sleep(5)
		API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
		time.sleep(1)

	print Module_Name + " :: " + "Exception Test Case #" + "3"
	for i in [1,2,3,4,5]:
		API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_window)
		time.sleep(1)
		API.TestACQSDK_API_ACQSDK_StartPlay(_test_object)
		time.sleep(1)
		API.TestACQSDK_API_ACQSDK_StopPlay(_test_object)
		time.sleep(1)
		API.TestACQSDK_API_ACQSDK_StartRecordEx(_test_object, _test_data)
		time.sleep(5)
		API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
		time.sleep(1)

	print Module_Name + " :: " + "Exception Test Case #" + "4"
	for i in [1,2,3,4,5]:
		API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_window)
		time.sleep(1)
		API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
		time.sleep(1)
		API.TestACQSDK_API_ACQSDK_StartRecordEx(_test_object, _test_data)
		time.sleep(5)

	print Module_Name + " :: " + "Exception Test Case #" + "5"
	for i in [1,2,3,4,5]:
		API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_window)
		time.sleep(1)
		gDef.USBCameraDisable()
		API.TestACQSDK_API_ACQSDK_StartRecordEx(_test_object, _test_data)
		time.sleep(5)
		API.TestACQSDK_API_ACQSDK_StopRecord(_test_object)
		time.sleep(1)
		API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
		time.sleep(1)
		gDef.USBCameraEnable()
"""
	print Module_Name + " :: " + "Exception Test Case #" + "6"
	for i in [1,2,3,4,5]:
		API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_window)
		time.sleep(1)
		API.TestACQSDK_API_ACQSDK_StartPlay(_test_object)
		time.sleep(1)
		gDef.USBCameraDisable()
		API.TestACQSDK_API_ACQSDK_StartRecordEx(_test_object, _test_data)
		time.sleep(5)
		API.TestACQSDK_API_ACQSDK_StopRecord(_test_object)
		time.sleep(1)
		API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
		time.sleep(1)
		gDef.USBCameraEnable()
"""
### Test: ACQSDK_StopRecord
def TestACQSDK_Test_Case_API_ACQSDK_StopRecord():
	Module_Name = sys._getframe().f_code.co_name

	### ### +

	_test_data = 10

	print Module_Name + " :: " + "Test Case #" + "1"
	while _test_data > 0 :
		API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_window)
		time.sleep(1)
		API.TestACQSDK_API_ACQSDK_StartPlay(_test_object)
		time.sleep(1)
		API.TestACQSDK_API_ACQSDK_StartRecordEx(_test_object, ".")
		time.sleep(5)
		API.TestACQSDK_API_ACQSDK_StopRecord(_test_object)
		time.sleep(1)
		API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
		time.sleep(1)
		_test_data-=1

	print Module_Name + " :: " + "Test Case #" + "2"
	API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_window)
	time.sleep(1)
	API.TestACQSDK_API_ACQSDK_StartPlay(_test_object)
	time.sleep(1)
	while _test_data > 0 :
		API.TestACQSDK_API_ACQSDK_StartRecordEx(_test_object, ".")
		time.sleep(5)
		API.TestACQSDK_API_ACQSDK_StopRecord(_test_object)
		time.sleep(1)
		_test_data-=1
	API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
	time.sleep(1)

	print Module_Name + " :: " + "Test Case #" + "3"
	API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_window)
	time.sleep(1)
	API.TestACQSDK_API_ACQSDK_StartPlay(_test_object)
	time.sleep(1)
	API.TestACQSDK_API_ACQSDK_StartRecordEx(_test_object, ".")
	time.sleep(5)
	while _test_data > 0 :
		API.TestACQSDK_API_ACQSDK_StopRecord(_test_object)
		time.sleep(1)
		_test_data-=1
	API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
	time.sleep(1)

	print Module_Name + " :: " + "Test Case #" + "4"
	API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_window)
	time.sleep(1)
	API.TestACQSDK_API_ACQSDK_StartPlay(_test_object)
	time.sleep(1)
	while _test_data > 0 :
		API.TestACQSDK_API_ACQSDK_StopRecord(_test_object)
		time.sleep(1)
		_test_data-=1
	API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
	time.sleep(1)

	### ### -

	_test_data = 5

	print Module_Name + " :: " + "Exception Test Case #" + "1"
	while _test_data > 0 :
		API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_window)
		time.sleep(1)
		API.TestACQSDK_API_ACQSDK_StartPlay(_test_object)
		time.sleep(1)
		API.TestACQSDK_API_ACQSDK_StopRecord(_test_object)
		time.sleep(1)
		API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
		time.sleep(1)
		_test_data-=1

	_test_data = 5

	print Module_Name + " :: " + "Exception Test Case #" + "2"
	while _test_data > 0 :
		API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_window)
		time.sleep(1)
		API.TestACQSDK_API_ACQSDK_StopRecord(_test_object)
		time.sleep(1)
		API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
		time.sleep(1)
		_test_data-=1
"""
	_test_data = 5

	print Module_Name + " :: " + "Exception Test Case #" + "3"
	while _test_data > 0 :
		API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_window)
		time.sleep(1)
		API.TestACQSDK_API_ACQSDK_StartPlay(_test_object)
		time.sleep(1)
		gDef.USBCameraDisable()
		API.TestACQSDK_API_ACQSDK_StartRecordEx(_test_object, ".")
		time.sleep(5)
		API.TestACQSDK_API_ACQSDK_StopRecord(_test_object)
		time.sleep(1)
		API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
		time.sleep(1)
		_test_data-=1
		gDef.USBCameraEnable()

	print Module_Name + " :: " + "Exception Test Case #" + "4"
	while _test_data > 0 :
		API.TestACQSDK_API_ACQSDK_Init(_test_object, _test_window)
		time.sleep(1)
		gDef.USBCameraDisable()
		API.TestACQSDK_API_ACQSDK_StartRecordEx(_test_object, ".")
		time.sleep(5)
		API.TestACQSDK_API_ACQSDK_StopRecord(_test_object)
		time.sleep(1)
		API.TestACQSDK_API_ACQSDK_UnInit(_test_object)
		time.sleep(1)
		_test_data-=1
		gDef.USBCameraEnable()
"""
### Set SDK's log
API.TestACQSDK_API_ACQSDK_SetLogPathEx(_test_object, _test_log_dir)

### Test Case Execution
