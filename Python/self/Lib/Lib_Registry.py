import sys

try:
    import _winreg as wreg    # Python 2
except:
    try:
        import winreg as wreg    # Python 3
    except Exception as e:
        print str(e)

class COMPort:

    def __init__(self):
        self.readkey = wreg.OpenKey(wreg.HKEY_LOCAL_MACHINE, 'HARDWARE\\DEVICEMAP\\SERIALCOMM\\')

    def get(self):
        i = 0
        COMList = []
        try:
            while 1:
                COMList.append(wreg.EnumValue(self.readkey, i)[1])
                i += 1
        except:
            pass
        finally:
            return COMList

class Version:
    pass