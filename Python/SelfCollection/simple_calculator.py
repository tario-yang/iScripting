# coding: utf-8

'''
计算器
'''

operator = {
	'a': ['a for addition','+'],
	'b': ['b for subtraction','-'],
	'c': ['c for multiplication','*'],
	'd': ['d for division','/'],
	'z': ['z for exit',None]
}

def DisplayOperationMenu():
	for key, data in operator.items():
		print data[0]
	print

def GetInputs():
	input_data = raw_input('Input two numbers (format -> number1,number2): ')
	return (int(input_data.split(',')[0]),int(input_data.split(',')[1]))

def GetOperator():
	input_operator = raw_input('Select one of the above operates: ')
	try:
		return operator[input_operator][1]
	except:
		return 'SKIP'

def Calculator(parameters, operator):
	strline = '{0}{2}{1}'.format(parameters[0],parameters[1],operator)
	try:
		print '{}={}'.format(strline, eval(strline))
	except:
		print '< Incorrect operation >'
	print

while True:
	DisplayOperationMenu()
	p = GetOperator()
	if p == 'SKIP':
		print 'Incorrect selection!'
		continue
	elif p is None:
		break
	else:
		Calculator(GetInputs(), p)