#! /usr/bin/env python

def square(num):
	'to calculate square of a number'
	return num*num

num = raw_input("enter a number :")
num = int(num)
print square(num)