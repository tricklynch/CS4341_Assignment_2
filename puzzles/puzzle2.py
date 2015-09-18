from ga import Genetic_Algorithm
from individual import Individual_P2
import sys
# Probably change the default population later


def main(puzzle, file, time, population=1):
    trials = 1000
    options = [-3.2, 7.0, -2.0, -6.5, 5.0, -5.4, 1.9, -2.3, -6.2, 5.5, -7.6, -3.2, -3.9, -
               7.3, -5.8, -8.0, 1.0, -7.0, -7.6, -3.4, 4.3, -1.0, -4.6, -6.0, 8.3, -2.6, -3.0, 2.1, 1.1, 2.0]
    #options, individual_class, num_generations, population_size, cull_size
    ga = Genetic_Algorithm(options, Individual_P2, trials, 10, 5)
    result = ga.start()
    solution = str(result[1].used_pieces)
    print "Best solution in generation {0} after {1} trials: {2}, with score {3}".format(result[0], trials, solution, result[1].fitness())
