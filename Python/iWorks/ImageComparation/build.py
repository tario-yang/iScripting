# This script is to build a exe for IC.py


from distutils.core import setup
import py2exe
setup(
    console=['ImageComparator.py'],
    options={
        'py2exe': {
            'dll_excludes': ['w9xpopen.exe'],
            'packages': ['optparse', 'Image'],
            'bundle_files': 1,
            'compressed': True,
        }
    }
)
