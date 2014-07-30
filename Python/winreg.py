import sys

try:
    import _winreg as wreg    # Python 2
except:
    try:
        import winreg as wreg    `# Python 3
    except Exception as e:
        print str(e)

readkey = wreg.OpenKey(
    wreg.HKEY_LOCAL_MACHINE, 'HARDWARE\\DEVICEMAP\\SERIALCOMM\\')

try:
    i = 0
    while 1:
        item = wreg.EnumValue(readkey, i)
        # print '{}\t= {}'.format(item[0], item[1])
        if item[0].find('Silabser') != -1:
            print 'COM port is found -> {}'.format(item[1])
            sys.exit(0)
        i += 1
except WindowsError as e:
    pass
    print str(e)
