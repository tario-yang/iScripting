# coding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


import os


def OutputDataToFile(filename, data):

	with open(filename, 'a+') as f:
		f.write('{}\n'.format(data.decode('gbk', 'ignore')))

def GeneratePathList(root, *arg):

	if arg is None:
		arg = ('desktop.ini')

	Result = []

	rootList = os.listdir(root)
	rootList.sort()
	rootList = filter(lambda x: x not in arg, rootList)
	rootList = filter(lambda x: os.path.isdir(r'{}\{}'.format(root, x)), rootList)
	rootList = map(lambda x: r'{}\{}'.format(root, x), rootList)

	for i in rootList:
		tmp = os.listdir(i)
		tmp.sort()
		tmp = filter(lambda x: x not in arg, tmp)
		tmp = filter(lambda x: os.path.isdir(r'{}\{}'.format(i, x)), tmp)
		tmp = map(lambda x: r'{}\{}'.format(i, x), tmp)
		Result.extend(tmp)

	return Result

def ToGetColorCalibData(filePathUnderSNDirectory='ColourImages\color_calib_result.ini'):

	outputFileName = 'output_color_calib_value.csv'
	if os.path.isfile(outputFileName):
		os.remove(outputFileName)
	OutputDataToFile(outputFileName, 'SN,Value1,Value2,Value3')

	for i in GeneratePathList(ROOT):
		tmp = []
		try:
			with open('{}\{}'.format(i, filePathUnderSNDirectory)) as f:
				srcData = f.readlines()[0].split(' ')
				tmp.append(i)
				tmp.append(int(srcData[1]))
				tmp.append(int(srcData[5]))
				tmp.append(int(srcData[9]))
				OutputDataToFile(outputFileName, str(tmp).replace('[','').replace(']',''))
		except Exception as e:
			print str(e)
			continue

ROOT = 'T:'
ToGetColorCalibData()
