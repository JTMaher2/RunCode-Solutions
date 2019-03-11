#!/usr/bin/env python3

import sys
import gzip
import shutil
import urllib.request
import json
import operator
import collections

with gzip.open(sys.argv[2], 'rb') as f_in:
    with open('/tmp/ips.txt', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

countries = {}

with open('/tmp/ips.txt') as ips:
    for line in ips:
        ip_addr = line[0:line.index(' - - ')]
        with urllib.request.urlopen(sys.argv[1] + '/json/' + ip_addr) as f:
            read_str = f.read(300).decode('utf-8')
            json_str = json.loads(read_str)
            country = json_str['country']
            in_list = False
            for c in range(0, len(countries)):
                if (list(countries)[c] == country): # it's already in list, increment
                    countries[list(countries)[c]] += 1
                    in_list = True
                    break

            if (in_list == False): # it's not already in list
                countries[country] = 1

# sort the dictionary by number of occurrences of each country
countries = sorted(countries.items(), key=operator.itemgetter(1), reverse=True)

is_sorted = False # is the list sorted?

while is_sorted == False:
    last_country_count = -1 # the number of occurrences of the previous country in the dictionary
    last_country = '' # the previous country in the dictionary

    for i in range(0, len(countries)):
        if countries[i][1] == last_country_count:
            new_countries = {}
            new_countries[last_country] = last_country_count
            new_countries[countries[i][0]] = countries[i][1]
            new_countries = sorted(new_countries.items()) # sort by country name

            # overwrite the affected countries
            countries[i] = list(new_countries[1])
            countries[i - 1] = list(new_countries[0])

        # update previous country and country count
        last_country_count = countries[i][1]
        last_country = countries[i][0]

    # check if sorted
    last_country_count = -1 # the number of occurrences of the previous country in the dictionary
    last_country = '' # the previous country in the dictionary

    num_sorted = 0

    for i in range(0, len(countries)):
        if countries[i][1] != last_country_count or countries[i][1] == last_country_count and countries[i][0] > last_country:
            num_sorted += 1

        # update previous country and country count
        last_country = countries[i][0]
        last_country_count = countries[i][1]

    if num_sorted == len(countries):
        is_sorted = True

for c in range(0, len(countries)):
    sys.stdout.write(list(countries)[c][0] + ' ')
    
    num_occurrences = int(countries[c][1])

    for i in range(0, num_occurrences):
        sys.stdout.write('*')
    
    if (c < len(countries) - 1):
        sys.stdout.write('\n')