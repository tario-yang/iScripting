#cs ================================================================================================

 �ű�����: James Jun Yang, 19011956
 �����ʼ�: jun.yang@carestream.com
 �ű��汾: 3.1
 �ű�����: Supoort functions on Laptop
 ǰ��������������ʾ������һ�£�һ��һ�������

 History
	3.0		support three monitor
			support to call cmd / taskmgr / pythonwin
	3.1		change the key mapping on window change
			merge maximum / restore function
			use function to get the current primary monitor's size

#ce ================================================================================================

#include <file.au3>

Local $TopWidth       = 1920
Local $TopHeight      = 1080
Local $TopRightWidth  = 1920 
Local $TopRightHeight = 1080

HotKeySet("!z", "MinimizeWindow")
HotKeySet("!+z", "MaxRestoreWindow")

HotKeySet("#a", "eTopMostWindow") ;enable activated window's Topmost mode
HotKeySet("#s", "dTopMostWindow") ;disable activated window's Topmost mode

HotKeySet("!1", "ResizeWindowHalfLeft")
HotKeySet("!2", "ResizeWindowHalfRight")
HotKeySet("!3", "HMaximizeWindow")
HotKeySet("!4", "ResizeWindow2Quarter")
HotKeySet("!5", "ResetWndPosition")

HotKeySet("#q", "CloseWindow")
HotKeySet("#!q", "ForceCloseWindow")

HotKeySet("!{F1}", "CmdConsole")
HotKeySet("!{F2}", "TaskMgr")
HotKeySet("!{F3}", "PythonWin")
HotKeySet("!+a", "DisplayCOMPort")



While 1
	Sleep(2000)
WEnd

Func LaptopWidth()
	Return @DesktopWidth
EndFunc

Func LaptopHeight()
	Return @DesktopHeight
EndFunc

Func MinimizeWindow()
	WinSetState("[ACTIVE]", "", @SW_MINIMIZE)
EndFunc

Func MaxRestoreWindow()
	Local $ret = WinGetState("[ACTIVE]")
	If $ret = 0 Then
		Return
	ElseIf BitAND($ret, 32) Then
		WinSetState("[ACTIVE]", "", @SW_RESTORE)
	Else
		WinSetState("[ACTIVE]", "", @SW_MAXIMIZE)
	EndIf
EndFunc

Func eTopMostWindow()
	WinSetOnTop("[ACTIVE]", "", 1)
EndFunc

Func dTopMostWindow()
	WinSetOnTop("[ACTIVE]", "", 0)
EndFunc

Func ResizeWindowHalfLeft()
	Local $ret = ScreenSizeDetect()
	Local $X = 0
	Local $Y = 0
	Local $W = 0
	Local $H = 0
	If $ret[2] == 0 Then
		$X = 0
		$Y = 0
	ElseIf $ret[2] == 1 Then
		$X = 0
		$Y = $TopHeight*-1
	ElseIf $ret[2] == 2 Then
		$X = $TopWidth+1
		$Y = $TopHeight*-1
	EndIf
	$W = $ret[0]/2
	$H = $ret[1]
	WinMove("[ACTIVE]", "", $X, $Y, $W, $H, 2)
EndFunc

Func ResizeWindowHalfRight()
	Local $ret = ScreenSizeDetect()
	Local $X = 0
	Local $Y = 0
	Local $W = 0
	Local $H = 0
	If $ret[2] == 0 Then
		$X = $ret[0]/2
		$Y = 0
	ElseIf $ret[2] == 1 Then
		$X = $TopWidth/2
		$Y = $TopHeight*-1
	ElseIf $ret[2] == 2 Then
		$X = $TopWidth+$TopRightWidth/2
		$Y = $TopHeight*-1
	EndIf
	$W = $ret[0]/2
	$H = $ret[1]
	WinMove("[ACTIVE]", "", $X, $Y, $W, $H, 2)
EndFunc

Func HMaximizeWindow()
	Local $ret = ScreenSizeDetect()
	Local $pos = WinGetPos("[ACTIVE]")
	If $ret[2] == 0 Then
		WinMove("[ACTIVE]", "", $pos[0], 0, $pos[2], $ret[1], 2)
	ElseIf $ret[2] == 1 Then
		WinMove("[ACTIVE]", "", $pos[0], $TopHeight*-1, $pos[2], $ret[1], 2)
	ElseIf $ret[2] == 2 Then
		WinMove("[ACTIVE]", "", $pos[0], $TopHeight*-1, $pos[2], $ret[1], 2)	
	EndIf
EndFunc

