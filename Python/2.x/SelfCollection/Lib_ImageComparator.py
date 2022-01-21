# coding: utf-8

'''
This script is to compare both images
'''

import Image

def ImageComparator(srcImage, destImage, isObject=False, thresholdValue=0.9, debug=False):
	if isObject:
		x = srcImage
		y = destImage
	else:
		x = Image.open(srcImage)
		y = Image.open(destImage)
	x = make_regalur_image(x)
	y = make_regalur_image(y)
	ret = calc_similar(x, y)
	if debug is True:
		print 'Similarity Rate is <{}>'.format(ret)
	return True if ret >= thresholdValue else False

def make_regalur_image(img, size=(512, 512)):
	return img.resize(size)

def calc_similar(li, ri):
	return sum(hist_similar(l.histogram(), r.histogram()) for l, r in zip(split_image(li), split_image(ri))) / 64.0

def hist_similar(lh, rh):
	assert len(lh) == len(rh)
	return sum(1 - (0 if l == r else float(abs(l - r)) / max(l, r)) for l, r in zip(lh, rh)) / len(lh)

def split_image(img, part_size=(64, 64)):
	w, h = img.size
	pw, ph = part_size
	assert w % pw == h % ph == 0
	return [img.crop((i, j, i + pw, j + ph)).copy() for i in xrange(0, w, pw) for j in xrange(0, h, ph)]
