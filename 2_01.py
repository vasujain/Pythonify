#!/usr/bin/env python
"""
Asks the user for her name, then asks for the amount of
money she has. It then asks for half the money.
"""

name = raw_input("Name please: ")
money = raw_input("How much money do you have?")

try:
    moneyInt = float(money)
except ValueError:
    print "Please try again"
else:
    print "%s, give me $%.2f." % (name, (moneyInt/2))
