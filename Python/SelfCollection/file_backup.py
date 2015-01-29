# coding: utf-8

import os
import hashlib
import shutil

def BackupDirectory(sDir, dDir, info, *exclude):
	sDirList = os.listdir(sDir)
	for i in sDirList:
		if os.path.isfile(i):
			BackupFile(i, r'{}\{}'.format(dDir, os.path.basename(i)), info, *exclude)
		if os.path.isdir(i):
			BackupDirectory(i, dDir, info, *exclude)

def BackupFile(sFile, sDir, info='', *exclude):

	dFile = r'{0}\{1}'.format(sDir, os.path.basename(sFile))

	if os.path.exists(sFile) == False:
		print 'File does not exist({})!'.format(sFile)
		return False

	if exclude is not None and sFile in exclude:
		print 'File is in filter list, ({})'.format(exclude)
		return False

	if os.path.exists(sDir):
		try:
			shutil.copy(sFile, dFile)
		except Exception as e:
			print '{} Failed to copy {} to {}'.format(info, sFile, dFile)
			print '\t', str(e)
		else:
			print '{} Copied {} to {}'.format(info, sFile, dFile)
	else:
		try:
			os.makedirs(targetDir)
		except Exception as e:
			print str(e)
			return False
		if IsFileSame(sFile, dFile):
			print '{} Skipped (no change), {}'.format(info, sFile)
		else:
			try:
				shutil.copy(sFile, dFile)
			except Exception as e:
				print '{} Fail to update {} to {}'.format(info, sFile, dFile)
				print '\t', str(e)
			else:
				print '{} Updated {} to {}'.format(info, sFile, dFile)


def IsFileSame(sFile, dFile):
	return True if ReturnMD5String(sFile) == ReturnMD5String(dFile) else False

def ReturnMD5String(iFile):
	HashID = hashlib.md5()
	objFile = file(iFile, 'rb')
	while True:
		block = objFile.read(8096)
		if not block:
			break
		else:
			HashID.update(block)
	objFile.close()
	return HashID.hexdigest().upper()

# source_file_list = os.environ.get('SOURCE_FILE').split('#')
# source_dir_list = os.environ.get('SOURCE_DIRECTORY').split('#')
# local_backup_path = os.environ.get('LOCAL_PATH')
# remote_backup_path = r'U:\\'


source_file_list = r'C:\Users\1901195\.bashrc#C:\Users\1901195\.gitconfig#C:\Users\1901195\.bash_history#C:\Users\1901195\Git_DentalDep.sh#C:\Users\19011956\Desktop\TMP#C:\Users\19011956\Desktop\PA#C:\Users\19011956\Desktop\CSH_PLI_DefectQuery_CS3500.xls#C:\Users\19011956\Desktop\订餐统计表.xls'.split('#')
source_dir_list = r'C:\Users\19011956\.ssh#C:\Users\19011956\Links#C:\Users\19011956\Favorites#D:\iBackup\Private Backup for HP ProBook 6470b#D:\XMIND'.split('#')
local_backup_path = ['D\\iBackup', 'G:\\iBackup']

print source_file_list
for f in source_file_list:
	BackupFile(f, local_backup_path[0], '[Local]', ['desktop.ini'])
	# BackupFile(f, local_backup_path[0], '[Remote]', ['desktop.ini'])
print '\n'

print source_dir_list
for d in source_dir_list:
	BackupDirectory(d, local_backup_path[0], '[Local]')
	# BackupDirectory(d, remote_backup_path, '[Remote]')
print '\n'