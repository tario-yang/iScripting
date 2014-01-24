"""
    This set is to test each ACQSDK API with different parameter
"""

# Import required modules
try:
	import os
	import sys
	sys.path.append(os.getcwd() + "\\Module")
	import time
	import win32com.client
	import win32gui
	import TestACQSDK_Module_Global_Definition as GDef
	import TestACQSDK_Module_Init_Environment as INIT
	import TestACQSDK_Module_API as MAPI
except ImportError:
	print "One or more required modules are missing!"
	sys.exit(1)

# Create COM Object
objACQSDK_CSDevice        = INIT.CreateCOMObject(GDef.ACQSDK_CSDevice_ProgID)
objACQSDK_ASImageUnit     = INIT.CreateCOMObject(GDef.ACQSDK_ASImageUnit_ProgID)
objACQSDK_SDKCallbackInfo = INIT.CreateCOMObject(GDef.ACQSDK_SDKCallbackInfo_ProgID)

# Create Live Video Window
objWindow = INIT.WindowObjectCreate()
