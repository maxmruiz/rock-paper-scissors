from random import randint

options = ['rock', 'paper', 'scissors']

player = False

computer = options[randint(0, 2)]

while player == False:
    player = input('rock paper or scissors?\n')
    if player == computer:
        print('tie')
    elif player == 'rock':
        if computer == 'paper':
            print('computer wins', computer, 'beats', player)
        else:
            print('player wins', player, 'beats', computer)
    elif player == 'scissors':
        if computer == 'rock':
            print('computer wins', computer, 'beats', player)
        else:
            print('player wins', player, 'beats', computer)
    elif player == 'paper':
        if computer == 'scissors':
            print('computer wins', computer, 'beats', player)
        else:
            print('player wins', player, 'beats', computer)
    else:
        print('invalid')
    
    player = False
    computer = options[randint(0,2)]
    