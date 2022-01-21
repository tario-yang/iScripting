# coding=utf-8

"""
Author:
    James Jun Yang, 19011956
    jun.yang@carestream.com

Description:
    This script is to parse DICOM file and output content to a XML file.

Usage:
    DICOM2XML -f DICOM_FILE
    DICOM2XML -f DICOM_FILE -l
    DICOM2XML --help

History:
    1.0 Draft version.
    1.1 Parse and add XML data to outputted file, it was filtered in the past.
        Add VR_Info attribute to explain the VR's meaning.
        Refine the string format of List.
        Remove '#' to make XML display in Web browser.

Known Issue:
    PLY/STL data is ignored.
    Array Data is not parsed.

"""

import os
import sys
import time
import xml.dom.minidom as DOM
import dicom
import optparse

def PackageList(dElement):
    try:
        VR_VALUE = FormatListString(str(DICOM_TAG_LIST[dElement.VR]))
    except:
        VR_VALUE = 'Incorrect VR'
    return [dElement.tag, dElement.name, dElement.VR, VR_VALUE, ReplaceRepValue(dElement)]

def FormatListString(ListString):
    ListString = ListString.replace("'", '')
    ListString = ListString.replace('[', '')
    ListString = ListString.replace(']', '')
    return ListString

def ReplaceRepValue(dElement):
    if dElement.repval[:9].upper().find('PLY') > 0:
        return u'(PLY Image Data)'
    elif dElement.repval[:9].upper().find('STL') > 0:
        return u'(STL Image Data)'
    elif dElement.repval[:9].upper().find('XML') > 0:
        return DICOMXMLParse(dElement)
    elif dElement.VR == 'OB':
        return u'(Other Byte Data)'
    else:
        return FormatListString(str(dElement.value))

def DICOMXMLParse(dElement):
    objContent = dElement.value
    objContent = objContent.replace(r'&lt;', '<')
    objContent = objContent.replace(r'&gt;', '>')
    objContent = objContent.replace(r'&quot;', '"')
    objContent = objContent.replace(r'\t', '')
    objContent = objContent.replace(r'\n', '')
    objXML = DOM.parseString(objContent)
    return objXML.getElementsByTagName(XMLCustomized)

def DICOMElementIsSequence(dElement):
    if dElement.VR == 'SQ':
        return True
    else:
        return False

def AddSequence(dDataSet):
    sequenceNode = AddElement(PackageList(dDataSet), Root, XMLSequenceName)
    counter = 0
    prefix  = 'item_'
    for ds in dDataSet:
        counter += 1
        counterNode = objDOM.createElement('{0}{1}'.format(prefix, counter))
        sequenceNode.appendChild(counterNode)
        for de in ds:
            AddElement(PackageList(de), counterNode, XMLElementName)

def AddElement(vList, parentNode, prefix):
    # Create a Element
    ElementNode = objDOM.createElement(prefix)
    ElementNode.setAttribute('Tag', str(vList[0]))
    ElementNode.setAttribute('Name', vList[1])
    ElementNode.setAttribute('VR', vList[2])
    ElementNode.setAttribute('VR_Info', vList[3])
    if prefix == XMLElementName:
        if repr(vList[4]).upper().find('DOM') > 0:
            for i in vList[4]:
                ElementNode.appendChild(i)
        else:
            ElementNode.appendChild(objDOM.createTextNode(vList[4]))

    # Append Node
    parentNode.appendChild(ElementNode)

    # Return Node
    return ElementNode

def ParserDICOMElement(dElement):
    if DICOMElementIsSequence(dElement):
        AddSequence(dElement)
    else:
        AddElement(PackageList(dElement), Root, XMLElementName)

def ParseDicomData(dObject):
    dObject.decode()
    for tElement in DICOMTopElementList(dObject):
        dTagObject = DICOMTagObject((tElement[0][0], tElement[0][1]))
        dElement   = dObject[dTagObject]
        ParserDICOMElement(dElement)

def DICOMTopElementList(dObject):
    dTopElementList = []
    for dElement in dObject:
        tmp = repr(dElement.tag).split(',')
        dTopElementList.append(
            [(tmp[0].strip()[1:],tmp[1].strip()[:-1]), dElement.VR, dElement.name]
        )
    return dTopElementList

def DICOMTagObject(dTagID):
    try:
        return dicom.tag.Tag(dTagID[0], dTagID[1])
    except:
        parser.error('Fail to load/parse DICOM tag.')

def DICOMObject(dFile):
    try:
        return dicom.read_file(dFile)
    except:
        parser.error('Fail to load/parse DICOM file.')

