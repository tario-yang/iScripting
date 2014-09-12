#cs # History # =======================================================================
	
	
	Build Number            Date            Modified        Comments
	0.1                     2014-09-01      James Yang      Initial
	
#ce ===================================================================================

#cs #FUNCTION List -> Support# ========================================================

	Logger($INFO, $TYPEID = "I", $Result="", $MISC = "")
	TestStepRecorder($Tag, $Result, $Comment = "")
	TestCaseRecorder($Tag, $Result, $Comment = "")
	
#ce ===================================================================================

#include-once
#include <File.au3>

AutoItSetOption("MustDeclareVars", 1)

Global $OUTPUT      = "Output\"
Global $LOGGER_DIR  = $OUTPUT & "Logger\"
Global $LOGGER_FILE = "UVC1x00_Integration_Testing_FW_And_SDK_Logger.xml"
Global $LOGGER_FULL = $LOGGER_DIR & $LOGGER_FILE
Global $REPORT_DIR  = $OUTPUT & "Report\"
Global $REPORT_FILE = "UVC1x00_Integration_Testing_FW_And_SDK_Report.xml"
Global $REPORT_FULL = $REPORT_DIR & $REPORT_FILE

; #FUNCTION# ==========================================================================
; Description ...: Write log information to sepcified log file
; Parameters ....: $TYPE   - Type of the log info. Such as, INFO (default), ERROR, WARN and RESULT.
;                  $INFO   - Log content
;                  $Result - Result of testing
;                  $MISC   - Additional information
; Return values .: 1       - Pass
;                  0       - Fail
; =====================================================================================
Func Logger($INFO, $TYPEID = "I", $Result="", $MISC = "")

	If LoggerInit() == 0 Then
		MsgBox(262160, "ERROR", "Fail to initiate logger file!")
		Return 0
	EndIf

	; Type, default is INFO; when inputting a wrong one, set to INFO as well
	Local $TYPEName = "INFO"
	Switch $TYPEID
		Case "I"
			$TYPEName = "INFO"
		Case "E"
			$TYPEName = "ERROR"
		Case "W"
			$TYPEName = "WARN"
		Case "R"
			$TYPEName = "RESULT"
		Case Else
			$TYPEName = "INFO"
	EndSwitch

	; Log element
	Local $LOGGER_ITEM[5]
	$LOGGER_ITEM[0] = @YEAR & '-' & @MON & '-' & @MDAY & ' ' & @HOUR & ':' & @MIN & ':' & @SEC & '.' & @MSEC ; Timestamp
	$LOGGER_ITEM[1] = $TYPEName ; Log type
	$LOGGER_ITEM[2] = $INFO ; Log content
	$LOGGER_ITEM[3] = $Result ; Result of testing
	$LOGGER_ITEM[4] = $MISC ; Additonal info.

	; Wirete log element
	If LoggerInsert($LOGGER_ITEM) == 1 Then
		Return 1 ; There is no exception dealed with on XMLDOM
	EndIf

EndFunc   ;==>Logger

; #FUNCTION# ==========================================================================
; Description ...: Alias of Logger, used to record test result for test step
; Parameters ....: $Result - Test Result
;                  $Tag    - Test Step's name
; Return values .: 1       - Pass
;                  0       - Fail
; =====================================================================================
Func TestStepRecorder($Tag, $Result, $Comment = "")

	$Tag = "[Test Step] " & $Tag
	Logger($Tag, "R", $Result, $Comment)

EndFunc   ;==>TestStepRecorder

; #FUNCTION# ==========================================================================
; Description ...: Alias of Logger, used to record test result for test case
; Parameters ....: $Result - Test Result
;                  $Tag    - Test Step's name
; Return values .: 1       - Pass
;                  0       - Fail
; =====================================================================================
Func TestCaseRecorder($Tag, $Result, $Comment = "")

	$Tag = "[Test Case] " & $Tag
	Logger($Tag, "R", $Result, $Comment)

