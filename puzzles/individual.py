import random
import copy

class Individual_P1():
    '''A class used to represent an individual member of the population for puzzle 1'''

    def __init__(self, options):
        # options is an array of numbers that the individual has access to
        self.options = options
        # Goal is the target
        self.goal = options[0]
        # used_pieces is an array of options that are being used
        self.used_pieces = self._random_subset()

    def __lt__(self, other):
        ''' Used to sort individuals on score '''
        return self.fitness() < other.fitness()

    def _random_subset(self):
        ''' Returns a random subset of the options. Goal is never included in the subset '''
        choices = self.options[1:]
        size = random.randint(0,len(choices))
        return random.sample(choices, size)

    @staticmethod
    def crossover(a, b):
        ''' Crosses invidual a with individual b '''
        cross_a = copy.deepcopy(a)
        cross_b = copy.deepcopy(b)
        #Get the size of half of the list
        a_half = len(a.used_pieces)/2
        b_half = len(b.used_pieces)/2
        #create the crosses
        cross_a.used_pieces = a.used_pieces[:a_half] + b.used_pieces[b_half:]
        cross_b.used_pieces = b.used_pieces[:b_half] + a.used_pieces[a_half:]
        return [cross_a, cross_b]



    def fitness(self):
        ''' Returns the overall fitness of the individual '''
        sum_used_pieces = sum(self.used_pieces)
        if sum_used_pieces > self.goal:
            return 0
        else:
            return sum_used_pieces
