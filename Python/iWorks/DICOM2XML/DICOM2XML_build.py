from distutils.core import setup
import py2exe

option = {
        'py2exe': {
            'packages'    : ['dicom', 'xml.dom.minidom'],
            'includes'    : ['os', 'sys', 'time', 'optparse'],
            'excludes'    : ['tcl', 'Tkinter', 'Tix', 'numpy', 'PIL', 'PySide',
                'email', 'distutils', 'unittest', 'importlib',
                'win32com', 'win32gui', 'win32con', 'win32api', 'win32pipe',
                '_ssl', 'ssl', '_hashlib', 'hashlib',
                'httplib', 'ftplib', 'urllib', 'urllib2', 'urlparser', 'threading', 'dummary_thread',
                'pkg_resources', 'bz2', 'tarfile', 'doctest', '_socket', 'locale'],
            'dll_excludes': ['w9xpopen.exe'],
            'unbuffered'  : True,
            'bundle_files': 1,
            'compressed'  : True,
            'optimize'    : 2,
        },
}

setup(
    name        = 'DICOM2XML.EXE',
    version     = '1.1',
    description = 'Conver a DICOM file to a XML file',
    author      = 'James Jun Yang, 19011956',
    console     = [
        {
            'script'         : 'DICOM2XML.py',
            'icon_resources' : [(1,'Dicom.ico')]
        }
    ],
    options     = option,
    zipfile   = None,
)
