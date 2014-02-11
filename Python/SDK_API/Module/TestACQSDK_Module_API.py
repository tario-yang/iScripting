# Import required module(s)
try:
	import sys
	import TestACQSDK_Module_Global_Definition as GDEF
except ImportError:
	print "One or more required modules are missing!"
	sys.exit(1)

# API: ACQSDK_SetLogPath
def TS0001_ACQSDK_SetLogPath(objACQSDK_CSDevice, para_path):
	Module_Name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_SetLogPath(para_path)
	except:
		pass
	finally:
		try:
			print type(eval(str(ret)))
		except NameError:
			GDEF.Logger("Fail to execute " + Module_Name)
		except TypeError:
			GDEF.Logger("Unexpected Type of ret is received.")
		else:
			GDEF.TEE(Module_Name, para_path, ret)
