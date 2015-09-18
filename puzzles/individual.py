import random
import copy
from itertools import islice
from pieces import Number_Piece
import functools

@functools.total_ordering
class Individual_Base:

    def __init__(self, options, used_pieces=[]):
        self.options = options
        self.used_pieces = used_pieces

    def __lt__(self, other):
        ''' Used to sort individuals on score '''
        return self.fitness() < other.fitness()

    def __eq__(self, other):
        ''' Used to determine if one individual == another '''
        return self.fitness() == other.fitness()

    def _rotate(self, amt):
        ''' Used in crossover, rotates the list so that crossed genes align properly '''
        self.used_pieces = (self.used_pieces[amt:] + self.used_pieces[:amt])

    def __repr__(self):
        return str(self.used_pieces)

    @classmethod
    def crossover(cls, a, b):
        '''
        Crosses invidual a with individual b
        See http://stackoverflow.com/questions/11782881/how-to-implement-ordered-crossover
        '''
        size = len(a.used_pieces)

        # Select a random range to cross from
        n1, n2 = random.randint(0, size), random.randint(0, size)
        start = min(n1, n2)
        end = max(n1, n2)

        b_swap = b.used_pieces[start: end]
        a_swap = a.used_pieces[start: end]
        cross_a, cross_b = cls(a.options), cls(b.options)
        cross_a.used_pieces = []
        cross_b.used_pieces = []

        cross_a.used_pieces.extend(a_swap)
        cross_b.used_pieces.extend(b_swap)

        index, gene_in_a, gene_in_b = 0, 0, 0
        for x in range(size):
            index = (end + x) % (size)
            gene_in_a = a.used_pieces[index]
            gene_in_b = b.used_pieces[index]

            if gene_in_b not in cross_a.used_pieces:
                cross_a.used_pieces.append(gene_in_b)

            if gene_in_a not in cross_b.used_pieces:
                cross_b.used_pieces.append(gene_in_a)

        cross_a._rotate(start)
        cross_b._rotate(start)
        return [cross_a, cross_b]


    def mutate(self, chance):
        ''' Goes through each gene in the individual and mutates it with a given probability '''
        for index, val in enumerate(self.used_pieces):
            if random.random() < chance:
                other = random.randint(0, len(self.used_pieces) - 1)
                temp = self.used_pieces[index]
                self.used_pieces[index] = self.used_pieces[other]
                self.used_pieces[other] = temp
        return self

class Individual_P1(Individual_Base):
    '''A class used to represent an individual member of the population for puzzle 1'''

    def __init__(self, options):
        # options is an array of numbers that the individual has access to
        self.options = options
        # used_pieces is an array of options that are being used
        self.used_pieces = self._randomize()

    def _randomize(self):
        ''' Returns a random subset of the options. Goal is never included in the subset '''
        choices = self.options[1:]
        result = []

        for num in choices:
            used = random.choice([True, False])
            new_piece = Number_Piece(num, used)
            result.append(new_piece)
        return result

    def mutate(self, chance):
        ''' Goes through each gene in the individual and mutates it with a given probability '''
        for index, val in enumerate(self.used_pieces):
            if random.random() < chance:
                used = self.used_pieces[index].used
                self.used_pieces[index].used = not used
        return self

    def fitness(self):
        ''' Returns the overall fitness of the individual '''
        score = 0
        for piece in self.used_pieces:
            if piece.used == True:
                score += piece.value
        if score > self.options[0]:
            return 0
        else:
            return score


class Individual_P2(Individual_Base):
    '''A class used to represent an individual member of the population for puzzle 2'''

    def __init__(self, options):
        # options is an array of numbers that the individual has
        # access to
        self.options = options
        # used_pieces is an array of options that are being used
        self.used_pieces = options
        random.shuffle(self.used_pieces)

    def fitness(self):
        ''' Returns the overall fitness of the individual '''
        bucket_size = len(self.used_pieces) / 3
        mult_bucket = self.used_pieces[0:bucket_size]
        add_bucket = self.used_pieces[bucket_size: 2 * bucket_size]
        nop_bucket = self.used_pieces[2 * bucket_size:]

        mult_bucket_score = functools.reduce(lambda x, y: x * y, mult_bucket)
        add_bucket_score = sum(add_bucket)
        score = (mult_bucket_score + add_bucket_score) / 2

        # If the fitness is negative, give a score of 0
        return max(0, score)
