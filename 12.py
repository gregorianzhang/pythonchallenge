import Image
import urllib2
import base64

#url="http://www.pythonchallenge.com/pc/return/evil1.jpg"

#auth="huge:file"
#password=base64.b64encode(auth)
#tt="Basic "+password
#req = urllib2.Request(url)
#req.add_header('Authorization',tt)
#data = urllib2.urlopen(req).read()

#with open('evil1.jpg','wb') as f:
#    f.write(data)

with open('evil2.gfx','rb') as f:
    data=f.read()


print len(data)
f1 = open('1.jpg','wb')
f2 = open('2.jpg','wb')
f3 = open('3.jpg','wb')
f4 = open('4.jpg','wb')
f5 = open('5.jpg','wb')

for n,x in enumerate(data):
    if str(n)[-1] =='0' or str(n)[-1] == '5':
        f1.write(x)
    if str(n)[-1] =='1' or str(n)[-1] == '6':
        f2.write(x)
    if str(n)[-1] =='2' or str(n)[-1] == '7':
        f3.write(x)
    if str(n)[-1] =='3' or str(n)[-1] == '8':
        f4.write(x)
    if str(n)[-1] =='4' or str(n)[-1] == '9':
        f5.write(x)

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()

for i in range(5):
    fobj = open('TT%d.jpg' % i, 'wb')
    fobj.write(data[i::5])
    fobj.close()
