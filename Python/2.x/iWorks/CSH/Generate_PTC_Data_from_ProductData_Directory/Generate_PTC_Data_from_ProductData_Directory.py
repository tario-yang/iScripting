# coding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


import os
import re
import uuid
import threading
import time


def UUIDGenerator():
    return uuid.uuid4()


def worker(sn, path, output_file):

    SearchEnable = False

    log_file_list = os.listdir(path)
    log_file_list.sort()
    log_file_list = filter(lambda x: x.find('CS3500_') == 0, log_file_list)
    log_file = '{}\\{}'.format(path, log_file_list[-1])
    with open(log_file) as target:
        for line in target:
            if line.find('[scanner] GetSN') > 0 and line.find(sn[0:8]) > 0:
                SearchEnable = True
            if line.find('[MFG_TOOL] > FWUpgrade: CheckHeatupTemp()') > 0 and SearchEnable is True:
                tmp_ret = line.split(',')
                OutputToFile(output_file, '{},{},{},{}'.format(sn[0:8], tmp_ret[5].split(
                    '=')[1].strip(), tmp_ret[6].split('=')[1].strip(), log_file))


def OutputToFile(filename, data, overwrite=False):

    if overwrite is True and os.path.exists(filename):
        os.remove(filename)
    with open(filename, 'a+') as f:
        f.write('{}\n'.format(data.decode('gbk', 'ignore')))


def IsSeriesNumberDirectory(directory):

    if re.match('[A-Z]{4}\d{4}', directory) is None:
        return False
    else:
        return True


def IsMatchedDirectory(directory):

    if re.match('20\d{2}-\d{2}', directory) is None:
        return False
    else:
        return True


def GeneratePathList(root, *arg):

    if arg is None:
        arg = ('desktop.ini')

    rootList = os.listdir(root)
    rootList.sort()
    rootList = filter(lambda x: x not in arg, rootList)
    rootList = filter(
        lambda x: os.path.isdir('{}\\{}'.format(root, x)) and IsMatchedDirectory(x), rootList)
    rootList = map(lambda x: '{}\\{}'.format(root, x), rootList)

    if os.path.isfile(PATH_LIST):
        os.remove(PATH_LIST)
    for i in rootList:
        tmp = os.listdir(i)
        tmp.sort()
        tmp = filter(lambda x: x not in arg and os.path.isdir(
            '{}\\{}'.format(i, x)) and IsSeriesNumberDirectory(x), tmp)
        for t in tmp:
            OutputToFile(PATH_LIST, '{0}#{1}\\{0}'.format(t, i))


def ToGetPTCData():

    GeneratePathList(ROOT)

    print 'Output to {}'.format(OUTPUTFILENAME)
    OutputToFile(OUTPUTFILENAME, 'SN,PTC 0,PTC 1,Log File', True)

    ret = []

    with open(PATH_LIST) as f:
        for i in f:
            i = i.replace('\n', '')
            sn, path = i.split('#')
            path = '{}\\log'.format(path)
            if os.path.exists(path) is False:
                continue
            ret.append(threading.Thread(
                target=worker, args=(sn, path, '{}.txt'.format(UUIDGenerator()))))

    for t in ret:
        t.setDaemon(True)
        t.start()
        time.sleep(1)


ROOT = 'T:'
PATH_LIST = 'paths.out'
OUTPUTFILENAME = '{}.csv'.format(sys.argv[0])
ToGetPTCData()
