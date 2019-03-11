#!/usr/bin/env python3

import sys

game_boy_games = []
game_boy_color_games = []
all_games = []

def flip(rows, cur_row, next_row):
	temp = rows[cur_row]
	rows[cur_row] = rows[next_row]
	rows[next_row] = temp

	return rows

with open(sys.argv[1]) as game_boy_list:
	with open(sys.argv[2]) as game_boy_color_list:
		for line in game_boy_list:
			game_boy_games.append(line)
		for line in game_boy_color_list:
			game_boy_color_games.append(line)

for line in game_boy_games:
	all_games.append(line.rstrip('\n').rstrip(',') + ',gb')

for line in game_boy_color_games:
	all_games.append(line.rstrip('\n').rstrip(',') + ',gbc')

all_games_parsed = []

for line in all_games:
	first_comma_index = line.find(',')
	second_comma_index = line.find(',', line.find(',') + 1)
	third_comma_index = line.find(',', line.find(',', line.find(',') + 1) + 1)
	title = line[0:first_comma_index] # title is 0 to 1st comma
	publisher = line[first_comma_index + 1:second_comma_index] # publisher is 1st comma + 1 to 2nd comma
	release_date = line[second_comma_index + 1:third_comma_index] # release date is 2nd comma + 1 to 3rd comma
	system = line[third_comma_index + 1:len(line)] # system is 3rd comma + 1 to end

	if title != 'Title':
		game = [title, publisher, release_date, system]
		all_games_parsed.append(game)

sorted = False

while sorted == False:
	for g in range(0, len(all_games_parsed) - 1):
		if all_games_parsed[g][2] > all_games_parsed[g + 1][2]:
			all_games_parsed = flip(all_games_parsed, g, g + 1)
		elif all_games_parsed[g][2] == all_games_parsed[g + 1][2]:
			if all_games_parsed[g][0] > all_games_parsed[g + 1][0]:
				all_games_parsed = flip(all_games_parsed, g, g + 1)

	num_sorted = 0

	for g in range(0, len(all_games_parsed) - 1):
		if all_games_parsed[g][2] > all_games_parsed[g + 1][2]:
			sorted = False
		else:
			num_sorted += 1
	if num_sorted == len(all_games_parsed) - 1:
		sorted = True

MAX_CHARS = 14

for game in all_games_parsed:
	if game[2] != 'gb' and game[2] != 'gbc': # if the release date is missing, the release date field will contain the system
		if len(game[0]) > MAX_CHARS:
			sys.stdout.write(game[0][0:MAX_CHARS] + '~')
		else:
			for i in range(0, MAX_CHARS - len(game[0]) + 1):
				sys.stdout.write(' ')
			sys.stdout.write(game[0])

		sys.stdout.write(' ' + game[2] + ' ')

		if game[3] == 'gb':
			sys.stdout.write('      Game Boy')
		else:
			sys.stdout.write('Game Boy Color')

		sys.stdout.write('\n')
