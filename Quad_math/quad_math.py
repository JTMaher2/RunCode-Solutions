#!/usr/bin/env python3

import sys
import math

with open(sys.argv[1], 'r') as input:
    for line in input:
        sum = 0
        prev = -1
        num_same = 0
        contains_float = False
        i = 0
        for num in line.split(' '):
            if math.floor(float(num)) != float(num):
                contains_float = True
            sum += float(num)
            if i != 0 and float(num) == prev:
                num_same += 1
            prev = float(num)
            i += 1
        if num_same == len(line.split(' ')) - 1:
            sum *= 4
        if contains_float == True:
            print(sum)
        else:
            print(int(sum))