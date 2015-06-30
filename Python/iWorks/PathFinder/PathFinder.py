'''
    This script is to export the expected files' path to a file.

    <Script> ROOT_PATH EXPORT_FILE FILE_EXTS
'''

import os
import sys

ROOT_PATH   = sys.argv[1]
try:
    EXPORT_FILE = sys.argv[2]
except:
    EXPORT_FILE = "file_path_export.list"
try:
    FILE_EXTS   = sys.argv[3:]
except:
    FILE_EXTS = ['.cpp', '.c', '.cc']

if ROOT_PATH == "":
    sys.exit(1)

# initiate export file
if os.path.exists(EXPORT_FILE):
    os.remove(EXPORT_FILE)
open(EXPORT_FILE, 'w').close()
file_handler = open(EXPORT_FILE, 'a+')

def PathFinder(ROOT, EXPORT_FILE_HANDLER, FILE_EXTS=FILE_EXTS):
    contentList = os.listdir(ROOT)
    for i in contentList:
        file_path = '{}\{}'.format(ROOT, i)
        file_ext  = '.{}'.format(i.split('.')[-1])
        print file_path, file_ext
        print
        if os.path.isdir(file_path):
            PathFinder(file_path, EXPORT_FILE_HANDLER, FILE_EXTS)
        elif os.path.isfile(file_path) and file_ext in FILE_EXTS:
            EXPORT_FILE_HANDLER.write('{}\n'.format(file_path))

PathFinder(ROOT_PATH, file_handler)

# close file handler
file_handler.close()
