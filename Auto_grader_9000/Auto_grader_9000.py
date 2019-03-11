#!/usr/bin/env python3

import sys
import os

path = 'C:\\Users\\James\\Documents\\CodeWarz\\Auto_grader_9000\\Student_work'

for folder, subs, files in os.walk(path):
    for filename in files:
        with open(os.path.join(folder, filename), 'r') as src:
            with open(src, 'r') as src_file:
                for line in src_file:
                    print(line)