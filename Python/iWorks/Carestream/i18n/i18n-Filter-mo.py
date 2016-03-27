import os
import sys
import polib

def Location():
    Path = os.environ.get('CommonProgramFiles(x86)')
    if Path is None:
        Path = os.environ.get('CommonProgramFiles')
    return r'{}\Trophy\Acquisition\DriverTaurus\local_uvc_3.1.8.2'.format(Path)

def ReturnMoObject(mofile):
    return polib.mofile(mofile)

def FuzzyItems(MoObject):
    return MoObject.fuzzy_entries()

def ObsoleteItems(MoObject):
    return MoObject.obsolete_entries()

def AllItems(MoObject): return MoObject

def AvailableItems(MoObject):
    return list(set(AllItems(MoObject))|set(ObsoleteItems(MoObject)))

def StandardMOList(moLocation, moFileName, Language = 'en_US'):
    objectMO_EN = ReturnMoObject('{}\{}\{}'.format(moLocation, Language, moFileName))
    objectMO_EN = AvailableItems(objectMO_EN)
    RetList = []
    for i in objectMO_EN:
        RetList.append(i.msgid)
    return RetList


if __name__ == '__main__':

    moLocation = Location()
    moFileName = 'ACQ.mo'
    languageList = os.listdir(moLocation)
    if len(languageList) == 0:
        print 'Empty language list.'
        sys.exit(1)

    """
    Test Case #1 : Check the metadata['Language'] for each po file.
        Expected result is, directory name is same as the property value.
    """
    print '\n'+'='*15+' Check metadata[\'Language\'] '+'='*15
    for i in languageList:
        print 'Check -> {}'.format(i),
        objectMO = ReturnMoObject('{}\{}\{}'.format(moLocation, i, moFileName))
        metadata = objectMO.metadata
        try:
            assert i.upper() == metadata['Language'].upper()
        except:
            print '-> Fail -> ',
            print 'Actual: {}, Expected: {}'.format(i, unicode(metadata['Language']))
        else:
            print '-> Pass'
    print '\n\n'


    """
    Test Case #2 : Check msgid and msgstr
        For English, msgid shall be same as msgstr;
            for the others, most msgid shall NOT be same as msgstr.
        For number, msgid shall be same as msgstr.
    """
    print '\n'+'='*15+' Check msgid and msgstr '+'='*15
    for i in languageList:
        print 'Check -> {}'.format(i)
        objectMO = ReturnMoObject('{}\{}\{}'.format(moLocation, i, moFileName))
        fuzzyPO  = FuzzyItems(objectMO)
        objectMO = AvailableItems(objectMO)
        if i == 'en_US' or i == 'en_GB':
            print '\tmsgid : msgstr (Shall be Same)'
            for j in objectMO:
                try:
                    assert j.msgid == j.msgstr
                except:
                    print '\tFail -> ',
                    print '{}::{}'.format(j.msgid, unicode(j.msgstr))
                    break
            print 'Done\n'
        else:
            print '\tmsgid : msgstr (Shall NOT be Same)'
            for j in objectMO:
                try:
                    assert j.msgid != j.msgstr
                except:
                    if j in fuzzyPO:
                        print '\t[Fuzzy] {}::{}'.format(j.msgid, unicode(j.msgstr))
                    else:
                        print '\t{}::{}'.format(j.msgid, unicode(j.msgstr))
                    continue
            print 'Done\n'
    print '\n'


    """
    Test Case #3 : Check the number of msgid. The base line is en_US.
        Expected result is, number of each PO file shall be same as English.
    """
    print '\n'+'='*15+' Check number of msgid '+'='*15
    for i in languageList:
        print 'Check -> {}'.format(i)
        objectMO = ReturnMoObject('{}\{}\{}'.format(moLocation, i, moFileName))
        objectMO = AvailableItems(objectMO)
        if i == 'en_US' or i == 'en_GB':
            print '\tNumber of {} :: {}'.format(i, len(objectMO)),
            print ' -> Skip'
            continue
        else:
            print '\tNumber of {} :: {}'.format(i, len(objectMO)),
            tmp1 = StandardMOList(moLocation, moFileName) # Source: en_US
            tmp2 = []
            for j in objectMO:
                tmp2.append(j.msgid)
            if len(tmp1) > len(tmp2):
                print '\t', list(set(tmp1)-set(tmp2))
            elif len(tmp1) < len(tmp2):
                print '\t', list(set(tmp2)-set(tmp1))
            else:
                print ' -> Pass'
    print '\n'

