#!/usr/bin/env python3.6

import sys
import string

invalidChars = set(string.punctuation.replace("_", ""))

def lookupWord(word):
    return {
        'Alpha': 'A',
        'alpha': 'a',
        'Bravo': 'B',
        'bravo': 'b',
        'Charlie': 'C',
        'charlie': 'c',
        'Delta': 'D',
        'delta': 'd',
        'Echo': 'E',
        'echo': 'e',
        'Foxtrot': 'F',
        'foxtrot': 'f',
        'Golf': 'G',
        'golf': 'g',
        'Hotel': 'H',
        'hotel': 'h',
        'India': 'I',
        'india': 'i',
        'Juliet': 'J',
        'juliet': 'j',
        'Kilo': 'K',
        'kilo': 'k',
        'Lima': 'L',
        'lima': 'l',
        'Mike': 'M',
        'mike': 'm',
        'November': 'N',
        'november': 'n',
        'Oscar': 'O',
        'oscar': 'o',
        'Papa': 'P',
        'papa': 'p',
        'Quebec': 'Q',
        'quebec': 'q',
        'Romeo': 'R',
        'romeo': 'r',
        'Sierra': 'S',
        'sierra': 's',
        'Tango': 'T',
        'tango': 't',
        'Uniform': 'U',
        'uniform': 'u',
        'Victor': 'V',
        'victor': 'v',
        'Whiskey': 'W',
        'whiskey': 'w',
        'Xray': 'X',
        'xray': 'x',
        'Yankee': 'Y',
        'yankee': 'y',
        'Zulu': 'Z',
        'zulu': 'z'
    }[word]

with open(sys.argv[1]) as file:
    for row in file:
        i = 0
        for word in row.split(' '):
            word = word.rstrip('\n')
            for milLetter in word.split('-'):
                builtWord = ''
                for letter in milLetter:
                    if letter in invalidChars:
                        sys.stdout.write(lookupWord(builtWord))
                        builtWord = ''
                        sys.stdout.write(letter)
                    else:
                        builtWord += letter
                if builtWord != '':
                    sys.stdout.write(lookupWord(builtWord))
            if i < len(row.split(' ')) - 1:
                sys.stdout.write(' ')
            else:
                sys.stdout.write('\n')
            i += 1
