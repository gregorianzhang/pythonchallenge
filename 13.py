import xmlrpclib

bb =  xmlrpclib.Server('http://www.pythonchallenge.com/pc/phonebook.php')

cc=bb.phone('Bert')
print cc
