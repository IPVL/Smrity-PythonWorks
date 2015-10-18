#! /usr/bin/env python
x = [1, 2, 3]
y = [2, 4]
print x is not y
del x[2]
print x
y[1] = 1
y.reverse()
print y
print x
print x == y
print x is y
"""
x = y = [1, 2, 3]
z = [1, 2, 3]
print x == y
print x == z
print x is y
print x is z


print "\n\n\n\n\n"
print "foo" == "foo"
print "foo" == "bar"
name = raw_input("name :")
if name.endswith('ty'):
	print "hello, " + name
else:
	print "wrong one!"
print bool()
"""