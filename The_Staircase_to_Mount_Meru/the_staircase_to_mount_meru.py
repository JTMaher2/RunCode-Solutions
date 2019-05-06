#!/usr/bin/env python3

import sys
import math

# generate Pascal's triangle up to a certain level
def gen_triangle(level):
    # calculate triangle width based on level
    num_digits_in_row = (level + 1) * 2 + 1
    tri = [] # array is the # of levels tall, and 3 + the # of levels wide
    
    for l in range(0, level + 1):
        if l == 0:
            # row is simply a bunch of 0s, with a 1 in the middle
            row = []
            for i in range(0, num_digits_in_row):
                if (i != math.floor(num_digits_in_row / 2)):
                    row.append(0)
                else:
                    row.append(1)
        else:
            # level > 0
            row = []
            prev_row = tri[l - 1]

            for i in range(0, num_digits_in_row):
                row.append(prev_row[i - 1] + prev_row[i])

            row.append(0) # add trailing 0

        tri.append(row) # add row to triangle grid

    return tri

with open(sys.argv[1]) as file_input:
    for line in file_input:
        parts = line.split(' ')
        level = int(parts[0])
        col = int(parts[1].rstrip('\n'))
        tri = gen_triangle(level)
        non_zero_digits_in_col = 0
        for i in range(0, len(tri[level])):
            if tri[level][i] != 0:
                non_zero_digits_in_col += 1
                if non_zero_digits_in_col == col + 1:
                    print(tri[level][i])
                    break