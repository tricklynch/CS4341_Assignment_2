from ga import Genetic_Algorithm
from individual import Individual_P1
import sys
import time

def main(puzzle, file, max_time, population, elitism, culling, trials, rate):
    start_time = time.time()
    options = Genetic_Algorithm.parse_file(file, 1)
    ga = Genetic_Algorithm(
        options, 
        Individual_P1, 
        trials, 
        population, 
        elitism, 
        culling, 
        rate,
        start_time,
        max_time
    )
    result = ga.start()
    time_run = time.time() - start_time
    print "Best solution in generation {0} after {1} trials and {2} seconds: {3}, with score {4}" \
        .format(result[0], result[2], time_run, result[1].used_pieces, result[1].fitness())

    table = [i.fitness() for i in ga.best_individuals]
    print table
