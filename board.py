from sign import Sign


class Board:
    ''' generic board of 3X3 which can represent a classic tic tac toe board
    and also a board made of other boards which used in super tic tac toe '''


    def __init__(self, empty_square_generator):
        '''function builds new board
         empty_square_generator --  function with no parameters which returns the representation of square in the board
        (can be a sign (X/O/-) or a board itself etc) and returns an empty board'''
        # initialize empty board
        self.__winner = Sign.E # winner hasn't charged yet
        self.__squares = [0,0,0] # 3 rows
        self.__squares[0] = [empty_square_generator(), empty_square_generator(), empty_square_generator()]
        self.__squares[1] = [empty_square_generator(), empty_square_generator(), empty_square_generator()]
        self.__squares[2] = [empty_square_generator(), empty_square_generator(), empty_square_generator()]

    def get_from_board(self, indices:tuple):
        return self.__squares[indices[1]][indices[0]]

    def insert(self, indices: tuple , add):
        x = indices[0]
        y = indices[1]
        self.__squares[y][x] = add
        x = indices[1]
        y = indices[0]
        # check whether this move lead to winning:

        # check if previous move caused a win on vertical line
        if not self.__squares[0][y] == Sign.E and self.__squares[0][y] == self.__squares[1][y] == self.__squares [2][y]:
            self.__winner = add

        # check if previous move caused a win on horizontal line
        if not self.__squares[x][0] == Sign.E and self.__squares[x][0] == self.__squares[x][1] == self.__squares [x][2]:
            self.__winner = add

        # check if previous move was on the main diagonal and caused a win
        if x == y and not self.__squares[0][0] == Sign.E and self.__squares[0][0] == self.__squares[1][1] == self.__squares [2][2]:
            self.__winner = add

        # check if previous move was on the secondary diagonal and caused a win
        if x + y == 2 and not self.__squares[0][2] == Sign.E and self.__squares[0][2] == self.__squares[1][1] == self.__squares [2][0]:
            self.__winner = add

    def get_winner(self):
        return self.__winner

    def is_active(self)->bool:
        return self.get_winner() == Sign.E

    def __str__(self):
        res = ''
        for i in self.__squares:
            res += str(i)
            res += '\n'
        return res

    def set_winner(self, winner:Sign):
        self.__winner = winner

    def __repr__(self):
        return str(self)

    # todo improve str method so it will print properly the board made of boards
