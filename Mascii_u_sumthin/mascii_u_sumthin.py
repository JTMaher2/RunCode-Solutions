#!/usr/bin/env python3.6

import sys
import binascii

with open(sys.argv[1]) as input:
    for row in input:
        nums = row.split(' ')
        for num in nums:
            if 'x' in num: # hexadecimal
                sys.stdout.write(chr(int(num, 0)))
            elif 'b' in num: # binary
                sys.stdout.write(chr(int(num, 2)))
            elif num[0] == '0': # octal
                sys.stdout.write(chr(int(num, 8)))
            else: # decimal
                sys.stdout.write(chr(int(num)))