#!/usr/bin/env python
"""uses local imports"""

import vcount, sys

def vowelCounting():
    # str = raw_input("Enter a string ")
    sys.stdout.write("Enter a String: ")
    str = sys.stdin.readline()
    if str == '\n':
        sys.stderr.write("Please enter correct input")
    else:
        print vcount.returnVowels(str)

def main():
    vowelCounting()

main()
