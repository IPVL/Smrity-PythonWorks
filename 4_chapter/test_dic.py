#! /usr/bin/env python
template = '''<html>
<head><title>%(title)s</title></head>
<body>
<h1>%(title)s</h1>
<p>%(text)s</p>
</body>'''
data = {'title': 'My Home Page', 'text': 'Welcome to my home page!'}
print template % data




print '\n\n\n\n\n\n'




people = {
	'Alice': {
	'phone': '2341',
	'addr': 'Foo drive 23'
	},
	'Beth': {
	'phone': '9102',
	'addr': 'Bar street 42'
	},
	'Cecil': {
	'phone': '3158',
	'addr': 'Baz avenue 90'
	}
}

labels = {
'phone': 'phone number',
'addr': 'address'
}


name = raw_input('Name: ')
# Are we looking for a phone number or an address?
request = raw_input('Phone number (p) or address (a)? ')
# Use the correct key:
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'
# Only try to print information if the name is a valid key in
# our dictionary:
if name in people: print "%s's %s is %s." % \
(name, labels[key], people[name][key])



print '\n\n\n\n\n\n'


names = ['lice', 'beth', 'cecil']
numbers = ['213', '342', '132']

print numbers[names.index('cecil')]

items = [('name', 'Gumby'), ('age', 42)]

d = dict(items)
print d