EndFunc   ;==>TestCaseRecorder

; #FUNCTION# ==========================================================================
; Description ...: Write log information to sepcified log file (XML). The input is from Logger
; Parameters ....: $LOGGER_ITEM - Array of a log item:
;                                 [0] Timestamp
;                                 [1] Log Type
;                                 [2] Log Content
;                                 [3] Result
;                                 [4] Comment
; Return values .: 1            - Pass
;                  0            - Fail, but there is no way to trace exception so far.
; =====================================================================================
Func LoggerInsert($LOGGER_ITEM)

	; XML object, using COM method
	Local $oXML = ObjCreate("Microsoft.XMLDOM")
	$oXML.async = False
	$oXML.load($LOGGER_FULL)
	
	; Append a log node
	Local $oXMLRoot = $oXML.selectSingleNode('/LoggerMan/Logger')
	Local $oXMLItem = $oXML.createElement('Log')
	$oXMLItem.setAttribute('timestamp', $LOGGER_ITEM[0])
	$oXMLItem.setAttribute('type', $LOGGER_ITEM[1])
	$oXMLItem.setAttribute('info', $LOGGER_ITEM[2])
	If $LOGGER_ITEM[3] <> "" Then
		$oXMLItem.setAttribute('result', $LOGGER_ITEM[3])
	EndIf
	If $LOGGER_ITEM[4] <> "" Then
		$oXMLItem.setAttribute('comment', $LOGGER_ITEM[4])
	EndIf
	$oXMLRoot.appendChild($oXMLItem)
	$oXML.save($LOGGER_FULL)
	
	; Cleanup
	$oXMLItem = 0
	$oXMLRoot = 0
	$oXML     = 0
	
	; Exit
	Return 1

EndFunc   ;==>LoggerInsert

; #FUNCTION# ==========================================================================
; Description ...: Initiate log directory and log file
; Parameters ....: None
; Return values .: 1 - Pass
;                  0 - Fail
; =====================================================================================
Func LoggerInit()

	; Check whether logger directory/file exists or not
	If FileExists($LOGGER_DIR) == 1 Then
		If FileExists($LOGGER_FILE) == 1 Then
			If FileGetSize($LOGGER_FILE) > 0 Then ; NOT an empty file, it shall be a correct file
				Return 1
			EndIf
		EndIf
	Else
		If DirCreate($LOGGER_DIR) == 0 Then
			Return 0
		EndIf
	EndIf

	; Call function to initiate logger file
	If LoggerCreateFile() == 1 Then
		Return 1
	ElseIf LoggerCreateFile() == 0 Then
		Return 0
	EndIf

EndFunc   ;==>LoggerInit


