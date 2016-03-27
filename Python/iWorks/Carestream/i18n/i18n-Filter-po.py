import os
import sys
import polib

def Location():
    Path = os.environ.get('CommonProgramFiles(x86)')
    if Path is None:
        Path = os.environ.get('CommonProgramFiles')
    return r'{}\Trophy\Acquisition\DriverTaurus\local_uvc_3.1.8.2'.format(Path)

def ReturnPoObject(pofile):
    return polib.pofile(pofile)

def FuzzyItems(PoObject):
    return PoObject.fuzzy_entries()

def ObsoleteItems(PoObject):
    return PoObject.obsolete_entries()

def AllItems(PoObject): return PoObject

def AvailableItems(PoObject):
    return list(set(AllItems(PoObject))-set(ObsoleteItems(PoObject)))

def StandardMOList(poLocation, PoFileName, Language = 'en_US'):
    objectPO_EN = ReturnPoObject('{}\{}\{}'.format(poLocation, Language, PoFileName))
    objectPO_EN = AvailableItems(objectPO_EN)
    RetList = []
    for i in objectPO_EN:
        RetList.append(i.msgid)
    return RetList


if __name__ == '__main__':

    poLocation = Location()
    PoFileName = 'ACQ.mo'
    languageList = os.listdir(poLocation)
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
        objectPO = ReturnPoObject('{}\{}\{}'.format(poLocation, i, PoFileName))
        metadata = objectPO.metadata
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
        objectPO = ReturnPoObject('{}\{}\{}'.format(poLocation, i, PoFileName))
        fuzzyPO  = FuzzyItems(objectPO)
        objectPO = AvailableItems(objectPO)
        if i == 'en_US' or i == 'en_GB':
            print '\tmsgid : msgstr (Shall be Same)'
            for j in objectPO:
                try:
                    assert j.msgid == j.msgstr
                except:
                    print '\tFail -> ',
                    print '{}::{}'.format(j.msgid, unicode(j.msgstr))
                    break
            print 'Done\n'
        else:
            print '\tmsgid : msgstr (Shall NOT be Same)'
            for j in objectPO:
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
        objectPO = ReturnPoObject('{}\{}\{}'.format(poLocation, i, PoFileName))
        objectPO = AvailableItems(objectPO)
        if i == 'en_US' or i == 'en_GB':
            print '\tNumber of {} :: {}'.format(i, len(objectPO)),
            print ' -> Skip'
            continue
        else:
            print '\tNumber of {} :: {}'.format(i, len(objectPO)),
            tmp1 = StandardMOList(poLocation, PoFileName) # Source: en_US
            tmp2 = []
            for j in objectPO:
                tmp2.append(j.msgid)
            if len(tmp1) > len(tmp2):
                print '\t', list(set(tmp1)-set(tmp2))
            elif len(tmp1) < len(tmp2):
                print '\t', list(set(tmp2)-set(tmp1))
            else:
                print ' -> Pass'
    print '\n'

