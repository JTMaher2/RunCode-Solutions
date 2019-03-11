#!/usr/bin/env python3.6

import sys

with open(sys.argv[1]) as file:
    for row in file:
        row = row.rstrip('\n') # remove newline
        if row == row[::-1]:
            print('True')
        else:
            print('False')
