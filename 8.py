import urllib2
import re
import bz2

url = "http://www.pythonchallenge.com/pc/def/integrity.html"

data = urllib2.urlopen(url).read()

un=re.compile(r"(?<=un: )(.+)")
pw=re.compile(r"(?<=pw: )(.+)")
tt = un.search(data)
user = bz2.decompress(eval(tt.group()))
dd = pw.search(data)
passwd = bz2.decompress(eval(dd.group()))
#print user
print "user %s and password %s" % (user,passwd)


