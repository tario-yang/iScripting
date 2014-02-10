import Tkinter
import win32com.client
import win32gui

def ACQSDK_Init():
	hWnd = win32gui.FindWindow("TkTopLevel","SDK Testing: Live Video")
	ret = objCSDevice.ACQSDK_Init(hWnd)
	print ret

def ACQSDK_Uninit():
	hWnd = win32gui.FindWindow("TkTopLevel","SDK Testing: Live Video")
	ret = objCSDevice.ACQSDK_Uninit()
	print ret
	
def ACQSDK_StartPlay():
	hWnd = win32gui.FindWindow("TkTopLevel","SDK Testing: Live Video")
	ret = objCSDevice.ACQSDK_StartPlay()
	print ret

def ACQSDK_PausePlay():
	hWnd = win32gui.FindWindow("TkTopLevel","SDK Testing: Live Video")
	ret = objCSDevice.ACQSDK_PausePlay()
	print ret

def ACQSDK_StopPlay():
	hWnd = win32gui.FindWindow("TkTopLevel","SDK Testing: Live Video")
	ret = objCSDevice.ACQSDK_StopPlay()
	print ret

def ACQSDK_Capture():
	hWnd = win32gui.FindWindow("TkTopLevel","SDK Testing: Live Video")
	num = 1
	ret = objCSDevice.ACQSDK_Capture(num)
	print ret
	
def ACQSDK_CaptureEx():
	hWnd = win32gui.FindWindow("TkTopLevel","SDK Testing: Live Video")
	num = 1
	position = u"aaa.jpg"
	if isinstance(position, unicode): 
		print "OK"
	ret = objCSDevice.ACQSDK_CaptureEx(num,position)
	print ret

window_control_panel = Tkinter.Tk()
window_live_video    = Tkinter.Tk()

button_init       = Tkinter.Button(window_control_panel, text ="ACQSDK_Init",      command = ACQSDK_Init).grid(row=1,column=1)
button_uninit     = Tkinter.Button(window_control_panel, text ="ACQSDK_Uninit",    command = ACQSDK_Uninit).grid(row=1,column=2)
button_startplay  = Tkinter.Button(window_control_panel, text ="ACQSDK_StartPlay", command = ACQSDK_StartPlay).grid(row=1,column=3)
button_pauseplay  = Tkinter.Button(window_control_panel, text ="ACQSDK_PausePlay", command = ACQSDK_PausePlay).grid(row=1,column=4)
button_stopplay   = Tkinter.Button(window_control_panel, text ="ACQSDK_StopPlay",  command = ACQSDK_StopPlay).grid(row=1,column=5)
button_capture    = Tkinter.Button(window_control_panel, text ="ACQSDK_Capture",   command = ACQSDK_Capture).grid(row=1,column=6)
button_captureex  = Tkinter.Button(window_control_panel, text ="ACQSDK_CaptureEx", command = ACQSDK_CaptureEx).grid(row=1,column=7)

window_control_panel.geometry("1024x23+0+0")
window_control_panel.title("SDK Testing: Control Panel")
window_live_video.geometry("640x480+300+300")
window_live_video.title("SDK Testing: Live Video")

objCSDevice = win32com.client.Dispatch("ACQSDK.CSDevice.1")

window_live_video.mainloop()