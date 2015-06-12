#!/usr/bin/env python
"""
Asks the user for a number to multiply by itself,
and asks the user for the number of digits beyond the decimal
point to display, and gives the answer.
"""

num = raw_input("Number to square please:")
try:
    numFloat = float(num)
except ValueError:
    print "Pls try again"
else:
    digitsToRight = raw_input("How many digits to right of the decimal place you would like to have displayed?")
    try:
        digitsToRightInt = int(digitsToRight)
    except ValueError:
        print "Pls try again"
    else:
        print "%.2f squared is %.*f." %(numFloat, digitsToRightInt, pow(numFloat, 2))

