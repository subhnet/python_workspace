def findAllPrimeFactors(num):
	setNum = set()
	copyInput = num
	for x in xrange(2,copyInput):
		if copyInput%x==0:
			setNum.add(x)
			copyInput = copyInput/x
			x = x-1
	print setNum



print 'Please Enter the number : '
num = int(raw_input())

findAllPrimeFactors(num)


			
