import random
from GA import GeneticAlgorithm
from Route import Route
from RoutesContainer import (RoutesContainer, 
                             generate_random_routes_container)
import helpers


class Population(object):
    
    population_size = helpers.population_size
    number_of_populations = 0
        
    def __init__(self, previous):
        
        if isinstance(previous, Population):    # population
            self.population = previous.get()
        else:       
            self.population = previous
            
        Population.number_of_populations += 1
        self.number = Population.number_of_populations
        
    def __len__(self):
        return len(self.population)
    
    def __repr__(self):
        return "Population {}".format(self.number)
    
    @classmethod
    def configure(cls, benchmark):
        points = benchmark.get_points()
        RoutesContainer.depot = points[0]
        RoutesContainer.points = points[1:]
    
    def get(self):
        return self.population
    
    def get_fittest_container(self):
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
            if crossed_2.uniques_only():
                crossover_result.append(crossed_2)
        self.population = crossover_result[:self.population_size]
        
    def mutate_population(self):
        for route in self.population:
            GeneticAlgorithm.mutation(route) 


def create_random_population():
    permutations = []
    for _ in range(Population.population_size):
        random_container = generate_random_routes_container(RoutesContainer.points)
        permutations.append(random_container)
    return Population(permutations)
            
