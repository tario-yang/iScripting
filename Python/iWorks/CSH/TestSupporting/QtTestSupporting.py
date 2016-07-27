# -*- config: utf-8 -*-

import os, sys
import threading
import subprocess
import time
import re
import win32api
from PySide import QtCore, QtGui, QtUiTools

# Support Functions
#   Basic
def LoadUiFile(path, parent = None):
    Loader = QtUiTools.QUiLoader()
    UiFile = QtCore.QFile(path)
    UiFile.open(QtCore.QFile.ReadOnly)
    Ui = Loader.load(UiFile, parent)
    UiFile.close()
    return Ui

#   Support
def OpenDirectory(path):
    def Executor():
        os.system(r'explorer "{}"'.format(path))
    threading.Thread(target = Executor).start()
    InfoStatusReport(path)

def OpenApplication(app):
    def Executor():
        subprocess.Popen(app)
    threading.Thread(target = Executor).start()
    InfoStatusReport(app)

def ReturnSysPath():
    WinVer = os.sys.getwindowsversion() # e.g. sys.getwindowsversion(major=5, minor=1, build=2600, platform=2, service_pack='Service Pack 2')
    if WinVer.major == 5 and WinVer.minor == 1: # Is WinXP
        ProgramData = r'{}\Application Data'.format(os.environ.get('ALLUSERSPROFILE'))
    else:
        ProgramData = os.environ.get('ProgramData')
    ProgramFiles       = os.environ.get('ProgramFiles')
    CommonProgramFiles = os.environ.get('CommonProgramFiles')
    Installation       = '{}\Trophy\Acquisition'.format(CommonProgramFiles)
    return (ProgramData, ProgramFiles, CommonProgramFiles, Installation, ProgramFiles)

def ProductSelected():
    if MainDialog.radioButtonCS3500.isChecked():
        return 'CS 3500'
    elif MainDialog.radioButtonUVC1X00.isChecked():
        return 'UVC1X00'

def ReturnProduct():
    if ProductSelected() == 'CS 3500':
        ret = ('AcqAltair', 'DriverAltair')
    elif ProductSelected() == 'UVC1X00':
        ret = ('AcqTaurus', 'DriverTaurus')
    return ret

def MessageBox(key, title, message):
    if key == 'information':
        QMessageBox.information(None, title, message)
    elif key == 'error':
        QMessageBox.critical(None, title, message)
    elif key == 'warn':
        QMessageBox.warning(None, title, message)
    elif key == 'question':
        QMessageBox.question(None, title, message)

def InfoMessageBox(title, message):
    MessageBox('information', title, message)

def ErrorMessageBox(title, message):
    MessageBox('error', title, message)

def WarnMessageBox(title, message):
    MessageBox('warning', title, message)

def QuestionMessageBox(title, message):
    MessageBox('question', title, message)

def StatusReport(key, message):
    if len(message) >= 41:
        message = message[:38] + '...'
    if key == 'information':
        MainDialog.labelStatus.setText('info -> {}'.format(message))
    elif key == 'error':
        MainDialog.labelStatus.setText('err -> {}'.format(message))

def InfoStatusReport(message):
    StatusReport('information', message)

def ErrorStatusReport(message):
    StatusReport('error', message)

def ReturnFileVersion(path):
    try:
        VerInfo = win32api.GetFileVersionInfo(path, '\\')
        ms = VerInfo['FileVersionMS']
        ls = VerInfo['FileVersionLS']
        return '{}.{}.{}.{}'.format(win32api.HIWORD(ms), win32api.LOWORD(ms), win32api.HIWORD(ls), win32api.LOWORD(ls))
    except:
        return 'NOT FOUND'

def GenerateADummyLogFile(fullfilename, message):
    try:
        with open(fullfilename, 'w+') as f: f.write('{}'.format(message))
    except:
        return False
    else:
        return True

def ReturnLogMetadata():
    timestamp = time.strftime('%Y%m%d')
    LogDir    = r'{}\TW\{}\log'.format(ReturnSysPath()[0], ReturnProduct()[0])
    return (timestamp, LogDir)


# Linked Functions
@QtCore.Slot()
def OpenLogFile():
    ret = ReturnLogMetadata()
    if ProductSelected() == 'CS 3500':
        LogFilePrefix = LogFilePrefix_CS3500[:]
    elif ProductSelected() == 'UVC1X00':
        LogFilePrefix = LogFilePrefix_UVC1X00[:]
    else:
        return
    for i in LogFilePrefix:
        LogFile = '{}\{}{}.csv'.format(ret[1], i, ret[0])
        if os.path.exists(LogFile):
            OpenApplication('notepad.exe {}'.format(LogFile))

