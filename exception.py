try:
	f = open('testFile','w')
	f.write('Oolala')
except Exception as e:
	print 'Error Occured...oooo'
	raise e
else:
	print 'Oolala written...'
	f.close()
