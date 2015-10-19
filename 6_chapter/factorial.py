#! /usr/bin/env python

def factorial(n):
	if n == 1:
		return 1
	else:
		return n*factorial(n-1)

"""
def factorial(n):
	result = n
	for i in range(1,n):
		result *= i
	return result

"""
print factorial(4)