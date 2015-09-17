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
        # individuals is a list of all members of the population
        self.individuals = self._make_individuals()
        #How likely a mutation is to occur
        self.mutation_chance = mutation_chance

    def _make_individuals(self):
        ''' Generates individuals to reside within the population '''
        # Make x new individuals, where x is the population count
        individuals = []
        if self.survivors == None:
            #Make totally new individuals
            for x in range(self.size):
                new_individual = self.individual_class(self.options)
                individuals.append(new_individual)
        return individuals

    def cull(self, cull_size):
        ''' Kills off the worst scoring members of the population. '''
        for x in range(cull_size):
            smallest = min(self.individuals)
            self.individuals.remove(smallest)
