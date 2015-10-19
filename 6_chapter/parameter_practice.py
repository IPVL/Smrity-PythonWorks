#! /usr/bin/env python
def story(**kwds):
	return 'Once upon a time, there was a ' \
			'%(job)s called %(name)s.' % kwds

def power(x, y, *others):
	if others:
		print 'Received redundant parameters:', others
	return pow(x, y)

def interval(start, stop=None, step=1):
	'Imitates range() for step > 0'
	if stop is None: # If the stop is not supplied...
		start, stop = 0, start # shuffle the parameters
	result = []
	i = start
	while i < stop:
		result.append(i)
		i += step
	return result

"""
print story(job='king', name='gumby')
print story(name='Sir Robin', job='brave knight')

params = {'job': 'language', 'name': 'Python'}
print story(**params)
del params['job']
#del params['job'] without deleting job from params, new value can't be assigned
print story(job='stroke of genius', **params)
"""
print interval(3, 7)
print power(*interval(3,7))

params = (5,) * 2
params = [2, 3]
print power(*params)