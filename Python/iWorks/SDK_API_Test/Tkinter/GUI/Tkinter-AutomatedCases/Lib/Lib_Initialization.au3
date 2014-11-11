#cs # History # =======================================================================

	
	Build Number            Date            Modified        Comments
	0.1                     2014-09-01      James Yang      Initial
	
#ce ===================================================================================

#cs #FUNCTION List -> Support# ========================================================

	FUNCTION($PARAMETER)
	
#ce ===================================================================================

#include-once
#Include <File.au3>
#Include <Lib_Logger.au3>

AutoItSetOption("MustDeclareVars", 1)

; #FUNCTION# ==========================================================================
; Name ..........: FUNCTION
; Description ...: Description
; Syntax.........: FUNCTION($PARAMETER)
; Parameters ....: $PARAMETER - Description
; Return values .: 1          - Pass
;                  0          - Fail
; =====================================================================================
Func Init_Configuration()
	Local $Path = @ScriptDir
	Local $Conf_File = $Path & "Conf\configuration.ini"
	If FileExists($Conf_File) == 0 Then
		_FileCreate($Conf_File)
	EndIf
EndFunc   ;==>FUNCTION