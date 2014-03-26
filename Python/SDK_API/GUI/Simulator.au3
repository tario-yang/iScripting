HotKeySet("#{F11}", "START")
HotKeySet("#{F12}", "END")

while 1
	Sleep(1000)
WEnd

Func START()
	while 1
		MouseClick("left", 260, 160)
		Sleep(2500)
	WEnd
EndFunc

Func END()
	Exit
EndFunc