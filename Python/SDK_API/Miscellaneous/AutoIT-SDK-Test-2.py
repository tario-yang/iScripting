from win32con import *
import win32gui
import win32com.client

def WndProc(hwnd, msg, wParam, lParam):
    if msg == WM_PAINT:
        hdc,ps = win32gui.BeginPaint(hwnd)
        rect = win32gui.GetClientRect(hwnd)
        win32gui.EndPaint(hwnd,ps)
    if msg == WM_DESTROY:
        win32gui.PostQuitMessage(0)
    return win32gui.DefWindowProc(hwnd, msg, wParam, lParam)

wc = win32gui.WNDCLASS()
wc.hbrBackground = COLOR_BTNTEXT
wc.hCursor = win32gui.LoadCursor(0, IDC_ARROW)
wc.hIcon = win32gui.LoadIcon(0, IDI_APPLICATION)
wc.lpszClassName = "UVC ACQ - SDK Testing"
wc.lpfnWndProc = WndProc

reg = win32gui.RegisterClass(wc)
hwnd = win32gui.CreateWindow(
            reg,
            'UVC ACQ - SDK Testing',
            WS_OVERLAPPEDWINDOW,
            0,
            0,
            640,
            480,
            0,
            0,
            0,
            None)

win32gui.ShowWindow(hwnd, SW_SHOWNORMAL)

try:
    class SDKEvents():
        def OnHPEvents():
            print "hello"

    objCSDevice        = win32com.client.Dispatch("ACQSDK.CSDevice.1")
    objCSDeviceEvent   = win32com.client.DispatchWithEvents("ACQSDK.CSDevice.1", SDKEvents)
    objASImageUnit     = win32com.client.Dispatch("ACQSDK.ASImageUnit.1")
    objSDKCallbackInfo = win32com.client.Dispatch("ACQSDK.SDKCallbackInfo.1")

    a = objCSDevice.ACQSDK_SetLogPath(r".")
    b = objCSDevice.ACQSDK_Init(hwnd)
    c = objCSDevice.ACQSDK_StartPlay()
    d = objCSDevice.ACQSDK_Capture(objASImageUnit)
    x1 = objASImageUnit.get_white_image()
    x2 = objASImageUnit.save_image(r".\abc", x1)





except:
    print "ERROR"

win32gui.UpdateWindow(hwnd)
win32gui.PumpMessages()
