#!/usr/bin/env python
"""I'm thinking-of-a-number game. """

userNum = raw_input("Think of a num b/w 1 to 10 and i will guess it.")

upper = 10
lower = 0
guessCount = 0
while lower != 10 or upper != 0:
    mid = (upper+lower)/2
    print "Is your num %d\n" % mid
    ans = raw_input("""Please press:
        'y' for yes
        'n' for no
        """)    
    guessCount = guessCount + 1
    if ans == 'n':
        ans2 = raw_input("""No? Then please press:
                             'h' if %d is higher
                             'l' if %d is lower\n"""
                         % (mid, mid))
        if ans2 == 'h':
            upper = mid
        elif(ans2 == 'l'):
            lower = mid
    elif ans == 'y':
        print "Hurray ! Only %d guesses" % (guessCount)
        break;
    else:
        print "Wrong input"
