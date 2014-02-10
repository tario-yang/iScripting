"""
    This set is to test each ACQSDK API with different parameter
"""

# Import required modules
try:
	import os, sys, time
	sys.path.append(os.getcwd() + r"../Module")
	import win32com.client, win32gui
	import TestACQSDK_Module_Global_Definition as GDEF
	import TestACQSDK_Module_API as MAPI
except ImportError:
	print "One or more required modules are missing!"
	sys.exit(1)

# Create COM Object
try:
	objACQSDK_CSDevice        = GDEF.CreateCOMObject(GDEF.ACQSDK_CSDevice_ProgID)
	objACQSDK_ASImageUnit     = GDEF.CreateCOMObject(GDEF.ACQSDK_ASImageUnit_ProgID)
	objACQSDK_SDKCallbackInfo = GDEF.CreateCOMObject(GDEF.ACQSDK_SDKCallbackInfo_ProgID)
except:
	print GDEF.Output_Header() + "\t" + "Error occurs when creating COM objects..."
	sys.exit(1)
else:
	print GDEF.Output_Header() + "\t" + "COM object has been created."
	print "Details:"
	print objACQSDK_CSDevice
	print objACQSDK_ASImageUnit
	print objACQSDK_SDKCallbackInfo

