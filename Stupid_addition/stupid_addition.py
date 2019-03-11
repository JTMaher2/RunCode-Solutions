#!/usr/bin/env python3.6

import sys
import math

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

with open(sys.argv[1]) as shafile:
    for row in shafile:
        if ' ' in row:
            num1 = row.split(' ')[0]
            num2 = row.split(' ')[1].rstrip('\n')

            if isfloat(num1) and isfloat(num2):
                sum = float(num1) + float(num2)

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