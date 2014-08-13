@echo off
echo 'Start to build...'
echo '+++++++++++++++++++++++++++++++++++++++'
python.exe build.py py2exe
echo\
rd /s /q build
ren dist ImageComparator
pause