#so, we are going to create a version fo the battleship game
#at first it will serve one player
from random import randint 
from battleship_classes import Carrier, Battleship, Cruiser, Destroyer, Submarine
import battleship_classes
    
def create_board(x=5):
    lst = ["O" for y in range(x)]
    return lst

def check_consecutive(board, spaces):
    #determines whether line or column has enough space for ship placement
    available = []
    for key in board:
        temp = 0
        for position in board[key]:
            if position == "O":
                temp +=1
            else:
                temp = 0
            if temp >= spaces:
                available.append(key)
                break
    return available

def create_matrix(x = 5):
    board = {}
    for i in range(1, x+1):
        board[i] = ["O" for y in range(x)]
    return board

def create_rows(x = 5):
    rows = {}
    for i in range(x):
        rows[i] = ["O" for y in range(x)]
    return rows
def change_os(board, ship):
    pass
def place_ship (b, ship):
    try:
        if ship:
            print (ship._hit_points)
            available_lines_in_board = check_consecutive(b, ship._hit_points)
            print (available_lines_in_board)
            row_or_column = "row" if randint(1, len(available_lines_in_board)) % 2 ==0 else "column"
            row = available_lines_in_board[randint(0, len(available_lines_in_board))]
            print (row)
            print (row_or_column)
            if row_or_column == "row":
                starting_point = randint(0, len(b[row]) - ship._hit_points)
                for i in range(starting_point, len(b[row])):
                    b[row][i] = ship.name
                    print (b[row])
    except AttributeError:
        print ("Incorrect type")
        
if __name__ == "__main__":
    b = create_matrix(6)
    print (check_consecutive(b, 8))
    carrier = Carrier("Carrier")
    place_ship(b, carrier)
    print (create_rows)