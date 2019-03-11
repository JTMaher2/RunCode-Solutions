#!/usr/bin/env python3

from urllib.request import urlopen
import sys
import json

def gen_new_pass(password, password_len):
    for i in range(0, password_len):
        password[i] = str(int(password[i]) + 1)

password_len = 1

password_found = False

while (password_found == False):
    gen_new_pass(password, password_len)
    resp = json.loads(urlopen('http://jq-me.runcode.ninja/checklogin.php?q=' + 'abc').read().decode('utf-8'))

    if (resp['fail'] != 'yeah'):
        print(password)
        password_found = True