#!/usr/bin/env python
""" Ask the user for exactly 5 words, one at a time. After
each word is collected from the user, print it only if it
is not a duplicate of a word already collected.
"""


def WordDoesNotExists(list, word):
    for l in list:
        if cmp(word, l) == 0:
            return False
    return True


def insertWords(num):
    list = []
    for i in range(num):
        word = raw_input("Enter a word:")
        if WordDoesNotExists(list, word) == True:
            print word
        list.append(word)
    return list


print insertWords(5) #prints final list

