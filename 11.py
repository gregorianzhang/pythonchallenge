import urllib2
import base64
import Image

#url="http://www.pythonchallenge.com/pc/return/cave.jpg"

#auth="huge:file"
#password=base64.b64encode(auth)
#tt="Basic "+password
#req = urllib2.Request(url)
#req.add_header('Authorization',tt)
#data = urllib2.urlopen(req).read()

#f = open('cave.jpg','wb')
#f.write(data)

f = Image.open('cave.jpg')
(h,w) = f.size

print h,w
for x in xrange(int(h)):
    for y in xrange(int(w)):
	if y % 2 ==0 and x % 2 ==0:
	    try:
                (a1,a2,a3)= f.getpixel((x-1,y))
                (b1,b2,b3)= f.getpixel((x+1,y))
                (c1,c2,c3)= f.getpixel((x,y-1))
                (d1,d2,d3)= f.getpixel((x,y+1))
		
		z1 = int((a1+b1+c1+d1)/4.0)
		z2 = int((a2+b2+c2+d2)/4.0)
		z3 = int((a3+b3+c3+d3)/4.0)
		#print z1,z2,z3
		try:
		    f.putpixel((x,y),(z1,z2,z3))
		except:
		    print z1,z2,z3,x,y
	    except:
		#print x,y
		pass
	if y % 2 ==1 and x % 2 ==1:
	    try:
                (a1,a2,a3)= f.getpixel((x-1,y))
                (b1,b2,b3)= f.getpixel((x+1,y))
                (c1,c2,c3)= f.getpixel((x,y-1))
                (d1,d2,d3)= f.getpixel((x,y+1))
		
		z1 = int((a1+b1+c1+d1)/4.0)
		z2 = int((a2+b2+c2+d2)/4.0)
		z3 = int((a3+b3+c3+d3)/4.0)
		#print z1,z2,z3
		try:
		    f.putpixel((x,y),(z1,z2,z3))
		except:
		    print z1,z2,z3,x,y
	    except:
		#print x,y
		pass
	

		

f.save('bbb.jpg')
	

image = Image.open("cave.jpg")
nsize = tuple([x / 2 for x in image.size])
odd = even = Image.new(image.mode, nsize)

for x in range(image.size[0]):
    for y in range(image.size[1]):
        if x % 2 == 0 and y % 2 == 0:
            even.putpixel((x / 2, y / 2), image.getpixel((x, y)))
        elif x % 2 == 0 and y % 2 == 1:
            odd.putpixel((x / 2, (y - 1) / 2), image.getpixel((x, y)))
        elif x % 2 == 1 and y % 2 == 0:
            even.putpixel(((x - 1) / 2, y / 2), image.getpixel((x, y)))
        else:
            odd.putpixel(((x - 1) / 2, (y - 1) / 2), image.getpixel((x, y)))

even.save('even.jpg')
odd.save('odd.jpg')

