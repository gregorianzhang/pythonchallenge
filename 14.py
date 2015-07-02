import Image
import base64
import urllib2

url="http://www.pythonchallenge.com/pc/return/wire.png"

auth="huge:file"
password=base64.b64encode(auth)
tt="Basic "+password
req = urllib2.Request(url)
req.add_header('Authorization',tt)
data = urllib2.urlopen(req).read()

with open('wire.png','wb') as f:
    f.write(data)





f1 = Image.open('wire.png')
#f1.show()
(h,w) = f1.size


def line2pic(file,x,y):
    totle = x*y
    old = file.load()
    new = Image.new('RGB',(x,y))
    sx = 0
    sy = 0
    ex = x
    ey = y
    num = 0
#    print "totle %s" % totle
    while num < totle:
#        print "num %s  sx %s sy %s ex %s ey %s" % (num,sx,sy,ex,ey)
        #if num > 1000:
        #    break
#        for n in xrange(sx,ey):
#            print "A sx %s sy %s ex %s ey %s" % (sx,sy,ex,ey)
#            print "A x %s y %s" % (sx,n)
#            new.putpixel((sx,n),old[num,0])
#            num += 1
#        sx += 1
#
#        for n in xrange(sx,ey):
#            print "B sx %s sy %s ex %s ey %s" % (sx,sy,ex,ey)
#            print "B x %s y %s" % (n,ey-1)
#            new.putpixel((n,ey-1),old[num,0])
#            num += 1
#        ey -= 1
#
#        for n in xrange(ey-1,sy-1,-1):
#            print "C sx %s sy %s ex %s ey %s" % (sx,sy,ex,ey)
#            print "C x %s y %s" % (ex-1,n)
#            new.putpixel((ex-1,n),old[num,0])
#            num +=1
#        ex -= 1
#
#        for n in xrange(ex-1,sx-1,-1):
#            print "D sx %s sy %s ex %s ey %s" % (sx,sy,ex,ey)
#            print "D x %s y %s" % (n,sy)
#            new.putpixel((n,sy),old[num,0])
#            num += 1
#        sy += 1
        for n in xrange(sx,ex):
#            print "A sx %s sy %s ex %s ey %s" % (sx,sy,ex,ey)
#            print "A x %s y %s" % (n,sy)
            new.putpixel((n,sy),old[num,0])
            num +=1
        sy += 1

        for n in xrange(sy,ey):
#            print "B sx %s sy %s ex %s ey %s" % (sx,sy,ex,ey)
#            print "B x %s y %s" % (ex-1,n)
            new.putpixel((ex-1,n),old[num,0])
            num +=1
        ex -= 1

        for n in xrange(ex-1,sx-1,-1):
#            print "C sx %s sy %s ex %s ey %s" % (sx,sy,ex,ey)
#            print "C x %s y %s" % (n,ey-1)
            new.putpixel((n,ey-1),old[num,0])
            num +=1
        ey -= 1

        for n in xrange(ey-1,sy-1,-1):
#            print "D sx %s sy %s ex %s ey %s" % (sx,sy,ex,ey)
#            print "D x %s y %s" % (sx,n)
            new.putpixel((sx,n),old[num,0])
            num +=1
        sx += 1


    return new

bb = line2pic(f1,100,100)
bb.save('ttt.jpg')

def pic2line(file,x,y):
    totle = x * y
    sx = 0
    sy = 0
    ex = x
    ey = y
    new = Image.new('RGB',(totle,1))
    data = file.load()

    num = 0
    while num < totle:
        for n in xrange(sx,ex):
#            print "A x %s y %s" % (n,sy)
#            print "file text %s" % data[n,sy]
            new.putpixel((num,0),data[n,sy])
            num +=1
        sy += 1

        for n in xrange(sy,ey):
#            print "B x %s y %s" % (ex-1,n)
            new.putpixel((num,0),data[ex-1,n])
            num +=1
        ex -= 1

        for n in xrange(ex-1,sx-1,-1):   
#            print "C x %s y %s" % (n,ey-1)
            new.putpixel((num,0),data[n,ey-1])
            num +=1
        ey -= 1

        for n in xrange(ey-1,sy-1,-1):   
#            print "C x %s y %s" % (sx,n)
            new.putpixel((num,0),data[sx,n])
            num +=1
        sx += 1
        
    return new


#f2 = Image.open('new.jpg')
#(sizex,sizey) = f2.size

#cc = pic2line(f2,sizex,sizey)
#cc.save('jj.png')


#dd = line2pic(cc,100,100)
#dd.save('newnew.jpg')



#f3 = Image.open('1.jpg')
#(sizex,sizey) = f3.size
#f4 = pic2line(f3,sizex,sizey)
#f4.save('1toline.png')

#f5 = line2pic(f4,sizex,sizey)
#f5.save('cover1.jpg')

