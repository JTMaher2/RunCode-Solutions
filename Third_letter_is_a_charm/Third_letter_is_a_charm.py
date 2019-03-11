#!/usr/bin/env python3.6

import sys

with open(sys.argv[1]) as file:
    for row in file:
        output = ''
        for word in row.split(' '):
            if len(word) > 2:
                output += word[1:3] + word[0] + word[3:len(word)].rstrip('\n') + ' '
            else:
                output += word.rstrip('\n') + ' '
        print(output.rstrip(' '))