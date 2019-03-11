import sys

dict_words = []

with open('../american-english') as dictionary:
    for dict_word in dictionary:
        lower_dict_word = dict_word.lower()
        dict_words.append(lower_dict_word.rstrip('\n'))

with open('input.txt') as file_input:
    for line in file_input:
        n = len(line)
        # there will always be at least 1 non-word character at each end of the word, and the word must be at least 1 char long
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                if line[i:j].lower() in dict_words:
                    print(line[i:j])