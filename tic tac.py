# from IPython.display import clear_output

def display_board(board):
    # clear_output()
    print(board[7]+'\t|\t'+board[8]+'\t|\t'+board[9])
    print('------------------------------------')    
    print(board[4]+'\t|\t'+board[5]+'\t|\t'+board[6]) 
    print('------------------------------------')   
    print(board[1]+'\t|\t'+board[2]+'\t|\t'+board[3])

def player_input():
    marker=''
    while not (marker=='X'or marker=='O'):
          marker= input('player 1 : choose x or o ').upper()
    if marker =='X':
        return('X','O')
    else:
        return('O','X')

def place_marker(board, marker,position):
    board[position]=marker

def win_check(board,mark):
    return((board[7]==mark and  board[8]==mark and board[9]==mark) or 
           (board[4]==mark and  board[5]==mark and board[6]==mark) or 
           (board[1]==mark and  board[2]==mark and board[3]==mark) or 
           (board[1]==mark and  board[5]==mark and board[9]==mark) or 
           (board[3]==mark and  board[5]==mark and board[7]==mark) or 
           (board[7]==mark and  board[4]==mark and board[1]==mark) or 
           (board[8]==mark and  board[5]==mark and board[2]==mark) or 
           (board[9]==mark and  board[6]==mark and board[3]==mark)  )

import random
def choose_first():
    flip =random.randint(0,1)
    if flip==0:
        return 'player1'
    else :
        return 'player2'               

def space_check(board,position):
    return board[position]==''

def full_board(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9]or not space_check(board, position):
        position=int(input('choose a position  '))

    return position    

def replay():
    choice = input('play again ? enter yes or no ')
    return choice =='yes'

print("\nWELCOME TO TIC TAC GAME")
while True:
    #set everyting up (board, who's first ,choose markers)
    the_board=['']*10
    player1_marker,player2_marker= player_input()
    turn =choose_first()
    print(turn + " will go first")
    play_game = input("\nready to play? y or n ?")
    if play_game == 'y':
        game_on=True
    else:
        game_on=False

    #player 1 turn
    while game_on:
        if turn== 'player1':
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,player1_marker,position)
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('\nplayer1 has won !')
                game_on=False

            else:
                if full_board(the_board):
                    display_board(the_board)
                    print('\ntie game!')
                    break

                else:
                    turn='player2'

        else:
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,player2_marker,position)
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('\nplayer2 has won !')
                game_on=False

            else:
                if full_board(the_board):
                    display_board(the_board)
                    print('\ntie game!')
                    break

                else:

                    turn='player1'


    if not replay():
        break

            





    




