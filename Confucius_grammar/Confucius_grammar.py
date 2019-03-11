#!/usr/bin/env python3.6

import sys

with open(sys.argv[1]) as file:
    for line in file:
        line_output = ''
        for sentence in line.split('.'):
            sentence = sentence.strip('\n').strip(' ')
            if len(sentence) > 0:
                output = ''
                i = 0
                for word in sentence.split(' '):
                    if i == 0:
                        c = 0
                        wo = ''
                        for ch in word:
                            if c == 0:
                                wo += word[c:c + 1].upper()
                            else:
                                wo += word[c:c + 1].lower()
                            c += 1
                        word = wo
                    elif word != 'I' and word != 'i':
                        wo = ''
                        c = 0
                        for ch in word:
                            wo += word[c:c + 1].lower()
                            c += 1
                        word = wo
                    elif word == 'i':
                        word = word[:1].upper()
                    i += 1
                    output += word
                    if i == len(sentence.split(' ')):
                        output += '. '
                    else:
                        output += ' '

                line_output += output
        
        print(line_output.rstrip(' '))