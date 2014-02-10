# Import required modules
try:
	import TestACQSDK_Module_Global_Definition as GDEF
except ImportError:
	print "The required module is missing!"
	sys.exit(1)

# API: ACQSDK_SetLogPath
def TestACQSDK_API_ACQSDK_SetLogPath(objACQSDK_CSDevice, para_path):
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
