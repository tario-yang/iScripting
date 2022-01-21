# -*- coding: utf-8 -*-

import os
from Tkinter import *


def executeViaCMD(cmd_line):
    print 'Received: {0}'.format(cmd_line)
    print os.system(cmd_line)


def callback(url_string):
    chrome_app = '/Applications/Google Chrome.app'
    cmd_line = 'open -na "{0}" --args --new-window --args --window-size=1440,1200 "{1}"'.format(
        chrome_app, url_string)
    executeViaCMD(cmd_line)


def returnBranchString(type):
    if type == 'master':
        return 'CURRENT_RELEASE={0}&CURRENT_RELEASE_BRANCH=master'.format(__current_version__)
    elif type == 'released':
        return 'CURRENT_RELEASE={0}&CURRENT_RELEASE_BRANCH={0}'.format(__current_released_version__)


def triggerAutomation(type, browser):
    jobName = 'neocore-dc2-automation'
    cmd_line = 'curl -I -X POST "https://{0}@{1}/{2}/{3}/buildWithParameters?{4}&BROWSER={5}&VM_USERNAME=system&VM_PASSWORD=hoofkick&WEBDRIVERIO_LOG_LEVEL=silent"'.format(
        credential, jenkinsURL, folderName, jobName, returnBranchString(type), browser)
    executeViaCMD(cmd_line)


def triggerIntegrationAutomation(type, browser):
    jobName = 'neocore-dc2-automation-integration'
    cmd_line = 'curl -I -X POST "https://{0}@{1}/{2}/{3}/buildWithParameters?{4}&BROWSER={5}&WEBDRIVERIO_LOG_LEVEL=silent"'.format(
        credential, jenkinsURL, folderName, jobName, returnBranchString(type), browser)
    executeViaCMD(cmd_line)

#   global definition
jenkinsURL = 'jenkins.xxxxxxxxxx.xxxxxxxxxx'
folderName = 'xxxxxxxxxx/xxxxxxxxxx/xxxxxxxxxx'
credential = 'xxxxxxxxxx%40xxxxxxxxxx.xxxxxxxxxx:xxxxxxxxxx'
__current_version__ = 'xxxxxxxxxx'
__current_released_version__ = 'xxxxxxxxxx'


#   initial
#############################################################
wControlPanel = Tk()
wControlPanel.title('*********')
wControlPanel.resizable(width=False, height=False)


#   GUI Definition: Property
#############################################################
ButtonWidth = 12


##    Group: Basic
#############################################################
BasicFrameRow = 0
BasicFrame = LabelFrame(
    wControlPanel, text='Jenkins Jobs', width=500, padx=3, pady=3)
BasicFrame.grid(row=BasicFrameRow, column=4, columnspan=1)


# standalone
#############################################################
autoJobRowNum = BasicFrameRow+10
autoJob = Label(
    BasicFrame, text='[neocore-dc2-automation]', fg='blue', cursor='hand2')
autoJob.grid(row=autoJobRowNum, column=1)
autoJob.bind('<Button-1>', lambda e: callback(
    'https://{0}/{1}/xxxxxxxxxx/'.format(jenkinsURL, folderName)))

Label(BasicFrame, text='Master').grid(row=autoJobRowNum, column=2)

master_chromeBTN = Button(BasicFrame, text='Chrome', width=ButtonWidth)
master_chromeBTN.grid(row=autoJobRowNum, column=3)
master_chromeBTN.bind(
    '<Button-1>', lambda e: triggerAutomation('master', 'chrome'))
###
master_firefoxBTN = Button(BasicFrame, text='Firefox', width=ButtonWidth)
master_firefoxBTN.grid(row=autoJobRowNum, column=4)
master_firefoxBTN.bind(
    '<Button-1>', lambda e: triggerAutomation('master', 'firefox'))
###
Label(BasicFrame, text='{0}'.format(__current_released_version__)).grid(
    row=autoJobRowNum+1, column=2)
###
release_chromeBTN = Button(BasicFrame, text='Chrome', width=ButtonWidth)
release_chromeBTN.grid(row=autoJobRowNum+1, column=3)
release_chromeBTN.bind(
    '<Button-1>', lambda e: triggerAutomation('released', 'chrome'))
###
# release_firefoxBTN = Button(BasicFrame, text='Firefox', width=ButtonWidth)
# release_firefoxBTN.grid(row=autoJobRowNum+1, column=4)
# release_firefoxBTN.bind('<Button-1>', lambda e: triggerAutomation('released', 'firefox'))


# integration
#############################################################
autoJobIRowNum = BasicFrameRow+20
autoJobI = Label(
    BasicFrame, text='[neocore-dc2-automation-Integration]', fg='blue', cursor='hand2')
autoJobI.grid(row=autoJobIRowNum, column=1)
autoJobI.bind('<Button-1>', lambda e: callback(
    'https://{0}/{1}/xxxxxxxxxx/'.format(jenkinsURL, folderName)))
###
Label(BasicFrame, text='Master').grid(row=autoJobIRowNum, column=2)
###
imaster_chromeBTN = Button(BasicFrame, text='Chrome', width=ButtonWidth)
imaster_chromeBTN.grid(row=autoJobIRowNum, column=3)
imaster_chromeBTN.bind(
    '<Button-1>', lambda e: triggerIntegrationAutomation('master', 'chrome'))
###
imaster_firefoxBTN = Button(BasicFrame, text='Firefox', width=ButtonWidth)
imaster_firefoxBTN.grid(row=autoJobIRowNum, column=4)
imaster_firefoxBTN.bind(
    '<Button-1>', lambda e: triggerIntegrationAutomation('master', 'firefox'))
###
Label(BasicFrame, text='{0}'.format(__current_released_version__)).grid(
    row=autoJobIRowNum+1, column=2)
###
irelease_chromeBTN = Button(BasicFrame, text='Chrome', width=ButtonWidth)
irelease_chromeBTN.grid(row=autoJobIRowNum+1, column=3)
irelease_chromeBTN.bind(
    '<Button-1>', lambda e: triggerIntegrationAutomation('released', 'chrome'))


#   Set Window Property
#############################################################
wControlPanel.geometry('+0+0')
wControlPanel.call('wm', 'attributes', '.', '-topmost', '0')
wControlPanel.update()


# Display GUI and wait message
#############################################################
wControlPanel.mainloop()
