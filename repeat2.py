def calRepeat(main_list):
	'''print(set(list))
	res = dict()
	for x in list:
		if x in res:
			count = res[x]
			res[x] = count +1
		else:
			res[x] = 1
	print res'''
	list_1 = [];
	list_2 = [];
	for each in main_list:
		if each not in list_1:
			list_1.append(each);
		if main_list.count(each) > 1 and each not in list_2:
			list_2.append(each);
	return list_1, list_2;


print(calRepeat([1,2,2,3,4,3,8,4,'7',4,5,5]));