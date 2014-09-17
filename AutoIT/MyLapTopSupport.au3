#cs ================================================================================================

 脚本作者: James Jun Yang, 19011956
 电子邮件: jun.yang@carestream.com
 脚本版本: 1.0
 脚本功能: Supoort functions on Laptop

#ce ================================================================================================

Local $SmallWidth  = @DesktopWidth
Local $SmallHeight = @DesktopHeight
Local $BigWidth    = 1920
Local $BigHeight   = 1080

HotKeySet("#z", "MinimizeWindow")
HotKeySet("#x", "MaximizeWindow")
HotKeySet("#c", "RestoreWindow")

HotKeySet("#a", "eTopMostWindow")
HotKeySet("#s", "dTopMostWindow")

HotKeySet("!1", "ResizeWindowHalfLeft")
HotKeySet("!{F1}", "ResizeWindowHalfLeftForceSmall")
HotKeySet("!{F2}", "ResizeWindowHalfLeftForceBig")
HotKeySet("!2", "ResizeWindowHalfRight")
HotKeySet("!3", "HMaximizeWindow")
HotKeySet("!4", "PushWindow2FourCorner")

HotKeySet("#q", "CloseWindow")
HotKeySet("#!q", "CloseWindow")

HotKeySet("!{F3}", "TaskMgr")

While 1
	Sleep(2000)
WEnd

Func MinimizeWindow()
	WinSetState("[ACTIVE]", "", @SW_MINIMIZE)
EndFunc

Func RestoreWindow()
	WinSetState("[ACTIVE]", "", @SW_RESTORE)
EndFunc

Func MaximizeWindow()
	WinSetState("[ACTIVE]", "", @SW_MAXIMIZE)
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
		$X = $SmallWidth+1
		$Y = 0
	EndIf
	$W = $ret[0]/2
	$H = $ret[1]
	WinMove("[ACTIVE]", "", $X, $Y, $W, $H, 2)
EndFunc

Func ResizeWindowHalfLeftForceSmall()
	Local $X = 0
	Local $Y = 0
	Local $W = $SmallWidth/2
	Local $H = $SmallHeight
	WinMove("[ACTIVE]", "", $X, $Y, $W, $H, 2)
EndFunc

Func ResizeWindowHalfLeftForceBig()
	Local $X = $SmallWidth+1
	Local $Y = 0
	Local $W = $BigWidth/2
	Local $H = $BigHeight
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
		$X = $SmallWidth+1+$ret[0]/2
		$Y = 0
	EndIf
	$W = $ret[0]/2
	$H = $ret[1]
	WinMove("[ACTIVE]", "", $X, $Y, $W, $H, 2)
EndFunc

Func HMaximizeWindow()
	Local $ret = ScreenSizeDetect()
	Local $pos = WinGetPos("[ACTIVE]")
	WinMove("[ACTIVE]", "", $pos[0], 0, $pos[2], $ret[1], 2)
EndFunc

Func PushWindow2FourCorner()
	Local $ret = ScreenSizeDetect()
	Local $X = 0
	Local $Y = 0
	Local $W = $ret[0]/2
	Local $H = $ret[1]/2
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
	If $ret[2] == 1 Then
		$X = $X+$SmallWidth
	EndIf
	WinMove("[ACTIVE]", "", $X, $Y, $W, $H, 2)
EndFunc

Func ScreenSizeDetect()
	Local $ret = WinGetPos("[ACTIVE]")
	Local $SIZE[5]
	If $ret[0] < $SmallWidth Then
		$SIZE[0] = $SmallWidth
		$SIZE[1] = $SmallHeight
		$SIZE[2] = 0
		$SIZE[3] = $ret[0]
		$SIZE[4] = $ret[1]
	ElseIf $ret[0] >= $SmallWidth Then
		$SIZE[0] = $BigWidth
		$SIZE[1] = $BigHeight
		$SIZE[2] = 1
		$SIZE[3] = $ret[0] - $SmallWidth
		$SIZE[4] = $ret[1]
	EndIf
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
