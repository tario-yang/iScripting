Local $i = RunWait('.\dist\IC.exe -s AA.jpg -d BB.jpg -r 90', '.\', @SW_HIDE)
MsgBox(0, '', $i)