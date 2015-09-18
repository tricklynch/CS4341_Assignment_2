from ga import Genetic_Algorithm
from individual import Individual_P1
import sys

def main(puzzle, file, time, population=1):
    options = [1570,1,2,303,600,5,8,16,12,22,3,7,60,113,11,36,78,103,200,400,8,64,44]
    #options, individual_class, num_generations, population_size, cull_size
    ga = Genetic_Algorithm(options, Individual_P1, 1000, 10, 5)
    result = ga.start()
    solution = str(result[1].used_pieces)
    print "Best solution in generation {0} after 1000 trials: {1}, with score {2}".format(result[0],solution,result[1].fitness())
