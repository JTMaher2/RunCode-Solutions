#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as file_input:
    for line in file_input:
        num_zeroes = 0

        line = line.rstrip('\n')

        if line != ' ':
            if len(line) > 1:
                for i in range(0, len(line)):
                    if line[i] == '0':
                        num_zeroes += 1
                    elif line[i] == '1' and num_zeroes > 0:
                        num_zeroes -= 1
                if num_zeroes == 0:
                    print('True')
                else:
                    print('False')
            else:
                print('False')