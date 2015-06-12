#!/usr/bin/env python

# 201 Zeroes
print [[0] for x in range(202)]

# List of strings till 10
print [str(x) for x in range(10)]

# List of strings till 10 with +
print ' + '.join([str(x) for x in range(10)])

# Append last name
print ', '. join(["%s Wu" % name for name in sorted(("An", "Li", "Bo", "On"))])

# Math Manipulations
print "\n".join(["%6.1f" % (x*20+0.1) for x in range(20)])

