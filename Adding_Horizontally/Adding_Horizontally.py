#!/usr/bin/env python3.6

import sys
import math

def convert_to_num(num):
    float_num = float(num)
    if math.floor(float_num) == float_num:
        return int(num)
    else:
        return float_num

input = []

with open(sys.argv[1]) as fileInput:
    for line in fileInput:
        input.append(convert_to_num(line.rstrip('\n')))

offset = 0

rev_input = input[::-1]

while offset < len(input) / 2:
    if offset < len(input) / 2 - 1:
        sys.stdout.write(str(input[offset] + rev_input[offset]) + ', ')
    else:
        if len(input) % 2 == 0:
            sys.stdout.write(str(input[offset] + rev_input[offset]))
        else:
            sys.stdout.write(str(input[offset]))

    offset += 1