#!/usr/bin/env python3

import sys, urllib3

with urllib3.request.urlopen(url) as f:
    print(f.read(300))