#!/usr/bin/env python3.6

import sys

with open(sys.argv[1]) as file:
    i = 0
    words = []
    for row in file:
        row = row.rstrip('\n')
        output = ''
        split_row = row.split(' ')
        for word in split_row:
            words.append(word)
    
    for word in words:
        if i % 2 == 0:
            print(word)
        else:
            print(word[::-1])
        i += 1