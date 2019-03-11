#!/usr/bin/env python3

import sys
import math

master_list = []

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_float(n):
    if float(n) == math.floor(float(n)):
        return False
    else:
        return True

with open(sys.argv[1]) as file_input:
    for line in file_input:
        line = line.rstrip('\n')
        split_line = line.split(',')

        if len(split_line) == 1:
            if is_number(split_line[0]):
                if is_float(split_line[0]):
                    master_list.append(float(split_line[0]))
                else:
                    master_list.append(int(split_line[0]))
        else:
            sub_list = []
            for value in split_line:
                if is_number(value):
                    if is_float(value):
                        sub_list.append(float(value))
                    else:
                        sub_list.append(int(value))
            if len(sub_list) > 0:
                master_list.append(sub_list)

if len(master_list) > 0:
    print(master_list)