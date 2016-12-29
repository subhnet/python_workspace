def vol(rad):
    return (4.0/3)*(3.14)*(rad**3)

def ran_check(num,low,high):
    if num in range(low,high+1):
        print " %s is in the range" %str(num)
    else :
        print "The number is outside the range"

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
def up_low(s):
    upCount = 0
    lowCount = 0
    for c in s:
        if c.isupper():
            upCount+=1
        elif c.islower():
            lowCount+=1
        else:
            pass
    print "Original String : ", s
    print "No. of Upper case characters : ", upCount
    print "No. of Lower case characters : ", lowCount

            
        



print ran_check(1,1,5)
up_low(s)
