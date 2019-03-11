#!/usr/bin/env python3

import sys
import math

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

with open('input.txt') as file_input:
    for line in file_input:
        cur_list = []
        line = line.lstrip('[').rstrip('\n').rstrip(']')

        for num in line.split(','):
            parsed_num = num.strip(' ')
            if is_float(parsed_num):
                float_num = float(parsed_num)

                if str(float_num) == str(parsed_num):
                    cur_list.append(float_num)
                else:
                    cur_list.append(int(float_num))
        
        print(cur_list)