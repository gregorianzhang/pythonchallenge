import urllib2
import re
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=63579"

baseurl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
aa = urllib2.urlopen(url)
data = aa.read()

dd=re.compile(r'(\d+)')
cc=dd.search(data)

while cc:
	num = cc.groups()[0]
	url1 = baseurl+num
	aa = urllib2.urlopen(url1)
	data = aa.read()
	cc=dd.search(data)
	print num
print data
