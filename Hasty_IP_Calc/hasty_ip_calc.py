#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as input:
    for line in input:
        parts = line.split(' ')

        ip_addr = parts[0].replace('\\', '\\\\')
        gateway_addr = parts[1]

        subnet = int(ip_addr[ip_addr.find('\\') - 1:len(ip_addr)])

        ip_addr = ip_addr[0:ip_addr.find('\\') - 2]

        print('Network: ' + ip_addr)

        num_bits = 0

        for segment in ip_addr.split('.'):
            num_bits += 8

        num_available_bits = num_bits - subnet

        max_addrs = 1
        bit_str = ''
        bit_strs = []

        for i in range(0, num_available_bits):
            bit_str += '1'
            if len(bit_str) == 8:
                bit_strs.append(bit_str)
                max_addrs *= (int(bit_str, 2) + 1)
                bit_str = ''

        # there is another bit string that is less than eight bits
        if bit_str != '':
            bit_strs.append(bit_str)
            max_addrs *= (int(bit_str, 2) + 1)

        max_addrs -= 2

        print('Total usable IP\'s: ' + str(max_addrs))
        sys.stdout.write('Usable range: ' + ip_addr[0:ip_addr.rfind('.') + 1] + str(int(ip_addr[ip_addr.rfind('.') + 1]) + 1) + '-')

        ip_parts = ip_addr.split('.')

        bit_strs = bit_strs[::-1]

        # determine gateway address and max. usable range
        gateway_addr_parts = gateway_addr.split('.')
        invalid = False
        if len(bit_strs) == 3:
            new_one = str(int(ip_parts[1]) + int(bit_strs[0], 2))
            new_two = str(int(ip_parts[2]) + int(bit_strs[1], 2))
            new_three = str(int(ip_parts[3]) + int(bit_strs[2], 2) - 1)
            gateway_sum = int(gateway_addr_parts[1]) + int(gateway_addr_parts[2]) + int(gateway_addr_parts[3])
            if int(gateway_addr_parts[0]) != int(ip_parts[0]) or int(gateway_addr_parts[1]) < int(ip_parts[1]) or int(gateway_addr_parts[2]) < int(ip_parts[2]) or int(gateway_addr_parts[3]) < int(ip_parts[3]) or gateway_sum < int(ip_parts[1]) + int(ip_parts[2]) + int(ip_parts[3]) + 1 or gateway_sum > int(new_one) + int(new_two) + int(new_three):
                invalid = True
            broadcast_address = ip_parts[0] + '.' + new_one + '.' + new_two + '.' + str(int(new_three) + 1)
            ip_parts[0] = '-1'
            ip_parts[1] = new_one
            ip_parts[2] = new_two
            ip_parts[3] = new_three
        elif len(bit_strs) == 2:
            new_two = str(int(ip_parts[2]) + int(bit_strs[0], 2))
            new_three = str(int(ip_parts[3]) + int(bit_strs[1], 2) - 1)
            gateway_sum = int(gateway_addr_parts[2]) + int(gateway_addr_parts[3])
            if int(gateway_addr_parts[0]) != int(ip_parts[0]) or int(gateway_addr_parts[1]) != int(ip_parts[1]) or int(gateway_addr_parts[2]) < int(ip_parts[2]) or int(gateway_addr_parts[3]) < int(ip_parts[3]) or gateway_sum < int(ip_parts[2]) + int(ip_parts[3]) + 1 or gateway_sum > int(new_two) + int(new_three):
                invalid = True
            broadcast_address = ip_parts[0] + '.' + ip_parts[1] + '.' + new_two + '.' + str(int(new_three) + 1)
            ip_parts[0] = '-1'
            ip_parts[1] = '-1'
            ip_parts[2] = new_two
            ip_parts[3] = new_three
        elif len(bit_strs) == 1:
            new_three = str(int(ip_parts[3]) + int(bit_strs[0], 2) - 1)
            if int(gateway_addr_parts[0]) != int(ip_parts[0]) or int(gateway_addr_parts[1]) != int(ip_parts[1]) or int(gateway_addr_parts[2]) != int(ip_parts[2]) or int(gateway_addr_parts[3]) < int(ip_parts[3]) or int(gateway_addr_parts[3]) < int(ip_parts[3]) + 1 or int(gateway_addr_parts[3]) > int(new_three):
                invalid = True
            broadcast_address = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.' + str(int(new_three) + 1)
            ip_parts[0] = '-1'
            ip_parts[1] = '-1'
            ip_parts[2] = '-1'
            ip_parts[3] = new_three

        for i in range(0, len(ip_parts)):
            if ip_parts[i] != '-1':
                if ip_parts[i] != '0':
                    sys.stdout.write(ip_parts[i].lstrip('0'))
                else:
                    sys.stdout.write(ip_parts[i])
                if i < len(ip_parts) - 1:
                    sys.stdout.write('.')
        sys.stdout.write('\n')

        # print broadcast address
        print('Broadcast Address: ' + broadcast_address)
        
        gateway_out = 'Gateway Address: '
        if invalid:
            gateway_out += 'Invalid\n'
        else:
            gateway_out += gateway_addr
        print(gateway_out)