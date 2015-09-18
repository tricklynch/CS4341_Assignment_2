class Tower_Piece:

    def __init__(self, piece, width, strength, cost):
        self.piece = piece
        self.width = width
        self.strength = strength
        self.cost = cost


class Number_Piece:

    def __init__(self, value, used):
        self.value = value
        self.used = used

    def __repr__(self):
        if self.used:
            return str(self.value)
        else:
            return "({0})".format(self.value)

    def __lt__(self, other):
        ''' Used to sort pieces on value '''
        return self.value < other.value

    def __eq__(self, other):
        ''' Used to determine if one individual == another '''
        return self.value == other.value
