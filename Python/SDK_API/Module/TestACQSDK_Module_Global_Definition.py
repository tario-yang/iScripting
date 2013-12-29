# Import required modules
try:
    import os
    import sys
    import time
    import datetime
    import platform
except ImportError:
    print "Required modules are NOT imported!"
    sys.exit(1)

# definition[variables]
ACQSDK_ProgID   = "ACQSDK.CSDevice.1"
Camera_Identity = "@ 'USB\VID_041E&PID_4059'"

# definition[function]
### Output Header for console
def Output_Header():
	return "[" + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "]" + "\t"
### Check system and define which devcon to use
def devcon():
    pwd = os.getcwd
    arch_type = platform.architecture()
    if arch_type[0] == "32bit" :
        devcon = pwd + "\\Tools\\devcon\\i386\\devcon.exe" + " "
    else:
        if arch_type[0] == "64bit" :
            devcon = pwd + "\\Tools\\devcon\\ia64\\devcon.exe" + " "
        else:
            print Output_Header() + "\t" + "Unknown system architecture type found!"
            sys.exit(1)
    return devcon

### Disable USB Device
def DisableUSBCamera():
    devcon = devcon()
    cmd = devcon + "disable" + Camera_Identity
    ret = os.system(cmd)
    if ret == 0 :
        print Output_Header() + "\t" + "USB Device is disabled."
    else:
        if ret == 1 :
            print Output_Header() + "\t" + "Error happens when trying to disable USB Device."
        else:
            print Output_Header() + "\t" + "Unknown error happens."
            sys.exit(1)

### Enable USB Device
def EnableUSBCamera():
    devcon = devcon()
    cmd = devcon + "enable" + Camera_Identity
    ret = os.system(cmd)
    if ret == 0 :
        print Output_Header() + "\t" + "USB Device is enabled."
    else:
        if ret == 1 :
            print Output_Header() + "\t" + "Error happens when trying to enable USB Device."
        else:
            print Output_Header() + "\t" + "Unknown error happens."
            sys.exit(1)

# definition: Live Video Window
TestACQSDK_LiveVideo_Window_Class    = "TestACQSDK"
TestACQSDK_LiveVideo_Window_Title    = "TestACQSDK: Live Video Display"
TestACQSDK_LiveVideo_Window_Position = (0,0)
TestACQSDK_LiveVideo_Window_Size     = (640,480)