#! /usr/bin/env python3

import sys
import re
import socket

THREE = 3

# does an IP addr's segment contain more than four digits?
def seg_contains_more_than_four_digits(ip_addr):
    for seg in ip_addr.split('.'):
        if len(seg) > THREE:
            return True
    return False

with open('ip_finder_and_validator_data1.txt') as file_input:
    ip_address_occurrences = {}
    ip_address_valid = {}
    
    for line in file_input:
        line = line.rstrip('\n')
        i = re.finditer(r'\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|\w)){4}\b', line)
        if i != None:
            element = ''
            use_group_zero = True # until proven otherwise, assume that the group 0 IP address is the complete IP address
            
            for element in i:
                # if the group 0 IP address is incomplete, use string instead
                if element.group(0)[len(element.group(0)) - 1] == '.':
                    try:
                        int(element.string[len(element.string) - 1])
                        # the final char of element.string is an int,
                        # so element.string should be used, because it is a valid IP addr.
                        use_group_zero = False
                    except:
                        # if the final char of the element is not an int,
                        # it is not an IP address, so do not continue
                        break

                try:
                    if use_group_zero:
                        socket.inet_aton(element.group(0))
                    else:
                        socket.inet_aton(element.string)
                    # it is a valid IP address
                    valid_ip = True
                except socket.error:
                    # it is not a valid IP address
                    valid_ip = False
                    # if any of its segments are more than 4 digits long,
                    # do not do anything more
                    if use_group_zero:
                        if seg_contains_more_than_four_digits(element.group(0)):
                            break
                    else:
                        if seg_contains_more_than_four_digits(element.string):
                            break

                # mark whether or not this IP address is valid
                if use_group_zero:
                    ip_address_valid[element.group(0)] = valid_ip
                    gotten_key = ip_address_occurrences.get(element.group(0),None)
                    if gotten_key == None:
                        ip_address_occurrences[element.group(0)] = 0
                    else:
                        ip_address_occurrences[element.group(0)] = ip_address_occurrences[element.group(0)] + 1 # increment number of occurrences for this IP address
                else:
                    ip_address_valid[element.string] = valid_ip
                    gotten_key = ip_address_occurrences.get(element.string,None)
                    if gotten_key == None:
                        ip_address_occurrences[element.string] = 0
                    else:
                        ip_address_occurrences[element.string] = ip_address_occurrences[element.string] + 1 # increment number of occurrences for this IP address

    for i in range(0, len(ip_address_occurrences)):
        
        sys.stdout.write('(' + str(ip_address_occurrences[list(ip_address_occurrences.keys())[i]]) + ')' + str(ip_address_valid[list(ip_address_valid.keys())[i]]) + ': ' + list(ip_address_occurrences.keys())[i] + ' ')
        j = 0

        j += 50

        num_occurrences = ip_address_occurrences[list(ip_address_occurrences.keys())[i]]

        #if j > num_occurrences:
            

        #for j in range(0, ):
         #   sys.stdout.write('*') # print a star for every 50 occurrences
        sys.stdout.write('\n')