import random
from IPython.core.display import clear_output

#List to define the values of the positions in the board
board = [" "]  * 9
players = [["name1","marker1"],["name2","marker2"]]

#Current player must be equal to either 0 or 1.
#Used for indexing purposes.
#For printing purposes use current_player + 1.
current_player = 0 

def display_board(board):

        print("")

        display = ("-------------" + "\n"
                   "| " + board[6] + " | " + board[7] + " | " + board[8] + " |" + "\n"
                   "-------------" + "\n"
                   "| " + board[3] + " | " + board[4] + " | " + board[5] + " |" + "\n"
                   "-------------" + "\n"
                   "| " + board[0] + " | " + board[1] + " | " + board[2] + " |" + "\n"
                   "-------------" + "\n")
        print(display)

        print("")

def player_input(players):
        markers = ["X","O"]

        P1_name = raw_input("Player 1, enter your name: ")
        players[0][0] = P1_name
        P1_symbol = raw_input("Player 1, select your marker ('X' or 'O'): ")
        while P1_symbol.upper() not in markers:
            P1_symbol = raw_input("Invalid option. Player 1, select your marker: 'X' or 'O': ")
        
        players[0][1] = P1_symbol.upper()

        markers.remove(P1_symbol.upper())

        players[1][1] = markers[0]
        P2_name = raw_input("Player 2, enter your name: ")
        players[1][0] = P2_name

        print("Thank you:\n" + "   - " + P1_name + ": " + 
              players[0][1] + "\n" + "   - " + P2_name + ": " + players[1][1] )

def place_marker(board, marker, position):
        board[position] = marker

def win_check(board,mark):

    win = False

    #Check horizontal lines
    for i in range(0,8,3):
        if board[i] == board[i+1] == board[i+2] == mark:
            win = True
    
    #Check vertical lines
    for i in range(0,3):
        if board[i] == board[i+3] == board[i+6] == mark:
            win = True

    #Check diagonal lines
    if (board[0] == board[4] == board[8] == mark or
        board[2] == board[4] == board[6] == mark):
        win = True

    return win
    
'''
    #ALTERNATIVE use or to concatenate all possibe win cases (see jupyter notebook).
    This is more efficiently from a computational point of view but less syntax clear maybe...
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
'''

def choose_first():
    first = random.randint(0,1)
    print (players[first][0] + " goes first!")
    return first

def space_check(board, position):
    return board[position] == " "


def full_board_check(board):
    full = False
    if not " " in board:
        full = True
    return full

    #Alternative
    #for i in range(1,10):
    #    if space_check(board, i):
    #        return False
    #return True

def next_player():
    global current_player
    current_player += 1
    if current_player >= 2:
        current_player = 0


def player_choice(board):
    position = " "
    #Using strings because of raw input
    #The order in the while statement below is important, because the first check filters already integer input.
    #If the second check of the "or" logic was put in first place, int() would cause the function to crash, because
    #a " " or "" character could be entered as argument for int. Check the commented line below.
    while position not in "1 2 3 4 5 6 7 8 9".split() or not space_check(board, int(position)-1):
    #while not space_check(board, int(position)-1) or position not in "1 2 3 4 5 6 7 8 9".split():
        position = raw_input(players[current_player][0] + " enter your next move (1-9): ")
    board[int(position)-1] = players[current_player][1]

def replay():
    valid = ["yes","no"]
    again = False
    choice = raw_input("Do you want to play again? (Yes / No): ").lower()
    while choice not in valid:
        choice = raw_input("Invalid input. Enter 'Yes' or 'No': ").lower()
    if choice == "yes":
        again = True
    return again

def reset_game(board):
    global first_move
    board[:] = [" " for elements in board]
    first_move = True
    print('************************************************************')
    print(" \n \n ")

play_again = True
given_inputs = False
first_move = True

while play_again == True:

    if given_inputs == False:
        print('Welcome to Tic Tac Toe!')
        print('************************************************************')
        player_input(players)
        given_inputs = True

    if first_move == True:
        display_board(board)
        current_player = choose_first()
        first_move = False

    if full_board_check(board) == False:    
        if (win_check(board, players[0][1]) == False and win_check(board, players[1][1]) == False):
            player_choice(board)
            display_board(board)
            next_player()
        elif win_check(board, players[0][1]) == True:
            print (players[0][0] + " wins!")
            play_again = replay()
            reset_game(board)
            continue
        elif win_check(board, players[1][1]) == True:
            print (players[1][0] + " wins!")
            play_again = replay()
            reset_game(board)
            continue
    else:
        print("Board full!.")
        play_again = replay()
        reset_game(board)
        continue