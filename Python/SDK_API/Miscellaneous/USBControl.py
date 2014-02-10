	### Query and Control USB Device
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
		time.sleep(1)
		if ret == 0 :
			print Output_Header() + "\t" + "Status of USB Camera is outputted."
			try:
				status_file = open(pwd + "\\Tools\\devcon\\USBCameraStatus.log", "r")
			except:
				print Output_Header() + "\t" + "Fail to open status output file..."
				retString = None
			else:
				status_file_content = status_file.read()
				if status_file_content.find("disabled") != -1 :
					retString = "Disabled"
				else:
					if status_file_content.find("running") != -1 :
						retString = "Running"
					else:
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