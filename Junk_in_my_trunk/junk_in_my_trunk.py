#!/usr/bin/env python3

import sys
import string

punctuation = set(string.punctuation.replace("_", ""))

with open(sys.argv[1], 'r') as input:
    for line in input:
        i = 0
        for word in line.split(' '):
            word = word.strip('\n')
            word = word[::-1]

            j = 0
            punctuation_letters = ''
            for letter in word:
                if letter not in punctuation:
                    letter_to_remove = j
                    break
                else:
                    punctuation_letters += letter
                j += 1
            
            word = punctuation_letters + word[letter_to_remove + 1:len(word)]

            word = word[::-1]

            if i < len(line.split(' ')) - 1:
                sys.stdout.write(word + ' ')
            else:
                sys.stdout.write(word + '\n')

            i += 1