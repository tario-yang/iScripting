#include <File.au3>

#comments-start
	[James Jun Yang] This script is to display the number of valid and maximum meshes.

	History:
	1.0		Initial Version
	1.1		Calculat all views' number under each mode
	1.2		Fix Bug (handle file deletion after monitoring starts)
			Expand monitoring from script starts
	1.3		Check OS type to match the changes in Preference.XML
			- WIN_32_MAX_VIEW_NUM
			- WIN_64_MAX_VIEW_NUM
#comments-end

AutoItSetOption("MustDeclareVars", 1)

Local $__PATH_PREFERENCE_XML		= @AppDataCommonDir & "\TW\AcqAltair\"
Local $__FILE_PREFERENCE_XML		= "preference.XML"
Local $__FULL_PREFERENCE_XML		= $__PATH_PREFERENCE_XML & $__FILE_PREFERENCE_XML
Local $__KEY_WORD_PREFERENCE		= "MAX_VIEW_NUM"
Local $__PATH_MULTIVIEWMODEL		= $__PATH_PREFERENCE_XML & "\Models\"
Local $__FILE_MULTIVIEWMODEL		= "MultiViewModel.TXT"
Local $__FULL_MULTIVIEWMODEL		= $__PATH_MULTIVIEWMODEL & $__FILE_MULTIVIEWMODEL
Local $__KEY_WORD_MULTIVIEWMODEL	= "VIEW_CONTENT"
Local $__MONITOR_INTERVAL			= 1500  ; This will be used in Loop as interval for each cycle.
											; Also, it is used in Tip() to control the display time of the tooltip function.
											; Its unit is "ms".
Local $__MONITOR_TIMES				= 100
Local $__MONITOR_TIMEOUT			= Int($__MONITOR_INTERVAL*2*$__MONITOR_TIMES/1000/60)
Local $__CURRENT_VALID_MESH
Local $__MAXIMUM_MESH				= "N/A" ; If the number cannot be got, "N/A" will be used.
Local $__FINAL_RESULT ;	Display string for tooltip function

HotKeySet("{ESC}","ESC")
DISPLAYNUMBER()

