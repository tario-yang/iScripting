# coding: utf-8

import os
import hashlib
import shutil


class FileSync:

	'''

	Target : use this class as a simple "rsync"

	'''

	def __init__(self, source, destination):
		self.source = source
		self.destination = destination

		retSource = self.WhatIsTarget(self.source)
		if retSource in [1]:
			self.ToSyncFile()
		elif retSource in [2]:
			self.ToSyncDirectory()
		else:
			print '\t*Fail to use source inputted*'
			return None

	def WhatIsTarget(self, input):
		'''
		Return Value shall be,
		1: File
		2: Directory
		4: Non-Existed
		8: Unknown
		'''
		# Input shall be FILE
		if os.path.isfile(input):
			return 1
		# Input shall be DIRECTORY
		elif os.path.isdir(input):
			return 2
		# Input is not available
		elif os.path.exists(input) is False:
			return 4
		# Input is an ET
		else:
			return 8

	def ToSyncDirectory(self):
		pass

	def ToSyncFile(self):
		ret = self.WhatIsTarget(self.destination)
		if ret == 1: # is a file
			destFile = self.destination
			if FileCopy(self.source, destFile):
				print 'Updated, "{}"'.format(destFile)
				return True
		elif ret == 2: # is a directlry
			destFile = r'{0}\{1}'.format(self.destination, os.path.basename(self.source))
			if FileCopy(self.source, destFile):
				print 'Updated, "{}"'.format(destFile)
				return True
		elif ret == 4: # others, recognized as a non-existed directory
			try:
				os.makedirs(self.destination)
			except Exception as e:
				print '\t*Failed to create directory, "{0}"*\n\t\t{1}\n\t*Skipped, "{0}"*'.format(self.destination, str(e))
				return False
			destFile = r'{0}\{1}'.format(self.destination, os.path.basename(self.source))
			if FileCopy(self.source, destFile):
				print 'Copied, "{}"'.format(destFile)
				return True
		else: # ET!~
			return None
		return False # All failure of FileCopy

	def FileCopy(self, srcFile, destFile):
		'''
		True: operated
		False: failed to operate
		'''
		if IsFileSame(srcF, destFile):
			print 'Skipped, "{}"'.format(srcFile)
			return True
		else:
			try:
				shutil.copy(srcFile, destFile)
			except Exception as e:
				print '\n\t*Error occurs while copying file, "{0}" to "{1}"*\n\t\t"{2}"'.format(srcFile, destFile, str(e))
				return False
			else:
				return True

	def IsFileSame(self, srcFile, destFile):
		if self.WhatIsTarget(srcFile) + self.WhatIsTarget(destFile) == 2:
			return True if ReturnMD5String(srcFile) == ReturnMD5String(destFile) else False
		else:
			return False

	def ReturnMD5String(self, srcFile):
		HashID = hashlib.md5()
		objFile = file(srcFile, 'rb')
		while True:
			block = objFile.read(8096)
			if not block:
				break
			else:
				HashID.update(block)
		objFile.close()
		return HashID.hexdigest().upper()


FileSync('D:\\ABC', 'D:\\ABC\\ABC')