# This script is to compare the image
#       supporting to rotate before comparing
#       supporting to compare with size or md5


import os
import sys
from optparse import OptionParser
import Image
import hashlib


def ImageCompare(options):

    x = Image.open(options.SOURCE)
    y = Image.open(options.DESTINATION)
    if options.ROTATION in ['90', '180', '270']:
        y = y.rotate(int(options.ROTATION), 0, 1)

    if options.MODE == 'SIZE':
        if x.size == y.size:
            sys.exit(StdErrCode['SUCCESS_SAME'])
    elif options.MODE == 'CONTENT':
        x = hashlib.md5(str(x))
        y = hashlib.md5(str(y))
        if x.hexdigest().upper() == y.hexdigest().upper():
            sys.exit(StdErrCode['SUCCESS_SAME'])
    sys.exit(StdErrCode['SUCCESS_DIFFERENT'])


StdErrCode = {
    'SUCCESS_SAME': 0,
    'SUCCESS_DIFFERENT': 1,
    'FILE_DOES_NOT_EXIST_SOURCE': 100,
    'FILE_DOES_NOT_EXIST_DESTINATION': 101,
    'INCORRECT_PARAMETER_VALUE_ROTATION_DEGREE': 200,
    'INCORRECT_PARAMETER_VALUE_MODE': 201,
    'NO_KEY_PARAMETER': 300,
}


#	Parse parameters
usage = 'usage: %prog -s SourceImage -d DestinationImage [-r Degree] [-m Mode]'
version = '1.0'
epilog = 'Definition of stderr is, ' + \
    ', '.join(['"{}: {}"'.format(key, value)
              for (key, value) in StdErrCode.items()])
parser = OptionParser(usage=usage, version=version, epilog=epilog)
parser.add_option('-s', '--source', dest='SOURCE',
                  help='Source image file')
parser.add_option('-d', '--destination', dest='DESTINATION',
                  help='Destination image file')
parser.add_option('-r', '--rotation', dest='ROTATION',
                  help='Rotate source image file by degrees before comparing. Value shall be 90 / 180 / 270.')
parser.add_option('-m', '--mode', dest='MODE', default='SIZE',
                  help='Mode of comparation (SIZE or CONTENT). Default is %default.')


#	Get parameters
(options, args) = parser.parse_args()


#	Check parameters
if options.SOURCE is None:
    parser.error('Souce image file shall be specified.')
    sys.exit(StdErrCode['NO_KEY_PARAMETER'])
if options.DESTINATION is None:
    parser.error('Destination image file shall be specified.')
    sys.exit(StdErrCode['NO_KEY_PARAMETER'])
if not os.path.exists(options.SOURCE):
    parser.error('Source image file does not exist!')
    sys.exit(StdErrCode['FILE_DOES_NOT_EXIST_SOURCE'])
if not os.path.exists(options.DESTINATION):
    parser.error('Destination image file does not exist!')
    sys.exit(StdErrCode['FILE_DOES_NOT_EXIST_DESTINATION'])
if not options.ROTATION in [None, '90', '180', '270']:
    parser.error('Rotation degree value is not an expected one!')
    sys.exit(StdErrCode['INCORRECT_PARAMETER_VALUE_ROTATION_DEGREE'])
if not options.MODE.upper() in ['SIZE', 'CONTENT']:
    parser.error('Mode does not recognize!')
    sys.exit(StdErrCode['INCORRECT_PARAMETER_VALUE_MODE'])


# Begin
if __name__ == '__main__':
    ImageCompare(options)
