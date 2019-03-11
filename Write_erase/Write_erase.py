#!/usr/bin/env python3

import sys
from socket import *

with open(sys.argv[1]) as file_input:
    for line in file_input:
        split_file_input = line.split(' ')
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((split_file_input[0], int(split_file_input[1]))) # connect to server

        # receive data
        data = b''
        while True:
            packet = s.recv(1)
            if not packet:
                break
            data += packet

        print(data.decode('utf-8'))