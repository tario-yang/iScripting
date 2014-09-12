#cs # History # =======================================================================

	
	Build Number            Date            Modified        Comments
	0.1                     2014-09-01      James Yang      Initial
	
#ce ===================================================================================

#cs #FUNCTION List -> Support# ========================================================

	FUNCTION($PARAMETER)
	
#ce ===================================================================================

#include-once

AutoItSetOption("MustDeclareVars", 1)

; #FUNCTION# ==========================================================================
; Description ...: Description
; Parameters ....: None
; Return values .: 1          - Pass
;                  0          - Fail
; =====================================================================================
Func LaunchSDKTool()
	Local $SDKTool = "..\Tkinter\SDKAPITest.py"
	Run("taskkill /f /im python.exe")
	Sleep(2000)
	Run("python.exe " & $SDKTool)
	If WinWaitActive("Operation History", "", 5) == 0 Then
		
	EndIf
EndFunc   ;==>LaunchSDKTool
