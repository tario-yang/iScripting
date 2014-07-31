import wmi

objWMI = wmi.WMI()

for os in objWMI.Win32_OperatingSystem():
    print '[{}]'.format(os.Caption)
