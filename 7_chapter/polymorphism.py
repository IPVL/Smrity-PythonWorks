#! /usr/bin/env python

class Polymorphism:
    """
	This class is an example of polymorphism  
    """	
    
    #def run_account(self, *args):
    def run_account(self, *args):
	"""polymorphism example in method overloading
	"""
	print" ".join(args)

# creating instance of a class, create an object obj of a class Ploymorphism
obj = Polymorphism()

# passing parameter to a class
obj.run_account("one")
obj.run_account("one", "two")
obj.run_account("one", "two", "three")

"""
print 'abcada'.count('a')
print [1, 3, 4, 2, 2, 1, 2].count(1)
"""