; #FUNCTION# ==========================================================================
; Description ...: Create the log file and then fill in default content
; Parameters ....: $FILENAME - File name of the log file
; Return values .: 1         - Pass
;                  0         - Fail
; =====================================================================================
Func LoggerCreateFile()
	
	_FileCreate($LOGGER_FULL)
	If @error == 1 Or @error == 2 Then ; Fail to open or write the target file. This @error returns by _FileCreate.
		Return 0
	EndIf
	
	; Store logger content
	Local $LOGGER_ITEM[18]
	Local $SWVersion = FetchSWVersion()
	$LOGGER_ITEM[0] = '<?xml version="1.0" encoding="UTF-8"?>' & @CRLF & '<LoggerMan>' & @CRLF & '<System>'
	$LOGGER_ITEM[1] = '<Computer name="' & @ComputerName & '" />'
	$LOGGER_ITEM[2] = '<OS name="' & @OSVersion & '" type="' & @OSArch & '" service_pack="' & @OSServicePack & '" />'
	$LOGGER_ITEM[3] = '<CPU name="' & FetchCPUInfo() & '"/>'
	$LOGGER_ITEM[4] = '<Memory total="' & FetchMemoryInfo() & 'MB" />'
	$LOGGER_ITEM[5] = '<IP address1="' & @IPAddress1 & '" />'
	$LOGGER_ITEM[6] = '<IP address2="' & @IPAddress2 & '" />'
	$LOGGER_ITEM[7] = '<IP address3="' & @IPAddress3 & '" />'
	$LOGGER_ITEM[8] = '<IP address4="' & @IPAddress4 & '" />'
	$LOGGER_ITEM[9] = '<User name="' & @UserName & '" />'
	$LOGGER_ITEM[10] = '<ACQ version="' & $SWVersion[0] & '" />'
	$LOGGER_ITEM[11] = '<SDK version="' & $SWVersion[1] & '" />'
	$LOGGER_ITEM[12] = '<Firmware name="CS 1200 UVC" version="' & $SWVersion[2] & '" />'
	$LOGGER_ITEM[13] = '<Firmware name="CS 1500 UVC" version="' & $SWVersion[3] & '" />'
	$LOGGER_ITEM[14] = '<Firmware name="CS 1600 UVC" version="' & $SWVersion[4] & '" />'
	$LOGGER_ITEM[15] = '<AutoIT version = "' & @AutoItVersion & '" />' & @CRLF & '</System>'
	$LOGGER_ITEM[16] = '<Logger />'
	$LOGGER_ITEM[17] = '</LoggerMan>'
	
	; Write file
	If _FileWriteFromArray($LOGGER_FULL, $LOGGER_ITEM) == 1 Then
		Return 1
	Else
		Return 0
	EndIf
	
EndFunc   ;==>LoggerCreateFile


; #FUNCTION# ==========================================================================
; Name ..........: FetchCPUInfo
; Description ...: Return the CPU name
; Syntax.........: FetchCPUInfo()
; Parameters ....: None
; Return values .: Name of the CPU if successful
;                  "" (empty string) if failed
; =====================================================================================
Func FetchCPUInfo()

	Return RegRead("HKEY_LOCAL_MACHINE\HARDWARE\DESCRIPTION\System\CentralProcessor\0", "ProcessorNameString")

EndFunc   ;==>FetchCPUInfo


; #FUNCTION# ==========================================================================
; Description ...: Return total size of pyhsical memory in MB
; Parameters ....: None
; Return values .: Int value of the total memory
; =====================================================================================
Func FetchMemoryInfo()

	Local $MEM = MemGetStats()
	Return Int($MEM[1]/1024) ; Unit is MB

EndFunc   ;==>FetchMemoryInfo


; #FUNCTION# ==========================================================================
; Description ...: Return an array ,which includes version of ACQ / SDK / Firmware
; Parameters ....: None
; Return values .: Array, which includes,
;                  ACQ Version
;                  SDK Version
;                  FW Version for CS 1200 UVC
;                  FW Version for CS 1500 UVC
;                  FW Version for CS 1600 UVC
;                  If fetching failed, it returns an empty string, "".
; =====================================================================================
Func FetchSWVersion()

	Local $Root ; Root of ACQ keys
	If @OSArch == "X86" Then
		$Root = "HKEY_LOCAL_MACHINE\SOFTWARE\Carestream\InstalledApplications"
	ElseIf @OSArch == "X64" Then
		$Root = "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Carestream\InstalledApplications"
	EndIf

	Local $SWVersion[5]
	$SWVersion[0] = RegRead($Root & "\Intra oral Camera", "Version")
	$SWVersion[1] = RegRead($Root & "\UVC SDK", "Version")
	$SWVersion[2] = RegRead($Root & "\CS1200UVC", "Version")
	$SWVersion[3] = RegRead($Root & "\CS1500UVC", "Version")
	$SWVersion[4] = RegRead($Root & "\CS1600UVC", "Version")

	Return $SWVersion
	
EndFunc   ;==>FetchSWVersion
