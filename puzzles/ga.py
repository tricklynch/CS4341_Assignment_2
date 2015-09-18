from population import Population
from collections import OrderedDict


class Genetic_Algorithm:

    def __init__(self, options, individual_class, num_generations,
                 population_size, cull_size, mutation_chance):
        self.best_individuals = OrderedDict()
        self.num_generations = num_generations
        self.population_size = population_size
        self.individual_class = individual_class
        self.cull_size = cull_size
        self.options = options
        self.mutation_chance = mutation_chance

    # Start the genetic algorithm.
    def start(self):
        initial_population = Population(
            self.options, self.mutation_chance, self.population_size, self.individual_class, None)

        survivors = initial_population.cull(self.cull_size)
        self.best_individuals[0] = initial_population.best()

        # Run for the number of generations
        for count in range(self.num_generations):
            new_population = Population(
                self.options, self.mutation_chance, self.population_size, self.individual_class, survivors)

            # store the best individual from this generation
            self.best_individuals[count] = new_population.best()
            survivors = new_population.cull(self.cull_size)

        overall_best = max(self.best_individuals.values())
        best_generation = self.best_individuals.values().index(overall_best)
        return (best_generation, overall_best)
