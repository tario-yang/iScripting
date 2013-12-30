@echo off
title USB Camera Status
%~dp0%1\devcon.exe Status "USB\VID_041E&PID_4059" > %~dp0USBCameraStatus.log