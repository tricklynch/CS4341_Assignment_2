from population import Population
from collections import OrderedDict
from pieces import Tower_Piece
import copy
import re


class Genetic_Algorithm:

    def __init__(self, options, individual_class, num_generations,
                 population_size, cull_size, mutation_chance):
        self.best_individuals = []
        self.num_generations = num_generations
        self.population_size = population_size
        self.individual_class = individual_class
        self.cull_size = cull_size
        self.options = options
        self.mutation_chance = mutation_chance

    def start(self):
        ''' Start the genetic algorithm.'''
        initial_population = Population(
            self.options, self.mutation_chance, self.population_size, self.individual_class, None)

        survivors = initial_population.cull(self.cull_size)
        self.best_individuals.append(copy.deepcopy(initial_population.best()))

        # Run for the number of generations
        for count in range(self.num_generations):
            new_population = Population(
                self.options, self.mutation_chance, self.population_size, self.individual_class, survivors)

            # store the best individual from this generation
            self.best_individuals.append(copy.deepcopy(new_population.best()))
            survivors = new_population.cull(self.cull_size)

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
            if puzzle == 2 or puzzle == 1:
                pieces.append(int(line))
        return pieces
