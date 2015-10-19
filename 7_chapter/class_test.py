#! /usr/bin/env python
class Person:

	varname = 5
	_varname = 7
	__varname = 55
	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

	def greet(self):
		print "Hello, world! I'm %s." % self.name

foo = Person()
"""
bar = Person()

foo.setName("sfasdf")
print foo.getName()
print foo.name

print foo.varname
print foo._varname
"""
print foo._Person__varname
