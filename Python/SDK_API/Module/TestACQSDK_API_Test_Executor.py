"""
    This executor is to execute the test cases defined in outside XML file.
"""

# Import required modules
import os, sys, time, gc, threading
import win32com.client
from Tkinter import *
from xml.dom import minidom
import TestACQSDK_Module_Global_Definition as GD
import TestACQSDK_Module_Wrapper as SDKAPI

# Execute
def Worker(api, para_list, expected_result):
	# Execute APIs
	if api == "API0001_ACQSDK_Init":
		if len(para_list) == 0: hWnd = root_id
		else: hWnd = para_list[0]
		ret = SDKAPI.ACQSDK_Init(objACQSDK_CSDevice, hWnd)
		if str(ret[1]) == expected_result: return ("Passed", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0002_ACQSDK_UnInit":
		ret = SDKAPI.ACQSDK_UnInit(objACQSDK_CSDevice)
		if str(ret[1]) == expected_result: return ("Passed", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0003_ACQSDK_OnUpdateLiveWnd":
		ret = SDKAPI.ACQSDK_OnUpdateLiveWnd(objACQSDK_CSDevice)
		if str(ret[1]) == expected_result: return ("Passed", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0004_ACQSDK_QueryDeviceInfo":
		if len(para_list) == 0: pDeviceInfo = objDeviceInfo
		else: pDeviceInfo = para_list[0]
		ret = SDKAPI.ACQSDK_QueryDeviceInfo(objACQSDK_CSDevice, pDeviceInfo)
		if str(ret[1]) == expected_result: return ("Passed", ret[1])
		else: return ("Failed", ret[1])

	# [Not Implemented] elif api == "API0005_ACQSDK_SetHPWorkMode":

	elif api == "API0006_ACQSDK_StartPlay":
		ret = SDKAPI.ACQSDK_StartPlay(objACQSDK_CSDevice)
		if str(ret[1]) == expected_result: return ("Passed", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0008_ACQSDK_StopPlay":
		ret = SDKAPI.ACQSDK_StopPlay(objACQSDK_CSDevice)
		if str(ret[1]) == expected_result: return ("Passed", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0009_ACQSDK_StartRecord":
		if len(para_list) == 0: return ("Failed", "No Parameter Inputted")
		ret = SDKAPI.ACQSDK_StartRecord(objACQSDK_CSDevice, para_list[0])
		if str(ret[1]) == expected_result: return ("Passed", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0010_ACQSDK_StopRecord":
		ret = SDKAPI.ACQSDK_StopRecord(objACQSDK_CSDevice)
		if str(ret[1]) == expected_result: return ("Passed", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0011_ACQSDK_Capture":
		if len(para_list) == 0: pImageUnit = objImageUnit
		else: pImageUnit = para_list[0]
		ret = SDKAPI.ACQSDK_Capture(objACQSDK_CSDevice, pImageUnit)
		if str(ret[1]) == expected_result: return ("Passed", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0012_ACQSDK_GetImageData":
		if len(para_list) == 0: pImageUnit = objImageUnit
		else: pImageUnit = para_list[0]
		ret = SDKAPI.ACQSDK_GetImageData(objACQSDK_CSDevice, pImageUnit)
		if str(ret[1]) == expected_result: return ("Passed", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0013_ACQSDK_SetLogPath":
		if len(para_list) == 0: return ("Failed", "No Parameter Inputted")
		ret = SDKAPI.ACQSDK_SetLogPath(objACQSDK_CSDevice, para_list[0])
		if str(ret[1]) == expected_result: return ("Passed", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0014_ACQSDK_GetSerialNumber":
		ret = SDKAPI.ACQSDK_GetSerialNumber(objACQSDK_CSDevice)
		if isinstance(ret[1], str) and len(ret[1]) >0: return ("Passed", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0015_ACQSDK_SetSerialNumber":
		if len(para_list) == 0: return ("Failed", "No Parameter Inputted")
		ret = SDKAPI.ACQSDK_SetSerialNumber(objACQSDK_CSDevice, para_list[0])
		if str(ret[1]) == expected_result: return ("Passed", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0016_ACQSDK_GetFirmwareVersion":
		ret = SDKAPI.ACQSDK_GetFirmwareVersion(objACQSDK_CSDevice)
		if str(ret[1]) == expected_result: return ("Passed", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0017_ACQSDK_UpgradeFirmware":
		if len(para_list) == 0: return ("Failed", "No Parameter Inputted")
		ret = SDKAPI.ACQSDK_UpgradeFirmware(objACQSDK_CSDevice, para_list[0])
		if str(ret[1]) == expected_result: return ("Passed", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0018_ACQSDK_AbortUpgrade":
		if len(para_list) == 0: return ("Failed", "No Parameter Inputted")
		class FWUpgrade(threading.Thread):
			def __init__(self): threading.Thread.__init__(self)
			def run(self):
				self.path = para_list[0]
				SDKAPI.ACQSDK_UpgradeFirmware(objACQSDK_CSDevice, self.path)
		instance = FWUpgrade()
		instance.setDaemon(True)
		instance.start()
		time.sleep(3)
		ret = SDKAPI.ACQSDK_AbortUpgrade(objACQSDK_CSDevice)
		if str(ret[1]) == expected_result: return ("Passed", ret[1])
		else: return ("Failed", ret[1])

	# [Not Implemented] elif api == "API0019_ACQSDK_UploadFile":

	# [Not Implemented] elif api == "API0020_ACQSDK_DownloadFile":

	elif api == "API0021_ACQSDK_EnableAutoPowerOn":
		if len(para_list) == 0: return ("Failed", "No Parameter Inputted")
		ret = SDKAPI.ACQSDK_EnableAutoPowerOn(objACQSDK_CSDevice, para_list[0])
		if str(ret[1]) == expected_result: return ("Passed", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0022_ACQSDK_GetBrightness":
		ret = SDKAPI.ACQSDK_GetBrightness(objACQSDK_CSDevice)
		if str(ret[1][0]) == expected_result: return ("Passed", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0023_ACQSDK_SetBrightness":
		if len(para_list) == 0: return ("Failed", "No Parameter Inputted")
		ret = SDKAPI.ACQSDK_SetBrightness(objACQSDK_CSDevice, para_list[0])
		if str(ret[1]) == expected_result: return ("Passed", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0024_ACQSDK_GetContrast":
		ret = SDKAPI.ACQSDK_GetContrast(objACQSDK_CSDevice)
		if str(ret[1][0]) == expected_result: return ("Passed", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0025_ACQSDK_SetContrast":
		if len(para_list) == 0: return ("Failed", "No Parameter Inputted")
		ret = SDKAPI.ACQSDK_SetContrast(objACQSDK_CSDevice, para_list[0])
		if str(ret[1]) == expected_result: return ("Passed", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0026_ACQSDK_SetPowerlineFrequency":
		if len(para_list) == 0: return ("Failed", "No Parameter Inputted")
		ret = SDKAPI.ACQSDK_SetPowerlineFrequency(objACQSDK_CSDevice, para_list[0])
		if str(ret[1]) == expected_result: return ("Passed", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0027_ACQSDK_GetPowerlineFrequency":
		ret = SDKAPI.ACQSDK_GetPowerlineFrequency(objACQSDK_CSDevice)
		if str(ret[1][0]) == expected_result: return ("Passed", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0028_ACQSDK_EnableAutoPowerOff":
		if len(para_list) == 0: return ("Failed", "No Parameter Inputted")
		ret = SDKAPI.ACQSDK_EnableAutoPowerOff(objACQSDK_CSDevice, para_list[0])
		if str(ret[1]) == expected_result: return ("Passed", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0029_ACQSDK_SetAutoPowerOffTime":
		if len(para_list) == 0: return ("Failed", "No Parameter Inputted")
		ret = SDKAPI.ACQSDK_SetAutoPowerOffTime(objACQSDK_CSDevice, para_list[0])
		if str(ret[1]) == expected_result: return ("Passed", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0030_ACQSDK_SetEnableSleep":
		if len(para_list) == 0: return ("Failed", "No Parameter Inputted")
		ret = SDKAPI.ACQSDK_SetEnableSleep(objACQSDK_CSDevice, para_list[0])
		if str(ret[1]) == expected_result: return ("Passed", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0031_ACQSDK_SetSleepTime":
		if len(para_list) == 0: return ("Failed", "No Parameter Inputted")
		ret = SDKAPI.ACQSDK_SetSleepTime(objACQSDK_CSDevice, para_list[0])
		if str(ret[1]) == expected_result: return ("Passed", ret[1])
		else: return ("Failed", ret[1])

	# [Removed] elif api == "API0032_ACQSDK_SetSystemTime":

	elif api == "API0033_ACQSDK_SetMirrorFlag":
		if len(para_list) == 0: return ("Failed", "No Parameter Inputted")
		ret = SDKAPI.ACQSDK_SetMirrorFlag(objACQSDK_CSDevice, para_list[0])
		if str(ret[1]) == expected_result: return ("Passed", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0034_ACQSDK_GetMirrorFlag":
		ret = SDKAPI.ACQSDK_GetMirrorFlag(objACQSDK_CSDevice)
		if isinstance(ret[1], int): return ("ManualCheck", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0035_ACQSDK_SetRotationFlag":
		if len(para_list) == 0: return ("Failed", "No Parameter Inputted")
		ret = SDKAPI.ACQSDK_SetRotationFlag(objACQSDK_CSDevice, para_list[0])
		if str(ret[1]) == expected_result: return ("Passed", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0036_ACQSDK_GetRotationFlag":
		ret = SDKAPI.ACQSDK_GetRotationFlag(objACQSDK_CSDevice)
		if isinstance(ret[1], int): return ("ManualCheck", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0037_ACQSDK_GetSDKVersion":
		ret = SDKAPI.ACQSDK_GetSDKVersion(objACQSDK_CSDevice)
		if isinstance(ret[1], str) and len(ret[1]) >0: return ("Passed", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0038_ACQSDK_GetEnableAutoPowerOff":
		ret = SDKAPI.ACQSDK_GetEnableAutoPowerOff(objACQSDK_CSDevice)
		if isinstance(ret[1], int): return ("ManualCheck", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0039_ACQSDK_GetEnableAutoPowerOn":
		ret = SDKAPI.ACQSDK_GetEnableAutoPowerOn(objACQSDK_CSDevice)
		if isinstance(ret[1], int): return ("ManualCheck", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0040_ACQSDK_GetAutoPowerOffTime":
		ret = SDKAPI.ACQSDK_GetAutoPowerOffTime(objACQSDK_CSDevice)
		if isinstance(ret[1], int): return ("ManualCheck", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0041_ACQSDK_GetEnableSleep":
		ret = SDKAPI.ACQSDK_GetEnableSleep(objACQSDK_CSDevice)
		if isinstance(ret[1], int): return ("ManualCheck", ret[1])
		else: return ("Failed", ret[1])

	elif api == "API0042_ACQSDK_GetSleepTime":
		ret = SDKAPI.ACQSDK_GetSleepTime(objACQSDK_CSDevice)
		if isinstance(ret[1], int): return ("ManualCheck", ret[1])
		else: return ("Failed", ret[1])
	else:
		return ("Inputted XML defines wrong API name", None)

# Function to invoke pointed test case
def DataParser(action, debug = 0):
	# Get parameter value
	arg0 = action[0] # Test Summary
	arg1 = action[1] # Test Case Name
	arg2 = action[2] # Expected Result
	arg3 = action[3] # Parameter Line

	# Debug Info
	if debug == 1:
		print "-"*60
		print "Debug Info:"
		print "\tTest Summary:\t\t%s"   % arg0
		print "\tTest Case Name:\t\t%s" % arg1
		print "\tExpected Result:\t%s"  % arg2
		print "\tParameter Line:\t\t%r" % arg3
		print "-"*60

	# Parse parameter
	para_list = []
	if arg3 == "": pass
	else:
		parameter_line  = arg3.split(";")
		for parameter in parameter_line:
			exec_string = ""
			x = parameter.split("=")
			if isinstance(x, list):
				para_list.append("")
			elif x[1].upper() == "TRUE": # is boolean
				para_list.append(bool(1))
			elif x[1].upper() == "FALSE": # is boolean
				para_list.append(bool(0))
			elif x[1].upper() == x[1].lower() and x[1].count(".") == 0: # is int
				para_list.append(int(x[1]))
			elif x[1].upper() == x[1].lower() and x[1].count(".") == 1: # is float
				para_list.append(float(x[1]))
			else:
				para_list.append(str(x[1]))
	return (arg1, para_list, arg2)

# Test and return the result of the step
def Action(action_list):
	working_list = DataParser(action_list, 0)
	return Worker(working_list[0], working_list[1], working_list[2])

# Start
GD.InitExecLogger()
GD.Logger("Info -> Start API Testing.")
GD.Logger("Info -> ========================================================== >> Preparation")

switch = "full"

# Function to get XML data and then parse it, finally, trigger the test.
# 	Make sure data source exists
#		Get XML list
if switch == "full":
	GD.Logger("Info -> Enter Full Testing Mode, reading all XML files under %s." % GD.ACQSDK_TestCaseXML_APIDir)
	location = GD.ACQSDK_TestCaseXML_APIDir
	try:    datasource_list = os.listdir(location)
	except:
		GD.Logger("Error -> Exception happens when getting XML file list!")
		sys.exit(1)
	else:
		#	List shall have content
		if len(datasource_list) == 0:
			GD.Logger("Error -> There is no XML file existed!")
			sys.exit(1)
		#	Remove non-XML file
		for i in datasource_list:
			ext = i.split(".")
			if len(ext) ==0: datasource_list.remove(i)
			elif ext[-1].upper() != "XML": datasource_list.remove(i)
elif switch == "list": pass # 1. Check whether file exists and is empty or not; 2. Convert content to a list
GD.Logger("Info -> data source list is generated, %r" % datasource_list)

# Logger Directory
DIR = GD.ACQSDK_OutputDir + "/" + "Test_Result_" + GD.Output_Header("%Y%m%d%H%M%S")
try: os.mkdir(DIR)
except:
	GD.Logger("Error -> Fail to create directory to store test result(s)!")
	sys.exit(1)
else:
	GD.Logger("Info -> Directory for storing test result(s) is created.")
	GD.Logger("Info -> ========================================================== >> Test Output")

# Parse data
for datasource in datasource_list:
	# Preparation
	GD.Logger("")
	GD.Logger("Info -> Input -> %r" % datasource)
	#	Logger -> Result, init
	LoggerResult = DIR + "/" + datasource.partition(".")[0] + "_Result.xml"
	with open(LoggerResult, "w") as f:
		f.write('<?xml version="1.0" encoding="utf-8"?>\n')
		f.write('<TestCase name="%s">\n' % datasource.partition(".")[0])

	#	Create a handler
	root_id = Tk().winfo_id()

	#	Create ACQSDK COM object
	try:
		objACQSDK_CSDevice = win32com.client.Dispatch(GD.ACQSDK_CSDevice_ProgID)
		objImageUnit       = win32com.client.Dispatch(GD.ACQSDK_ASImageUnit_ProgID)
		objDeviceInfo      = win32com.client.Dispatch(GD.ACQSDK_ASDeviceInfor_ProgID)
	except:
		GD.Logger("Error -> Fail to create COM object.")
		sys.exit(1)
	# else:
	# 	GD.Logger("Info -> COM object created, %r" % objACQSDK_CSDevice)
	# 	GD.Logger("Info -> COM object created, %r" % objImageUnit)
	# 	GD.Logger("Info -> COM object created, %r" % objDeviceInfo)

	#	if Not ACQSDK_Init, it needs to trigger an Init
	if datasource.find("ACQSDK_Init") == -1: SDKAPI.ACQSDK_Init(objACQSDK_CSDevice, root_id)

	#	Restore result
	test_result = []

	# Parse XML
	datasource_xml = minidom.parse("%s/%s" % (location, datasource))
	ts_list        = datasource_xml.getElementsByTagName(GD.ACQSDK_TestStepTag)
	for ts in ts_list:
		# Parameter to transfer to the next function
		#	1st element: Test Summary
		#	2nd element: Test Case Name
		#	3rd element: Expected Result
		#	4th element: Parameter List
		action = []
			# Test Summary
		action.append(ts.getAttribute(GD.ACQSDK_TestSummaryTag))
			# Fetch all parameters (include APIName, Parameter and Return)
		para_list  = ts.getElementsByTagName(GD.ACQSDK_ParameterTag)
		name_list  = []
		value_list = []
		for para in para_list:
			name  = str(para.getAttribute(GD.ACQSDK_ParameterNameTag))
			value = str(para.getAttribute(GD.ACQSDK_ParameterValueTag))
			name_list.append(name)
			value_list.append(value)
		if len(name_list) > 0 and len(value_list) > 0 and len(name_list) == len(value_list):
			# Test Case Name
			x = name_list.index(GD.ACQSDK_TestCase)
			action.append(value_list.pop(x))
			name_list.pop(x)
			del x
			# Expected Result
			x = name_list.index(GD.ACQSDK_ExpectedResult)
			action.append(value_list.pop(x))
			name_list.pop(x)
			del x
			# Parameter(s)
			para_line = ""
			while len(name_list) > 0:
				if para_line == "": para_line = name_list.pop() + "=" + value_list.pop()
				else: para_line = name_list.pop() + "=" + value_list.pop() + ";" + para_line
			# Parameter List
			action.append(para_line)
			GD.Logger("Info -> Parameter -> %s" % str(action))

			# Trigger the execution
			test_result.append((action[0], Action(action)))
		else:
			GD.Logger("Error -> Exception occurs when fetching parameters from XML file, %r." % datasource)
			GD.Logger("Error -> Fetched %r list and %r list is not correct (length)." % (GD.ACQSDK_ParameterNameTag, GD.ACQSDK_ParameterValueTag))
			sys.exit(1)

	# Check & Output Result
	GD.Logger("Info -> Get Result -> %r" % test_result)
	result_collection = []
	if len(test_result) > 0:
		for i in test_result:
			with open(LoggerResult, "a+") as f: f.write('\t<Teststep name="%s" value="%s" />\n' % (i[0], str(i[1])))
			if i[1] is None: result_collection.append(None)
			else: result_collection.append(i[1][0])
		with open(LoggerResult, "a+") as f: f.write('</TestCase>\n')
		failednum = result_collection.count("Failed")
		nonenum   = result_collection.count(None)

	else:
		GD.Logger("Error -> Exception occurs when fetching test result list, %r." % test_result)

	# Clean
	try:
		del objACQSDK_CSDevice
		del objImageUnit
		del objDeviceInfo
		del root_id
		gc.collect()
	except:
		GD.Logger("Error -> Fail to remove the created COM object.")
	# else:
	# 	GD.Logger("Info -> COM objects are removed.")

# End
GD.Logger("")
GD.Logger("Info -> END")

# Open file
os.system("notepad.exe .\\Output\\ACQSDK_Execution.csv")

# Close
os.system("taskkill /f /im python.exe")