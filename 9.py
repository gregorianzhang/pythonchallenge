import urllib2
import base64
import Image

auth="huge:file"
password=base64.b64encode(auth)
tt="Basic "+password
url = "http://www.pythonchallenge.com/pc/return/good.html"
req = urllib2.Request(url)
req.add_header('Authorization',tt)
data = urllib2.urlopen(req).read()

#print data,type(data)
n=0
first=""
second=""
for x in data.split('\n'):
    if x == 'first:':
	n =1
	continue


    if x == 'second:':
	n = 2
	continue
	
    if n == 1 and x != '':
        first += x
    if n == 2 and x != '' and x != '-->':
        second += x

#print first
#print "*"*40
#print second
first1 = first.split(",")
second1 = second.split(",")

firstlist = [[first1[n],first1[n+1]] for n in xrange(0,len(first1),2)]
secondlist = [[second1[n],second1[n+1]] for n in xrange(0,len(second1),2)]
#print firstlist


im = Image.new("RGB", (512, 512), "white")
for v in firstlist:
    #print v[0],v[1]
    im.putpixel((int(v[0]),int(v[1])), (0,0,0))

for v in secondlist:
    im.putpixel((int(v[0]),int(v[1])), (255,0,0))

im.save('bbb.png')



