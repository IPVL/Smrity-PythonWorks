#! /usr/bin/env python
class Class:
	def method(self):
		print 'I have a self!'
def function():
	print "I don't..."

instance = Class()
"""
instance.method()

instance.method = function
instance.method()
"""
function()

function = instance.method
function