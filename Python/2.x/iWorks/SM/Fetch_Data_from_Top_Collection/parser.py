# coding: utf-8
# this script will generate resource.xls, storing cpu / mem data

import os
import sys
import re
import xlwt

def parseJCMD():
    pass

def DealwithStringLine(stringline):
    return stringline.rstrip('\n')

def IsTimestamp(stringline):
    ret = re.match('\d{8}_\d{6}\+\d{4}_\d{9}', stringline)
    if ret is None:
        return False
    else:
        return True

# Define
SampleLog = 'tests/Java_Native_Memory_Recorder.log'
Outputter = 'resource.xls'
book      = xlwt.Workbook(encoding="utf-8")
sheet1    = book.add_sheet("Statistic")

# CPU - general
sheet1.write(0, 0, 'Top CPU - General')
sheet1.write(1, 0, 'CPU - us')
sheet1.write(1, 1, 'CPU - sy')
sheet1.write(1, 2, 'CPU - ni')
sheet1.write(1, 3, 'CPU - id')
sheet1.write(1, 4, 'CPU - wa')
sheet1.write(1, 5, 'CPU - hi')
sheet1.write(1, 6, 'CPU - si')
sheet1.write(1, 7, 'CPU - st')

# Mem - General
sheet1.write(0, 8, 'Memory - General')
sheet1.write(1, 8, 'MEM - total')
sheet1.write(1, 9, 'MEM - used')
sheet1.write(1, 10, 'MEM - free')
sheet1.write(1, 11, 'MEM - buffers')
sheet1.write(1, 12, 'SWAP - total')
sheet1.write(1, 13, 'SWAP - used')
sheet1.write(1, 14, 'SWAP - free')
sheet1.write(1, 15, 'SWAP - cached')

# CPU - Java
sheet1.write(0, 16, 'Top CPU - Java')
sheet1.write(1, 16, 'CPU - us')
sheet1.write(1, 17, 'CPU - sy')
sheet1.write(1, 18, 'CPU - ni')
sheet1.write(1, 19, 'CPU - id')
sheet1.write(1, 20, 'CPU - wa')
sheet1.write(1, 21, 'CPU - hi')
sheet1.write(1, 22, 'CPU - si')
sheet1.write(1, 23, 'CPU - st')

# Mem - Java
sheet1.write(0, 24, 'Memory - Java')
sheet1.write(1, 24, 'MEM - total')
sheet1.write(1, 25, 'MEM - used')
sheet1.write(1, 26, 'MEM - free')
sheet1.write(1, 27, 'MEM - buffers')
sheet1.write(1, 28, 'SWAP - total')
sheet1.write(1, 29, 'SWAP - used')
sheet1.write(1, 30, 'SWAP - free')
sheet1.write(1, 31, 'SWAP - cached')

# Mem - jcmd
# sheet1.write(0, 33, 'Memory - jcmd')
# sheet1.write(1, 33, 'reserved')
# sheet1.write(1, 34, 'committed')

# Define variables
LineCount    = 2
retTopCPU    = []
retTopCPUALL = []
retTopMEM    = []
retTopMEMALL = []
retTopSWP    = []
retTopSWPALL = []
retJCMD      = []


with open(SampleLog) as f:
    for i in f.readlines():
        i = DealwithStringLine(i)

        if i.find('Cpu(s)') >= 0:
            for j in i.split(':')[1].strip(' ').split(','):
                retTopCPU.append(j.strip(' ').split(' ')[0])
            retTopCPUALL.append(retTopCPU)
            retTopCPU = []

        if i.find('KiB Mem') >= 0:
            for j in i.split(':')[1].strip(' ').split(','):
                retTopMEM.append(j.strip(' ').split(' ')[0])
            retTopMEMALL.append(retTopMEM)
            retTopMEM = []

        if i.find('KiB Swap') >= 0:
            for j in i.split(':')[1].strip(' ').split(','):
                retTopSWP.append(j.strip(' ').split(' ')[0])
            retTopSWP.append(j.split('.')[1].strip(' ').split(' ')[0])
            retTopSWPALL.append(retTopSWP)
            retTopSWP = []

        # if i.find('Total:') >= 0:
        #     for j in i.split(':')[1].strip(' ').split(', '):
        #         retJCMD.append(j.strip(' ').split(' ')[0].split('=')[1])

# Write data
for i in xrange(0, len(retTopCPUALL), 3):

    for j in [0, 1, 2]:

        # CPU - general
        sheet1.write(LineCount+i+j,  0, retTopCPUALL[i+j][0])
        sheet1.write(LineCount+i+j,  1, retTopCPUALL[i+j][1])
        sheet1.write(LineCount+i+j,  2, retTopCPUALL[i+j][2])
        sheet1.write(LineCount+i+j,  3, retTopCPUALL[i+j][3])
        sheet1.write(LineCount+i+j,  4, retTopCPUALL[i+j][4])
        sheet1.write(LineCount+i+j,  5, retTopCPUALL[i+j][5])
        sheet1.write(LineCount+i+j,  6, retTopCPUALL[i+j][6])
        sheet1.write(LineCount+i+j,  7, retTopCPUALL[i+j][7])

        # Mem - General
        sheet1.write(LineCount+i+j,  8, retTopMEMALL[i+j][0])
        sheet1.write(LineCount+i+j,  9, retTopMEMALL[i+j][1])
        sheet1.write(LineCount+i+j, 10, retTopMEMALL[i+j][2])
        sheet1.write(LineCount+i+j, 11, retTopMEMALL[i+j][3])
        sheet1.write(LineCount+i+j, 12, retTopSWPALL[i+j][0])
        sheet1.write(LineCount+i+j, 13, retTopSWPALL[i+j][1])
        sheet1.write(LineCount+i+j, 14, retTopSWPALL[i+j][2])
        sheet1.write(LineCount+i+j, 15, retTopSWPALL[i+j][3])

        # CPU - Java
        sheet1.write(LineCount+i+j, 16, retTopCPUALL[i+j+3][0])
        sheet1.write(LineCount+i+j, 17, retTopCPUALL[i+j+3][1])
        sheet1.write(LineCount+i+j, 18, retTopCPUALL[i+j+3][2])
        sheet1.write(LineCount+i+j, 19, retTopCPUALL[i+j+3][3])
        sheet1.write(LineCount+i+j, 20, retTopCPUALL[i+j+3][4])
        sheet1.write(LineCount+i+j, 21, retTopCPUALL[i+j+3][5])
        sheet1.write(LineCount+i+j, 22, retTopCPUALL[i+j+3][6])
        sheet1.write(LineCount+i+j, 23, retTopCPUALL[i+j+3][7])

        # Mem - Java
        sheet1.write(LineCount+i+j, 24, retTopMEMALL[i+j+3][0])
        sheet1.write(LineCount+i+j, 25, retTopMEMALL[i+j+3][1])
        sheet1.write(LineCount+i+j, 26, retTopMEMALL[i+j+3][2])
        sheet1.write(LineCount+i+j, 27, retTopMEMALL[i+j+3][3])
        sheet1.write(LineCount+i+j, 28, retTopSWPALL[i+j+3][0])
        sheet1.write(LineCount+i+j, 29, retTopSWPALL[i+j+3][1])
        sheet1.write(LineCount+i+j, 30, retTopSWPALL[i+j+3][2])
        sheet1.write(LineCount+i+j, 31, retTopSWPALL[i+j+3][3])

        book.save(Outputter)

