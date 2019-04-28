#!/usr/bin/env python3

import sys
import string

num_checks = 5
min_chars = 8
max_chars = 20
punctuation = set(string.punctuation.replace("_", ""))

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def hasUppercase(inputString):
    return any(char.isupper() for char in inputString)

def hasLowercase(inputString):
    return any(char.islower() for char in inputString)

def hasPunctuation(inputString):
    return any((char in punctuation) for char in inputString)

def isBetweenEightAndTwentyChars(inputString):
    return len(inputString) >= min_chars and len(inputString) <= max_chars

with open('input.txt') as file_input:
    for line in file_input:
        line = line.rstrip('\n')
        checks_passed = 0
        if hasNumbers(line):
            checks_passed += 1
        if hasUppercase(line):
            checks_passed += 1
        if hasLowercase(line):
            checks_passed += 1
        if hasPunctuation(line):
            checks_passed += 1
        if isBetweenEightAndTwentyChars(line):
            checks_passed += 1
        line_len = len(line)
        sys.stdout.write('Password: (' + f'{line_len:0{2}}' + ') ' + f'{line[0:20]:{20}}' + '  Status: ')
        if checks_passed == num_checks:
            sys.stdout.write('Passed all checks!\n')
        else:
            sys.stdout.write('Failed ')
            checks_failed = num_checks - checks_passed
            sys.stdout.write(str(checks_failed))
            if checks_failed == 1:
                sys.stdout.write(' check\n')
            else:
                sys.stdout.write(' checks\n')