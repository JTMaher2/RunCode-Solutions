#!/usr/bin/env python3.6

import sys

with open(sys.argv[1]) as input:
    for row in input:
        chars = row.split(' ')
        for c in chars:
            sys.stdout.write(chr(int(c)))