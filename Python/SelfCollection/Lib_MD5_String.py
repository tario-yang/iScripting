import hashlib

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