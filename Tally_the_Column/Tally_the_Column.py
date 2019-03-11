#!/usr/bin/env python3

import sys
import math

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

sums = []

with open(sys.argv[1]) as file_input:
    lines = []
    for line in file_input:
        lines.append(line)
    for l in range(0, len(lines)):
        split_line = lines[l].split(',')
        if l == 0:
            for data in range(0, len(split_line)):
                sums.append(0)
            sys.stdout.write(lines[l])
        else:
            for data in range(0, len(split_line)):
                if is_float(split_line[data]):
                    sums[data] += float(split_line[data])
    for s in range(0, len(sums)):
        cur_sum = sums[s]

        if cur_sum == math.floor(cur_sum):
            cur_sum = int(cur_sum)
        else:
            cur_sum = "{0:.9f}".format(cur_sum)
        sys.stdout.write(str(cur_sum).rstrip('0'))
        if s < len(sums) - 1:
            sys.stdout.write(',')