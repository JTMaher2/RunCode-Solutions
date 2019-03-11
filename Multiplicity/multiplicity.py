#!/usr/bin/env python3

import sys
import math

def round_to_precision(strSum):
    dotReached = False
    nonZeroAfterDotReached = False
    for i in range(0, len(strSum)):
        if i == len(strSum) - 1:
            print(strSum)
        elif strSum[i] == '.':
            dotReached = True
        elif strSum[i] != '0' and dotReached:
            nonZeroAfterDotReached = True
        elif strSum[i] == '0' and nonZeroAfterDotReached:
            print(float(strSum[:i]))
            break

with open(sys.argv[1], 'r') as input:
    for line in input:
        product = 0.0
        i = 0
        has_float = False
        for num in line.split(' '):
            if math.floor(float(num)) != float(num):
                has_float = True
            if i > 0:
                product *= float(num)
            else:
                product = float(num)
            i += 1

        if has_float == True:
            round_to_precision(str(product))
        else:
            print(int(product))