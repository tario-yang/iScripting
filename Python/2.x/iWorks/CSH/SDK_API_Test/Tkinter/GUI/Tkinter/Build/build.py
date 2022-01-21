from distutils.core import setup
import py2exe
import sys

sys.path.append(r'../../../Module/')

option = {
        'py2exe': {
            'packages': ['TestACQSDK_Module_Wrapper','TestACQSDK_Module_Global_Definition']
        },
}

setup(
    options = option,
	windows = [r'../SDKAPITest.py']
)