; Functions
Func DISPLAYNUMBER()
	Local $i ; Used in Loop
	Local $j ; Used to save string
	Local $k ; Used to save the array of splitted string
	Local $prefix ; Used to add a prefix for $__KEY_WORD_PREFERENCE.
	              ; This is because, from 1.0.4.1, ACQ starts to use different maximum number on 32bit and 64bit OS.
		      ; 1.0.4.1 : 100 for 32bit and 300 for 64bit.
	Local $file_line_number ; Used to record the number of lines
	Local $file_modify_time = "" ; Used to record the modification time of the file
	Local $counter_lower_jaw ; Counter for meshes in Lower Jaw
	Local $counter_upper_jaw ; Counter for meshes in Upper Jaw
	Local $counter_bite_registration ; Counter for meshes in Buccal Bite Registration
	Local $counter_file_missing ; Counter for MultiViewModel.TXT's missing

	; Check Maximum Number of meshes from Preference.XML
	If Not FileExists($__FULL_PREFERENCE_XML) Then
		ToolTip($__FILE_PREFERENCE_XML & " does not exist!",0,0,"STOP",3)
		Sleep($__MONITOR_INTERVAL)
		ESC()
	Else
		$file_line_number = _FileCountLines($__FULL_PREFERENCE_XML)
		Switch @OSArch
			Case "X86"
				$prefix = "WIN_32_"
			Case "X64"
				$prefix = "WIN_64_"
			Case "IA64"
				ToolTip("Current OS Type is not supported!",0,0,"STOP",3)
				Sleep($__MONITOR_INTERVAL)
				ESC()
		EndSwitch
		$__KEY_WORD_PREFERENCE = $prefix & $__KEY_WORD_PREFERENCE
		For $i = 1 To $file_line_number Step 1
			$j = FileReadLine($__FULL_PREFERENCE_XML,$i)
			If StringInStr($j,$__KEY_WORD_PREFERENCE,1) Then
				$k = StringSplit($j,'"')
				$__MAXIMUM_MESH = $k[4] ; The number is the 4th element.
				ExitLoop
			EndIf
		Next

		; Zeroing the Vars used. I dont wanna the previous value affect next `check`
		$file_line_number = 0
		$i = 0
		$j = ""
	EndIf

	; Check current valid meshes' number from MultiViewModel.TXT
	$counter_file_missing = 0 ; Initial number of the counter
	While 1 ; Main Part: Keep monitoring
		; Initiate and display zero when file does not exist.
			$counter_lower_jaw = 0
			$counter_upper_jaw = 0
			$counter_bite_registration = 0
		If FileExists($__FULL_MULTIVIEWMODEL) Then
			$counter_file_missing = 0 ; Clear counter as file exists.
			If $file_modify_time = FileGetTime($__FULL_MULTIVIEWMODEL,0,1) Then ; If the time is same, that means there is nothing happened.
				ContinueLoop
			Else
				$file_modify_time	= FileGetTime($__FULL_MULTIVIEWMODEL,0,1)
				$file_line_number	= _FileCountLines($__FULL_MULTIVIEWMODEL)
				For $i = 1 To $file_line_number Step 1
					$j = FileReadLine($__FULL_MULTIVIEWMODEL,$i)
					If StringRegExp($j,"^" & $__KEY_WORD_MULTIVIEWMODEL) Then ; based on current file content, calculate the rest lines' number
						; Old method
							#comments-start
								If StringRegExp(FileReadLine($__FULL_MULTIVIEWMODEL,$file_line_number),"^$",0) Then
									$__CURRENT_VALID_MESH = $file_line_number - $i - 1 ; -1 is because there is a ^$ at end of the file currently.
								Else
									$__CURRENT_VALID_MESH = $file_line_number - $i
								EndIf
							#comments-end

						; New method to calculat all views' number under each mode
							For $i = $i+1 To $file_line_number Step 1
								$j = FileReadLine($__FULL_MULTIVIEWMODEL,$i)
								If (Not StringRegExp($j,"^$")) And StringRegExp($j,"^\d+\h\d{1}") Then
									ReDim $k = StringSplit($j," ") ; $k is used before, need to "ReDim" it.
									Switch $k[2]
										Case "1" ; Lower Jaw
											$counter_lower_jaw += 1
										Case "0" ; Upper Jaw
											$counter_upper_jaw += 1
										Case "2" ; Buccal Bite Registration
											$counter_bite_registration += 1
									EndSwitch
								Else
									ContinueLoop
								EndIf
							Next
							ExitLoop ; Goto: Display part
					EndIf
				Next
			EndIf
		Else
			$counter_file_missing += 1
			If $counter_file_missing > $__MONITOR_TIMES Then
				ToolTip($__FULL_MULTIVIEWMODEL & " has been lost for " & $__MONITOR_TIMEOUT & " minute(s)!",0,0,"STOP",3)
				Sleep($__MONITOR_INTERVAL)
				ESC()
			EndIf
		 EndIf

		; Display Part
		$__CURRENT_VALID_MESH = _
		   "Lower Jaw:" & @TAB & @TAB & $counter_lower_jaw & @CRLF & _
		   "Upper Jaw:" & @TAB & @TAB & $counter_upper_jaw & @CRLF & _
		   "Buccal Bite Registration:" & @TAB & $counter_bite_registration
		$__FINAL_RESULT = ($counter_lower_jaw + $counter_upper_jaw + $counter_bite_registration) & "/" & $__MAXIMUM_MESH
		TIP()
		Sleep($__MONITOR_INTERVAL) ; Use two sleep due to logic. One is for display, the other is for loop.
	WEnd
EndFunc ;==> DISPLAYNUMBER()

Func TIP()
	ToolTip($__CURRENT_VALID_MESH,0,0,"Status - " & $__FINAL_RESULT,1,4)
	Sleep($__MONITOR_INTERVAL)
EndFunc ;==> TIP()

Func ESC()
   Exit
EndFunc ;==>ESC()