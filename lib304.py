#!/usr/bin/env python
"""Write a DoBreakfast function that takes five arguments:
meat, eggs, potatos, toast, and beverage.  The default
meat is bacon, eggs are over easy, potatos is hash browns,
toast is white, and beverage is coffee.

The function prints:

Here is your bacon and scrambled eggs with home fries
and rye toast.  Can I bring you more milk?

Call it at least 3 different times, scrambling the arguments.
"""


def DoBreakfast(meat = "bacon", eggs = "over easy", potato = "hash brown", toast = "white", beverage = "coffee"):
    print "Here is your %s and %s eggs wih %s and %s toast. Can i bring you more %s?" %(meat, eggs, potato, toast, beverage)

DoBreakfast()
DoBreakfast("ham", "white", "boiled", "brown", "juice")
DoBreakfast(beverage = "vodka", eggs = "over easy", toast = "burnt", potato = "hash brown")
DoBreakfast(beverage = "tea", eggs = "hard")
