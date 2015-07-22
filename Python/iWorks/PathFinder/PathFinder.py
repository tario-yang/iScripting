'''
    This script is to export the expected files' path to a file.

    <Script> ROOT_PATH EXPORT_FILE FILE_EXTS
'''

import os
import sys

try:
    ROOT_PATH = sys.argv[1]
except:
    sys.exit(110)

try:
    EXPORT_FILE = sys.argv[2]
except:
    EXPORT_FILE = "full_file_path_export.list"

if len(sys.argv[3:]) == 0:
    FILE_EXTS = ['.cxx', '.cpp', '.c', '.cc', '.h']

print 'File extention set to search is, ', str(FILE_EXTS)

# initiate export file
if os.path.exists(EXPORT_FILE):
    os.remove(EXPORT_FILE)
open(EXPORT_FILE, 'w').close()
file_handler = open(EXPORT_FILE, 'a+')

def PathFinder(ROOT, EXPORT_FILE_HANDLER, FILE_EXTS=FILE_EXTS):
    contentList = os.listdir(ROOT)
    for i in contentList:
        full_path = r'{0}{1}{2}'.format(ROOT, os.sep, i)
        file_ext  = '.{}'.format(full_path.split('.')[-1])
        if os.path.isdir(full_path):
            PathFinder(full_path, EXPORT_FILE_HANDLER, FILE_EXTS)
        elif file_ext in FILE_EXTS:
            EXPORT_FILE_HANDLER.write(u'{}\n'.format(full_path))

PathFinder(ROOT_PATH, file_handler)

# close file handler
file_handler.close()
