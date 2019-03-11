#!/usr/bin/env python3.6

import sys
from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect((sys.argv[1], int(sys.argv[2]))) # connect to server

# receive data
data = b''
while True:
    packet = s.recv(1)
    if not packet:
        break
    data += packet

print(data.decode('utf-8'))