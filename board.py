from sign import Sign


class Board:
    ''' generic board of 3X3 which can represent a classic tic tac toe board
    and also a board made of other boards which used in super tic tac toe '''

    def __init__(self, empty_square):
        '''function gets the representation of square in the board
        (can be a sign (X/O/-) or a board itself) and returns an empty board'''
        # initialize empty board
        self.__winner = Sign.E
        self.__squares = [0,0,0] # 3 rows
        self.__squares[0] = [empty_square, empty_square, empty_square]
        self.__squares[1] = [empty_square, empty_square, empty_square]
        self.__squares[2] = [empty_square, empty_square, empty_square]

    def insert(self, square, x, y):
        self.__squares[y][x] = square
        # check whether this move lead to winning:

        # check if previous move caused a win on vertical line
        if self.__squares[0][y] == self.__squares[1][y] == self.__squares [2][y]:
            self.__winner = square

        # check if previous move caused a win on horizontal line
        if self.__squares[x][0] == self.__squares[x][1] == self.__squares [x][2]:
            self.__winner = square

        # check if previous move was on the main diagonal and caused a win
        if x == y and self.__squares[0][0] == self.__squares[1][1] == self.__squares [2][2]:
            self.__winner = square

        # check if previous move was on the secondary diagonal and caused a win
        if x + y == 2 and self.__squares[0][2] == self.__squares[1][1] == self.__squares [2][0]:
            self.__winner = square

    def get_winner(self):
        return self.__winner

    def __str__(self):
        res = ''
        for i in self.__squares:
            res += str(i)
            res += '\n'
        return res
