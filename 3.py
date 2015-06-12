import urllib2
import re

url = "http://www.pythonchallenge.com/pc/def/equality.html"

aa= urllib2.urlopen(url)
data=aa.read()
num = data.find('<!--')
data1 = data[num:]

#dd=re.compile(r'[A-Z]{3}([a-z])[A-Z]{3}')
dd=re.compile(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')
tt=""
#print data1
for x in data1.split('\n'):
    #print x
    #print "-" * 30
    cc=dd.search(x)
    if cc:
        tt += cc.groups()[0]
        print x

print tt

