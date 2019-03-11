#!/usr/bin/env python3.6

import sys

with open(sys.argv[1]) as input:
    for row in input:
        sys.stdout.write(bytearray.fromhex(row).decode())