#!/usr/bin/env python3.6

import sys

# gets the next highest integer in a series
def searchForNextHighest(ints, origVal, index, end):
    while index < end:
        curVal = int(ints[index])
        if curVal > origVal:
            return curVal
        index += 1
    return -1

with open(sys.argv[1]) as file:
    for row in file:
        parts = row.split(' ')
        origIndex = int(parts[0]) - 1
        ints = parts[1].split(',') # list of ints

        origVal = int(ints[origIndex]) # value that index points to

        nextHighest = -1
        nextHighest = searchForNextHighest(ints, origVal, origIndex + 1, len(ints))

        # if no next highest val was found, and the original index was greater than 0
        if nextHighest == -1 and origIndex > 0:
            nextHighest = searchForNextHighest(ints, origVal, 0, origIndex)

        if nextHighest > -1:
            print(nextHighest)