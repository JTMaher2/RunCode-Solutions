#!/usr/bin/env python3

import sys
import operator

with open(sys.argv[1]) as file_input:
    lower_range = sys.argv[2]
    upper_range = sys.argv[3]

    lines = []
    sals = []
    i = 0
    for line in file_input:
        line = line.strip('\n').strip(' ')
        split_line = line.split(' ')
        full_sal = split_line[len(split_line) - 1]
        sal = int(full_sal[1:len(full_sal)])
        if sal >= int(lower_range) and sal <= int(upper_range):
            sals.append([i, sal])
        lines.append([i, line])
        i += 1

sorted_sals = sorted(sals, key=operator.itemgetter(1))

for sal in range(0, len(sorted_sals)):
    print(lines[sorted_sals[sal][0]][1])