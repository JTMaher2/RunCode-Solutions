#! /usr/bin/env python3

import math

# |0|1|0|
# 0|1|1|0
# |1|2|1|
# 1|3|3|1
# generate Pascal's triangle up to a certain level
def gen_triangle(level):
    if level == 0:
        return [[1]]
    
    tri = [] # array is the # of levels tall, and 3 + the # of levels wide
    num_digits_in_row = level * 2 + 1
    for l in range(0, level + 1):
        tri2 = []
        # total no. of zeros in row is height - dist. from current row to highest row
        
        num_zeros = level * ((level - l) + 1)
        num_zeros_on_each_side = int(num_zeros / 2)

        # pad left side with zeros
        for z in range(0, num_zeros_on_each_side):
            tri2.append(0)
        
        # add middle numbers
        for m in range(0, num_digits_in_row - num_zeros):
            
            if l == 0:
                # if this was the first row, add 1
                tri2.append(1)
            else:
                # find numbers in prev. row that are diagonal from this number
                prev_row = tri[l - 1]
                # there is a previous row, so add the sum of the two diagonal digits
                tri2.append(prev_row[num_zeros_on_each_side + m - 1] + prev_row[num_zeros_on_each_side + m + 1])
            
            # in either case, add a zero after the just-added digit
            #tri2.append(0)

        # pad right side with zeros
        for z in range(0, int(num_zeros_on_each_side)):
            tri2.append(0)

        tri.append(tri2) # add row to triangle grid

    return tri

with open('sample.txt') as file_input:
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