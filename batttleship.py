#so, we are going to create a version fo the battleship game
#at first it will serve one player
from random import randint as rand_int
#from battleship_classes import Carrier, Battleship, Cruiser, Destroyer, Submarine
import battleship_classes
    
def create_board(x:int = 5):
    lst = []
    for i in range(x):
        lst.append(["O", "O", "O", "O", "O"])
    return lst

def create_matrix(x:int = 5):
    board = {}
    for i in range(1, x+1):
        board[i] = []
        for y in range(x):
            board[i].append("O")
    return board
def place_carrier(board: dict):
    carrier = battleship_classes.Carrier()
    for key in board:
        if board[key].count("O") >= 5:
            
    return carrier
if __name__ == "__main__":
    car = place_carrier()
    print (car.name)
    cruiser = battleship_classes.Cruiser("cru")
    board = create_matrix(6)
    for key in board:
        s = "-"
        print (s.join(board[key]))