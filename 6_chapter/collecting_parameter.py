#! /usr/bin/env python

def with_stars(**kwds):
	print kwds['name'], 'is', kwds['age'], 'years old'

def without_stars(kwds):
	print kwds['name'], 'is', kwds['age'], 'years old'
	
args = {'name': 'Mr. Gumby', 'age': 42}
with_stars(**args)
without_stars(args)
