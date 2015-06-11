#!/usr/bin/env python
"""A coin flipping emulation. """

import random

def flipcoin() :
    flip = random.choice(("heads", "tails"))
    print flip

def test():
    for i in range(10):
        flipcoin()

test()
