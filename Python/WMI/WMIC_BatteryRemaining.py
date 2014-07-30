import wmi
objWMI = wmi.WMI()
for i in objWMI.Win32_Battery():
	print '{}%'.format(i.EstimatedChargeRemaining)
