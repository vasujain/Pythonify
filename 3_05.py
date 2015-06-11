#!/usr/bin/env python
"""Coin flip Experiments, continued. """

from __future__ import division
import random


def flipCoin() :
    flip = random.choice(("heads", "tails"))
    return flip

def getHeads(target = 1):
    numHeads = 0
    numFlips = 0
    flippy = False
    while(flippy != True):
        flipResult = flipCoin()
        numFlips += 1
        print flipResult
        if(flipResult == "heads"):
            numHeads += 1
            if(numHeads == target):
                print "Number of flips %s to get continuous %s heads" %(numFlips, numHeads)
                flippy = True
        else:
            numHeads = 0

def getHeadsReport(target = 1):
    numHeads = 0
    numFlips = 0
    flippy = False
    while(flippy != True):
        flipResult = flipCoin()
        numFlips += 1
        #print flipResult
        if(flipResult == "heads"):
            numHeads += 1
            if(numHeads == target):
                print "Number of flips %s to get continuous %s heads" %(numFlips, numHeads)
                flippy = True
        else:
            numHeads = 0
    return(numFlips, numHeads)

#getHeads(5)


def NumOfExperiments(num):
    globalFlipCount = 0
    for i in range(0,num):
        report = getHeadsReport(3)
        globalFlipCount += report[0]
        #print report, globalFlipCount
        print "Toal flips for %d flips is %d, avg is %.2f chances for a heads" % (num *3, globalFlipCount, globalFlipCount/(num * 3)) 

NumOfExperiments(4)

