#!/usr/bin/env python
"""Provides a vowel counting function.
"""

def returnVowels(str) :
    vowels = ('a', 'e', 'i', 'o', 'u')
    vowelCount = 0
    for ch in str :
        if ch in vowels:
            # print ch
            vowelCount += 1
    return vowelCount

print returnVowels("vasu")

"""Invokes the test function for current class"""
def main() :
    if __name__ == '__main__':
        test()
    else :
        "Imported Vowel Count v 0.1 by VJ"


def test():
    testInput = ("nil vwls", "Math, science, history, unraveling the"
                 " mysteries, that all started with the big"
                 " bang!", "", "vasujain")
    for test in testInput:
        print returnVowels(test)

main()
