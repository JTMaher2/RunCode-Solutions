#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as file_input:
    for line in file_input:
        with open('/usr/share/dict/american-english') as dictionary:
            