# coding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os

Root = 'T:'
target = r'ColourImages\color_calib_result.ini'

RootList = os.listdir(Root)
RootList.sort()
RootList = filter(lambda x: os.path.isdir(r'{}\{}'.format(Root, x)), RootList)
RootList = map(lambda x: r'{}\{}'.format(Root, x), RootList)
print RootList

with open('output.csv', 'a+') as f:
	f.write('SN,Value1,Value2,Value3\n')

for i in RootList:
	i_list = os.listdir(i)
	i_list.sort()
	i_list = filter(lambda x: os.path.isdir(r'{}\{}'.format(i, x)), i_list)
	i_list = map(lambda x: r'{}\{}'.format(i, x), i_list)

	for j in i_list:
		tmp = []
		try:
			t = r'{}\{}'.format(j, target)
			if os.path.isfile(t):
				with open(t) as f:
					srcData = f.readlines()[0].split(' ')
					tmp.append(j)
					tmp.append(int(srcData[1]))
					tmp.append(int(srcData[5]))
					tmp.append(int(srcData[9]))
					with open('output.csv', 'a+') as f:
						f.write('{}\n'.format(str(tmp).replace('[','').replace(']','')))
		except Exception as e:
			print str(e)
			continue
