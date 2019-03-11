#!/usr/bin/env python3.6

import sys

output = ''

with open(sys.argv[1]) as fileInput:
    for line in fileInput:
        output += line.rstrip('\n')[::-1]

print(output)