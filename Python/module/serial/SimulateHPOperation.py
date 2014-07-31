import sys
import time
import re
from optparse import OptionParser
import serial
import _winreg as wreg


# Output COM port via OS's registry
def FetchCOMPort(usbid):

    # Read keys
    readkey = wreg.OpenKey(
        wreg.HKEY_LOCAL_MACHINE, 'HARDWARE\\DEVICEMAP\\SERIALCOMM\\')

    # Filter required COM port information
    try:
        i = 0
        COMList = []
        while 1:
            item = wreg.EnumValue(readkey, i)
            if item[0].find(usbid) != -1:
                COMList.append(item[1])
            i += 1
    except WindowsError as e:
        pass

    # Return
    if len(COMList) == 1:
        return COMList[0]
    else:
        return None


# Main function to deal with transferred command
def Main(CMDList, COMPort, debug):

    # Create serial port object
    try:
        serialPort = serial.Serial(port=COMPort, baudrate=115200, timeout=1)
    except Exception as e:
        if debug == True:
            print 'Error -> Exception happens,\n\t{}'.format(str(e))
        sys.exit(StdErrDict['FAIL_TO_INSTANCE_COM_PORT'])
    else:
        if debug == True:
            print 'Info -> Details of COM Port: %s' % str(serialPort)
        if str(serialPort).find(COMPort) == -1:
            if debug == True:
                print 'Error -> Serial Port is not available to use. Check status of handpiece.'
            sys.exit(StdErrDict['FAIL_TO_CONFIRM_COM_PORT'])

    # Login: user & password
    user = u'root'
    password = u'aluirp;as#iwer2354123'

    # Check the status of embedded OS and login if necessary
    if debug == True:
        print '[Description] Check Status of Embedded OS.'
    SendCommand(serialPort, None)
    retBuffer = serialPort.readlines()
    if debug == True:
        PrintBuffer(retBuffer)

    #   Check whether it needs to Login
    if SeekKeyString(retBuffer, "(none) login:"):
        if debug == True:
            print '[Description] Input username and password.'
        SendCommand(serialPort, user)
        SendCommand(serialPort, password)
        tmp_retBuffer = serialPort.readlines()
        if debug == True:
            PrintBuffer(tmp_retBuffer)
        if SeekKeyString(tmp_retBuffer, '# '):
            if debug == True:
                print 'Info -> Login to embedded OS.'
        else:
            if debug == True:
                print 'Error -> Login failed.'
            sys.exit(StdErrDict['LOGIN_FAILED'])
        del tmp_retBuffer
    elif SeekKeyString(retBuffer, '# '):
        if debug == True:
            print 'Info -> Logined to embedded OS.'
        pass
    else:
        if debug == True:
            print 'Error -> Unknown stastus of embedded OS. Suggest to reboot the handpiece and then try again!'
        sys.exit(StdErrDict['UNKNOWN_STATUS_OF_EMBEDDED_OS'])
    del retBuffer

    # Make sure Login, using command, pwd, to test.
    if debug == True:
        print '[Description] Double Confirm Status of Embedded OS.'
    SendCommand(serialPort, 'pwd')
    retBuffer = serialPort.readlines()
    if debug == True:
        PrintBuffer(retBuffer)
    if SeekKeyString(retBuffer, '# ') and SeekKeyString(retBuffer, '/root') and SeekKeyString(retBuffer, 'pwd'):
        # Confirm Status of Embedded OS
        if debug == True:
            print 'Info -> Status of embedded OS is confirmed!'

        # Start to send command
        for CMD in CMDList:
            SendCommand(serialPort, CMD)
            SendCommand(serialPort, u'echo $?')
            tmp_retBuffer = serialPort.readlines()
            if debug == True:
                PrintBuffer(tmp_retBuffer)
            if SeekKeyString(tmp_retBuffer, 'echo $?'):
                if SeekKeyString(tmp_retBuffer, '0\r\n'):
                    if debug == True:
                        print 'Info -> Execution is successful.'
                    pass
                elif SeekKeyString(tmp_retBuffer, '1\r\n'):
                    if debug == True:
                        print 'Error -> Execution failed.'
                    sys.exit(StdErrDict['EXECUTION_FAILED'])
                else:
                    if debug == True:
                        print 'Error -> Undefined stderr of command execution.'
                    sys.exit(
                        StdErrDict['UNDEFINED_STATUS_OF_EXECUTION_OF_COMMAND'])
            else:
                if debug == True:
                    print 'Error -> Undefined status of embedded OS.'
                sys.exit(StdErrDict['UNKNOWN_STATUS_OF_EMBEDDED_OS'])
            del tmp_retBuffer
            time.sleep(0.2)
    else:
        if debug == True:
            print 'Error -> Unknown status of embedded OS. Suggest to reboot the handpiece and then try again!'
        sys.exit(StdErrDict['UNKNOWN_STATUS_OF_EMBEDDED_OS'])

    # Close port
    serialPort.close()    # -> SendDbusCommand

    # EOF
    sys.exit(StdErrDict['SUCCESS'])


# Send the command to COM object
def SendCommand(objSerialPort, command):
    if command is not None:
        print u'Command Sent >> {}'.format(command)
        objSerialPort.write(command)
    else:
        print u'Command Sent >> {ENTER}'
    objSerialPort.write('\n')
    # Need to wait,
    # otherwise, it fails to get the expected response from embedded OS.
    time.sleep(0.2)    # -> SendCommand


