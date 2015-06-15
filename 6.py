import urllib2
import zipfile
import re

url = "http://www.pythonchallenge.com/pc/def/channel.zip"
data = urllib2.urlopen(url).read()

file1='ttt.zip'
with open(file1,'wb+') as fzip:
    fzip.write(data)


#dd=re.compile(r'[from|is] (\d+$)')
dd = re.compile(r'(?<=[from|is] )(\d+)')
zf = zipfile.ZipFile(file1,'r')
text=zf.read('readme.txt')
cc = dd.search(text)
while cc:
    #print text
    text = zf.read(cc.group()+'.txt')
    cc = dd.search(text)

print text

dd = re.compile(r'(?<=[from|is] )(\d+)')
zf = zipfile.ZipFile(file1,'r')
text=zf.read('readme.txt')
cc = dd.search(text)
data1=""
while cc:
    #print text
    text = zf.read(cc.group()+'.txt')
    data1 += zf.getinfo(cc.group()+'.txt').comment
    cc = dd.search(text)


print text 
print data1
