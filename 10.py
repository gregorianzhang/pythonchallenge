import urllib2

url = "http://www.pythonchallenge.com/pc/return/sequence.txt"

a = [1, 11, 21, 1211, 111221]
b = [1]
nn=[]


def bb(n):
    z=""
    y=None
    b=0
    num=len(n)
    dd=1
    for x in n :

	if y == None:
	    print "none x %s b %s" % (x,b)
	    y = x
	  
	if y == x:
	    b+=1
	    print "y == x  x %s b %s" % (x,b)

        else:
	    z+=str(b)+str(y)
	    print "else y != x  x %s b %s" % (x,b)
	    print "z %s " % z
	    
	    y=None
	    b=0
	    print "else y != x  x %s b %s" % (x,b)

	if dd == num:
	    z+=str(b)+str(x)
	else:
	    dd+=1

    return z   


#print bb('1211')	

def ab(n):
    y=n[0]
    tt=1
    num=len(n)
    b=0
    z=""
    for x in n:
	#print "x %s y %s b %s z %s" % (x,y,b,z)
        if y == x:
	    b+=1
	else:
	    
	    z += str(b)+str(y)
	    b=1
	    y=x

	if num == tt:
	    z += str(b)+str(x)

	tt += 1

    return z
	
print ab('111221')
		
for x in xrange(32):
    b.append(ab(str(b[-1])))

print len(b[30])


