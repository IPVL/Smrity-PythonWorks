#! /usr/bin/env python
#users = ['aaa', 'bbb', 'xyz']
#print raw_input('enter your name: ') in users

database = [
['albert', '1234'],
['dilbert', '4242'],
['smith', '7524'],
['jones', '9843']
]
username = raw_input('user name: ')
pin = raw_input('pin code: ')

if [username, pin] in database:
	print 'access granted'
else:
	print 'sorry try again'




