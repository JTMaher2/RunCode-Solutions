#!/usr/bin/env python3

import sys
import json

json_str = ''

with open(sys.argv[1]) as file_input:
    for line in file_input:
        json_str += line

if json_str != '':
    json_obj = json.loads(json_str)

    rounds = json_obj.keys()

    board = [['*','*','*'],['*','*','*'],['*','*','*']]

    for round in rounds:
        cur_round = json_obj[round]
        x_found = False
        y_found = False
        if cur_round != {}:
            if cur_round['X'] != []:
                x_y = cur_round['X'][0]
                x_x = cur_round['X'][1]
                x_found = True
            if cur_round['O'] != []:
                y_y = cur_round['O'][0]
                y_x = cur_round['O'][1]
                y_found = True
        
            if x_found and y_found:
                board[x_x][x_y] = 'X'
                board[y_x][y_y] = 'O'

    winner = False

    for row in range(0, len(board[0])):
        sys.stdout.write('[')
        for col in range(0, len(board)):
            sys.stdout.write('\'' + board[col][row] + '\'')
            if col < len(board[0]) - 1:
                sys.stdout.write(', ')
            else:
                sys.stdout.write(']')
        if row < len(board[0]) - 1:
            sys.stdout.write('\n')

    sys.stdout.write('\n')

    for row in range(0, len(board)):
        num_xs = 0
        num_os = 0
        for col in range(0, len(board[row])):
            if board[row][col] == 'X':
                num_xs += 1
            elif board[row][col] == 'O':
                num_os += 1
        if num_xs == 3:
            print('X Wins!')
            winner = True
        elif num_os == 3:
            print('O Wins!')
            winner = True

    for col in range(0, len(board[0])):
        num_xs = 0
        num_os = 0
        for row in range(0, len(board)):
            if board[row][col] == 'X':
                num_xs += 1
            elif board[row][col] == 'O':
                num_os += 1
        if num_xs == 3:
            print('X Wins!')
            winner = True
        elif num_os == 3:
            print('O Wins!')
            winner = True

    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        print('X Wins!')
        winner = True
    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        print('X Wins!')
        winner = True
    elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        print('O Wins!')
        winner = True
    elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        print('O Wins!')
        winner = True

    if winner == False:
        print('Draw!')