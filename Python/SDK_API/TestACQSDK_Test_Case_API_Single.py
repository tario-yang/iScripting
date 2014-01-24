"""
    This set is to test each ACQSDK API with different parameter
"""

# Import required modules
try:
	import os, sys, time
	sys.path.append(os.getcwd() + "\\Module")
	import win32com.client, win32gui
	import TestACQSDK_Module_Global_Definition as GDef
	import TestACQSDK_Module_Init_Environment as INIT
	import TestACQSDK_Module_API as MAPI
except ImportError:
	print "One or more required modules are missing!"
	sys.exit(1)

# Create COM Object
try:
	objACQSDK_CSDevice        = INIT.CreateCOMObject(GDef.ACQSDK_CSDevice_ProgID)
	objACQSDK_ASImageUnit     = INIT.CreateCOMObject(GDef.ACQSDK_ASImageUnit_ProgID)
	objACQSDK_SDKCallbackInfo = INIT.CreateCOMObject(GDef.ACQSDK_SDKCallbackInfo_ProgID)
except:
	print INIT.Output_Header() + "\t" + "Error occurs when creating COM objects..."
	sys.exit(1)
else:
	print INIT.Output_Header() + "\t" + "COM object has been created."
	print "Details:"
	print objACQSDK_CSDevice
	print objACQSDK_ASImageUnit
	print objACQSDK_SDKCallbackInfo
	print

# Create Live Video Window
import thread
thread.start_new_thread(INIT.WindowObjectCreate, ())