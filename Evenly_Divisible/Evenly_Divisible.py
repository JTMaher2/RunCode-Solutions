#!/usr/bin/env python3.6

import sys
import math

with open(sys.argv[1]) as file:
    output = ''
    for row in file:
        dividendMax = row.split(' ')
        dividend = float(dividendMax[0])
        maxVal = math.floor(float(dividendMax[1]))

        # if dividend is non-zero
        if dividend != 0:
            for i in range(1, maxVal + 1):
                quotient = round(i / dividend, 13)
                if quotient == math.floor(quotient): # if i can be evenly divided by dividend
                    output += str(i) + '\n'
        output += '\n'
    sys.stdout.write(output.rstrip('\n'))