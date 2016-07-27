# coding: utf-8

import xlwt
import json
import iso8601
import datetime
import xlsxwriter

def ParserJSON(stringline):
    json_sample = json.loads(stringline)

    state       = json_sample['metrics']['state']
    uptime      = json_sample['metrics']['stats']['uptime']
    name        = json_sample['metrics']['stats']['name']
    fds_quota   = json_sample['metrics']['stats']['fds_quota']
    mem_quota   = float(json_sample['metrics']['stats']['mem_quota'])/1024/1024
    disk_quota  = float(json_sample['metrics']['stats']['disk_quota'])/1024/1024
    host        = json_sample['metrics']['stats']['host']
    usage_cpu   = str(round(float(json_sample['metrics']['stats']['usage']['cpu']), 4))
    usage_mem   = float(json_sample['metrics']['stats']['usage']['mem'])/1024/1024
    usage_disk  = float(json_sample['metrics']['stats']['usage']['disk'])/1024/1024
    usage_time  = datetime.datetime.strftime(iso8601.parse_date(json_sample['metrics']['stats']['usage']['time']), "%Y-%m-%d %H:%M:%S")
    uris        = str(json_sample['metrics']['stats']['uris']).strip('[]').lstrip("'u").rstrip("'")
    port        = json_sample['metrics']['stats']['port']

    return (name, uris, port, host, state, uptime, fds_quota, mem_quota, disk_quota, usage_time, usage_cpu, usage_mem, usage_disk)


# Define
SampleLog = 'sample.log'
Outputter = 'cf_statistics_resource.xlsx'
sheetname = 'Statistic'
workbook  = xlsxwriter.Workbook(Outputter)
worksheet = workbook.add_worksheet(sheetname)
retResult = []
LineCount = 2


# Generate data
with open(SampleLog) as f:
    for i in f.readlines():
        retResult.append(ParserJSON(i.strip('\n')))


# Add Title
header = [  'name', 'uris', 'port', 'host', 'state', 'uptime',
            'fds_quota', 'mem_quota (MB)', 'disk_quota (MB)',
            'usage_time', 'usage_cpu', 'usage_mem (MB)', 'usage_disk (MB)']
formatter_header = workbook.add_format({'bold': 1, 'font_name': 'Courier New', 'font_size': 11})
worksheet.write('A1', 'CF STATISTICS REPORT', formatter_header)
worksheet.write_row('A2', header, formatter_header)


# Add Data
formatter_content  = workbook.add_format({'bold': 1, 'font_name': 'Courier New', 'font_size': 9})
for i in retResult:
    worksheet.write(LineCount, 0,  i[0],  formatter_content)
    worksheet.write(LineCount, 1,  i[1],  formatter_content)
    worksheet.write(LineCount, 2,  i[2],  formatter_content)
    worksheet.write(LineCount, 3,  i[3],  formatter_content)
    worksheet.write(LineCount, 4,  i[4],  formatter_content)
    worksheet.write(LineCount, 5,  i[5],  formatter_content)
    worksheet.write(LineCount, 6,  i[6],  formatter_content)
    worksheet.write(LineCount, 7,  i[7],  formatter_content)
    worksheet.write(LineCount, 8,  i[8],  formatter_content)
    worksheet.write(LineCount, 9,  i[9],  formatter_content)
    worksheet.write(LineCount, 10, i[10], formatter_content)
    worksheet.write(LineCount, 11, i[11], formatter_content)
    worksheet.write(LineCount, 12, i[12], formatter_content)
    LineCount += 1

# Chart #1
chartsheet1 = workbook.add_chartsheet('CPU')
chart1      = workbook.add_chart({'type': 'line'})
chart1.add_series({
    'name':        [sheetname, 1, 10],
    'categories':  [sheetname, 2, 9,  LineCount - 1, 9],
    'values':      [sheetname, 2, 10, LineCount - 1, 10],
    'marker':      {'type': 'diamond', 'size': 8},
    'data_labels': {'category': True},
})
chart1.set_title ({'name': 'Usage of CPU'})
chart1.set_x_axis({'name': 'usage_time'})
chart1.set_y_axis({'name': 'usage_cpu'})
chart1.set_style(10)
chartsheet1.set_chart(chart1)

# Chart #2
chartsheet2 = workbook.add_chartsheet('MEM')
chart2      = workbook.add_chart({'type': 'bar'})
chart2.add_series({
    'name':        'used',
    'categories':  [sheetname, 2, 9,  LineCount - 1, 9],
    'values':      [sheetname, 2, 11, LineCount - 1, 11],
    'marker':      {'type': 'diamond', 'size': 8},
    'data_labels': {'category': True},
})
chart2.add_series({
    'name':        'total',
    'categories':  [sheetname, 2, 9,  LineCount - 1, 9],
    'values':      [sheetname, 2, 7, LineCount - 1, 7],
    'marker':      {'type': 'diamond', 'size': 8},
    'data_labels': {'category': True},
})
chart2.set_title ({'name': 'Usage of MEM'})
chart2.set_x_axis({'name': 'usage_time'})
chart2.set_y_axis({'name': 'usage_mem'})
chart2.set_style(10)
chartsheet2.set_chart(chart2)

# Chart #3
chartsheet3 = workbook.add_chartsheet('DISK')
chart3      = workbook.add_chart({'type': 'bar'})
chart3.add_series({
    'name':        'used',
    'categories':  [sheetname, 2, 9,  LineCount - 1, 9],
    'values':      [sheetname, 2, 12, LineCount - 1, 12],
    'marker':      {'type': 'diamond', 'size': 8},
    'data_labels': {'category': True},
})
chart3.add_series({
    'name':        'total',
    'categories':  [sheetname, 2, 9, LineCount - 1, 9],
    'values':      [sheetname, 2, 8, LineCount - 1, 8],
    'marker':      {'type': 'diamond', 'size': 8},
    'data_labels': {'category': True},
})
chart3.set_title ({'name': 'Usage of Disk'})
chart3.set_x_axis({'name': 'usage_time'})
chart3.set_y_axis({'name': 'usage_disk'})
chart3.set_style(10)
chartsheet3.set_chart(chart3)

workbook.close()

