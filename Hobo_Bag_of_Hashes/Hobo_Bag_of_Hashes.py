#!/usr/bin/env python3

import sys
import os
import hashlib

file_hashes = []

for algo in hashlib.algorithms_available():
                print(algo)

for filename in os.listdir(sys.argv[2]):
    with open(sys.argv[2] + filename) as hobo_file:
        for line in hobo_file:
            file_hashes.append((hashlib.sha1(line.encode('utf-8')).hexdigest(), filename))
            file_hashes.append((hashlib.sha256(line.encode('utf-8')).hexdigest(), filename))
            file_hashes.append((hashlib.md5(line.encode('utf-8')).hexdigest(), filename))
            file_hashes.append((hashlib.sha224(line.encode('utf-8')).hexdigest(), filename))
            file_hashes.append((hashlib.sha384(line.encode('utf-8')).hexdigest(), filename))
            file_hashes.append((hashlib.sha512(line.encode('utf-8')).hexdigest(), filename))
            
with open(sys.argv[1]) as hashes:
    for hash in hashes:
        hash = hash.rstrip('\n')
        for file_hash in file_hashes:
            if hash == file_hash[0]:
                print('Found the file ' + sys.argv[2] + file_hash[1] + ' with the hash of ' + file_hash[0])