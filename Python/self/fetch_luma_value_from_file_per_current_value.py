# coding=utf-8

'''
Export BlueYUV data to one Excel file which is in same path of this script.

Usage,
1. Map the remote path to local drive, for example, "T:\\"
2. Assign this drive to variable, ROOT
3. Execute the script.

Workflow,
1. Get directory list from ROOT
2. Directory traversal: date / SN directory
3. Parse file under SN directory
4. Get data and update 'result' list. Element in 'result' is, (date, SN, value_680, value_800). When value is inavailable, set it to zero.
'''

import os
import sys
try:
    import xlwt
except:
    print 'Module, "xlwt", is not installed. This script cannot work.'
    sys.exit(1)

def fetch_directory_list(root):
    if os.path.exists(root):
        directory_list = os.listdir(root)
    else:
        return None

    output = []
    for i in directory_list:
        if os.path.isdir('{0}\{1}'.format(root, i)):
            output.append(i)
    output.sort()

    return output

def validate_file(folder):
    if os.path.exists('{0}\{1}'.format(folder, input_file_name)):
        return True
    else:
        return False

def parse_file(folder):
    global result

    with open('{0}\{1}'.format(folder, input_file_name)) as f:
        check_list = f.readlines()

    element = [0, 0]
    for i in range(len(check_list)):
        check_list[i] = check_list[i].strip('\n')
        check_list[i] = check_list[i].strip('\r')
        check_list[i] = check_list[i].replace(' = ', ',')
        check_list[i] = check_list[i].split(' ')
        if check_list[i][0].upper() == 'CURRENT,{}'.format(key_value[0]):
            if element[0] == 0:
                element[0] = check_list[i][3].partition(',')[2]
            else:
                raise 'incorrect file content -> duplicated current value ({}).'.format(key_value[0])
        elif check_list[i][0].upper() == 'CURRENT,{}'.format(key_value[1]):
            if element[1] == 0:
                element[1] = check_list[i][3].partition(',')[2]
            else:
                raise 'incorrect file content -> duplicated current value ({}).'.format(key_value[1])

    j = os.path.split(folder)
    result.append((os.path.split(j[0])[1], j[1][:8], element[0], element[1]))

def output2excel():
    try:
        if os.path.exists(output_file_name):
            os.remove(output_file_name)

        # Create file
        objWorkbook = xlwt.Workbook(encoding = 'utf-8')
        objWorksheet = objWorkbook.add_sheet(sheetname = 'BlueYUV data')

        # Write title
        objWorksheet.write(0, 0, 'The following data is fetched when current value is {} or {}.'.format(key_value[0], key_value[1]))

        # Write Data
        # 1
        objWorksheet.write(1, 1, 'SN')
        objWorksheet.write(1, 2, 'Luma per Current: {}'.format(key_value[0]))
        start_point = [2, 0]
        start_title = ''
        for i in result:
            if i[2] > 0:
                if start_title != i[0]:
                    objWorksheet.write(start_point[0], start_point[1], i[0])
                    start_title = i[0]
                objWorksheet.write(start_point[0], start_point[1]+1, i[1])
                objWorksheet.write(start_point[0], start_point[1]+2, int(i[2]))
                start_point[0] += 1
        # 2
        objWorksheet.write(1, 5, 'SN')
        objWorksheet.write(1, 6, 'Luma per Current: {}'.format(key_value[1]))
        start_point = [2, 4]
        start_title = ''
        for i in result:
            if i[3] > 0:
                if start_title != i[0]:
                    objWorksheet.write(start_point[0], start_point[1], i[0])
                    start_title = i[0]
                objWorksheet.write(start_point[0], start_point[1]+1, i[1])
                objWorksheet.write(start_point[0], start_point[1]+2, int(i[3]))
                start_point[0] += 1

        # Save
        objWorkbook.save(output_file_name)
    except:
        return False
    else:
        return True

def main(debug = False):
    root = ROOT
    for i in fetch_directory_list(root):
        print 'Checking >>> %s' % i,
        for j in fetch_directory_list('{0}\{1}'.format(root, i)):
            if j in exclude_directory_list:
                continue
            path = '{0}\{1}\{2}'.format(root, i, j)
            if validate_file(path):
                parse_file(path)
            else:
                continue
        print ' >>> Done'
        if debug:
            break
    print 'Output to file...'
    output2excel()

if __name__ == '__main__':
    global key_value, ROOT, input_file_name, exclude_directory_list, output_file_name, result
    key_value = (680, 800)
    ROOT = 'T:\\'
    input_file_name = 'opt_led_calibration.txt'
    exclude_directory_list = ['config']
    output_file_name = 'output_current_value_BlueYUV_list.xls'
    result = []
    main()