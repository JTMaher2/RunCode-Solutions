#!/usr/bin/env python3.6

import sys, hashlib

print(hashlib.sha1('Electricity! Constitution! Philadelphia!\
Fish! Pony! Hip, Hip Hop, Hip Hop anonymous? Darn you! You gave him the easy ones.'.strip().encode('utf-8')).hexdigest())