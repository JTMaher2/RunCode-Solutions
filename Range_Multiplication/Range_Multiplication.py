#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as file_input:
    for line in file_input:
        min_num = 0
        mid_num = 0
        max_num = 0
        num_list = []
        nums = line.split(' ')
        for i in range(0, len(nums)):
            if i == 0:
                min_num = int(nums[i])
            elif i == 1:
                mid_num = int(nums[i])
            else:
                max_num = int(nums[i])
            
            for j in range(min_num, max_num):
                if j % min_num == 0 and j % mid_num == 0:
                    num_list.append(j)

        print(num_list)