# Check whether the target KeyString is in buffer.
def SeekKeyString(SerialBuffer, keyString):
    for i in xrange(0, len(SerialBuffer)):
        if SerialBuffer[i].find(keyString) >= 0:
            return True
    return False


# Format the buffer outputted from COM object
#   Convert list to string
def FormatBuffer(SerialBuffer):
    return ''.join(['\t{}'.format(i.replace('\r', '')) for i in SerialBuffer])


# Print the buffer outputted from COM object.
def PrintBuffer(SerialBuffer):
    print 'Buffer Got <<'
    print FormatBuffer(SerialBuffer)


# ============================== Main ==============================
if __name__ == '__main__':

    # Error Code Definition, return to stderr
    StdErrDict = {
        'SUCCESS':                                   0,
        'COM_PORT_ERROR':                            100,
        'FAIL_TO_INSTANCE_COM_PORT':                 200,
        'FAIL_TO_CONFIRM_COM_PORT':                  201,
        'UNKNOWN_STATUS_OF_EMBEDDED_OS':             300,
        'LOGIN_FAILED':                              400,
        'EXECUTION_FAILED':                          500,
        'UNDEFINED_STATUS_OF_EXECUTION_OF_COMMAND':  501,
        'INCORRECT_SUPPLIED_PARAMETER_COMMAND_TYPE': 1001,
        'INCORRECT_SUPPLIED_PARAMETER_BUTTON':       1002,
        'INCORRECT_SUPPLIED_PARAMETER_COM_PORT':     1003,
        'INCORRECT_SUPPLIED_PARAMETER_DEBUG':        1004,
    }

    # Deal with parameter inputted
    #   Additional Information: Error Code
    #       parser = OptionParser(epilog=ErrorCodeInfo)
    parser = OptionParser()
    parser.add_option(
        '-t', '--type', dest='COMMAND_TYPE', default='SCRIPT',
        help='Specify the command type, such as SCRIPT, BUTTON and STATE. Default is SCRIPT.')
    parser.add_option('-b', '--button', dest='BUTTON', default='CAPTURE',
                      help='One button name of handpiece, such as UP, DOWN, POWER and CAPTURE. This option is available when BUTTON type (-t) is specified. Default is CAPTURE.')
    parser.add_option('-p', '--port', dest='COM_PORT',
                      help='COM port which is used to communicate with handpiece. If this option is not specified, it needs to specify option, -i.')
    parser.add_option('-i', '--usbid', dest='USB_ID', default='Silabser',
                      help='Identifier which is used to specify name of the USB serial chip.')
    parser.add_option('-d', '--debug', dest='DEBUG', default='False',
                      help='One switch which is used to output additional information to stdout. Default is False.')
    (options, args) = parser.parse_args()

    # Generate parameters for Main

    #   Command Type
    if options['COMMAND_TYPE'] == 'SCRIPT':
        print 'SCRIPT'
        pass
    elif options['COMMAND_TYPE'] == 'BUTTON':

        # Key Pressing

        #   Command to simulate Key Pressing
        CMD_Key_Press = r'dbus-send --session --dest=com.csh.UvcDaemon --type=method_call --print-reply /com/csh/UvcDaemon com.csh.UvcDaemon.ProcessInputEvent int32:# uint32:0'
        #   Key Dict
        keyDict = {
            'UP':      (0, 2),    # -> [0]: Press, [1]: Release
            'DOWN':    (1, 3),
            'POWER':   (4, 5),
            'CAPTURE': (8, 9),
        }

        #   Command List
        if keyDict.get(options['BUTTON']) is None:
            if debug == True:
                print 'Error -> Incorrect button name specified.'
                sys.exit(StdErrDict['INCORRECT_SUPPLIED_PARAMETER_BUTTON'])
        else:
            CMDList = []
            for i in keyDict[options['BUTTON']]:
                CMDList.append(unicode(CMD_Key_Press.replace('#', str(i))))
    elif options['COMMAND_TYPE'] == 'STATUS':
        pass    # Placeholder for STATUS: Sleep, Holder
    else:
        if debug == True:
            print 'Error -> Incorrect supplied parameter for -t.'
        sys.exit(StdErrDict['INCORRECT_SUPPLIED_PARAMETER_COMMAND_TYPE'])

    #   COM port
    if options['COM_PORT'] is None:
        COMPort = FetchCOMPort(options['USB_ID'])
        if COMPort is None:
            sys.exit(StdErrDict['COM_PORT_ERROR'])
    else:
        if debug == True:
            print 'Error -> Incorrect supplied parameter for -p.'
        sys.exit(StdErrDict['INCORRECT_SUPPLIED_PARAMETER_COM_PORT'])



    #   Debug Mode
    if options['DEBUG'].upper() != 'FALSE' and options['DEBUG'].upper() != 'TRUE':
        if debug == True:
            print 'Error -> Incorrect supplied parameter for -d.'
        sys.exit(StdErrDict['INCORRECT_SUPPLIED_PARAMETER_DEBUG'])

    # Execute
    Main(CMDList=CMDList, COMPort=COMPort, debug=False)
