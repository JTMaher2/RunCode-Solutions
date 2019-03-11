#!/usr/bin/env python3

import sys

letter_frequencies = []
letters = []

NUM_SPACES = 4
ALPHABET_LEN = 26

for i in range(0, ALPHABET_LEN):
    letter_frequencies.append(0)

with open(sys.argv[1]) as file_input:
    for line in file_input:
        for letter in line:
            if (letter.isalpha()):
                letter_frequencies[ord(letter.lower()) - ord('a')] += 1 # increment # of occurrences for this letter
                if letter.lower() not in letters:
                    letters.append(letter.lower())

output = 'letters:   '

for l in range(0, len(letters)):
    output += letters[l].lower() + ',    '

output = output.rstrip(',    ')

output += '\ncounts:    '

first = True

for f in range(0, len(letters)):
    if not first:
        # prepend with comma and spaces
        output += ','
        for i in range(0, NUM_SPACES - len(str(letter_frequencies[ord(letters[f]) - ord('a')])) + 1):
            output += ' '
    output += str(letter_frequencies[ord(letters[f]) - ord('a')])
    first = False
    
print(output.lstrip(',').lstrip())