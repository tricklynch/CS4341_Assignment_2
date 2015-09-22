from ga import Genetic_Algorithm
from individual import Individual_P2
import sys
# Probably change the default population later


def main(puzzle, file, time, population, elitism, culling, trials, rate):
    if not population:
        population = 15
    if not elitism:
        elitism = 3
    if not culling:
        culling = 2
    if population <= (elitism + culling):
        print "The population is less than the sum of the number of elite clones and the number culled."
        print "Don't do that"
        sys.exit(1)
    if not trials:
        trials = 100
    if not rate:
        rate = 0.05

    options = Genetic_Algorithm.parse_file(file, 2)
    
    # options, individual_class, num_generations,
    # population_size, elitism, cull_size, mutation_chance
    ga = Genetic_Algorithm(
        options, 
        Individual_P2, 
        trials, 
        population, 
        elitism, 
        culling, 
        rate
    )
    result = ga.start()
    solution = str(result[1].used_pieces)
    print "Best solution in generation {0} after {1} trials: {2}, with score {3}" \
        .format(result[0], trials, solution, result[1].fitness())

    table = [i.fitness() for i in ga.best_individuals]
    print table
