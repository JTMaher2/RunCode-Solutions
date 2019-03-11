import sys
import urllib.request

with urllib.request.urlopen('http://gtp.runcode.ninja') as f:
    read_str = f.read(300).decode('utf-8')
    print(read_str)
