from distutils.core import setup
import py2exe
import sys
sys.path.append(r'../')
sys.path.append(r'../../Module/')
setup(
	console=[r"../SDKGUI.py"],
	options = {
		"py2exe": {
			"packages": ["win32com.client","TestACQSDK_Module_Wrapper","TestACQSDK_Module_Global_Definition"]
		}
	}
)
