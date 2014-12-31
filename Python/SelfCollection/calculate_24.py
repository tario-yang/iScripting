# coding: utf-8

'''
计算24点
'''

import random


def DivisionCheck(number1, number2):
	'''
	0 : number1 mod number2 is zero
	1 : number2 mod number1 is zero
	2 : the others
	'''
	try:
		return 0 if number1%number2 == 0 else 2
	except:
		return 1 if number2%number1 == 0 else 2

def Expression(number1, number2, operator):
	if operator == '1':
		return ['{0} {2} {1}'.format(number1, number2, operator_dict[operator]),
			'{1} {2} {0}'.format(number1, number2, operator_dict[operator])]
	elif operator == '3' and DivisionCheck(number1, number2) == 1:
		return ['{1} {2} {0}'.format(number1, number2, operator_dict[operator])]
	else:
		return ['{0} {2} {1}'.format(number1, number2, operator_dict[operator])]

def Judgement(operation_expression):
	return True if eval(ur'{}'.format(operation_expression)) == 24 else False

def Calculate24Expression(number_list, phase):
	global expression_list
	for item in phase:
		for i in range(3):
			for exp in Expression(number_list[item[0]], number_list[item[1]], str(i)):
				tmp = exp.split(' ')
				if len(number_list) == 4:
					expression_list.append(tmp)
					ret = [eval(exp), number_list[item[2]], number_list[item[3]]]
					Calculate24Expression(ret, phase_two)
				elif len(number_list) == 3:
					expression_list.append(tmp[1])
					expression_list.append(tmp[2])
					ret = [eval(exp), number_list[item[2]]]
					Calculate24Expression(ret, phase_three)
				elif len(number_list) == 2:
					if Judgement(exp) is True:
						expression_list.append(tmp[1])
						expression_list.append(tmp[2])
						print expression_list
					else:
						expression_list = []
				else:
					print 'Unknown Error'

# set target
target         = 24
minimum_number = 1
maximum_number = 13
operator_dict  = {
	'0' : '+',
	'1' : '-',
	'2' : '*',
	'3' : '/',
}

# prepare data
input_data  = []
for i in range(4):
	input_data.append(random.randint(minimum_number,maximum_number))
print input_data

# set phases of calculation
phase_one   = [(0,1,2,3), (0,2,1,3), (0,3,1,2), (1,2,0,3), (1,3,0,2), (2,3,0,1)]
phase_two   = [(0,1,2), (0,2,1), (1,2,0)]
phase_three = [(0,1), (1,0)]

# set result list
global expression_list
expression_list = []

# Main function
Calculate24Expression(input_data, phase_one)
