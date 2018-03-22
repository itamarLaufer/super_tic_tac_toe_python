from board import Board
from sign import Sign

def get_cur_sign():
    return signs[turns%2]

def get_cur_player():
    return players[turns%2]

def get_winning_board(sign: Sign):
    return x_square if sign == Sign.X else o_square

def input_indices(type:str = 'square')->tuple:
    return (int(input("insert x of the "+ type+" (0-2)")),int(input("insert y of the "+ type+" (0-2)")))
def print_board():
    for i in range(9):
        for j in range(9):
            print(board.get_from_board((int(j/3), int(i/3))).get_from_board((int(j%3), int(i%3))), end=',')
        print()

# assumes input is always legal


signs = [Sign.X, Sign.O] # used to know what sign is the cur player
turns = 0
# those objects used to replace boards that someone won
x_square = Board(lambda : Sign.X)
x_square.set_winner(Sign.X)
o_square = Board(lambda : Sign.O)
o_square.set_winner(Sign.O)



players = []
players.append (str(input("Insert X player name!")))
players.append (str(input("Insert O player name!")))
# creates the board
board = Board(lambda :Board(lambda :Sign.E))
board_indices = None

while(board.is_active()):
    print_board()
    print(get_cur_player()+",", end=" ")
    if not board_indices: # can put where he wants
        board_indices = input_indices('board')
    square_indices = input_indices()
    board.get_from_board(board_indices).insert(square_indices, get_cur_sign())
    if board.get_from_board(board_indices).get_winner() == get_cur_sign():
        board.insert(board_indices, get_winning_board(get_cur_sign()))
    if board.get_from_board(square_indices).get_winner() != Sign.E: # sent to terminal board
        square_indices = None # so next player can put wherever he wants
    board_indices = square_indices
    turns += 1