if __name__ == '__main__':

    global DICOM_TAG_LIST
    DICOM_TAG_LIST = {
    'AE' : ['Application Entity',    '16 Bytes Maximum'],
    'AS' : ['Age String',            '4 Bytes Fixed'],
    'AT' : ['Attribute Tag',         '4 Bytes Fixed'],
    'CS' : ['Code String',           '16 Bytes Maximum'],
    'DA' : ['Date',                  '8 Bytes Fixed'],
    'DS' : ['Decimal String',        '16 Bytes Maximum'],
    'DT' : ['Date Time',             '26 Bytes Maximum'],
    'FL' : ['Floating Point Single', '4 Bytes Fixed'],
    'FD' : ['Floating Point Double', '8 Bytes Fixed'],
    'IS' : ['Integer String',        '12 Bytes Maximum'],
    'LO' : ['Long String',           '64 Bytes Maximum'],
    'LT' : ['Long Text',             '10240 Bytes Maximum'],
    'OB' : ['Other Byte String',     'Unlimited'],
    'OF' : ['Other Float String',    'Unlimited'],
    'OW' : ['Other Word String',     'Unlimited'],
    'PN' : ['Person Name',           '64 Bytes Maximum'],
    'SH' : ['Short String',          '16 Bytes Maximum'],
    'SL' : ['Signed Long',           '4 Bytes Fixed'],
    'SQ' : ['Sequence of Items',     'Unlimited'],
    'SS' : ['Signed Short',          '2 Bytes Fixed'],
    'ST' : ['Short Text',            '1024 Bytes Maximum'],
    'TM' : ['Time',                  '16 Bytes Maximum'],
    'UI' : ['Unique Identifier',     '64 Bytes Maximum'],
    'UL' : ['Unsigned Long',         '4 Bytes Fixed'],
    'UN' : ['Unknown',               'Unlimited'],
    'US' : ['Unsigned Short',        '2 Bytes Fixed'],
    'UT' : ['Unlimited Text',        'Unlimited'],
    }

    #   Define / Parse parameters
    usage = """
    Call:
        %prog -f|--dicom-file Dicom_File
        %prog -f|--dicom-file Dicom_File -l|--list-tag
    """
    version = '1.0'
    epilog  = ''

    parser  = optparse.OptionParser(usage = usage, version = version, epilog = epilog)
    parser.add_option('-f', '--dicom-file',
            dest = 'DICOM_FILE',
            help = "The full path of a dicom file (*.dcm).")
    parser.add_option('-l', '--list-tags',
            dest = 'LIST_TAGS',
            action="store_true",
            default = False,
            help = 'Display whole tags of DICOM standard.')

    #   Get parameters
    (options, args) = parser.parse_args()

    #    Deal with parameters
    if options.DICOM_FILE is None:
        parser.error('No DICOM File is specified.')

    elif os.path.exists(options.DICOM_FILE) is False: # Test whether the file is available
        parser.error('Specified DICOM File is not available.')

    else:
        dObject         = DICOMObject(options.DICOM_FILE)
        dTopElementList = DICOMTopElementList(dObject)

    if options.LIST_TAGS is False:
        # File name
        dOutputXMLDir  = options.DICOM_FILE.split('\\')
        dOutputXMLDir.pop()
        dOutputXMLDir  = '\\'.join([i for i in dOutputXMLDir])
        if len(dOutputXMLDir) == 0:
            dOutputXMLFile = '{}.xml'.format(options.DICOM_FILE.split('\\')[-1].split('.')[0])
        elif len(dOutputXMLDir) > 0:
            dOutputXMLFile = '{0}\\{1}.xml'.format(
                dOutputXMLDir,
                options.DICOM_FILE.split('\\')[-1].split('.')[0]
            )

        # Initiate XML file
        if os.path.exists(dOutputXMLFile):
            os.remove(dOutputXMLFile)
        xmlRootName = 'DICOM_Parser'
        objXML      = DOM.getDOMImplementation()
        objDOM      = objXML.createDocument(None, xmlRootName, None)
        Root        = objDOM.documentElement
        summaryNode = objDOM.createElement('Summary')
        summaryNode.setAttribute('file', options.DICOM_FILE)
        summaryNode.setAttribute('timestamp', time.strftime('%Y-%m-%d %H:%M:%S'))
        Root.appendChild(summaryNode)
        XMLElementName  = 'Element'
        XMLSequenceName = 'Sequence'
        XMLCustomized   = 'trophy'

        # Parse Data
        ParseDicomData(dObject)

        # Output to the file
        with open(dOutputXMLFile, 'w+') as f:
            objDOM.writexml(f, addindent='\t', newl='\n',encoding='utf-8')

    elif options.LIST_TAGS is True:
        print '\n'.join(
            ['({0}:{1})    {2}    {3}'.format(i[0].upper(), i[1].upper(), j, k)
                for i, j, k in dTopElementList]
        )
        sys.exit(0)
