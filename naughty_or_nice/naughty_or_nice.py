#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as input:
    niceList = 0
    naughtyList = 0
    for line in input:
        goodBadReached = False
        goodBad = ''

        for ch in line:
            if goodBadReached == False:
                if ch == '-' or ch == ':':
                    goodBadReached = True
            else:
                goodBad += ch

        goodBad = goodBad.strip()

        if goodBad == 'good':
            niceList += 1
        else:
            naughtyList += 1
    
    print('Naughty list has ' + str(naughtyList) + ' people!')
    print('Nice list has ' + str(niceList) + ' people!')