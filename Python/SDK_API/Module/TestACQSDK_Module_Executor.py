"""
    This executor is to execute the test cases defined in outside XML file.
"""

# Import required modules
try:
	import os, sys, time
	from xml.dom import minidom
	import win32com.client, win32gui
	import TestACQSDK_Module_Global_Definition as GDEF
	#import TestACQSDK_Module_TestCase_API as TCAPI
	GDEF.InitExecLogger() # Initiate Execution Logger
	GDEF.InitExecReporter() # Initiate Execution Reporter
except ImportError:
	GDEF.Logger("Error -> One or more required modules are missing!")
	sys.exit(1)
except:
	GDEF.Logger("Error -> Error occurs when initiating Logger and Reporter.")
	sys.exit(1)
else:
	GDEF.Logger("Info -> Initiated.")

def START(XMLFile):
	# Make sure data source exists
	if not os.path.isfile(XMLFile):
		GDEF.Logger("Error -> XML file does not exist!")
		sys.exit(1)

	# Create COM Object
	try:
		objACQSDK_CSDevice        = GDEF.CreateCOMObject(GDEF.ACQSDK_CSDevice_ProgID)
		objACQSDK_ASImageUnit     = GDEF.CreateCOMObject(GDEF.ACQSDK_ASImageUnit_ProgID)
		objACQSDK_SDKCallbackInfo = GDEF.CreateCOMObject(GDEF.ACQSDK_SDKCallbackInfo_ProgID)
	except:
		GDEF.Logger("Error: Error occurs when creating COM objects.")
		sys.exit(1)
	else:
		GDEF.Logger("Info -> COM object has been created.")
		GDEF.Logger("Info -> Details: %r; %r; %r" % (objACQSDK_CSDevice, objACQSDK_ASImageUnit, objACQSDK_SDKCallbackInfo))

	# Read XML file and then execute test
	datasource = minidom.parse(XMLFile)
	ts_list    = datasource.getElementsByTagName("Teststep")
	for ts in ts_list:
		ts_summary = ts.getAttribute("index")
		GDEF.Logger("Test -> %r" % ts_summary)
		para_list  = ts.getElementsByTagName("Parameter")
		execution_list = []
		for para in para_list:
			name  = para.getAttribute("name")
			value = para.getAttribute("value")
			execution_list.append((name, value))
		if execution_list.count == 1:
			pass # execute the test directly
		else:



START(GDEF.ACQSDK_TestCaseXML_API)