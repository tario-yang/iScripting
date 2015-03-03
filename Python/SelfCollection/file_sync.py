# coding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import md5
import shutil

class SyncProcessor:

	def __init__(self, source, destination, ignore=('desktop.ini', 'Thumbs.db')):
		self.Source      = source
		self.Destination = destination
		self.IgnoreList  = ignore
		retSource        = self.WhatIsTarget(self.Source)
		retDestination   = self.WhatIsTarget(self.Destination)

		self.Output('*** Source:      {} ***'.format(self.Source))
		self.Output('*** Destination: {} ***'.format(self.Destination))

		if retSource in [1] and retDestination in [1,2,4]:
			self.ToSyncFile(self.Source, self.Destination)
		elif retSource in [2] and retDestination in [2,4]:
			self.ToSyncDirectory()

	def WhatIsTarget(self, input):
		'''
		Return Value shall be,
			1: File
			2: Directory
			4: Non-Existed
			8: *ET*
		'''

		# Input shall be FILE
		if os.path.isfile(input): return 1
		# Input shall be DIRECTORY
		elif os.path.isdir(input): return 2
		# Input is not available
		elif os.path.exists(input) is False: return 4
		# Input is an ET
		else: return 8

	def ToSyncDirectory(self):
		pass

	def ListDirectory(self, destination):
		ret = os.listdir(destination)
		ret = filter(lambda i: i not in self.IgnoreList, ret)
		return ret.sort()

	def ToSyncFile(self, src, dest):
		'''
		Return Value shall be
			0: Failed
			1: Copied
			2: Skipped

		src  shall be a File;
		dest shall be a File or Dir
		'''

		if self.WhatIsTarget(src) != 1:
			self.Output('Error: ToSyncFile received a non-file parameter -> {}'.format(src), True)
			return 0

		ret = self.WhatIsTarget(dest)
		if ret in [1,2,4]:
			if ret == 4:
				target = '{}\\{}'.format(dest, src)
				if self.OperateMkdir(dest) is False:
					return 0
			elif ret == 2:
				target = '{}\\{}'.format(dest, src)
			elif ret == 1:
				target = dest

			if self.IsFileSame(src, target):
				self.Output('Skipped file -> {}'.format(src))
				return 2
			else:
				if self.OperateCopy(src, target):
					self.Output('Copied file -> {}'.format(src))
					return 1
				else:
					return 0
		else:
			self.Output('Error: ToSyncFile received an illegel destination parameter -> {}'.format(dest), True)
			return 0

	def OperateMkdir(self, dest):
		'''
		Return Value shall be
			False : Failed
			True  : Operated
		'''

		try:
			os.makedirs(dest)
		except Exception as e:
			self.Output('Error: OperateMkdir got exception while creating "{}"'.format(dest))
			self.Output('Error: Error information -> {}'.format(str(e)))
			return False
		else:
			return True

	def OperateCopy(self, src, dest):
		'''
		Return Value shall be
			False : Failed
			True  : Operated
		'''

		try:
			shutil.copy(src, dest)
		except Exception as e:
			self.Output('Error: OperateCopy got exception while copying "{0}" to "{1}"'.format(src, dest), True)
			self.Output('Error: Error information -> {}'.format(str(e)), True)
			return False
		else:
			return True

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

	def Output(self, string, isError=False):
		if isError is True:
			print '\n\t*{}*\n'.format(string)
		else:
			print '{}'.format(string)
