import sys
import time
import serial

# Login: user & password
user = unicode('root')
password = unicode('aluirp;as#iwer2354123')

# Create serial port object
try:
    serialPort = serial.Serial(port='COM9', baudrate=115200, timeout=1)
except:
    print 'Port does not exist or is in used by others.'
    sys.exit(1)

# Make sure console is ready
serialPort.write('\n')
time.sleep(1)

# Suppose camera is powered on and ready
for i in user, password:
    serialPort.write(i)
    serialPort.write('\n')
    time.sleep(1)

serialPort.write(unicode('cat /opt/vega/fs.ver'))
serialPort.write('\n')
# print str(serialPort.readall())
print str(serialPort.readline())

serialPort.close()
