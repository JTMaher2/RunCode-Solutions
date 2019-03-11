#!/usr/bin/env python3

import itertools
import string
import hashlib
import sys
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(( sys.argv[1], int(sys.argv[2]) ))

s.recv(1024)
data = s.recv(1024).decode('utf-8')

# get starting string chars
give_me_a_str = 'Give me a string starting with '
base_str = data[data.index(give_me_a_str) + len(give_me_a_str):data.index(',')]

# get ending SHA-1 sum chars
such_that_its_sha1 = 'such that its sha1 sum ends in '
sha1_end = data[data.index(such_that_its_sha1) + len(such_that_its_sha1):len(data) - 2]

letters_and_numbers = string.ascii_letters.replace("_", '') + string.digits.replace("_", "")

for perm in itertools.permutations(letters_and_numbers, 5):
    full_str = base_str + ''.join(str(i) for i in perm)

    # if this hash matches
    if hashlib.sha1(full_str.encode('utf-8')).hexdigest()[::-1][0:6][::-1] == sha1_end:
        # send it to server
        s.sendall(full_str.encode())

        # receive server's response
        print(s.recv(1024).decode('utf-8'))

        # close connection
        s.shutdown(socket.SHUT_WR)
        s.close()
        break