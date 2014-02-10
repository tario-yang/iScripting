# Import required modules
try:
	import os, sys
	import TestACQSDK_Module_Global_Definition as GDEF
except ImportError:
	print "One or more required modules are missing!"
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
			print GDEF.Output_Header() + "\t" + "Exception happens when executing" + " " + Module_Name
			print GDEF.Output_Header() + "\t" + " - There is no output return, ret does not exist!\n"
		except TypeError:
			print GDEF.Output_Header() + "\t" + "Unexpected Type of ret is received."
		else:
			GDEF.TEE(Module_Name, ret)

# API: ACQSDK_Init
def TestACQSDK_API_ACQSDK_Init(objACQSDK_CSDevice, para_hWnd):
	Module_Name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_Init(para_hWnd)
	except:
		pass
	finally:
		try:
			type(eval(str(ret)))
		except NameError:
			print GDEF.Output_Header() + "\t" + "Exception happens when executing " + Module_Name
			print GDEF.Output_Header() + "\t" + " - There is no output return, ret does not exist!\n"
		except TypeError:
			print GDEF.Output_Header() + "\t" + "Unexpected Type of ret is received."
		else:
			TestACQSDK_API_Output(Module_Name, ret)

# API: ACQSDK_Uninit
def TestACQSDK_API_ACQSDK_UnInit(objACQSDK_CSDevice):
	Module_Name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_UnInit()
	except:
		pass
	finally:
		try:
			type(eval(str(ret)))
		except NameError:
			print GDEF.Output_Header() + "\t" + "Exception happens when executing " + Module_Name
			print GDEF.Output_Header() + "\t" + " - There is no output return, ret does not exist!\n"
		except TypeError:
			print GDEF.Output_Header() + "\t" + "Unexpected Type of ret is received."
		else:
			TestACQSDK_API_Output(Module_Name, ret)

# API: ACQSDK_StartPlay
def TestACQSDK_API_ACQSDK_StartPlay(objACQSDK_CSDevice):
	Module_Name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_StartPlay()
	except:
		pass
	finally:
		try:
			type(eval(str(ret)))
		except NameError:
			print GDEF.Output_Header() + "\t" + "Exception happens when executing" + " " + Module_Name
			print GDEF.Output_Header() + "\t" + " - There is no output return, ret does not exist!\n"
		except TypeError:
			print GDEF.Output_Header() + "\t" + "Unexpected Type of ret is received."
		else:
			TestACQSDK_API_Output(Module_Name, ret)

# API: ACQSDK_StopPlay
def TestACQSDK_API_ACQSDK_StopPlay(objACQSDK_CSDevice):
	Module_Name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_StopPlay()
	except:
		pass
	finally:
		try:
			type(eval(str(ret)))
		except NameError:
			print GDEF.Output_Header() + "\t" + "Exception happens when executing" + " " + Module_Name
			print GDEF.Output_Header() + "\t" + " - There is no output return, ret does not exist!\n"
		except TypeError:
			print GDEF.Output_Header() + "\t" + "Unexpected Type of ret is received."
		else:
			TestACQSDK_API_Output(Module_Name, ret)

# API: ACQSDK_StartRecord
def TestACQSDK_API_ACQSDK_StartRecord(objACQSDK_CSDevice, para_file_path):
	Module_Name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_StartRecordEx(para_file_path)
	except:
		pass
	finally:
		try:
			type(eval(str(ret)))
		except NameError:
			print GDEF.Output_Header() + "\t" + "Exception happens when executing" + " " + Module_Name
			print GDEF.Output_Header() + "\t" + " - There is no output return, ret does not exist!\n"
		except TypeError:
			print GDEF.Output_Header() + "\t" + "Unexpected Type of ret is received."
		else:
			TestACQSDK_API_Output(Module_Name, ret)

# API: ACQSDK_StopRecord
def TestACQSDK_API_ACQSDK_StopRecord(objACQSDK_CSDevice):
	Module_Name = sys._getframe().f_code.co_name
	try:
		ret = objACQSDK_CSDevice.ACQSDK_StopRecord()
	except:
		pass
	finally:
		try:
			type(eval(str(ret)))
		except NameError:
			print GDEF.Output_Header() + "\t" + "Exception happens when executing" + " " + Module_Name
			print GDEF.Output_Header() + "\t" + " - There is no output return, ret does not exist!\n"
		except TypeError:
			print GDEF.Output_Header() + "\t" + "Unexpected Type of ret is received."
		else:
			TestACQSDK_API_Output(Module_Name, ret)
