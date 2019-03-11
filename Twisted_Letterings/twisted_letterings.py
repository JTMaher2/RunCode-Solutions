#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as input:
    for line in input:
        sys.stdout.write('twisted: ')
        i = 0
        for word in line.split(' '):
            word = word.strip('\n')
            if i < len(line.split(' ')) - 1:
                sys.stdout.write(word + ' ')
            else:
                sys.stdout.write(word + '\n')
            i += 1
        sys.stdout.write('plain  : ')
        i = 0
        for word in line.split(' '):
            word = word.strip('\n')
            first = ''
            last = ''
            j = 0
            for letter in word:
                if j % 2 == 0:
                    last += letter
                else:
                    first += letter
                j += 1
            last = last[::-1]
            if i < len(line.split(' ')) - 1:
                sys.stdout.write(first + last + ' ')
            else:
                sys.stdout.write(first + last + '\n')
            i += 1
