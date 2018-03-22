from enum import Enum


class Sign (Enum):
    X = 'X'
    O = 'O'
    E = ' '
    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)
