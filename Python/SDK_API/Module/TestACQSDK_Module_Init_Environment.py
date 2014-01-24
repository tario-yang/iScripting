# Import required modules
try:
	import sys, time, datetime
	import win32com.client, win32gui, win32con
	from win32con import *
	import xml.etree.ElementTree as XMLET
	import TestACQSDK_Module_Global_Definition as GDef
except ImportError:
	print "One or more required modules are missing!"
	sys.exit(1)

try:
	# Function to return Output Header. The header is a timestamp.
	def Output_Header():
		return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "\t"

	# Function to output content to console and log file
	# [Placeholder]

	# Function of Creating COM Object
	def CreateCOMObject(ProgID):
		return win32com.client.Dispatch(ProgID)
	# Function of Creating COM Event
	def CreateCOMObjectEvent(ProgID, Event):
		return win32com.client.DispatchEvents(ProgID,Event)

	# Class of Callback
	# [Placeholder]

	# Function of XMLReader
	# [Placeholder]

	# Functions of Window object
	def WndProc(hWnd, msg, wParam, lParam):
		if msg == WM_PAINT:
			hdc,ps = win32gui.BeginPaint(hWnd)
			rect = win32gui.GetClientRect(hWnd)
			win32gui.EndPaint(hWnd,ps)
		if msg == WM_DESTROY:
			win32gui.PostQuitMessage(0)
		return win32gui.DefWindowProc(hWnd, msg, wParam, lParam)
	def WindowObjectCreate():
		objWin = win32gui.WNDCLASS()
		objWin.hbrBackground = COLOR_BTNFACE
		objWin.hCursor = win32gui.LoadCursor(0, IDC_ARROW)
		objWin.hIcon = win32gui.LoadIcon(0, IDI_APPLICATION)
		objWin.lpszClassName = GDef.TestACQSDK_LiveVideo_Window_Class
		objWin.lpfnWndProc = WndProc
		reg_objWin = win32gui.RegisterClass(objWin)
		hWnd = win32gui.CreateWindow(
				reg_objWin,
				GDef.TestACQSDK_LiveVideo_Window_Title,
				WS_OVERLAPPEDWINDOW,
				GDef.TestACQSDK_LiveVideo_Window_Position[0],
				GDef.TestACQSDK_LiveVideo_Window_Position[1],
				GDef.TestACQSDK_LiveVideo_Window_Size[0],
				GDef.TestACQSDK_LiveVideo_Window_Size[1],
				0, 0, 0, None)
		win32gui.ShowWindow(hWnd, SW_SHOWNORMAL)
		win32gui.UpdateWindow(hWnd)
		win32gui.PumpMessages()
	def WindowObjectKill(hWnd):
		win32gui.PostMessage(hWnd, win32con.WM_CLOSE, 0, 0)
except:
	print "Defined function/class includes error/mistake."
	sys.exit(1)
else:
	print Output_Header() + "\t" + "Initiated."

# Display the window when executing directly
if __name__ == '__main__':
	WindowObjectCreate()
