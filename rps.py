from random import randint

options = ['rock', 'paper', 'scissors']

player = False

computer = options[randint(0, 2)]

if player == False:
    player = input('rock paper or scissors?\n')
    if player == computer:
        print('tie')
    elif player == 'rock':
        if computer == 'paper':
            print('computer wins')
    elif player == 'scissors':
        if computer == 'rock':
            print('computer wins')
    