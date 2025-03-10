
import math
import os

def cls():                      # cleans previous terminal
    if os.name == 'nt':
        os.system('cls')
    else: os.system('clear')

cls()


def new_board():
    """creates a new board that consists of a dictonary with cordinates and player {(0,0),"Player1"}"""


    return {} # key spot for the tuple with coords and value is the player.
    

def is_free(board, x, y): 
    """checks if the spot x,y is occupied"""

    if (x,y) in board:
        return False
    else: return True



def place_piece(board, x, y, player): 
    """places a piece on x,y by player unless spot is occupied"""

    if is_free(board,x,y):
        board[x,y] = player
        print(f'Placed new piece on ({x},{y}) for "{player}"')
        return True

    else: 
        print(f'Piece already placed on ({x},{y})')
        return False



def get_piece(board, x, y): 
    """tells you who is the owener of a piece on x,y unless empty"""

    if not is_free(board,x,y):
        print(f'Piece placed by "{board[x,y]}"')
        return board[x,y]

    else: 
        print(f'No piece is placed on ({x},{y})')
        return False
    


def remove_piece(board, x, y): 
    """removes the piece on x,y unless empty"""
    
    if not is_free(board,x,y):
        del(board[x,y])
        print(f'Piece removed from coordinates ({x},{y})')
        return True

    else: 
        print(f'No piece is placed on ({x},{y})')
        return False


def move_piece(board, x1, y1, x2, y2) :
    """moves a piece from x1,y1 to x2,y2 unless x1,y1 is empty or x2,y2 is occupied"""

    if not is_free(board,x1,y1):

        if is_free(board,x2,y2):
            player = get_piece(board,x1,y1)
            place_piece(board,x2,y2,player)
            remove_piece(board,x1,y1)
            print(f'Piece moved from ({x1},{y1}) to ({x1},{y1})')
            return True

        else: 
            print('Postion you are trying to move to is occupied')
            return False

    else: 
        print(f'No piece is placed on ({x1},{y1})')
        return False

    

def count(board, orientation, number, player):
    """gives you the number of pieces placed by one player on either a row or column"""

    if orientation.lower() == 'column':
        amount = 0

        for each in board:

            if each[0] == number and board[each] == player: 
                amount += 1
        print(f'There are {amount} pieces belonging to "{player}" on {orientation.lower()} {number}')
        return amount

    elif orientation.lower() == 'row':
        amount = 0
        for each in board:

            if each[1] == number and board[each] == player: 
                amount += 1

        print(f'There are {amount} pieces belonging to "{player}" on {orientation.lower()} {number}')
        return amount

    else: 
        print('Try using "column" or "row" for orientation')
        return False
    
    

def nearest_piece(board, x, y):
    """gives you the piece that is closest to x,y"""

    viable = False

    if is_free(board,x,y):
        closest = (x,y)
        closest_distance = 'Undefined'
        closest_player = 'None'

        for each in board:
            viable = True
            distance_squared = (each[0]-x)**2 + (each[1]-y)**2
            distance = math.sqrt(distance_squared)

            # print(distance, board[each])
            if type(closest_distance) == str:
                closest = (each[0],each[1])
                closest_player = board[each]
                closest_distance = distance

            elif distance < closest_distance:
                closest = (each[0],each[1])
                closest_player = board[each]
                closest_distance = distance

        if viable == False:
            return False

    else: 
        closest = (x,y)
        closest_distance = 0
        closest_player = board[x,y]

    print('The closest Piece is',closest_distance,'spaces away on the coordinates',closest, 'and is owned by',closest_player)
    return closest

board = new_board()
place_piece(board,500,100,'player1')
nearest_piece(board,500,105)

"""Lab 3b under"""


def permutation(num,limit = 1):
    """Permutates a number a certain amount of times. sending eg. (1000 choose 200) insted of (1000 choose 800). the limit is the second value when counting the top whilest the limit is one for the rest"""
    
    if num == limit or num == 0:
        return 1
    else: return num * permutation(num-1,limit)

def choose(num1,num2):
    """gives the amount of combinations you can have of num2 out of num1 possible"""

    print(num1,num2)

    if num2 > num1/2:       # reversing second number in the function as it is the same as original
        num2 = num1 - num2
    
    limit = num1 - num2     # limit is how many times the permutaion should loop

    print(num1,num2,limit)

    num_top = permutation(num1,limit)
    num_bot = permutation(num2)

    value = num_top // num_bot

    return value

# print(choose(1000, 800))