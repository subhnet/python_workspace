def calRepeat(list):
	print(set(list))
	res = dict()
	for x in list:
		if x in res:
			count = res[x]
			res[x] = count +1
		else:
			res[x] = 1
	print res


calRepeat([1,2,2,3,4,5,5])