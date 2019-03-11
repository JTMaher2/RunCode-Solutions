#!/usr/bin/env python3

import itertools
import string
import hashlib
import sys
import socket

def receiveAll (sock):
    data = ""
    buff_size = 1024
    while True: 
       part = sock.recv (buff_size)
       data = data + str(part)
       if len(part) < buff_size:
          break
    return data

def receiveAllSmallBuff (sock):
    data = ""
    buff_size = 1
    while True: 
       part = sock.recv (buff_size)
       data = data + str(part)
       if len(part) < buff_size:
          break
    return data

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(( 'listen.codewarz.ninja', 9014 ))

data = receiveAll(s)

s.sendall('01234'.encode())
print(receiveAllSmallBuff(s))
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