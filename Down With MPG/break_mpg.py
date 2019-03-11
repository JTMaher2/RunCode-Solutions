#!/usr/bin/env python3.6

import csv
import os.path
import sys

with open(sys.argv[1]) as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        print('{:>10} {:5.2f}'.format(row[' car'], (float(row[' miles_stop']) - float(row['miles_start'])) / float(row[' gallons'])))