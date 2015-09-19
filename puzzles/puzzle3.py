import sys
from individual import Individual_P3
from ga import Genetic_Algorithm
from pieces import Tower_Piece

def main(puzzle, file, time, population=1):
    trials = 1000

    options = Genetic_Algorithm.parse_file(file, 3)
    #options, individual_class, num_generations, population_size, cull_size
    ga = Genetic_Algorithm(options, Individual_P3, trials, population, 5, 0.5)
    result = ga.start()
    solution = str(result[1].used_pieces)
    print "Best solution in generation {0} after {1} trials: {2}, with score {3}" \
        .format(result[0], trials, solution, result[1].fitness())
