# -*- coding: utf-8 -*-

"""

Read MO files and output whole data to an Excel file
Limitation:
1. Suppose all MO files are available to use.
2. If msgid does not exist in mo of EN-US, ignore its msgstr.
3. Obsolete items are ignored directly.

Author   : James Jun Yang (19011956), Email: jun.yang@carestream.com
History  :
    1.0     2014-09-15      Draft version
"""

import os
import sys
import time
import polib
import xlwt
import optparse

def Location(product, position):
    Path = os.environ.get('CommonProgramFiles(x86)')
    if Path is None:
        Path = os.environ.get('CommonProgramFiles')
    return r'{}\Trophy\Acquisition\{}\{}'.format(Path, product, position)

def ReturnMOObject(mofile):
    return polib.mofile(mofile)

def ObsoleteItems(MOObject):
    return MOObject.obsolete_entries()

def AllItems(MOObject): return MOObject

def AvailableItems(MOObject):
    return list(set(AllItems(MOObject))|set(ObsoleteItems(MOObject)))

def MOItemList(moLocation, mofileName, Language):
    objectMO = ReturnMOObject('{}\{}\{}'.format(moLocation, Language, mofileName))
    objectMO = AvailableItems(objectMO)
    RetList = []
    for i in objectMO:
        RetList.append([i.msgid, unicode(i.msgstr)])
    return RetList

def Output2Excel(excelFile, langList, outputList):
    if os.path.exists(excelFile) is True:
        os.remove(excelFile)
    objWorkbook  = xlwt.Workbook(encoding = 'utf-8')
    objWorksheet = objWorkbook.add_sheet(sheetname = 'General')

    # Language Title
    for i in range(len(langList)):
        objWorksheet.write(0, i, langList[i])

    # msgstr
    for i in range(len(outputList)):
        for j in range(len(outputList[i])):
            objWorksheet.write(i+1, j, outputList[i][j])

    # Save to file
    objWorkbook.save(excelFile)

if __name__ == '__main__':

    # Optparse
    usage = """
    %prog -p|--product-name PRODUCT -d|--directory-name DIRECTORY
    """
    version = '1.0'
    epilog = ''
    parser = optparse.OptionParser(usage = usage, version = version, epilog = epilog)
    parser.add_option('-p', '--product-name',
        dest = 'PRODUCT',
        default = 'DriverAltair',
        help = 'Product name. Default is "DriverAltair".')
    parser.add_option('-d', '--directory-name',
        dest = 'DIRECTORY',
        default = 'local',
        help = 'Directory name of the i18n files. Default is "local".')
    (options, args) = parser.parse_args()

    # Need product name, this name is the installation directory name of specified product
    if options.PRODUCT is None:
        parser.error('Product name is not specified.')

    # General definition of variables: mail path
    moLocation = Location(options.PRODUCT, options.DIRECTORY)
    if os.path.exists(moLocation) is False:
        parser.error('Specified path of MO files does not exist!')
    else:
        languageList = os.listdir(moLocation)
        default_language = 'EN-US'
        languageList.remove(default_language)
        languageList.insert(0, default_language)
        if len(languageList) == 0:
            parser.error('Directory, {}, is empty!'.format(options.DIRECTORY))

    # General definition of variables: others
    mofileName = 'ACQ.mo'
    outputFile = 'i18n_Output_{}.xls'.format(time.strftime(r'%Y%m%d%H%M%S'))
    outputList = []

    # Generate base msgid: default langauge
    DefaultList = MOItemList(moLocation, mofileName, Language = default_language)
    for i in DefaultList:
        outputList.append([i[0]])
    outputList.sort()

    # Generate msgstr: other language
    for l in languageList:
        if l == default_language:
            continue
        TargetOutputList = MOItemList(moLocation, mofileName, Language = l)
        TargetOutputList.sort()
        for item in TargetOutputList:
            for i in outputList:
                if item[0] == i[0]:
                    i.append(unicode(item[1]))
                    continue

    # Output data to excel file.
    Output2Excel(outputFile, languageList, outputList)
