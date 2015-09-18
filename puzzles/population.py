import random


class Population:

    def __init__(self, options, mutation_chance, size, individual_class, survivors):
        # Size is the number of individuals in the population
        self.size = size
        # invdividual_class is the class to use when constructing an individual
        self.individual_class = individual_class
        # survivors is a list of individuals that survived the culling from the
        # previous generation
        self.survivors = survivors
        # options is the set of pieces that can be used in the puzzle
        self.options = options
        # How likely a mutation is to occur
        self.mutation_chance = mutation_chance
        # individuals is a list of all members of the population
        self.individuals = []
        self._make_individuals()

    def _make_individuals(self):
        ''' Generates individuals to reside within the population '''
        individuals = []
        if self.survivors == None:
            # Make totally new individuals
            self._gen_start_population()
        else:
            self._gen_next_population()
            self._mutate_population()

    def _gen_start_population(self):
        ''' Make a brand new population of individuals '''
        self.individuals = []
        for x in range(self.size):
            new_individual = self.individual_class(self.options)
            self.individuals.append(new_individual)

    def _gen_next_population(self):
        ''' Make the next population using the survivors of the previous '''
        self.individuals = []
        self.individuals.extend(self.survivors[:self._spots_left()])

        while self._spots_left() > 0:
            p1 = self.individuals[self._fitness_selection()]
            p2 = self.individuals[self._fitness_selection()]
            children = self.individual_class.crossover(p1, p2)
            self.individuals.extend(children[:self._spots_left()])

    def _spots_left(self):
        ''' Number of open spots that can be filled by new individuals in the population '''
        return self.size - len(self.individuals)

    def _mutate_population(self):
        ''' Mutate population in place '''
        for i in range(len(self.individuals)):
            self.individuals[i].mutate(self.mutation_chance)

    def cull(self, cull_size):
        ''' Kills off the worst scoring members of the population. '''
        for x in range(cull_size):
            smallest = min(self.individuals)
            self.individuals.remove(smallest)
        return self.individuals

    def _fitness_selection(self):
        '''
        Selects a parent for crossover. Better fitness, better chance of selection.
        https://en.wikipedia.org/wiki/Fitness_proportionate_selection
        '''
        total_fitness = sum(i.fitness() for i in self.individuals)
        value = random.random() * total_fitness

        for i, indiv in enumerate(self.individuals):
            value -= indiv.fitness()
            if value <= 0:
                return i

    def best(self):
        ''' Get the best performer of all the individuals in this population '''
        return max(self.individuals)
