from ga import Genetic_Algorithm
from individual import Individual_P2
import sys
# Probably change the default population later


def main(puzzle, file, time, population=1):
    trials = 1000
    options = [-7, -2, -3, -4, -5, -6, 1, 2, 3, 4, 5, 6]

    #options, individual_class, num_generations, population_size, cull_size
    ga = Genetic_Algorithm(options, Individual_P2, trials, 10, 5)
    result = ga.start()
    solution = str(result[1].used_pieces)
    print "Best solution in generation {0} after {1} trials: {2}, with score {3}".format(result[0], trials, solution, result[1].fitness())