@QtCore.Slot()
def OpenRecentLogSession(): pass
    # ret = ReturnLogMetadata()
    # if ReturnProduct()[0] == 'AcqAltair':
    #     pass
    # elif ReturnProduct()[0] == 'AcqTaurus':
    #     pass
    # else:
    #     return

@QtCore.Slot()
def TrackLogFile(path): pass

@QtCore.Slot()
def GenerateDummyLogFiles():
    Number = 100
    outputDir = r'{}\TW\{}\log'.format(ReturnSysPath()[0], ReturnProduct()[0])
    if ReturnProduct()[0] == 'AcqAltair':
        LogFileList = LogFilePrefix_CS3500[:]
    elif ReturnProduct()[0] == 'AcqTaurus':
        LogFileList = LogFilePrefix_UVC1X00[:]
    for i in LogFileList:
        for j in xrange(0,Number):
            timemark  = int(time.time()-j*24*3600)
            timestamp = time.strftime('%Y%m%d', time.localtime(timemark))
            dummyfile = '{}\{}{}.csv'.format(outputDir, i, timestamp)
            if GenerateADummyLogFile(dummyfile, timestamp):
                os.utime(dummyfile, (timemark, timemark))

@QtCore.Slot()
def DisplayAvailableMeshNumber():
    if ReturnProduct()[0] == 'AcqAltair':
        ModelFile = r'{}\TW\{}\Models\MultiViewModel.txt'.format(ReturnSysPath()[0], ReturnProduct()[0])
        if os.path.exists(ModelFile):
            numLower      = 0
            numUpper      = 0
            numBuccal     = 0
            ModelFileList = open(ModelFile, 'r').readlines()
            for i in xrange(0, len(ModelFileList)):
                if re.match('^[0-9]+\s[012]{1}\\n', ModelFileList[i]):
                    j = ModelFileList[i].split(' ')
                    if j[1] == '0\n':
                        numLower += 1
                    elif j[1] == '1\n':
                        numUpper += 1
                    elif j[1] == '2\n':
                        numBuccal += 1
            InfoStatusReport('L({}) + U({}) + B({}) = {}'.format(numLower, numUpper, numBuccal, numLower+numUpper+numBuccal))
        else:
            ErrorStatusReport('MultiViewModel.txt is not found.')
    else:
        return

@QtCore.Slot()
def ReportSWVersion():
    if ReturnProduct()[0] == 'AcqAltair':
        SWList = [('ACQ', r'{}\{}\CS 3500 Acquisition Interface.exe'.format(ReturnSysPath()[3], ReturnProduct()[1])),
            ('Algorithm', r'{}\{}\D3DAlgorithm.dll'.format(ReturnSysPath()[3], ReturnProduct()[1]))
            ('DIS/TW', ''),
            ('CSOI', ''),
            ('SDK', ''),
            ('CS Restore', ''),
            ('CS Model', ''),
            ('MeshConvert', ''),
            ('Firmware', ''),
        ]
    elif ReturnProduct()[0] == 'AcqTaurus':
        SWList = [('ACQ', ''),
            ('DIS/TW', ''),
            ('SDK', ''),
            ('Firmware 1500 UVC', ''),
        ]
    else:
        return

