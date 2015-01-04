# coding: utf-8

'''
计算24点
	tested @ Windows 7 Pro 64-bit ENU
'''


try:
	import Tkinter as TK
except:
	import tkinter as TK
from ScrolledText import ScrolledText as ST
from random import randint


# GUI EVENT
def EntryUpdate(number_list):
	'Display the number list in Entry'
	inputbox.delete('0',TK.END)
	inputbox.insert('0', ', '.join([str(i) for i in number_list]))

def ScrolledTextClear():
	'Clear content in ST'
	outputbox.delete('1.0', TK.END)

def ScrolledTextAppend(message):
	'Append content in ST'
	outputbox.insert(TK.END, message)

# def SetTriggerState(status=1):
# 	'Set button status'
# 	trigger.config(state='disabled') if status == 0 else trigger.config(state='active')

def MessageProcessor():
	'Deal with message queue'
	if len(MessageQueue) > 0:
		ret = str(MessageQueue.pop(0))
		ScrolledTextAppend('{}\n'.format(ret))
	root.after(30, MessageProcessor)

# Calculator Event
def DivisionVerification(number1, number2):
	try:
		if number1%number2 == 0:
			return 0
	except:
		try:
			if number2%number1 == 0:
				return 1
		except:
			return 2

def Expression(number1, number2, operator):
	'Return the expression(s)'
	if operator == '1':
		return ['({0}{2}{1})'.format(number1, number2, operator_dict[operator]),
			'({1}{2}{0})'.format(number1, number2, operator_dict[operator])]
	elif operator == '3':
		ret = DivisionVerification(number1, number2)
		if ret == 0:
			return ['({0}{2}{1})'.format(number1, number2, operator_dict[operator])]
		if ret == 1:
			return ['({1}{2}{0})'.format(number1, number2, operator_dict[operator])]
		if ret == 2:
			return None
	else:
		return ['({0}{2}{1})'.format(number1, number2, operator_dict[operator])]

def Judgement(operation_expression):
	'Verify whether the expression equals to `target`.'
	try:
		return True if eval(ur'{}'.format(operation_expression)) == target else False
	except:
		return False

def EnumerateExpression(number_list):
	'''
	[A, B, C, D]

	1. Calculate A and B -> [R, C, D]
	2. Three scenarios:
		type 1:
			R,C and D
			R,D and C
		type 2:
		R and C,D
	'''

	strategy = [[[(0,1),2,3],
				[(0,1),3,2],
				[(0,2),1,3],
				[(0,2),3,1],
				[(0,3),1,2],
				[(0,3),2,1],
				[(1,2),0,3],
				[(1,2),3,0],
				[(2,3),0,1],
				[(2,3),1,0]],
				[[(0,1),(2,3)],
				[(0,2),(1,3)],
				[(0,3),(1,2)]]]

	# type 1
	for item in strategy[0]:
		ds = [number_list[item[0][0]], number_list[item[0][1]], number_list[item[1]], number_list[item[2]]]
		for i in range(4):
			try:
				for sub_exp_phase_one in Expression(ds[0], ds[1], str(i)):
					for j in range(4):
						try:
							for sub_exp_phase_two in Expression(sub_exp_phase_one, ds[2], str(j)):
								for k in range(4):
									try:
										for sub_exp_phase_three in Expression(sub_exp_phase_two, ds[3], str(k)):
											if Judgement(sub_exp_phase_three) is True:
												MessageQueue.append(sub_exp_phase_three)
									except:
										continue
						except:
							continue
			except:
				continue

	# type 2
	for item in strategy[1]:
		ds = [number_list[item[0][0]], number_list[item[0][1]]], [number_list[item[1][0]], number_list[item[1][1]]]
		for i in range(4):
			try:
				for sub_exp_left in Expression(ds[0][0], ds[0][1], str(i)):
					for j in range(4):
						try:
							for sub_exp_right in Expression(ds[1][0], ds[1][1], str(j)):
								for k in range(4):
									try:
										for sub_exp_final in Expression(sub_exp_left, sub_exp_right, str(k)):
											if Judgement(sub_exp_final) is True:
												MessageQueue.append(sub_exp_final)
									except:
										continue
						except:
							continue
			except:
				continue

def Executor():
	# prepare data
	input_data  = []
	for i in range(4):
		input_data.append(randint(minimum_number,maximum_number))
	EntryUpdate(input_data)

	# main function
	ScrolledTextClear()
	EnumerateExpression(input_data)
	if len(MessageQueue) > 0:
		MessageQueue.append('{}\nDone'.format('-'*32))
	else:
		MessageQueue.append(str(input_data))
		MessageQueue.append('Nothing!')

# set target
target         = 24
minimum_number = 1
maximum_number = 13
operator_dict  = {
	'0' : '+',
	'1' : '-',
	'2' : '*',
	'3' : '/',}

# Generate window
root = TK.Tk()
root.attributes('-topmost', 1)
root.attributes('-alpha', 0.85)
root.geometry('+{}+{}'.format(root.winfo_screenwidth()/8, root.winfo_screenheight()/8))
root.title('Generator -> 24')

# Add output box, each result will be filled in automatically
outputbox = ST(root,
	width=35, height=20,
	font=('Courier New', 13),
	fg='yellow', bg='black')
outputbox.pack(expand=1, fill='both')

# Add input box, its content will be filled in automatically
inputbox = TK.Entry(root, bd=2, bg='yellow')
inputbox.pack(side=TK.LEFT, expand=1, fill='x')

# Add button, which will trigger the calculation
trigger = TK.Button(root,
	text='Go!',
	command=Executor)
trigger.pack(side=TK.RIGHT, expand=1, fill='x')

# Add message queue to avoid blocking the GUI while calculating.
MessageQueue=[]
root.after(30, MessageProcessor)

# Display window
TK.mainloop()
