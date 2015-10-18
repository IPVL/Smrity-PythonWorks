#! /usr/bin/env python

from string import maketrans   # Required to call maketrans function.

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

str = "this is string example....wow!!!";
print str.translate(trantab)



print '            this            is a test         '.strip()
seq = ['1', '2', '3']
plus = '+'
print plus.join(seq)



format = "Pi : %.6f"
from math import pi
print format % pi


#format = "hi, %s, how are you?"
#names = raw_input("Please enter your name: ");
#print format % names
