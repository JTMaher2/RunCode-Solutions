#!/usr/bin/env python3

import sys
import operator

letter_frequencies = []
letters = []

NUM_SPACES = 4
ALPHABET_LEN = 26

for i in range(0, ALPHABET_LEN):
    letter_frequencies.append(0)

total_chars = 0
space_frequency = 0

with open(sys.argv[1]) as file_input:
    for line in file_input:
        for char in line:
            if (char.isalpha() or char == ' '):
                if (char.isalpha()):
                    letter_frequencies[ord(char.lower()) - ord('a')] += 1 # increment # of occurrences for this letter
                else:
                    space_frequency += 1

                total_chars += 1
                if char.lower() not in letters:
                    letters.append(char.lower())

char_percentages = {}

for l in range(0, len(letters)):
    if (letters[l].lower() != ' '):
        char_percentages[letters[l].lower()] = (letter_frequencies[ord(letters[l]) - ord('a')] * 100) / total_chars
    else:
        char_percentages[letters[l].lower()] = (space_frequency * 100) / total_chars

sorted_by_value = sorted(char_percentages.items(), key=operator.itemgetter(1), reverse=True)

char_percentages_that_are_the_same = [] # a dict of tuples where each tuple's key is a list of characters, and each tuple's value is a percentage

for char_percentage in sorted_by_value:
    added = False
    for same_char_percentage in char_percentages_that_are_the_same:
        if char_percentage[0] not in same_char_percentage[0] and char_percentage[1] == same_char_percentage[1]:
            same_char_percentage[0].append(char_percentage[0])
            added = True
    if not added:
        # make a new list with this char and this char's value
        char_percentages_that_are_the_same.append(([char_percentage[0]], char_percentage[1]))

sorted_char_percentages_that_are_the_same = []

# sort each list of same value by character
for char_percentage in char_percentages_that_are_the_same:
    if len(char_percentage[0]) > 0:
        sorted_char_percentage = (sorted(char_percentage[0]), char_percentage[1])
        sorted_char_percentages_that_are_the_same.append(sorted_char_percentage)

for sorted_char_percentage in sorted_char_percentages_that_are_the_same:
    for char in sorted_char_percentage[0]:
        print('\'' + char + '\'' + ' ' + '{0:.2f}'.format(sorted_char_percentage[1]) + '%')