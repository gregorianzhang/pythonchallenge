import urllib2
import Image

picurl = "http://www.pythonchallenge.com/pc/def/oxygen.png"

data = urllib2.urlopen(picurl).read()

file1="oxygen.png"
with open(file1,'wb') as picf:
    picf.write(data)

fpic = Image.open(file1)
h,w = fpic.size
tt=""
y=45
z=0
(w,e,r,t)=(0,0,0,0)
for x in xrange(h,):
    (a,b,c,d)=fpic.getpixel((x,y))
    if a == b ==c:
        if w == a:
            z +=1
            #print "z is %s" % z
            if z> 7:
                tt +=''.join(chr(a))
                z=0
            #print x,chr(w)
        else:
            z=0
            #print x,w,chr(w)
            tt +=''.join(chr(a))
        #tt +=''.join(chr(a))
        (w,e,r,t) = (a,b,c,d)

print tt

cc=""
bb= [105, 110, 116, 101, 103, 114, 105, 116, 121]
for x in bb:
    cc += ''.join(chr(x))

print cc
