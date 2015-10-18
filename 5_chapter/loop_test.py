#! /usr/bin/env python

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
letterGirls = {}
for girl in girls:
	letterGirls.setdefault(girl[0], []).append(girl)
print [b+'+'+g for b in boys for g in letterGirls[b[0]]]


"""
girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
print [b+'+'+g for b in boys for g in girls if b[0] == g[0]]




strings = ['xxx', 'aaa', 'bbb', 'xxxx', 'xxx']
print strings


index = 0
for string in strings:
	if 'xxx' in string:
		strings[index] = '[censored]'
	index += 1



for string in strings:
	if 'xxx' in string:
		index = strings.index(string) # Search for the string in the list of strings
		strings[index] = '[censored]'
print strings


names = ['anne', 'beth', 'george', 'damon', 'abir']
ages = [12, 45, 32, 102, 5345]
print zip(names, ages)

names = ['anne', 'beth', 'george', 'damon', 'abir']
ages = [12, 45, 32, 102, 5345]
print range(len(names))
for i in range(len(names)):
	print names[i], 'is', ages[i], 'years old'



d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
	print key, 'corresponds to', d[key]


for i in range(0, 20):
	print i
for i in xrange(0, 20):
	print i

for num in range(5, 7):
	print num
words = ['this', 'is', 'an', 'ex', 'parrot']
for word in words:
	print word,
print ""
var = 1
while var < 5:
	print var
	var += 1
"""