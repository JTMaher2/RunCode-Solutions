#!/usr/bin/env python3

import sys
import math

with open(sys.argv[1]) as file_input:
    for line in file_input:
        buffer = ''
        message = ''
        i = 0
        for c in range(0, len(line)):
            buffer += line[c]
            
            if c < len(line) - 1 and line[c + 1] == '0' and line[c + 2] == 'x':
                message += chr(int(math.ceil(math.sqrt(int(buffer, 16)))))
                buffer = ''

            i += 1
        message += chr(int(math.ceil(math.sqrt(int(buffer, 16)))))
        print(message)