@echo off
title USB Camera Disable
%~dp0%1\devcon.exe DISABLE "USB\VID_041E&PID_4059"