#!/usr/bin/env python3.6

import sys
from urllib.request import urlopen

print(urlopen(sys.argv[1]).read().decode('utf-8'))