@QtCore.Slot()
def ButtonStatus():
    ButtonList_CS3500  = ['MainDialog.pushButton_CS3500_Data',
        'MainDialog.pushButton_CS3500_Debug_Images',
        'MainDialog.pushButton_CS3500_Diagnose',
        'MainDialog.pushButton_CS3500_Models',
        'MainDialog.pushButton_DisplayMeshNumber'
    ]
    ButtonList_UVC1X00 = ['MainDialog.pushButton_UVC1X00_Data',
        'MainDialog.pushButton_UVC1X00_Tmp',
        'MainDialog.pushButton_Installation_SDK'
    ]
    if MainDialog.radioButtonCS3500.isChecked():
        for i in ButtonList_CS3500:
            exec('{}.setEnabled(True)'.format(i))
        for i in ButtonList_UVC1X00:
            exec('{}.setEnabled(False)'.format(i))
    elif MainDialog.radioButtonUVC1X00.isChecked():
        for i in ButtonList_CS3500:
            exec('{}.setEnabled(False)'.format(i))
        for i in ButtonList_UVC1X00:
            exec('{}.setEnabled(True)'.format(i))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    MainDialog = LoadUiFile('./TestSupporting.ui')
    MainDialog.move(0,0)
    # Set style of GUI
    QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Plastique'))
    # Connect signal
    #   Buttons
    MainDialog.pushButton_TW                   .clicked.connect(lambda: OpenDirectory(ReturnSysPath()[0]+'\TW'))
    MainDialog.pushButton_ProductHome          .clicked.connect(lambda: OpenDirectory(r'{}\TW\{}'.format(ReturnSysPath()[0], ReturnProduct()[0])))
    MainDialog.pushButton_Log                  .clicked.connect(lambda: OpenDirectory(r'{}\TW\{}\log'.format(ReturnSysPath()[0], ReturnProduct()[0])))
    MainDialog.pushButton_CS3500_Debug_Images  .clicked.connect(lambda: OpenDirectory(r'{}\TW\{}\cs3500_debug_image'.format(ReturnSysPath()[0], ReturnProduct()[0])))
    MainDialog.pushButton_CS3500_Models        .clicked.connect(lambda: OpenDirectory(r'{}\TW\{}\Models'.format(ReturnSysPath()[0], ReturnProduct()[0])))
    MainDialog.pushButton_CS3500_Data          .clicked.connect(lambda: OpenDirectory(r'{}\TW\{}\Data'.format(ReturnSysPath()[0], ReturnProduct()[0])))
    MainDialog.pushButton_CS3500_Diagnose      .clicked.connect(lambda: OpenDirectory(r'{}\TW\{}\Diagnose'.format(ReturnSysPath()[0], ReturnProduct()[0])))
    MainDialog.pushButton_UVC1X00_Data         .clicked.connect(lambda: OpenDirectory(r'{}\TW\{}\data'.format(ReturnSysPath()[0], ReturnProduct()[0])))
    MainDialog.pushButton_UVC1X00_Tmp          .clicked.connect(lambda: OpenDirectory(r'{}\TW\{}\tmp'.format(ReturnSysPath()[0], ReturnProduct()[0])))
    MainDialog.pushButton_WinVirtualStore      .clicked.connect(lambda: OpenDirectory('{}\AppData\Local\VirtualStore'.format(os.environ.get('HOMEPATH'))))
    MainDialog.pushButton_Installation_Home    .clicked.connect(lambda: OpenDirectory(r'{}\{}'.format(ReturnSysPath()[3], ReturnProduct()[1])))
    MainDialog.pushButton_Installation_SDK     .clicked.connect(lambda: OpenDirectory(r'{}\AcqSdk'.format(ReturnSysPath()[3])))
    MainDialog.pushButton_FirmwarePackage      .clicked.connect(lambda: OpenDirectory(r'{}\{}\update'.format(ReturnSysPath()[0], ReturnProduct()[0])))
    MainDialog.pushButton_OpenLogFile          .clicked.connect(OpenLogFile)
    MainDialog.pushButton_TrackLogFile         .clicked.connect(TrackLogFile)
    MainDialog.pushButton_OpenRecentLogSession .clicked.connect(OpenRecentLogSession)
    MainDialog.pushButton_GenerateDummyLogFiles.clicked.connect(GenerateDummyLogFiles)
    MainDialog.pushButton_DisplayMeshNumber    .clicked.connect(DisplayAvailableMeshNumber)
    MainDialog.pushButton_SDKLauncher          .clicked.connect(lambda: OpenApplication(r'{}\AcquisitionSampleAdvanced.exe'.format(ReturnSysPath()[3])))
    MainDialog.pushButton_Version              .clicked.connect(ReportSWVersion)
    #   Event
    MainDialog.radioButtonCS3500               .clicked.connect(ButtonStatus)
    MainDialog.radioButtonUVC1X00              .clicked.connect(ButtonStatus)
    #   Some variables used for `def`
    LogFilePrefix_CS3500  = ['AcqAltair_']
    LogFilePrefix_UVC1X00 = ['AcqTaurus_sw_log_', 'AcqTaurus_fw_log_', 'AcqTaurus_sdk_log_']
    # Display GUI
    ButtonStatus()
    InfoStatusReport('Initiated.')
    MainDialog.show()
    sys.exit(app.exec_())
