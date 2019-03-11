#!/usr/bin/env python3.6

import sys
import hashlib

sha_256 = hashlib.sha256()

with open(sys.argv[1]) as shafile:
    for row in shafile:
        with open(sys.argv[2]) as dictionary:
            for word in dictionary:
                word = word.rstrip().encode('utf-8')
                sha_256.update(word)
                if sha_256.hexdigest().encode('utf-8') == row.rstrip():
                    print(word)
                    break