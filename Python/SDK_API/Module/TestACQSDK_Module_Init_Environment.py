# Import required modules
try:
    import sys
    import win32com.client
    import win32gui
    from win32con import *
    import win32con
    import TestACQSDK_Module_Global_Definition as gDef
except ImportError:
    print "Required modules are NOT imported!"
    sys.exit(1)
else:
    # Mark: start
    print gDef.Output_Header() + "Initialization process starts."
    print gDef.Output_Header() + "\t" + "Required modules are imported."

# Create COM object
try:
    objACQSDK_CSDevice_1 = win32com.client.Dispatch(gDef.ACQSDK_ProgID)
except:
    print gDef.Output_Header() + "\t" + "Error occurs when creating COM object for " + '"' + gDef.ACQSDK_ProgID + '"' + "!"
    sys.exit(1)
else:
    print gDef.Output_Header() + "\t" + "COM object, " + '"' + gDef.ACQSDK_ProgID + '"' + ",has been created."

# Create Window object
try:
    def WndProc(hWnd, msg, wParam, lParam):
        if msg == WM_PAINT:
            hdc,ps = win32gui.BeginPaint(hWnd)
            rect = win32gui.GetClientRect(hWnd)
            win32gui.EndPaint(hWnd,ps)
        if msg == WM_DESTROY:
            win32gui.PostQuitMessage(0)
        return win32gui.DefWindowProc(hWnd, msg, wParam, lParam)
    def WaitWindowMessage(hWnd):
        win32gui.ShowWindow(hWnd, SW_SHOWNORMAL)
        win32gui.UpdateWindow(hWnd)
        win32gui.PumpMessages()
    def WindowObjectCreate():
        objWin = win32gui.WNDCLASS()
        objWin.hbrBackground = COLOR_BTNFACE
        objWin.hCursor = win32gui.LoadCursor(0, IDC_ARROW)
        objWin.hIcon = win32gui.LoadIcon(0, IDI_APPLICATION)
        objWin.lpszClassName = gDef.TestACQSDK_LiveVideo_Window_Class
        objWin.lpfnWndProc = WndProc
        reg_objWin = win32gui.RegisterClass(objWin)
        hWnd = win32gui.CreateWindow(
                reg_objWin,
                gDef.TestACQSDK_LiveVideo_Window_Title,
                WS_OVERLAPPEDWINDOW,
                gDef.TestACQSDK_LiveVideo_Window_Position[0],
                gDef.TestACQSDK_LiveVideo_Window_Position[1],
                gDef.TestACQSDK_LiveVideo_Window_Size[0],
                gDef.TestACQSDK_LiveVideo_Window_Size[1],
                0,
                0,
                0,
                None)
        return hWnd
    def WindowObjectKill(hWnd):
        win32gui.PostMessage(hWnd, win32con.WM_CLOSE, 0, 0)
except:
    print gDef.Output_Header() + "\t" + "Error occurs when creating functions of Window object."
    sys.exit(1)
else:
    print gDef.Output_Header() + "\t" + "Functions of Window object have been defined."

# Mark: end
print gDef.Output_Header() + "Initialization process ends.\n"

# Display the window when executing directly
if __name__ == '__main__':
    hWnd = WindowObjectCreate()
    WaitWindowMessage(hWnd)
