K=range(16)
K[0] = ''
print '\t'.join([str(i) for i in K])
for i in xrange(1, len(K)):
	print '{}\t'.format(K[i]),
	for j in K[1:]:
		print '{}\t'.format(K[i]*j),
	print