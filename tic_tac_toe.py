import sys
import random

board_g = {1:' ' , 2: ' ', 3:' ' , 4: ' ', 5:' ' , 6: ' ', 7:' ' , 8: ' ', 9:' '}

def replay():
    global board_g
    board_g = {1:' ' , 2: ' ', 3:' ' , 4: ' ', 5:' ' , 6: ' ', 7:' ' , 8: ' ', 9:' '}
    
def display_game_rules():
    print "\nTic Tac Toe"
    print "\nEach player takes a turn to fill the position with 'X' or 'O'"
    print "\nThe position on the board is like below"
    print """\n
    1 | 2 | 3
    ----------
    4 | 5 | 6
    ----------
    7 | 8 | 9
    """
    
def display_gaming_board(board):
    """Takes a dictionary as an input"""
    print "\n"
    count = 1
    for i in xrange(3):
        for j in xrange(3):
            print board[count]+'|',
            count += 1
        print "\n---------"

def is_space_available(board):
    """Takes a dictionary as an input 
    and returns true if there is a key where the marker has not been put in"""
    for i in board.values():
        if i == ' ':
            return True
    return False

def is_position_available(board, position):
    if board[position] == ' ':
        return True
    print "\nPosition already filled. You lost your chance"
    return False

def place_marker(board,marker,position):
    """Places the marker in the position"""
    board[position] = marker

def win_check(board, marker,player):
    cross_map = ['147','258','369','123','456','789','159','357']
    for pattern in cross_map:
        if reduce(lambda x, y:x+y,[board[int(key)] for key in pattern]) == marker*3:
            print "\n"+player+ " wins"
            return True
    return False

def assign_markers():
    markers_assigned = False
    while(not markers_assigned):
        choice = raw_input("Player 1, please choose X or O as your marker: ")
        if choice.lower() == 'x':
            marker1, marker2 = 'X', 'O'
            break
        elif  choice.lower() == 'o':
            marker1, marker2 = 'O', 'X'
            break
        else:
            print " Pick one of the two"
    return marker1, marker2

def player_choice(board,player):
    position = int(raw_input("\n"+player+ " - enter a position"))
    marker = (lambda x:marker2 if x[-1] == '2' else marker1)(player)
    if is_space_available(board) and is_position_available(board,position):
        place_marker(board,marker,position)
        display_gaming_board(board)
    return win_check(board,marker, player)
    

def choose_first():
    return random.randint(1,2)

def replay_input():
    choice = False
    while(not choice):
        answer = raw_input(" Continue : Y/N ").lower()
        if answer =='y' or answer == 'n':
            break
        else:
            print "\nChoose between Y or N"
    if answer == 'y':
        print "\nRebooting"
        return True
    print "\n Thanks for playing the game"
    return False

display_game_rules()

marker1, marker2 = assign_markers()

num = choose_first()
replay_choice = True
while(replay_choice):
    continue_game = True
    while(continue_game):
        for i in [str(num), (lambda x:'2' if x ==1 else '1')(num)]:
            if player_choice(board_g,"player"+i):
                continue_game = False
                break
            elif not is_space_available(board_g):
                print "\n Looks like a draw"
                continue_game = False
                break
            else:
                pass
        
        
    replay_choice = replay_input()
    replay()
