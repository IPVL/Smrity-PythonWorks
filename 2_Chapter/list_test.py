#! /usr/bin/env python
a = [1, 2, 3]

print list(reversed(a))
print a

a.reverse()
print a



print "\n\n\n"
b = [4, 5, 6]
print a+b
print a
a = a+b
print a
a.extend(b)
print a


names = ['sss', 'aaa', 'bbb']
print names
del names[2]
print names

mylist2 = list('   world')

print mylist2

mylist2[0] = 'm'
mylist2[1] = 'y'

print mylist2