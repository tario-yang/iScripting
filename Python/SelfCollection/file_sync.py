# coding: utf-8

'''
Implement a simple rsync
'''

import os
import hashlib
import shutil


class FileSync:

	def __init__(self, source, destination):

		'''
		Rule:
			File -> File
			Directory -> Directory
		'''

		self.Source = source
		self.Destination = destination

		retSource = self.WhatIsTarget(self.Source)
		if (retSource in [1] and
			self.ToSyncFile(self.Source, self.Destination) is None
			) or (
			retSource in [2] and
			self.ToSyncDirectory(self.Source, self.Destination) is None):
			print '\t*Incorrect parameter*'
			print '\t\tJust allowed File to File or Directory to Directory.'
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

	def ToSyncDirectory(self, src, dest):
		ret = self.WhatIsTarget(dest)
		if ret in [2, 4]:
			if ret == 2:
				pass
			elif ret == 4:
		else: # illegal
			return None
		return False

	def ListDirectory(self, src):


	def ToSyncFile(self, src, dest):
		ret = self.WhatIsTarget(dest)
		if ret in [1,2,4]:
			if ret == 1: # is a file
				if self.FileCopy(src, dest) == 1:
					print 'Updated, "{}"'.format(dest)
					return True
			elif ret == 2: # is a directlry
				destFile = r'{0}\{1}'.format(dest, os.path.basename(src))
				if self.FileCopy(src, destFile) == 1:
					print 'Updated, "{}"'.format(destFile)
					return True
			elif ret == 4: # others, recognized as a non-existed directory
				try:
					os.makedirs(dest)
				except Exception as e:
					print '\t*Failed to create directory, "{0}"*\n\t\t{1}\n\t*Skipped, "{0}"*'.format(dest, str(e))
					return False
				else:
					destFile = r'{0}\{1}'.format(dest, os.path.basename(src))
					if self.FileCopy(src, destFile) == 1:
						print 'Copied, "{}"'.format(destFile)
						return True
		else: # illegal
			return None
		return False # All failure of FileCopy

	def FileCopy(self, srcFile, destFile):
		'''
		0: Skipped
		1: Copied
		2: Failed
		'''
		if self.IsFileSame(srcFile, destFile):
			print 'Skipped, "{}"'.format(srcFile)
			return 0
		else:
			try:
				shutil.copy(srcFile, destFile)
			except Exception as e:
				print '\n\t*Error occurs while copying file, "{0}" to "{1}"*\n\t\t"{2}"'.format(srcFile, destFile, str(e))
				return 2
			else:
				return 1

	def IsFileSame(self, srcFile, destFile):
		if self.WhatIsTarget(srcFile) + self.WhatIsTarget(destFile) == 2:
			return True if self.ReturnMD5String(srcFile) == self.ReturnMD5String(destFile) else False
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


FileSync('D:\\ABC.db', 'D:\\ABC\\DEF\\GHIJK')
