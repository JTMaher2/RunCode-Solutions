#!/usr/bin/env python3.6

import sys

with open(sys.argv[1]) as file:
    output = ''
    for row in file:
        sentences = row.split('.')

        for sentence in sentences:
            output += sentence.lstrip(' ').split(' ')[0] + ' '
    
    print(output.rstrip(' '))