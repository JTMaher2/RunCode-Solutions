#!/usr/bin/env python3.6

import sys

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def convert_to_ip(num):
    if num < 16777216:
        return str(num)

    ip = ''
    first = int(num / 16777216) & 255
    second = int(num / 65536) & 255
    third = int(num / 256) & 255
    fourth = num & 255

    ip = str(first) + '.' + str(second) + '.' + str(third) + '.' + str(fourth)

    return ip

with open(sys.argv[1]) as fileInput:
    for line in fileInput:
        split_line = line.split(' ')

        for i in range(0, len(split_line)):
            trimmed_word = split_line[i].rstrip('\n')
            if is_integer(trimmed_word):
                sys.stdout.write(convert_to_ip(int(trimmed_word)))
            else:
                sys.stdout.write(trimmed_word)

            if i < len(split_line) - 1:
                sys.stdout.write(' ')
            else:
                sys.stdout.write('\n')