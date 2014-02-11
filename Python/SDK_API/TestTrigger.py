"""
    This trigger is to start the execution of test cases. The data source is from the XML file.
    Also, if GUI is required to operate the XML file before executing, related code needs to be added here.
"""

# Import required module(s)
try:
	import sys
	import TestACQSDK_Module_Global_Definition as GDEF
	import TestACQSDK_Module_Executor as EXEC
except ImportError:
	print "One or more required modules are missing!"
	sys.exit(1)

EXEC.START(GDEF.ACQSDK_TestCaseXML_SingleAPI)
