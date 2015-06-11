#!/usr/bin/env python
"""Prints the decimal equivalent of a binary string."""


binaryString = "110110011"
decimalInt = 0
counter = 0
for ch in binaryString :
    if ch not in "01":
        print "invalid input"
        break
else:
    for ch in reversed(binaryString) :
        decimalInt += pow(2, counter) * int(ch)
        # print int(ch), counter, pow(2, counter), bin
        counter = counter +1
    print "decimal value is", decimalInt
