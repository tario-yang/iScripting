import os

'''
Define class'students'
-- inside class define method to read instudents_old.txt
-- inside class define method to sort the namesalphabetically
-- inside class define method to write tostudents_new.txt
-- inside class define method to find the name 'Morgan,Lillian' and print the name position in the list
-- inside class define method to find the 10th name inthe list and print the name and position in the list

Define class 'stack'
-- initialise stack
-- define empty stack method
-- define push method that pushes an entire list to thestack
-- define pop method that pops the entire stack
-- define peek method to check how big the stack is

Create the students object
Create the stack object
Call the students objects' read method
Call the student objects' sort method
Call the stack objects' push method
Call the stack objects' pop method
Call the student objects' write method to write the sorted and reversed student list to the students_new.txt file
Call the student objects' method to find 'Morgan,Lillian'
Call the student objects' method to print the 10th name in the list
'''

class students:
	def __init__(self):
		self.input_file = 'instudents_old.txt'
		if not os.path.exists(self.input_file):
			print 'io error: file does not exist.'
			return None
		else:
			with open(self.input_file, 'rU') as f:
				self.input_list = f.readlines()
			self.output_file = 'outstudents_old.txt'
			if os.path.exists(self.output_file):
				os.remove(self.output_file)
	def sort(self):
		self.input_list.sort()
	def output(self):
		with open(self.output_file, 'w') as f:
			for i in self.input_list:
				f.write(i + '\n')
	def findbyname(self, name):
		try:
			index = self.input_list.index(name)
		except:
			print 'name dose not exist!'
		else:
			print 'index: {}'.format(index+1)
	def findbyindex(self, index):
		try:
			print self.input_list[index-1]
		except:
			print 'index error'

class stack:
	def __init__(self):
		self.stack = []
	def empty(self):
		self.stack = []
	def pushstack(self, element):
		self.stack.append(element)
	def popstack(self):
		return self.stack.pop()
	def peekstack(self):
		return len(self.stack)
