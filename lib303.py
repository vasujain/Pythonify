#!/usr/bin/env python
""" Write a function that returns a total cost from the 
sales price and sales tax.  The default value for the 
tax rate should be 8.25%.
"""

def totalCost(price, taxRate = .0825):
    return price * (1 + taxRate)

def main() :
    for i in range(500, 1000, 100) :
        print totalCost(i), totalCost(i, .095)

main()
