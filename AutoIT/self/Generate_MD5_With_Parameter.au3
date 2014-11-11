#include <Crypt.au3>

#comments-start
	This script is used to calculate the MD5 value.
#comments-end

Local $INPUT = $CmdLine[1] ;Get the input data
                           ;$CmdLine is the array to store the transferred parameter.
                           ;$CmdLine[0] is $#
                           ;$CmdLine[1] is the 1st parameter
If FileOpen($INPUT,0) Then
	GetMD5Value($INPUT)
EndIf

Func GetMD5Value(ByRef $input)
	#Local $algorithm          = $CALG_MD2
	#Local $algorithm          = $CALG_MD4
	Local $algorithm           = $CALG_MD5
	#Local $algorithm          = $CALG_SHA1
	Local $output              = _Crypt_HashFile($input,$algorithm)
	Local $output_purge_string = StringSplit($output,"x")
	MsgBox(64,"MD5 Generation", _
               "Input:" & @TAB & $INPUT & @CRLF & _
               "Output:" & @TAB & $output_purge_string[2] & @CRLF)
	ClipPut($output_purge_string[2])
EndFunc
