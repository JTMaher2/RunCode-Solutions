#!/usr/bin/env python3

import sys
import itertools

with open(sys.argv[1]) as file_input:
    for line in file_input:
        line_list = line.split(',')
        for perm in itertools.permutations(line_list):
            print(perm)