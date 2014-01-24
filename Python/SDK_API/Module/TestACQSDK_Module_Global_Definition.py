# Import required modules
try:
	import os
	import sys
except ImportError:
	print "One or more required modules are missing!"
	sys.exit(1)

# ProgID of each CoClass
ACQSDK_CSDevice_ProgID        = "ACQSDK.CSDevice.1"
ACQSDK_ASImageUnit_ProgID     = "ACQSDK.ASImageUnit.1"
ACQSDK_SDKCallbackInfo_ProgID = "ACQSDK.SDKCallbackInfo.1"

# definition: Live Video Window
TestACQSDK_LiveVideo_Window_Class	= "TestACQSDK"
TestACQSDK_LiveVideo_Window_Title	= "TestACQSDK: Live Video Display"
TestACQSDK_LiveVideo_Window_Position = (0,0)
TestACQSDK_LiveVideo_Window_Size	 = (640,480)