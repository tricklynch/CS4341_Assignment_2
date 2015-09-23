import sys
from individual import Individual_P3
from ga import Genetic_Algorithm
from pieces import Tower_Piece
import time

def main(puzzle, file, max_time, population, elitism, culling, trials, rate):
    start_time = time.time()
    options = Genetic_Algorithm.parse_file(file, 3)
    ga = Genetic_Algorithm(
        options, 
        Individual_P3, 
        trials, 
        population, 
        elitism, 
        culling, 
        rate,
        start_time,
        max_time
    )
    result = ga.start()
    solution = str(result[1].used_pieces)
    time_run = time.time() - start_time
    print "Best solution in generation {0} after {1} trials and {2}: {3}, with score {4}" \
        .format(result[0], trials, time_run, solution, result[1].fitness())

    table = [i.fitness() for i in ga.best_individuals]
    print table
