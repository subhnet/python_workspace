lst = [1,2,3,4,5,6,7,8,9,10,11]

checkGreatFive = lambda x,y: y if x<4 else 'oolala'


for x,y in enumerate(lst):
	print checkGreatFive(x,y)
		
