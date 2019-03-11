#!/usr/bin/env python3.6

import sys

with open(sys.argv[1]) as input:
    for row in input:
        i = 0
        built_str = ''
        j = 0
        while j < len(row):
            if i < 8:
                built_str += row[j]
                i += 1
                j += 1
            else:
                sys.stdout.write(chr(int(built_str, 2)))
                built_str = ''
                i = 0
        sys.stdout.write(chr(int(built_str, 2)))