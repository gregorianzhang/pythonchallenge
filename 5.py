import urllib2
import pickle
import sys

url = "http://www.pythonchallenge.com/pc/def/banner.p"
aa = urllib2.urlopen(url)
data = aa.read()


data2 = pickle.loads(data)
#print data2

for x in data2:
    for y in x:
	sys.stdout.write(y[0] * y[1])
    print ""


for x in data2:
    print ("".join([y[0] * y[1] for y in x]))
