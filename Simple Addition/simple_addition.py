#!/usr/bin/env python3.6

import sys
import math

with open(sys.argv[1]) as input:
    for row in input:
        sum = float(row.split(' ')[0]) + float(row.split(' ')[1])

        if sum == math.floor(sum):
            print('{:0.0f}'.format(sum))
        else:
            strSum = str(sum)
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