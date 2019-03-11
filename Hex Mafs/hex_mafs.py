#!/usr/bin/env python3.6

import sys

with open(sys.argv[1]) as input:
    for row in input:
        sum = 0
        for num in row.split(' '):
            sum += int(num, 0)
        print(sum)