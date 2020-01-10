import random


def clear_screen():
    print('\n' * 100)


def display_board(board):
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])


def player_assignment():
    user_input = input("Do you want to play with 'X' or with '0'? \n")

    while user_input not in ['X', '0', 'x']:
        print("Input is not correct, please enter 'X' or '0' \n")
        user_input = input("Do you want to play with 'X' or with '0'? \n")
    player_1 = user_input.upper()
    player_2 = 'X' if player_1 == '0' else '0'
    return {1: player_1, 2: player_2}


def player_input(marker, board):
    user_input = input(f"Where do you want to put the {marker}? (number from 1 to 9) \n")
    while user_input not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        print("Input is not correct, please choose a correct value \n")
        user_input = input(f"Where do you want to put the {marker}? (number from 1 to 9) \n")

    while board[int(user_input)] != ' ':
        print("There is already a value in that field. Please choose an empty cell! \n")
        user_input = input(f"Where do you want to put the {marker}? (number from 1 to 9) \n")
    return int(user_input)


def update_board(marker, input, board):
    board[input] = marker
    return board


def what_player_starts():
    return random.randint(1, 2)


def win_check(board, marker):

    if (board[1] == board[2] == board[3] == marker) or (board[4] == board[5] == board[6] == marker) or \
            (board[7] == board[8] == board[9] == marker) or (board[1] == board[5] == board[9] == marker) or \
            (board[3] == board[5] == board[7] == marker):
        print(f"Player '{marker}' won!")
        ask_rematch()
        return True
    else:
        return False


def ask_rematch():
    play_again = input('Would you like to play again? (yes/no)\n')

    while play_again not in ['yes', 'no']:
        play_again = input('Would you like to play again? (yes/no)\n')
    if play_again == 'yes':
        game_on()
    else:
        print('Thanks for playing!')


def game_on():
    clear_screen()
    players = player_assignment()
    print(players)
    empty_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    board = empty_board

    player_to_start = what_player_starts()
    print(f"The player to start was randomly picked to be {player_to_start}, playing with '{players[player_to_start]}'")
    display_board(board)

    game_over = False
    current_player_marker = players[player_to_start]
    moves = 1

    while game_over is False and moves < 10:

        move_to_play = player_input(current_player_marker, board)
        board = update_board(current_player_marker, move_to_play, board)
        display_board(board)
        moves += 1
        game_over = win_check(board, current_player_marker)
        current_player_marker = 'X' if current_player_marker == '0' else '0'

    if moves == 10:
        print('The game is over, no-one won, no-one lost! It was a tie!')
        ask_rematch()


game_on()

