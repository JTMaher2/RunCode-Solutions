#!/usr/bin/env python3.6

import sys

with open(sys.argv[1]) as file:
    for row in file:
        sum = 0
        for num in row.split(' '):
            sum += int(num)
            sum += 1
        print(sum)