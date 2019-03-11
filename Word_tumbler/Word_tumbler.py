#!/usr/bin/env python3

import sys
from itertools import permutations

# get list of permutations for word, avoiding repeated words with more than 1 of the same character
def unique_permutations(iterable, r=None):
    previous = tuple()
    for p in permutations(sorted(iterable), r):
        if p > previous:
            previous = p
            yield ''.join(str(i) for i in p)

dict_words = []

with open('/usr/share/dict/american-english') as dictionary:
    for dict_word in dictionary:
        lower_dict_word = dict_word.lower()
        if lower_dict_word not in dict_words:
            dict_words.append(lower_dict_word)

with open(sys.argv[1]) as file_input:
    for line in file_input:
        # check if each perm is in dictionary, and if so, print it
        for word_perm in list(unique_permutations(line.rstrip('\n'))):
            for dict_word in dict_words:
                stripped_word = dict_word.rstrip('\n')
                if stripped_word == word_perm:
                    print(stripped_word)