def isPrime(num):
	intnum = int(num)
	return all(intnum%x != 0 for x in range(2, intnum))

while True:
	inputVal =  raw_input('Enter a number : (N to Exit)')
	if inputVal=='N':
		break
	print isPrime(inputVal)

			
