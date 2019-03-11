#!/usr/bin/env python3

import sys

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

with open(sys.argv[1]) as file_input:
    for line in file_input:
        start_stop = line.split(' ')
        first = int(start_stop[0])
        last = int(start_stop[1])
        sum = 0
        
        for i in range(first, last):
            fib_num = fib(i)
            if fib_num % 2 != 0:
                sum += fib_num

        print(sum)