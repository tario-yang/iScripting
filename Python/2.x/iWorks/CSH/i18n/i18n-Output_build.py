from distutils.core import setup
import py2exe
import sys

option = {
        'py2exe': {
            'packages'     : ['polib','xlwt'],
            'includes'     : ['os', 'sys', 'time','optparse'],
            'dll_excludes' : ['w9xpopen.exe'],
            'bundle_files' : 1,
            'compressed'   : True,
        }
}

setup(
    options = option,
    console = [
        {
            'script'         : 'i18n-Output.py',
            'icon_resources' : [(1,'logo.ico')],
        }
    ],
    zipfile     = None,
    name        = 'i18n-Output',
    version     = '1.0.0.0',
    description = 'Output whole msgstr to one Excel file. This script is just for ACQ.',
    author      = 'James Jun Yang, 19011956'
)
