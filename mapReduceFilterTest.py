#Map Demo
def word_lengths(phrase):
	print map(lambda x:len(x),phrase.split())
word_lengths('How long are the words in this phrase')


#Reduce Demo
def digits_to_num(digits):
    print reduce(lambda x,y:x*10+y,digits)
digits_to_num([3,4,3,2,1])


#Filter Demo
def filter_words(word_list, letter):
    print filter(lambda x:x[0]==letter,word_list)

l = ['hello','are','cat','dog','ham','hi','go','to','heart']
filter_words(l,'h')


#Zip Demo
def concatenate(L1, L2, connector):
	print [word1+connector+word2 for word1,word2 in zip(L1,L2)]

concatenate(['A','B'],['a','b'],'-')



#Enumeration demo
def count_match_index(L):
	print len([x for i,x in enumerate(L) if x==i])

count_match_index([0,2,2,1,5,5,6,10])