def isPrime(num):
	intnum = int(num)
	for x in range(2,intnum):
		if intnum%x==0:
			return False
	return True

while True:
	inputVal =  raw_input('Enter a number : (N to Exit)')
	if inputVal=='N':
		break
	print isPrime(inputVal)

			
