import os
from Tkinter import *


def executeViaCMD(cmd_line):
    print os.system(cmd_line)

def callback(url_string):
    chrome_app='/Applications/Google Chrome.app'
    cmd_line='open -na "{0}" --args --new-window --args --window-size=1440,1200 "{1}"'.format(chrome_app,url_string)
    executeViaCMD(cmd_line)

def returnBranchString(type):
    if type == 'master':
        return 'CURRENT_RELEASE={0}&CURRENT_RELEASE_BRANCH=master'.format(__current_version__)
    elif type == 'released':
        return 'CURRENT_RELEASE={0}&CURRENT_RELEASE_BRANCH={0}'.format(__current_released_version__)

def triggerAutomation(type, browser):
    cmd_line='curl -I -X POST "https://{0}@jenkins.servicemax.io/job/Max/job/neocore-dc2-automation/buildWithParameters?{1}&BROWSER={2}&TEST_SUITE=smoke&VM_USERNAME=system&VM_PASSWORD=hoofkick&WEBDRIVERIO_LOG_LEVEL=silent"'.format(credential, returnBranchString(type), browser)
    executeViaCMD(cmd_line)

def triggerIntegrationAutomation(type, browser):
    cmd_line='curl -I -X POST "https://{0}@jenkins.servicemax.io/job/Max/job/neocore-dc2-automation-integration/buildWithParameters?{1}&BROWSER={2}&SYSTEM_PASSWORD=hoofkick&WEBDRIVERIO_LOG_LEVEL=silent"'.format(credential, returnBranchString(type), browser)
    executeViaCMD(cmd_line)


#   global definition
credential="james:xxxxxxxxxxxxxxx"
__current_version__='20.1.0'
__current_released_version__='19.3.0'

#   initial
wControlPanel=Tk()
wControlPanel.title('Control Panel of Automation Jobs')
wControlPanel.resizable(width=False, height=False)

#   GUI Definition: Property
ButtonWidth=10

##    Group: Basic
BasicFrameRow=0
BasicFrame=LabelFrame(wControlPanel, text='Automation Daily Jobs', width=300, padx=3, pady=3)
BasicFrame.grid(row=BasicFrameRow, column=4, columnspan=1)

##  standard
autoJob=Label(BasicFrame, text='[neocore-dc2-automation]', fg='blue', cursor="hand2")
autoJob.grid(row=BasicFrameRow+1, column=1)
autoJob.bind('<Button-1>', lambda e: callback('https://jenkins.servicemax.io/job/Max/job/neocore-dc2-automation/'))
###
Label(BasicFrame, text='Master').grid(row=BasicFrameRow+1, column=2)
###
master_chromeBTN = Button(BasicFrame, text='Chrome', width=ButtonWidth)
master_chromeBTN.grid(row=BasicFrameRow+1, column=3)
master_chromeBTN.bind('<Button-1>', lambda e: triggerAutomation('master', 'chrome'))
###
master_firefoxBTN = Button(BasicFrame, text='Firefox', width=ButtonWidth)
master_firefoxBTN.grid(row=BasicFrameRow+1, column=4)
master_firefoxBTN.bind('<Button-1>', lambda e: triggerAutomation('master', 'firefox'))
###
Label(BasicFrame, text='{0}'.format(__current_released_version__)).grid(row=BasicFrameRow+2, column=2)
###
release_chromeBTN = Button(BasicFrame, text='Chrome', width=ButtonWidth)
release_chromeBTN.grid(row=BasicFrameRow+2, column=3)
release_chromeBTN.bind('<Button-1>', lambda e: triggerAutomation('released', 'chrome'))
###
# release_firefoxBTN = Button(BasicFrame, text='Firefox', width=ButtonWidth)
# release_firefoxBTN.grid(row=BasicFrameRow+2, column=4)
# release_firefoxBTN.bind('<Button-1>', lambda e: triggerAutomation('released', 'firefox'))

##  integration
autoJobI=Label(BasicFrame, text='[neocore-dc2-automation-Integration]', fg='blue', cursor="hand2")
autoJobI.grid(row=BasicFrameRow+3, column=1)
autoJobI.bind('<Button-1>', lambda e: callback('https://jenkins.servicemax.io/job/Max/job/neocore-dc2-automation-integration/'))
###
Label(BasicFrame, text='Master').grid(row=BasicFrameRow+3, column=2)
###
imaster_chromeBTN=Button(BasicFrame, text='Chrome', width=ButtonWidth)
imaster_chromeBTN.grid(row=BasicFrameRow+3, column=3)
imaster_chromeBTN.bind('<Button-1>', lambda e: triggerIntegrationAutomation('master', 'chrome'))
###
imaster_firefoxBTN=Button(BasicFrame, text='Firefox', width=ButtonWidth)
imaster_firefoxBTN.grid(row=BasicFrameRow+3, column=4)
imaster_firefoxBTN.bind('<Button-1>', lambda e: triggerIntegrationAutomation('master', 'firefox'))
###
Label(BasicFrame, text='{0}'.format(__current_released_version__)).grid(row=BasicFrameRow+4, column=2)
###
irelease_chromeBTN = Button(BasicFrame, text='Chrome', width=ButtonWidth)
irelease_chromeBTN.grid(row=BasicFrameRow+4, column=3)
irelease_chromeBTN.bind('<Button-1>', lambda e: triggerIntegrationAutomation('released', 'chrome'))
###
# irelease_firefoxBTN = Button(BasicFrame, text='Firefox', width=ButtonWidth)
# irelease_firefoxBTN.grid(row=BasicFrameRow+4, column=4)
# irelease_firefoxBTN.bind('<Button-1>', lambda e: triggerIntegrationAutomation('released', 'firefox'))


#    Set Window Property
wControlPanel.geometry('+100+0')
wControlPanel.call('wm', 'attributes', '.', '-topmost', '1')
wControlPanel.update()

# Display GUI and wait message
wControlPanel.mainloop()
