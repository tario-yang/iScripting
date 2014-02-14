"""
    This executor is to execute the test cases defined in outside XML file.
"""

# Import required modules
try:
	import os, sys, time
	sys.path.append(r"../TestCase")
	from xml.dom import minidom
	import win32com.client, win32gui
	import TestACQSDK_Module_Global_Definition as GDEF
	GDEF.InitExecLogger() # Initiate Execution Logger
	GDEF.InitExecReporter() # Initiate Execution Reporter
	import TestACQSDK_Module_TestCase_API as TCAPI
except ImportError:
	GDEF.Logger("Info -> %r" % sys._getframe().f_code.co_filename)
	GDEF.Logger("Error -> One or more required modules are missing!")
	sys.exit(1)
except:
	GDEF.Logger("Info -> %r" % sys._getframe().f_code.co_filename)
	GDEF.Logger("Error -> Exception occurs when initiating Logger and Reporter.")
	sys.exit(1)
else:
	GDEF.Logger("Info -> Initiated.")

# Function to invoke pointed test case
def Action(action, objects, debug = 0):
	# Get parameter value
	arg0 = action[0] # Test Summary
	arg1 = action[1] # Test Case Name
	arg2 = action[2] # Expected Result
	arg3 = action[3] # Parameter Line
	obj0 = objects[0] # objACQSDK_CSDevice
	obj1 = objects[1] # objACQSDK_ASImageUnit
	obj2 = objects[2] # objACQSDK_SDKCallbackInfo

	if debug == 1:
		print "-"*33
		print "Test Summary: %s" % arg0
		print "Test Case Name: %s" % arg1
		print "Expected Result: %s" % arg2
		print "Parameter Line: %r" % arg3
		print "objACQSDK_CSDevice: %r" % obj0
		print "objACQSDK_ASImageUnit: %r" % obj1
		print "objACQSDK_SDKCallbackInfo: %r" % obj2
		print

	# Store test result
	result = []

	# Parse parameter
	parameter_line  = arg3.split(";")
	para_list = []
	for parameter in parameter_line:
		exec_string = ""
		para_list.append(x[0])
		x = parameter.split("=")
		if x[1].upper() == "TRUE": # is boolean
			exec_string = "%s = bool(1)" % x[0]
		elif x[1].upper() == "FALSE": # is boolean
			exec_string = "%s = bool(0)" % x[0]
		elif x[1].upper() == x[1].lower() and x[1].count(".") == 0: # is int
			exec_string = "%s = int(%s)" % (x[0], x[1])
		elif x[1].upper() == x[1].lower() and x[1].count(".") == 0: # is float
			exec_string = "%s = float(%s)" % (x[0], x[1])
		else:
			exec_string = "%s = str(%s)" % (x[0], x[1])
		print exec_string
		#exec(exec_string)

	# Invoke test case
	#exec_string = "%s(%r," % arg1


# Function to get XML data and then parse it, finally, trigger the test.
def START(flag = "api", switch = "full"):
	# Make sure data source exists
	#	Get list
	location = ""
	if switch == "full":
		if flag == "api":
			location = GDEF.ACQSDK_TestCaseXML_APIDir
		elif flag == "workflow":
			location = GDEF.ACQSDK_TestCaseXML_WorkflowDir
		else:
			GDEF.Logger("Info -> %r" % sys._getframe().f_code.co_filename)
			GDEF.Logger("Error -> Incorrect flag (api|workflow) received!")
			sys.exit(1)
		try:
			datasource_list = os.listdir(location)
		except:
			GDEF.Logger("Info -> %r" % sys._getframe().f_code.co_filename)
			GDEF.Logger("Error -> Exception happens when getting XML file list!")
			sys.exit(1)
		else:
			#	Filter list
			for i in datasource_list:
				ext = str(i).split(".")
				if ext[-1].upper() != "XML":
					datasource_list.remove(i)
			#	List shall have content
			if len(datasource_list) == 0:
				GDEF.Logger("Info -> %r" % sys._getframe().f_code.co_filename)
				GDEF.Logger("Error -> There is no XML file existed!")
				sys.exit(1)
	elif switch == "list": pass # 1. Check whether file exists and is empty or not; 2. Convert content to a list

	# Create COM Object
	try:
		objACQSDK_CSDevice        = GDEF.CreateCOMObject(GDEF.ACQSDK_CSDevice_ProgID)
		objACQSDK_ASImageUnit     = GDEF.CreateCOMObject(GDEF.ACQSDK_ASImageUnit_ProgID)
		objACQSDK_SDKCallbackInfo = GDEF.CreateCOMObject(GDEF.ACQSDK_SDKCallbackInfo_ProgID)
		objects = (objACQSDK_CSDevice, objACQSDK_ASImageUnit, objACQSDK_SDKCallbackInfo)
	except:
		GDEF.Logger("Info -> %r" % sys._getframe().f_code.co_filename)
		GDEF.Logger("Error: Exception occurs when creating COM object(s).")
		sys.exit(1)
	else:
		GDEF.Logger("Info -> COM object has been created.")
		GDEF.Logger("Info -> Details: %r; %r; %r" % (objACQSDK_CSDevice, objACQSDK_ASImageUnit, objACQSDK_SDKCallbackInfo))

	# Parse data
	try:
		for datasource in datasource_list:
			datasource_xml = minidom.parse("%s/%s" % (location, datasource))
			ts_list        = datasource_xml.getElementsByTagName(GDEF.ACQSDK_TestStepTag)
			for ts in ts_list:
				# Parameter to transfer to the next function
				#	1st element: Test Summary
				#	2nd element: Test Case Name
				#	3rd element: Expected Result
				#	4th element: Parameter List
				action = []
					# Test Summary
				action.append(ts.getAttribute(GDEF.ACQSDK_TestSummaryTag))
					# Fetch all parameters (include APIName, Parameter and Return)
				para_list  = ts.getElementsByTagName(GDEF.ACQSDK_ParameterTag)
				name_list  = []
				value_list = []
				for para in para_list:
					name  = str(para.getAttribute(GDEF.ACQSDK_ParameterNameTag))
					value = str(para.getAttribute(GDEF.ACQSDK_ParameterValueTag))
					name_list.append(name)
					value_list.append(value)
				if len(name_list) > 0 and len(value_list) > 0 and len(name_list) == len(value_list):
					x = name_list.index(GDEF.ACQSDK_TestCase)
					# Test Case Name
					action.append(value_list.pop(x))
					name_list.pop(x)
					x = name_list.index(GDEF.ACQSDK_ExpectedResult)
					# Expected Result
					action.append(value_list.pop(x))
					name_list.pop(x)
					para_line = ""
					while len(name_list) > 0:
						if para_line == "":
							para_line = name_list.pop() + "=" + value_list.pop()
						else:
							para_line = name_list.pop() + "=" + value_list.pop() + ";" + para_line
					# Parameter List
					action.append(para_line)

					# Trigger the execution
					Action(action, objects, 1)
				else:
					GDEF.Logger("Info -> %r" % sys._getframe().f_code.co_filename)
					GDEF.Logger("Error -> Exception occurs when fetching parameters from XML file, %r." % datasource)
					GDEF.Logger("Error -> Fetched %r list and %r list is not correct (length)." % (GDEF.ACQSDK_ParameterNameTag, GDEF.ACQSDK_ParameterValueTag))
					sys.exit(1)
	except:
		GDEF.Logger("Info -> %r" % sys._getframe().f_code.co_filename)
		GDEF.Logger("Error -> Exception occurs when fetching parameters from XML file.")
		sys.exit(1)

START()