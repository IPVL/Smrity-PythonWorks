#! /usr/bin/env python
from string import Template
s = Template("It's ${x}tastic!")
print s.substitute(x='slurm')
s = Template('$x, glorious $x!')
print s.substitute(x='slurm')
