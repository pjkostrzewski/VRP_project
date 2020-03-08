import random
from GA import GeneticAlgorithm
from Route import Route

class Population(object):
    
    population_size = 40
    number_of_populations = 0
    
    def __init__(self):  
        self.population = list()
        Population.number_of_populations += 1
        
    def get_population(self):
        return self.population
    
    def get_fittest_route(self):
        return sorted(self.population, key=lambda x: x.calculate_distance())[0]
         
    def clear_population(self):
        self.population.clear()
    
    def sort(self):
        self.population.sort(key=lambda x: x.calculate_distance())
        
    def get_random_route(self):
        self.sort()
        sum_of_distances = sum([x.calculate_distance() for x in self.population])
        return random.choices(self.population, [x.fitness/sum_of_distances for x in self.population])[0]
    
    def get_route_via_tournament(self, tournament_size=4):
        tournament = []
        for _ in range(tournament_size):
            route = random.choice(self.population)
            tournament.append(route)
        return sorted(tournament, key=lambda x: x.calculate_distance())[0]
        
    def crossover_population(self):
        crossover_result = []
        assert self.population, "Population is empty."
        while len(crossover_result) < self.population_size:
            route_1 = self.get_route_via_tournament()
            route_2 = self.get_route_via_tournament()
            crossed_1, crossed_2 = GeneticAlgorithm.crossover(route_1, route_2)
            if crossed_1.uniques_only():
                crossover_result.append(crossed_1)
            if crossed_1.uniques_only():
                crossover_result.append(crossed_2)
        self.population = crossover_result[:self.population_size]
        
    def mutate_population(self):
        for route in self.population:
            GeneticAlgorithm.mutation(route) 


class FirstPopulation(Population):
    
    def __init__(self, points):
        super().__init__()
        self.depot = points[0]
        self.points = points[1:]
        self.create_random_population()
        
    def create_random_population(self):
        self.clear_population()
        for _ in range(self.population_size):
            permutation = random.sample(self.points, len(self.points))
            self.population.append(Route(permutation))
            
            
class ChildsPopulation(Population):
    
        def __init__(self, previous_population):
            super().__init__()
            self.population = previous_population
