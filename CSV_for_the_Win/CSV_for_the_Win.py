#!/usr/bin/env python3.6

import sys

with open(sys.argv[1]) as file:
    for line in file:
        sum = 0
        num_decimal_places_all = []
        for num in line.split(','):
            if '.' in num:
                num_decimal_places = len(num[num.index('.') + 1:len(num)])
                num = float(num)
            else:
                num_decimal_places = 0
                num = int(num)
            num_decimal_places_all.append(num_decimal_places)
            
            sum += num
        print(round(sum, max(num_decimal_places_all)))