#!/usr/bin/env python3.6

import sys

with open(sys.argv[1]) as file:
    for row in file:
        num1 = int(row.split(' ')[0])
        num2 = int(row.split(' ')[1])
        output = ''
        if (num1 < num2):
            for num in range(int(num1), int(num2) + 1):
                if num % 7 == 0 and num % 5 != 0:
                    output += str(num) + ','
        else:
            for num in range(int(num2), int(num1) + 1):
                if num % 7 == 0 and num % 5 != 0:
                    output += str(num) + ','

        print(output.rstrip(','))