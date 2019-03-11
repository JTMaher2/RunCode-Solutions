#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as file_input:
    lines = []
    for line in file_input:
        lines.append(line)
    i = 0
    for line in lines:
        if line == '\n':
            sys.stdout.write(' ')
        else:
            sys.stdout.write(line.rstrip('\n'))
            if i < len(lines) - 1 and lines[i + 1] != '\n':
                sys.stdout.write(' ')
        i += 1