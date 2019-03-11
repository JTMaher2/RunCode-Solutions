#!/usr/bin/env python3

import sys
import operator

years = []

def is_beg_of_cent(year):
    beg_of_cent = True
    for i in range(0, len(year)):
        if len(year) > 2 and i > len(year) - 2 - 1 and int(year[i]) != 0:
            beg_of_cent = False
            break

    return beg_of_cent

def is_new_mil(year):
    year = year[len(year) - 4:len(year)]
    new_mil = True
    for i in range(0, len(year) - 1):
        if i > 0 and year[i] != '0':
            new_mil = False
            break
    return new_mil

def is_leap_year(year):
    if int(year) % 4 == 0:
        if len(year) > 3 and is_new_mil(year):
            return True
        elif not is_beg_of_cent(year):
            return True
    else:
        return False

with open(sys.argv[1]) as file_input:
    for line in file_input:
        for year in line.split(' '):
            if year.find('-') == -1:
                cur_year = [int(year.rstrip('\n'))]
                if is_leap_year(year.rstrip('\n')):
                    cur_year.append('True')
                else:
                    cur_year.append('False')
                years.append(cur_year)
            else:
                parts = year.split('-')
                for i in range(int(parts[0]), int(parts[1].rstrip('\n')) + 1):
                    cur_year = [i]
                    if is_leap_year(str(i)):
                        cur_year.append('True')
                    else:
                        cur_year.append('False')
                    years.append(cur_year)

sorted_years = sorted(years, key=operator.itemgetter(0))

for year in sorted_years:
    print(str(year[0]) + ': ' + year[1])
