#! /usr/bin/env python
def fibs(num):
	result = [0, 1]
	for i in range(num-2):
		result.append(result[-2] + result[-1])
	return result
num = raw_input("enter a number :")
num = int(num)
print fibs(num)
"""
fibs = [0, 1]
num = input('How many Fibonacci numbers do you want? ')
for i in range(num-2):
	fibs.append(fibs[-2] + fibs[-1])
print fibs


fibs = [0, 1]
for i in range(8):
	fibs.append(fibs[-2] + fibs[-1])
print fibs

"""