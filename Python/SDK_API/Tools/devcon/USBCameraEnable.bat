@echo off
title USB Camera Enable
%~dp0%1\devcon.exe ENABLE "USB\VID_041E&PID_4059"