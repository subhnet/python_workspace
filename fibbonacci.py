def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)


def fib():	
    a,b = 0,1
    while True:
    	yield a
    	a,b = b,a+b

while True:
	inputVal =  raw_input('Enter a number : (N to Exit)')
	if inputVal=='N':
		break
	for index,num in enumerate(fib()):
		print str(index) + ' : ' + str(num)
		if index == int(inputVal):
			break

			
