# This script is to compare the image
#	supporting to rotate before comparing


import os
import sys
from optparse import OptionParser
import Image
import hashlib


def ImageCompare(options):

    if options.MODE == 'SIZE':
        x = Image.open(options.SOURCE)
        y = Image.open(options.DESTINATION)
        if options.ROTATION in ['90', '180', '270']:
            y = y.rotate(int(options.ROTATION), 0, 1)
        if x.size == y.size:
            sys.exit(StdErrCode['SUCCESS_SAME'])
    elif options.MODE == 'CONTENT':
        x = hashlib.md5()
        x.update(file(options.SOURCE).read())
        y = hashlib.md5()
        z = Image.open(options.DESTINATION)
        if options.ROTATION in ['90', '180', '270']:
            tmp = z.rotate(int(options.ROTATION), 0, 1)
            tmpfilename = "tmp_{}".format(os.path.basename(options.DESTINATION))
            tmp.save(tmpfilename)
            y.update(file(tmpfilename).read())
        else:
            y.update(file(options.DESTINATION).read())
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
}


#	Parse parameters
usage = "usage: %prog -s SourceImage -d DestinationImage -r Degree -m Mode "
version = '1.0'
parser = OptionParser(usage=usage, version=version)
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
