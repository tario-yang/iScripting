# coding: utf-8

'''
完全数
如果一个数恰好等于它的因子之和，则称该数为“完全数”。
各个小于它的约数（真约数,列出某数的约数，去掉该数本身，剩下的就是它的真约数）的和等于它本身的自然数叫做完全数（Perfect number），又称完美数或完备数。
例如：
	第一个完全数是6，它有约数1、2、3、6，除去它本身6外，其余3个数相加，1+2+3=6。
	第二个完全数是28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。
	第三个完全数是496，有约数1、2、4、8、16、31、62、124、248、496，除去其本身496外，其余9个数相加，1+2+4+8+16+31+62+124+248=496。
	后面的完全数还有8128、33550336等等。

亏数
对于“4”这个数，它的真约数有1、2，其和是3，比4本身小，像这样的自然数叫做亏数。

盈数
对于“12”这个数，它的真约数有1、2、3、4、6，其和是16，比12本身大，像这样的自然数叫做盈数。

所以，完全数就是既不盈余，也不亏欠的自然数。
'''


def Factors(number):
	return [i for i in xrange(1,number) if number%i==0]

# Check Single Number
def IsPrefectNumber(number):
	return True if reduce(lambda x,y: x+y, Factors(number)) == number else False

def IsDeficientNumber(number):
	return True if sum(Factors(number)) < number else False

def IsExcessNumber(number):
	return True if sum(Factors(number)) > number else False

# Check range
for n in range(1,10000):
    nlist = Factors(n)
    if sum(nlist) == n:
        print ''.join([str(n),'=','+'.join([str(n) for n in nlist])])