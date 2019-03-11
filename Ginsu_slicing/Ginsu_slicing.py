#!/usr/bin/env python3

import sys
import math
lines = []
with open(sys.argv[1]) as file_input:
    for line in file_input:
        lines.append(line)
    for line_index in range(0, len(lines)):
        line = lines[line_index]
        words = line.rstrip('\n').rstrip(' ').split(' ')
        for word_index in range(0, len(words)):
            word = words[word_index]
            if len(word) > 2 and len(word) % 2 == 0:
                segment_size = len(word) / 2

                segment = ''

                for c in range(0, len(word)):
                    if len(segment) < segment_size:
                        segment += word[c]
                    else:
                        sys.stdout.write(segment[::-1])
                        segment = word[c]
                sys.stdout.write(segment[::-1])
            else:
                segment_size = math.floor(len(word) / 2)

                segment = ''
                num_segments_printed = 0
                middle_printed = False
                for c in range(0, len(word)):
                    if len(segment) < segment_size:
                        segment += word[c]
                    elif num_segments_printed == 0:
                        sys.stdout.write(segment[::-1])
                        num_segments_printed += 1
                        sys.stdout.write(word[c])
                        segment = ''
                    else:
                        sys.stdout.write(segment[::-1])
                        segment = word[c]
                sys.stdout.write(segment[::-1])
            
            if (word_index < len(words) - 1):
                sys.stdout.write(' ')
        if (line_index < len(lines) - 1):
            sys.stdout.write('\n')