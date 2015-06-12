#!/usr/bin/env python
"""Produces a christmas tree pattern of stars."""

ch = "*"
bl = " "

for i in range(10):
    print bl*(9-i),
    print ch*(2*i -1),
    print bl*(9-1)



#9 bl 1 star 9 bl
#8 bl 3 star 8 bl
#7 bl 5 star 7 bl
