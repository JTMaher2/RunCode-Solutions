#!/usr/bin/env python3.6

import sys
import string

invalidChars = set(string.punctuation.replace("_", ""))

with open(sys.argv[1]) as file:
    for line in file:
        lineOut = ''
        i = 0
        for word in line.split(' '):
            word = word.rstrip('\n')

            for letter in word:
                if letter not in invalidChars:
                    newLetter = ord(letter) - i
                
                    if letter.isupper() and newLetter < ord('A') or letter.islower() and newLetter < ord('a'):
                        newLetter = newLetter + 26

                    lineOut += chr(newLetter)
                else:
                    lineOut += letter
            if i < len(line.split(' ')) - 1:
                lineOut += ' '
            i += 1
        lineOut += '\n'
        sys.stdout.write(lineOut)