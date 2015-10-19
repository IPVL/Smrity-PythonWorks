#! /usr/bin/env python
class Filter:
	def init(self):
		self.blocked = []
	def filter(self, sequence):
		return [x for x in sequence if x not in self.blocked]


class SPAMFilter(Filter): # SPAMFilter is a subclass of Filter
	def init(self): # Overrides init method from Filter superclass
		self.blocked = ['SPAM']

'''
f = Filter()
f.init
print f.filter([1, 2, 3])
'''
s = SPAMFilter()
s.init()
print s.filter(['SPAM', 'SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM'])