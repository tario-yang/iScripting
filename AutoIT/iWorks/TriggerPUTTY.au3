Local $ret   = ProcessExists('PUTTY.EXE')
Local $PUTTY = "E:\ProgramFiles\PUTTY\PUTTY.EXE"
Local $PWD   = "aluirp;as#iwer2354123"
If $ret == 0 Then
	If FileExists($PUTTY) Then
		Run($PUTTY)
		Sleep(100)
		WinActivate("[CLASS:PuTTYConfigBox]")
	EndIf
EndIf
ClipPut($PWD)