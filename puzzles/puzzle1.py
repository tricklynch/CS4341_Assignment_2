from ga import Genetic_Algorithm
from individual import Individual_P1
import sys


def main(puzzle, file, time, population=1):
    trials = 100
    options = [100,1,2,3,4,17,23,6,14,25,20]
    #options, individual_class, num_generations, population_size, cull_size
    ga = Genetic_Algorithm(options, Individual_P1, trials, 10, 5, 0.05)
    result = ga.start()
    print "Best solution in generation {0} after {1} trials: {2}, with score {3}" \
        .format(result[0], trials, result[1].used_pieces, result[1].fitness())

    table = [i.fitness() for i in ga.best_individuals]
    #print table
