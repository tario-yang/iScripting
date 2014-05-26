# This script is to compare the image
#       supporting to rotate before comparing
#       supporting to compare with size or md5


import os
import sys
from optparse import OptionParser
import Image


def ImageCompare(options):
    x = Image.open(options.SOURCE)
    y = Image.open(options.DESTINATION)
    if options.ROTATION in ['90', '180', '270']:
        y = y.rotate((360 - int(options.ROTATION)), 0, 1)
    if options.MODE == 'SIZE':
        if x.size == y.size:
            sys.exit(StdErrCode['SUCCESS_SAME'])
    elif options.MODE == 'CONTENT':
        x = make_regalur_image(x)
        y = make_regalur_image(y)
        ret = calc_similar(x, y)
        print ret
        if ret >= 0.9:
            sys.exit(StdErrCode['SUCCESS_SAME'])
    sys.exit(StdErrCode['SUCCESS_DIFFERENT'])


def hist_similar(lh, rh):
    assert len(lh) == len(rh)
    return sum(1 - (0 if l == r else float(abs(l - r)) / max(l, r)) for l, r in zip(lh, rh)) / len(lh)


def calc_similar(li, ri):
    return sum(hist_similar(l.histogram(), r.histogram()) for l, r in zip(split_image(li), split_image(ri))) / 16.0


def split_image(img, part_size=(64, 64)):
    w, h = img.size
    pw, ph = part_size
    assert w % pw == h % ph == 0
    return [img.crop((i, j, i + pw, j + ph)).copy() for i in xrange(0, w, pw) for j in xrange(0, h, ph)]


def make_regalur_image(img, size=(256, 256)):
    return img.resize(size)


StdErrCode = {
    'SUCCESS_SAME': 0,
    'SUCCESS_DIFFERENT': 1,
    'FILE_DOES_NOT_EXIST_SOURCE': 100,
    'FILE_DOES_NOT_EXIST_DESTINATION': 101,
    'INCORRECT_PARAMETER_VALUE_ROTATION_DEGREE': 200,
    'INCORRECT_PARAMETER_VALUE_MODE': 201,
    'NO_KEY_PARAMETER': 300,
}


#	Define / Parse parameters
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
parser.add_option('-m', '--mode', dest='MODE', default='CONTENT',
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
