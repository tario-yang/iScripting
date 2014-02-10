"""
    This executor is to execute the test cases defined in outside XML file.
"""

def START():
	# Initiate Execution Logger
	GDEF.InitExecLogger()

	# Import required modules
	try:
		import time
		import win32com.client, win32gui
		import TestACQSDK_Module_Global_Definition as GDEF
		import TestACQSDK_Module_API as MAPI
	except ImportError:
		GDEF.Logger("One or more required modules are missing!")
		sys.exit(1)

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
		GDEF.Logger("Details:")
		GDEF.Logger(objACQSDK_CSDevice)
		GDEF.Logger(objACQSDK_ASImageUnit)
		GDEF.Logger(objACQSDK_SDKCallbackInfo)
