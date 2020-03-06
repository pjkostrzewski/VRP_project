import random
from TSP import TSP
from Route import Route

class Population(object):
    
    population_size = 30
    number_of_populations = 0
    tsp = TSP()
    
    def __init__(self):  
        self.population = list()
        Population.number_of_populations += 1
        
    def get_population(self):
        return self.population
            
    def _clear_population(self):
        self.population.clear()

    def crossover_population(self):
        crossover_result = []
        assert self.population, "Population is empty."
        attempts = 0
        while len(crossover_result) < self.population_size and attempts < 3:
            paired_routes = [(self.population[i], self.population[i+1]) for i in range(0, len(self.population)-1, 2)]
            for route_1, route_2 in paired_routes:
                crossed_1, crossed_2 = self.tsp.crossover(route_1, route_2)
                if crossed_1.uniques_only() and crossed_1 not in crossover_result:
                    crossover_result.append(crossed_1)
                if crossed_1.uniques_only() and crossed_2 not in crossover_result:
                    crossover_result.append(crossed_2)
                attempts += 1
        self.population = crossover_result[:self.population_size]
        
    def mutate_population(self):
        for route in self.population:
            self.tsp.mutation(route) 


class FirstPopulation(Population):
    
    def __init__(self, points):
        super().__init__()
        self.points = points
        self.create_random_population()
        
    def create_random_population(self):
        self._clear_population()
        for _ in range(self.population_size):
            permutation = random.sample(self.points, len(self.points))
            self.population.append(Route(permutation))
            
            
class ChildsPopulation(Population):
    
        def __init__(self, previous_population):
            super().__init__()
            self.previous_population = previous_population
        
        def get_previous_population(self):
            return self.previous_population
        