import time
import datetime

# definition[variables]
ACQSDK_ProgID  = "ACQSDK.CSDevice.1"

# definition[function]
def Output_Header():
	return "[" + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "]" + "\t"

# definition: Live Video Window
TestACQSDK_LiveVideo_Window_Class    = "TestACQSDK"
TestACQSDK_LiveVideo_Window_Title    = "TestACQSDK: Live Video Display"
TestACQSDK_LiveVideo_Window_Position = (0,0)
TestACQSDK_LiveVideo_Window_Size     = (640,480)