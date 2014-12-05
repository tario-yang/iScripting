# coding=utf-8

"""
1. 有ABCD四个列表，每个列表有不同的元素（理解为字母）；
2. 每次从四个列表里面pop第一个元素组成一个单词作为新列表（输出的列表）的元素；
3. pop完之后要判断：
        D列表长度可以为0
        C列表长度可以为0，当D列表长度为0
        B列表长度可以为0，当C列表长度为0
        A列表长度可以为0，当B列表长度为0
4. 如果有异常（不符合上述条件），组成的单词要追回（remove）。
5. 输出包含新生成单词的列表。

另外要注意异常：
    当输入的四个列表已经有长度为0的情况
    当第一次pop之后，有列表长度为0的情况
"""

def GenerateRndList():
	"Call ListFactory and check whether the list is empty. If it is, repeat ListFactory."
	while 1:
		list = ListFactory()
		if len(list) > 0:
			return list

def ListFactory():
	"Generate list"
	from random import randint
	List = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	tmpID = randint(0,len(List)) # how many elements require to be removed
	for i in range(tmpID):
		List.pop(randint(0, (len(List) - 1)))
	return List

def AddWord(character_list, debug = False):
	"Add word to output list"
	global WORD_LIST
	word = ''
	for i in character_list:
		word += i
	if debug is True:
		print 'Combined -> ', word
	WORD_LIST.append(word)

def RemoveWord(debug = False):
	"Remove final word to output list"
	global WORD_LIST
	if debug is True:
		print 'Remove -> ', WORD_LIST[-1]
	WORD_LIST.pop()

def Outputter():
	print '\n{}\n'.format(WORD_LIST)

def WordVerifier(word):
	"Send out word to one web site to verify whether word is meaningful."
	import urllib2
	url = "http://fanyi.baidu.com"
	print urllib2.urlopen(url, word).read()

def ListVerifier(input_list):
	"Check whether length of list items matches the requirement"
	global ProcessFlag

	# Prepare a flag list, whose element is 1 or 0.
	original_length_list = []
	for i in range(len(input_list)):
		if len(input_list[i]) == 0:
			original_length_list.append(0)
		if len(input_list[i]) >= 1:
			original_length_list.append(1)

	'''
	Compare whether the list is same after sorted,
		- if same, rule is matched;
		- if not same, rule is NOT matched.
	'''
	compare_length_list = original_length_list[:]
	compare_length_list.sort()
	compare_length_list.reverse()
	if str(compare_length_list) != str(original_length_list):
		RemoveWord()
		ProcessFlag = False
	elif original_length_list.count(0) > 0:
		ProcessFlag = False

def Callback(input_list,  Callback_Support_Function):
	"Generate new word"
	while 1:
		new_word = []
		for i in range(len(input_list)):
			new_word.append(input_list[i].pop(0))
		AddWord(new_word)
		Callback_Support_Function(input_list)
		if ProcessFlag is False:
			break

def main(list_number = 4):
	INPUT = []
	for i in range(list_number):
		INPUT.append(GenerateRndList())
	print 'Generated lists are,'
	for i in INPUT:
		print '\t', i

	Callback(INPUT, ListVerifier)
	Outputter()

	# WordVerifier(word)

if __name__ == '__main__':
	global WORD_LIST, ProcessFlag
	WORD_LIST = []
	ProcessFlag = True
	main(list_number = 4)
