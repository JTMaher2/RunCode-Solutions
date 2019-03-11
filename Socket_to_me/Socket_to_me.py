#! /usr/bin/env/python3

import sys
import socket

addr = sys.argv[1]
port = sys.argv[2]

sock = socket.create_connection((sys.argv[1], sys.argv[2]))

amount_received = 0
amount_expected = len('What do you want?')

while amount_received < amount_expected:
    data = sock.recv(16)
    amount_received += len(data)
    print(data)

sock.sendall(b'The key')