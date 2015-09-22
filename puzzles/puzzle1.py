from ga import Genetic_Algorithm
from individual import Individual_P1
import sys
import time

def main(puzzle, file, max_time, population, elitism, culling, trials, rate):
    start_time = time.time()
    options = Genetic_Algorithm.parse_file(file, 1)
    # (options, individual_class, num_generations, 
    # population_size, elitism, cull_size, mutation_size, start_time, max_time)
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
    print "Best solution in generation {0} after {1} trials: {2}, with score {3}" \
        .format(result[0], trials, result[1].used_pieces, result[1].fitness())

    table = [i.fitness() for i in ga.best_individuals]
    print table
