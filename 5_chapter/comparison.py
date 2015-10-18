#! /usr/bin/env python
print [1, [2, 3]] < [[0, 0], 0]
print [1, [2, 3]] < [[1, 0], 0]
print [1, [2, 3]] < [[1, 1], 0]
print [1, [2, 3]] < [[1, 1], 3]
print [1, [2, 3]] < [[1, 2], 3]
print [1, 2] < [1, 2]
print [1, 2] > [1, 2]

print "alpha" < "beta"
print "alpha" < "Beta"