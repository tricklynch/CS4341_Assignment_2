class Tower_Piece:

    def __init__(self, kind, width, strength, cost):
        self.kind = kind
        self.width = width
        self.strength = strength
        self.cost = cost
        self.used = False

    def __repr__(self):
        rep = "P:{0} W:{1} S:{2} C:{3}".format(
            self.kind, self.width, self.strength, self.cost)
        if not self.used:
            return "({0})".format(rep)
        else:
            return rep

    def equals(self, other):
        ''' Checks if one piece is equal to another. Note that we do not want to override __eq__ here.'''
        return self.kind == other.kind \
            and self.width == other.width \
            and self.cost == other.cost \
            and self.strength == other.strength \



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

    def equals(self, other):
        ''' Checks if one piece is equal to another. Note that we do not want to override __eq__ here.'''
        return self.value == other.value