Func ResizeWindow2Quarter()
	Local $ret = ScreenSizeDetect()
	Local $X = 0
	Local $Y = 0
	Local $W = $ret[0]/2
	Local $H = $ret[1]/2
	If $ret[2] == 0 Then
		If $ret[3] < $ret[0]/2 And $ret[4] < $ret[1]/2 Then
			$X = 0
			$Y = 0
		ElseIf $ret[3] >= $ret[0]/2 And $ret[4] < $ret[1]/2 Then
			$X = $W
			$Y = 0
		ElseIf $ret[3] < $ret[0]/2 And $ret[4] >= $ret[1]/2 Then
			$X = 0
			$Y = $H
		ElseIf $ret[3] >= $ret[0]/2 And $ret[4] >= $ret[1]/2 Then
			$X = $W
			$Y = $H
		EndIf
	ElseIf $ret[2] == 1 Then
		If $ret[3] < $ret[0]/2 And Abs($ret[4]) < $ret[1]/2 Then
			$X = 0
			$Y = $H*-1
		ElseIf $ret[3] >= $ret[0]/2 And Abs($ret[4]) < $ret[1]/2 Then
			$X = $W
			$Y = $H*-1
		ElseIf $ret[3] < $ret[0]/2 And Abs($ret[4]) >= $ret[1]/2 Then
			$X = 0
			$Y = $H*-1*2
		ElseIf $ret[3] >= $ret[0]/2 And Abs($ret[4]) >= $ret[1]/2 Then
			$X = $W
			$Y = $H*-1*2
		EndIf
	ElseIf $ret[2] == 2 Then
		If $ret[3] < ($TopWidth+$ret[0]/2) And Abs($ret[4]) < $ret[1]/2 Then
			$X = $TopWidth+1
			$Y = $H*-1
		ElseIf $ret[3] >= ($TopWidth+$ret[0]/2) And Abs($ret[4]) < $ret[1]/2 Then
			$X = $TopWidth+1+$W
			$Y = $H*-1
		ElseIf $ret[3] < ($TopWidth+$ret[0]/2) And Abs($ret[4]) >= $ret[1]/2 Then
			$X = $TopWidth+1
			$Y = $H*-1*2
		ElseIf $ret[3] >= ($TopWidth+$ret[0]/2) And Abs($ret[4]) >= $ret[1]/2 Then
			$X = $TopWidth+1+$W
			$Y = $H*-1*2
		EndIf
	EndIf
	WinMove("[ACTIVE]", "", $X, $Y, $W, $H, 2)
EndFunc

Func ResetWndPosition()
	WinMove("[ACTIVE]", "", 0, 0, LaptopWidth()/2, LaptopHeight(), 2)
EndFunc

Func ScreenSizeDetect()
	Local $ret = WinGetPos("[ACTIVE]")
	Local $SIZE[5]
	
	If $ret[1]>=0 Then ; y>=0
		If $ret[0]<=LaptopWidth() Then
			$SIZE[0] = LaptopWidth()
			$SIZE[1] = LaptopHeight()
			$SIZE[2] = 0
		Else
			MsgBox(0, "", "You find the God!")
		EndIf
	Else ; $ret[1]<0
		If $ret[0]<=$TopWidth Then
			$SIZE[0] = $TopWidth
			$SIZE[1] = $TopHeight
			$SIZE[2] = 1
		ElseIf $ret[0]>$TopWidth And $ret[0]<=($TopWidth+$TopRightWidth) Then
			$SIZE[0] = $TopRightWidth
			$SIZE[1] = $TopRightHeight
			$SIZE[2] = 2
		EndIf
	EndIf
	$SIZE[3] = $ret[0] ;X
	$SIZE[4] = $ret[1] ;Y
	Return $SIZE
EndFunc

Func CloseWindow()
	Send("!{F4}")
EndFunc

Func ForceCloseWindow()
	Local $ret = WinGetProcess("[ACTIVE]")
	ProcessClose($ret)
EndFunc

Func TaskMgr()
	Run("taskmgr")
EndFunc

Func CmdConsole()
	Run("cmd")
EndFunc

Func PythonWin()
	Run("C:\Python27\Lib\site-packages\pythonwin\pythonwin.exe")
EndFunc

Func DisplayCOMPort()
	Local $ROOT = "HKEY_LOCAL_MACHINE\HARDWARE\DEVICEMAP\SERIALCOMM"
	Local $ret = ""
	For $i = 1 To 10
		Local $key = RegEnumVal($ROOT, $i)
		Local $tmp = RegRead($ROOT, $key) & @TAB & $key
		If @error Then ExitLoop
		$ret = $ret & $tmp & @CRLF
	Next
	MsgBox(64, "COM Port", $ret)
EndFunc