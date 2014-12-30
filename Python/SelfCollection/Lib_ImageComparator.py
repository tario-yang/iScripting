# This script is to compare the image
#       supporting to rotate before comparing
#       supporting to compare with size or md5


import Image


def ImageCompare(options):
    x = Image.open(options.SOURCE)
    y = Image.open(options.DESTINATION)

    #   Mirror comparing
    if options.MIRROR in ['L', 'T']:
        if options.MIRROR == 'L':
            x = x.transpose(Image.FLIP_LEFT_RIGHT)
        elif options.MIRROR == 'T':
            x = x.transpose(Image.FLIP_TOP_BOTTOM)
        Result(x, y, 0.8, "Mirror")

    #   Rotation comparing
    if options.ROTATION in ['90', '180', '270']:
        if options.ROTATION == '90':
            x = x.transpose(Image.ROTATE_270)
        elif options.ROTATION == '180':
            x = x.transpose(Image.ROTATE_180)
        elif options.ROTATION == '270':
            x = x.transpose(Image.ROTATE_90)
        Result(x, y, 0.8, "Rotation")

    #   Common comparing
    Result(x, y, 0.8, "Common")


def Result(SourceImage, DestImage, ThresholdValue, Prefix):
    x = make_regalur_image(SourceImage)
    y = make_regalur_image(DestImage)
    ret = calc_similar(x, y)
    print 'Similarity Rate is <{}>'.format(ret)
    if ret >= ThresholdValue:
        print 'Result({}): <{}>'.format(Prefix, 'Pass')
        sys.exit(StdErrCode['SUCCESS_SAME'])
    print 'Result({}): <{}>'.format(Prefix, 'Failure')
    sys.exit(StdErrCode['SUCCESS_DIFFERENT'])


def hist_similar(lh, rh):
    assert len(lh) == len(rh)
    return sum(1 - (0 if l == r else float(abs(l - r)) / max(l, r)) for l, r in zip(lh, rh)) / len(lh)


def calc_similar(li, ri):
    return sum(hist_similar(l.histogram(), r.histogram()) for l, r in zip(split_image(li), split_image(ri))) / 64.0


def split_image(img, part_size=(64, 64)):
    w, h = img.size
    pw, ph = part_size
    assert w % pw == h % ph == 0
    return [img.crop((i, j, i + pw, j + ph)).copy() for i in xrange(0, w, pw) for j in xrange(0, h, ph)]


def make_regalur_image(img, size=(512, 512)):
    return img.resize(size)


# Begin
if __name__ == '__main__':

    import os
    import sys
    from optparse import OptionParser

    #   Define / Parse parameters
    usage = 'usage: %prog -s SourceImage -d DestinationImage [-r Degrees]|[-m [L|U]]'
    version = '1.0'
    epilog = 'ERROR CODE: , ' + \
        ', '.join(['"{}: {}"'.format(key, value)
                  for (key, value) in StdErrCode.items()])
    parser = OptionParser(usage=usage, version=version, epilog=epilog)
    parser.add_option('-s', '--source', dest='SOURCE',
                      help='Source image file. This image shall NOT be mirrored or rotated!')
    parser.add_option('-d', '--destination', dest='DESTINATION',
                      help='Destination image file')
    parser.add_option('-r', '--rotation', dest='ROTATION',
                      help='Rotate source image file by degrees (clockwise) before comparing. Value shall be 90 / 180 / 270. This switch cannot work with -m.')
    parser.add_option('-m', '--mirror', dest='MIRROR',
                      help='Mirror source image file if this switch is specified. Value shall be L (Left-to-Right) or T (Top-to-Bottom). This switch cannot work with -r.')

    #   Get parameters
    (options, args) = parser.parse_args()

    #   Check parameters
    if options.SOURCE is None:
        parser.error('Souce image file shall be specified.')
    if options.DESTINATION is None:
        parser.error('Destination image file shall be specified.')
    if os.path.exists(options.SOURCE) is False:
        parser.error('Source image file does not exist!')
    if os.path.exists(options.DESTINATION) is False:
        parser.error('Destination image file does not exist!')
    if options.ROTATION not in [None, '90', '180', '270']:
        parser.error('Rotation degree value is not an expected one!')
    if options.MIRROR not in [None, 'L', 'T']:
        parser.error('Mirror method is not an expected one!')
    if options.ROTATION is not None and options.MIRROR is not None:
        parser.error('Rotation and Mirror cannot be specified at the same time!')

    #   Start comparing
    ImageCompare(options)
