#! /usr/bin/env python
from copy import deepcopy
d = {}
d['names'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['names'].append('Clive')
print c
#{'names': ['Alfred', 'Bertrand', 'Clive']}
print dc
#{'names': ['Alfred', 'Bertrand']}




print '\n\n\n\n\n'
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
y['username'] = 'mlh'
y['machines'].remove('bar')
print y
#{'username': 'mlh', 'machines': ['foo', 'baz']}
print x
#{'username': 'admin', 'machines': ['foo', 'baz']}