from __future__ import print_function

print '='*60
print ' '*20+'TIC TAC TOE'+' '*30
print '='*60
entries = []
boardList = [[9,9,9],[9,9,9],[9,9,9]]

def displayBoard():
	for rows in boardList:
		print "		      %d|%d|%d			" % (rows[0],rows[1],rows[2])
		print "    		      -----			"
		
		
	
def updateBoard(entry,playerId):
	a = (entry-1)/3
	b = (entry-1)%3
	#print 'Setting %d , %d as %d' % (a,b,playerId)
	boardList[a][b] = playerId
	displayBoard()

def checkIfWon():
	#check horizontal rows
	flag = False
	for row in boardList:
		flag =  row[0] != 9 and len(set(row))==1
		#flag =  all((x != 9 and x == row[0]) for x in row)
		if flag == True:
			print "Player %d won..Congrats!!" % row[0]
			return True
	
	
	#check vertical columns
	for i in range(0,3):
		li = []
		li += (row[i] for row in boardList)
		flag = li[i] != 9 and len(set(li))==1
		if flag == True:
			print "Player %d won..Congrats!!" % li[0]
			return True
	return flag
	
	#check diagonals
	
			
		
	
def startGame():
	displayBoard()
	win = False
	i = 1
	while not win:
		print '-'*10
		print 'Player %d:' % (i%2)		
		print '-'*10
		entry = input()
		updateBoard(int(entry),i%2)		
		i +=1
		win = checkIfWon()
		
	displayBoard()	
	
#main function
startGame()
	