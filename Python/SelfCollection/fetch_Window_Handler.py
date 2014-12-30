import win32gui

def handler(hwnd, lParam):
	if win32gui.IsWindowVisible(hwnd):
		if 'Stack Overflow' in win32gui.GetWindowText(hwnd):
			win32gui.MoveWindow(hwnd, 0,0,760, 500, True)

win32gui.EnumWindows(handler, None)
