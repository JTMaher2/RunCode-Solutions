#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as file_input:
	for line in file_input:
		line_parts = line.split(' ')
		i = 0
		for word in line_parts:
			if i + 1 >= len(line_parts) or word != line_parts[i + 1]:
				sys.stdout.write(word)
				if i < len(line_parts) - 1:
					sys.stdout.write(' ')
			i += 1