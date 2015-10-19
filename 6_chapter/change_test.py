#! /usr/bin/env python
#local, global test
def change(names):
	names[0] = 'sss' #this names is local variable

names = ['aaa', 'bbb'] #global variable
change(names)
print names

#because n and names are differnt variable and n just holding the value of name
#here n and name are not identical, they are similar
def try_to_change(n):
	n = 'Mr. Gumby'

name = 'Mrs. Entity'
try_to_change(name)
print name

#because n and names refer to the same list, so any change in any of them will affect other
#here n and names are identical
def change(n):
	n[0] = 'Mr. Gumby'

names = ['Mrs. Entity', 'Mrs. Thing']
change(names)
print names
