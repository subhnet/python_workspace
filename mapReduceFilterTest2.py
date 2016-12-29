lst = [1,3,6,2,5,8,4,9]
lst2 = [1,3,6,2,5,8,4,9]

max_find = lambda x,y : x if(x > y) else y

print max_find(2,3)



print map(lambda x,y:x+y,lst,lst2)


print reduce(max_find,lst)

#Even check using Filter
print filter(lambda x:x%2==0,lst)