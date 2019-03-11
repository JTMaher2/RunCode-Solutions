#!/usr/bin/env python3

import sys
import operator
import csv

path = sys.argv[1]
reader = csv.reader(open(path), delimiter=',')

rows = []
rows_that_begin_with_the = []

i = 0
for row in reader:
    if i > 0:
        rows.append(row)
    i += 1

rows_with_same_dates = [] # array of arrays, where each sub-array is a unique date

for row in rows:
    row_date = row[2]
    num_lists_not_in = 0 # the num of sub-arrays in rows_with_same_dates that this row's date is not in
    for row_list in rows_with_same_dates:
        if row[2] == row_list[0][2]: # if this sub-array has rows with same date as current row
            row_list.append(row)
        else:
            num_lists_not_in += 1 # increment the num. of sub-arrays that this row's date is not in

    if num_lists_not_in == len(rows_with_same_dates):
        # if the num of sub-arrays that this row's date is not in is equal to the num of sub-arrays in rows_with_same_dates, make a new sub-array for this row
        rows_with_same_dates.append([row])

# sort each group of rows with same date by name
for r in range(0, len(rows_with_same_dates)):
    sorted_sub_array = sorted(rows_with_same_dates[r], key=operator.itemgetter(0)) # sort by name
    rows_with_same_dates[r] = sorted_sub_array

# combine all groups of rows with same date
all_sorted_rows = []
for r in rows_with_same_dates:
    for s in r:
        all_sorted_rows.append(s)

# sort all groups of sorted-by-name rows by date
sortedlist = sorted(all_sorted_rows, key=operator.itemgetter(2))

name_char_limit = 15

for row in range(0, len(sortedlist)):
    if (len(sortedlist[row][0]) < name_char_limit):
        while (len(sortedlist[row][0]) < name_char_limit):
            sortedlist[row][0] = ' ' + sortedlist[row][0]
    elif (len(sortedlist[row][0]) > name_char_limit - 1):
        sortedlist[row][0] = sortedlist[row][0][0:name_char_limit - 1] + '~'

    print(sortedlist[row][0] + ' ' + sortedlist[row][2])