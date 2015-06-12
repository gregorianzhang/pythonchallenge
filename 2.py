import urllib2

url = "http://www.pythonchallenge.com/pc/def/ocr.html"
aa = urllib2.urlopen(url)
data = aa.read()
num1 = data.find('<!--')
num2 = data[num1+1:].find('<!--')

data1= data[num2+num1:]

bb=""
for x in data1:
    if x.isalpha():
        bb += x

print bb
