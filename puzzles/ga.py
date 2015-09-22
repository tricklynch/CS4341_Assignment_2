from population import Population
from collections import OrderedDict
from pieces import Tower_Piece
import copy
import re
import time

class Genetic_Algorithm:

    def __init__(self, options, individual_class, num_generations,
                 population_size, cull_size, elitism_size, mutation_chance,
                 start_time, max_time):
        self.best_individuals = []
        self.num_generations = num_generations
        self.population_size = population_size
        self.individual_class = individual_class
        self.cull_size = cull_size
        self.elitism_size = elitism_size
        self.options = options
        self.mutation_chance = mutation_chance
        self.survivors = None
        self.start_time = start_time
        self.max_time = max_time

    def start(self):
        ''' Start the genetic algorithm.'''

        # Run for the number of generations
        for count in range(self.num_generations):
            new_population = Population(
                self.options,
                self.mutation_chance,
                self.population_size,
                self.individual_class,
                self.survivors
            )

            # store the best individual from this generation
            self.best_individuals.append(copy.deepcopy(new_population.best()))
            self.survivors = new_population.cull(self.cull_size)

            if self.max_time + self.start_time > time.time():
                break

        overall_best = max(self.best_individuals)
        index = self.best_individuals.index(overall_best)
        return (index, overall_best)

    @staticmethod
    def parse_file(file, puzzle):
        ''' Parses a file of input '''
        pieces = []
        text = open(file)
        for line in text:
            if not line:
                continue
            if puzzle == 3:
                p = re.split(r"\t+", line)
                new_piece = Tower_Piece(p[0], int(p[1]), int(p[2]), int(p[3]))
                pieces.append(new_piece)
            if puzzle == 2:
                pieces.append(float(line.rstrip('\n')))
            if puzzle == 1:
                pieces.append(int(line.rstrip('\n')))
        return pieces
