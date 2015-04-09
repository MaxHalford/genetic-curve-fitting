import numpy.random as rand
from copy import deepcopy

# Polynomial
class Individual:
    # c is the number of coefficient
    # d is the number of variables
    def __init__(self, c, d):
        # Generate normal distributed coefficients for each variable plus the intercept
        self.values = [[rand.normal() for _ in range(c + 1)] for _ in range(d)]
        self.fitness = None

    # The objective function is the squared error
    def evaluate(self, lookupTable):
        self.fitness = 0
        # For each input
        for x in lookupTable.keys():
            image = 0
            # For each variable
            for variable in self.values:
                # For each coefficient
                for power, coefficient in enumerate(variable):
                    # Compute polynomial image
                    image += coefficient * x ** power
            # Compute squared error
            target = lookupTable[x]
            mse = (target - image) ** 2
            self.fitness += mse

    def mutate(self, rate):
        # Coefficients take a random uniform value in their neighbourhood
        self.values = [[rand.uniform(c - rate, c + rate) for c in variable]
                       for variable in self.values]

    def roundCoefficients(self):
        self.values = [[round(value, 1) for value in variable]
                       for variable in self.values] 
                
# List of polynomials
class Population:
    
    def __init__(self, c, d, size=100):
        # Create individuals
        self.individuals = [Individual(c, d) for _ in range(size)]
        # Store the best individuals
        self.best = [Individual(c, d)]
        # Mutation rate
        self.rate = 0.1

    def sort(self):
        self.individuals = sorted(self.individuals, key=lambda indi: indi.fitness)
                    
    def evaluate(self, lookupTable):
        for indi in self.individuals:
            indi.evaluate(lookupTable)
        self.sort()

    def enhance(self, generations, lookupTable):
        for g in range(generations):
            newIndividuals = []
            # Go through top 10 individuals
            for individual in self.individuals[:10]:
                # Create 1 exact copy of each top 10 individuals
                newIndividuals.append(deepcopy(individual))
                # Create 4 mutated individuals
                for _ in range(4):
                    newIndividual = deepcopy(individual)
                    newIndividual.mutate(self.rate)
                    newIndividuals.append(newIndividual)
            # Replace the old population with the new population of offsprings
            self.individuals = deepcopy(newIndividuals)
            self.evaluate(lookupTable)
            # Store the best individuals
            self.best.append(self.individuals[0])
            # Increment the mutation rate if the population didn't change
            if self.best[-1].fitness == self.best[-2].fitness:
                self.rate += 0.1
            else:
                self.rate = 0.1
