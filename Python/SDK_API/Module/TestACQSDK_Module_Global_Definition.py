# Import required modules
try:
    import os
    import sys
    import time
    import datetime
except ImportError:
    print "Required modules are NOT imported!"
    sys.exit(1)

# definition[variables]
ACQSDK_ProgID   = "ACQSDK.CSDevice.1"
#Camera_Identity = "USB\VID_041E&PID_4059"

# definition[function]
### Output Header for console
def Output_Header():
	return "[" + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "]" + "\t"
### Check system and define which devcon to use
def devconVer():
    tmp = os.getcwd()
    pwd = os.chdir("..\\")
    pwd = os.getcwd()
    try:
        os.environ['PROGRAMFILES(X86)']
    except:
        devconVer = "x86"
    else:
        devconVer = "x64"
    pwd = os.chdir(tmp)
    return devconVer

### Status of USB Camera
def USBCameraStatus():
    dVer = devconVer()
    tmp = os.getcwd()
    pwd = os.chdir("..\\")
    pwd = os.getcwd()
    cmd = "RUNAS /User:Administrator /SaveCred /ENV /NoProfile" + " \"" + pwd + "\\Tools\\devcon\\USBCameraStatus.bat" + " " + dVer + " " + "\""
    ret = os.system(cmd)
    if ret == 0 :
        print Output_Header() + "\t" + "Status of USB Camera is outputted."
        try:
            status_file = open(pwd + "\\Tools\\devcon\\USBCameraStatus.log", "rU")
        except:
            print Output_Header() + "\t" + "Fail to open status output file..."
            retString = None
        else:
            #-----------------------------------------------------------------Read a file as a list
            if len(status_file.readlines()) == 4 :
                retString =
            else:
                print Output_Header() + "\t" + "Format of output file is incorrect! Maybe some issue happened."
                retString = None
        finally:
            status_file.close()
    else:
        if ret == 1 :
            print Output_Header() + "\t" + "Error happens when trying to check status of USB Camera."
        else:
            print Output_Header() + "\t" + "Unknown error happens."
        retString = None
    pwd = os.chdir(tmp)
    return retString

### Disable USB Camera
def USBCameraDisable():
    dVer = devconVer()
    tmp = os.getcwd()
    pwd = os.chdir("..\\")
    pwd = os.getcwd()
    cmd = "RUNAS /User:Administrator /SaveCred /ENV /NoProfile" + " \"" + pwd + "\\Tools\\devcon\\USBCameraDisable.bat" + " " + dVer + " " + "\""
    ret = os.system(cmd)
    if ret == 0 :
        print Output_Header() + "\t" + "USB Camera is disabled."
    else:
        if ret == 1 :
            print Output_Header() + "\t" + "Error happens when trying to disable USB Camera."
        else:
            print Output_Header() + "\t" + "Unknown error happens."
            sys.exit(1)
    pwd = os.chdir(tmp)

### Enable USB Camera
def USBCameraEnable():
    dVer = devconVer()
    tmp = os.getcwd()
    pwd = os.chdir("..\\")
    pwd = os.getcwd()
    cmd = "RUNAS /User:Administrator /SaveCred /ENV /NoProfile" + " \"" + pwd + "\\Tools\\devcon\\USBCameraEnable.bat" + " " + dVer + " " + "\""
    ret = os.system(cmd)
    if ret == 0 :
        print Output_Header() + "\t" + "USB Camera is enabled."
    else:
        if ret == 1 :
            print Output_Header() + "\t" + "Error happens when trying to enable USB Camera."
        else:
            print Output_Header() + "\t" + "Unknown error happens."
            sys.exit(1)
    pwd = os.chdir(tmp)

# definition: Live Video Window
TestACQSDK_LiveVideo_Window_Class    = "TestACQSDK"
TestACQSDK_LiveVideo_Window_Title    = "TestACQSDK: Live Video Display"
TestACQSDK_LiveVideo_Window_Position = (0,0)
TestACQSDK_LiveVideo_Window_Size     = (640,480)