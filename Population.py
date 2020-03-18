import random
from GA import GeneticAlgorithm
from Route import Route
from RoutesContainer import (RoutesContainer, 
                             generate_random_routes_container)
import helpers


class Population(object):
    
    population_size = helpers.population_size
    number_of_populations = 0
    depot = None
    points = None
        
    def __init__(self):  
        self.population = list()
        Population.number_of_populations += 1
    
    @classmethod
    def configure(cls, points):
        Population.depot = points[0]
        Population.points = points[1:]
    
    def get_population(self):
        return self.population
    
    def get_fittest_route(self):
        return sorted(self.population, key=lambda x: x.calculate_distance())[0]
         
    def clear_population(self):
        self.population.clear()
    
    def sort(self):
        self.population.sort(key=lambda x: x.calculate_distance())
        
    def get_route_via_tournament(self, tournament_size=helpers.tournament_size):
        tournament = []
        for _ in range(tournament_size):
            route_container = random.choice(self.population)
            tournament.append(route_container)
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
    
    def __init__(self):
        super().__init__()
        self.create_random_population()
        
    def create_random_population(self):
        self.clear_population()
        for _ in range(self.population_size):
            random_container = generate_random_routes_container(self.points)
            self.population.append(random_container)
            
            
class ChildsPopulation(Population):
    
        def __init__(self, previous_population):
            super().__init__()
            self.population = previous_population
