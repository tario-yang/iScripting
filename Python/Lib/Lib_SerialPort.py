import sys, time
import re
import serial

class SERIAL:
    def __init__(self, port, baudrate = 115200, timeout = 1):
        self.port       = port
        self.baudrate   = baudrate
        self.timeout    = timeout
        self.connection = serial.Serial(self.port, self.baudrate, self.timeout)

    def sendcommand(self, cmd = None):
        "Send command to serial port"
        if not cmd is None:
            self.connection.write(cmd)
        self.connection.write('\n')
        time.sleep(0.2)

    def login(user = u'root', password = u'aluirp;as#iwer2354123'):
        "Login embedded system"
        sendcommand()
        sendcommand(user)
        sendcommand(password)
        sendcommand('pwd')
        if findkeyword(readbuffer, '# ') and findkeyword(readbuffer, '/root') and findkeyword(readbuffer, 'pwd'):
            return True
        else:
            return False

    def readbuffer():
        "Return the stdout buffer"
        return self.connection.readlines()

    def findkeyword(buffer, keyword):
        "Find specified string"
        for i in xrange(0, len(buffer)):
            if SerialBuffer[i].find(keyword) >= 0:
                return True
        return False

    def executionresult(self):
        "Check the whether command is executed successfully or not"
        sendcommand('echo $?')
        if findkeyword(readbuffer, '0\r\n'):
            return True
        elif findkeyword(readbuffer, '1\r\n'):
            return False
        else:
            return None

    def uvc_sendmirrorcmd(self, id):
        "Mirror command"
        cmd = r'debus-send --sesion --dest=com.csh.EncodeStream --type=method_call /com/csh/EncodeStream com.csh.EncodeStream.SetWorkParams int32:8 int32:{}'.format(id)
        sendcommand(cmd)
        executionresult()

    def uvc_sendrotationcmd(self, id):
        "Rotation command"
        cmd = r'debus-send --sesion --dest=com.csh.EncodeStream --type=method_call /com/csh/EncodeStream com.csh.EncodeStream.SetWorkParams int32:9 int32:{}'.format(id)
        sendcommand(cmd)
        executionresult()

    def uvc_setshorttimer(self, second = 20):
        "Sleep timer"
        cmd = r'dbus-send --session --dest=com.csh.UvcDaemon --type=method_call /com/csh/UvcDaemon com.csh.UvcDaemon.ResetShortTimer int32:{}'.format(second)
        sendcommand(cmd)
        executionresult()

    def uvc_setlongtimer(self, second = 30):
        "Power off timer"
        cmd = r'dbus-send --session --dest=com.csh.UvcDaemon --type=method_call /com/csh/UvcDaemon com.csh.UvcDaemon.ResetLongTimer int32:{}'.format(second)
        sendcommand(cmd)
        executionresult()

    def uvc_findprocessinfo(self, keyword, isprocmonitor = False):
        "Return the process name and its switches"
        if isprocmonitor:
            cmd = 'ps -ef | grep "procmonitor" | grep "{}" | grep -v grep'.format(keyword)
        else:
            cmd = 'ps -ef | grep -v "procmonitor" | grep "{}" | grep -v grep'.format(keyword)
        sendcommand(cmd)
        if findkeyword(keyword):
            return True
        else:
            return False

    def uvc_fetchprocesspid(self, keyword, isprocmonitor = False):
        "Return the pid of a pointed process"
        if isprocmonitor:
            cmd = "ps -ef | grep 'procmonitor' | grep '{}' | grep -v grep | awk '{print $1}'".format(keyword)
        else:
            cmd = "ps -ef | grep -v 'procmonitor' | grep '{}' | grep -v grep | awk '{print $1}'".format(keyword)
        sendcommand(cmd)
        return readbuffer[:-2]

    def uvc_disableprocmonitor(self):
        pass

    def uvc_enableprocmonitor(self):
        pass
