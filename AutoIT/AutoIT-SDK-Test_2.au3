#include <ButtonConstants.au3>
#include <GUIConstantsEx.au3>
#include <WindowsConstants.au3>
#Region ### START Koda GUI section ### Form=
$Form1    = GUICreate("Control Panel", 647, 130, 0, 0, $WS_SYSMENU)
$Group1   = GUICtrlCreateGroup("", 0, 0, 640, 97)
$Button1  = GUICtrlCreateButton("Init", 8, 16, 89, 33)
$Button2  = GUICtrlCreateButton("Uninit", 8, 56, 89, 33)
$Button3  = GUICtrlCreateButton("Start Play", 112, 16, 89, 33)
$Button4  = GUICtrlCreateButton("Stop Play", 112, 56, 89, 33)
$Button5  = GUICtrlCreateButton("Pause Play", 208, 16, 89, 33)
$Button6  = GUICtrlCreateButton("Capture", 304, 16, 89, 33)
$Button7  = GUICtrlCreateButton("Start Record", 400, 16, 89, 33)
$Button8  = GUICtrlCreateButton("Stop Record", 400, 56, 89, 33)
$Button9  = GUICtrlCreateButton("+", 509, 16, 17, 73)
$Button10 = GUICtrlCreateButton("Set Log Path", 544, 16, 89, 33)
GUISetState(@SW_SHOW)
$Form2 = GUICreate("Live Video", 640, 480)
GUISetState(@SW_SHOW)
#EndRegion ### END Koda GUI section ###

Local $objDevice = ObjCreate("ACQSDK.CSDevice.1")
$hWnd = $Form2

While 1
	$nMsg = GUIGetMsg()
	Switch $nMsg
		Case $GUI_EVENT_CLOSE
			Exit

		Case $Button1
			Local $ret_init = $objDevice.ACQSDK_Init($hWnd)
			ConsoleWrite("$ret_init: " & $ret_init & @CRLF)
		Case $Button2
			Local $ret_Uninit = $objDevice.ACQSDK_Uninit()
			ConsoleWrite("$ret_Uninit: " & $ret_Uninit & @CRLF)
		Case $Button3
			Local $ret_StartPlay = $objDevice.ACQSDK_StartPlay()
			ConsoleWrite("$ret_StartPlay: " & $ret_StartPlay & @CRLF)
		Case $Button4
			Local $ret_StopPlay = $objDevice.ACQSDK_StopPlay()
			ConsoleWrite("$ret_StopPlay: " & $ret_StopPlay & @CRLF)
		Case $Button5
			Local $ret_PausePlay = $objDevice.ACQSDK_PausePlay()
			ConsoleWrite("$ret_PausePlay: " & $ret_PausePlay & @CRLF)
		Case $Button6
		Case $Button7
			Local $path = @DesktopDir
			Local $ret_StartRecord = $objDevice.StartRecord($path)
			ConsoleWrite("$ret_StartRecord: " & $ret_StartRecord & @CRLF)
		Case $Button8
			Local $ret_StopRecord = $objDevice.StopRecord()
			ConsoleWrite("$ret_StopRecord: " & $ret_StopRecord & @CRLF)
		Case $Button9
			Exit
		Case $Button10
			Local $log = "xxx.acq"
			Local $ret_SetLogPathEx = $objDevice.ACQSDK_SetLogPathEx($log)
			ConsoleWrite("Return_SetLogPath: " & $ret_SetLogPathEx & @CRLF)
	EndSwitch
WEnd
