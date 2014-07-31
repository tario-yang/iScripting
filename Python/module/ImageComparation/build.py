# This script is to build a exe for IC.py


from distutils.core import setup
import py2exe
setup(
    console=['IC.py'],
    options={
        'py2exe': {
            'packages': ['optparse', 'Image', 'hashlib']
        }
    }
)
