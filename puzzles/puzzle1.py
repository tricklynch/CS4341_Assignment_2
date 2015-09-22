from ga import Genetic_Algorithm
from individual import Individual_P1
import sys
import time

def main(puzzle, file, max_time, population, elitism, culling, trials, rate):
    if not population:
        population = 15
    if not elitism:
        elitism = 3
    if not culling:
        culling = 5
    if population <= (elitism + culling):
        print "The population is less than the sum of the number of elite clones and the number culled."
        print "Don't do that"
        sys.exit(1)
    if not trials:
        trials = 100
    if not rate:
        rate = 0.05

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
