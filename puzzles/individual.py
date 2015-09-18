import random
import copy
from itertools import islice
import functools


class Individual_P1(object):
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
        result = {}

        for choice in choices:
            result[choice] = random.choice([True, False])
        return result

    @staticmethod
    def crossover(a, b):
        ''' Crosses invidual a with individual b '''
        cross_a = copy.deepcopy(a)
        cross_b = copy.deepcopy(b)
        size = len(a.used_pieces)

        for k, v in islice(b.used_pieces.iteritems(), size / 2):
            # A gets the first half of B's keys
            cross_a.used_pieces[k] = v
        for k, v in islice(a.used_pieces.iteritems(), size / 2):
            # B gets the first half of A's keys
            cross_b.used_pieces[k] = v
        return [cross_a, cross_b]

    def mutate(self, chance):
        ''' Goes through each gene in the individual and mutates it with a given probability '''
        for k, v in self.used_pieces.iteritems():
            if random.random() < chance:
                self.used_pieces[k] = not v
        return self

    def fitness(self):
        ''' Returns the overall fitness of the individual '''
        score = 0
        for k, v in self.used_pieces.iteritems():
            if v == True:
                score += k

        if score > self.goal:
            return 0
        else:
            return score


class Individual_P2(object):
    '''A class used to represent an individual member of the population for puzzle 2'''

    def __init__(self, options):
        # options is an array of numbers that the individual has
        # access to
        self.options = options
        # used_pieces is an array of options that are being used
        self.used_pieces = options
        random.shuffle(self.used_pieces)


    def __lt__(self, other):
        ''' Used to sort individuals on score '''
        return self.fitness() < other.fitness()

    def _rotate_buckets(self, amt):
        self.used_pieces = (self.used_pieces[amt:] + self.used_pieces[:amt])

    @staticmethod
    def crossover(a, b):
        '''
        Crosses invidual a with individual b
        See http://stackoverflow.com/questions/11782881/how-to-implement-ordered-crossover
        '''
        size = len(a.options)
        start = random.randint(0, 2) * (size / 3)
        end = start + (size / 3)

        b_swap_bucket = b.used_pieces[start: end]
        a_swap_bucket = a.used_pieces[start: end]

        cross_a, cross_b = Individual_P2([]), Individual_P2([])
        cross_a.used_pieces.extend(a_swap_bucket)
        cross_b.used_pieces.extend(b_swap_bucket)

        index, gene_in_a, gene_in_b = 0, 0, 0
        for x in range(size):
            index = (end + x) % size
            gene_in_a = a.used_pieces[index]
            gene_in_b = b.used_pieces[index]

            if gene_in_b not in cross_a.used_pieces:
                cross_a.used_pieces.append(gene_in_b)

            if gene_in_a not in cross_b.used_pieces:
                cross_b.used_pieces.append(gene_in_a)

        cross_a._rotate_buckets(start)
        cross_b._rotate_buckets(start)
        return [cross_a, cross_b]

    def mutate(self, chance):
        ''' Goes through each gene in the individual and mutates it with a given probability '''
        for index, val in enumerate(self.used_pieces):
            if random.random() < chance:
                other = random.randint(0, len(self.options) - 1)
                temp = self.used_pieces[index]
                self.used_pieces[index] = self.used_pieces[other]
                self.used_pieces[other] = temp
        return self

    def fitness(self):
        ''' Returns the overall fitness of the individual '''
        bucket_size = len(self.used_pieces) / 3
        mult_bucket = self.used_pieces[0:bucket_size]
        add_bucket = self.used_pieces[bucket_size: 2 * bucket_size]
        nop_bucket = self.used_pieces[2 * bucket_size:]

        mult_bucket_score = functools.reduce(lambda x, y: x * y, mult_bucket)
        add_bucket_score = sum(add_bucket)
        score = (mult_bucket_score + add_bucket_score) / 2
        return score
