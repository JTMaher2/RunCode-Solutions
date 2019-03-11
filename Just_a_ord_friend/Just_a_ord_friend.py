#!/usr/bin/env python3

import sys
import string

sum = 0

valid_chars = set(string.ascii_letters.replace("_", ""))

with open(sys.argv[1]) as fileInput:
    for line in fileInput:
        for c in line:
            if c in valid_chars:
                sum += ord(c)

print(sum)