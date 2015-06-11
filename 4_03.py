#!/usr/bin/env python
"""Sorts name strings by last name."""


def sortList(names):
    # return sorted(names)  # Sort by First Name
    return sorted(names, key = lastName)

def lastName(str):
    parts = str.split()
    # print parts[-1]
    return parts[-1]

def printList(list):
    for l in list:
        parts = l.split()
        partsSize = len(parts)
        print parts[partsSize-1], ",",
        parts2 = parts[:-1]
        for i in range(len(parts2)) :
            print parts2[i],
        print ""

def main():
    nameList = ["Jack Sparrow", "George Washington", 
             "Tiny Sparrow", "Jean Ann Kennedy"]
    nameListSorted = sortList(nameList)
    printList(nameListSorted)

main()



        
