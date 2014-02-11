"""
    This executor is to execute the test cases defined in outside XML file.
"""

# Import required modules
try:
	import os, sys, time
	from xml.etree.ElementTree import ElementTree, Element
	import win32com.client, win32gui
	import TestACQSDK_Module_Global_Definition as GDEF
	import TestACQSDK_Module_API as MAPI
except ImportError:
	GDEF.Logger("One or more required modules are missing!")
	sys.exit(1)

def START(XMLFile):
	# Make sure data source exists
	if not os.path.isfile(XMLFile):
		GDEF.Logger("XML file does not exist!")
		sys.exit(1)

	# Initiate Execution Logger
	GDEF.InitExecLogger()

	# Initiate Execution Reporter
	#GDEF.InitExecReporter()

	# Create COM Object
	try:
		objACQSDK_CSDevice        = GDEF.CreateCOMObject(GDEF.ACQSDK_CSDevice_ProgID)
		objACQSDK_ASImageUnit     = GDEF.CreateCOMObject(GDEF.ACQSDK_ASImageUnit_ProgID)
		objACQSDK_SDKCallbackInfo = GDEF.CreateCOMObject(GDEF.ACQSDK_SDKCallbackInfo_ProgID)
	except:
		GDEF.Logger("Error occurs when creating COM objects...")
		sys.exit(1)
	else:
		GDEF.Logger("COM object has been created.")
		print "Details:"
		print objACQSDK_CSDevice
		print objACQSDK_ASImageUnit
		print objACQSDK_SDKCallbackInfo

	# Read XML file


START(GDEF.ACQSDK_TestCaseXML_SingleAPI)
