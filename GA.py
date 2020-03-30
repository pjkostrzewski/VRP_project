import random
from Route import Route
from RoutesContainer import RoutesContainer
from itertools import repeat
import helpers
from copy import deepcopy


class GeneticAlgorithm(object):

    mutation_rate = 0.3
    crossover_rate = 1

    @classmethod
    def crossover(cls, route_1, route_2):
        if random.random() <= cls.crossover_rate:
            pivot_1 = random.randint(0, route_1.routes.get_length())
            pivot_2 = random.randint(0, route_1.routes.get_length())
            pivot_1, pivot_2 = sorted([pivot_1, pivot_2])
            crossover_1 = deepcopy(route_1)
            crossover_2 = deepcopy(route_2)
            crossover_1.routes = Route(route_1.routes[:pivot_1] + route_2.routes[pivot_1:pivot_2] + route_1.routes[pivot_2:])
            crossover_2.routes = Route(route_2.routes[:pivot_1] + route_1.routes[pivot_1:pivot_2] + route_2.routes[pivot_2:])
            return crossover_1, crossover_2
        else:
            return route_1, route_2
        
    @classmethod
    def mutation(cls, route):
        if random.random() <= cls.mutation_rate:
            l,r = random.sample(range(route.routes.get_length()), 2)
            l_value = route.routes[l]
            r_value = route.routes[r]
            if len(route.details) == 1:
                route.details[0] = route.details[0] + 1 if random.choice([True, False]) else route.details[0] - 1
            else:
                route.routes[l], route.routes[r] = r_value, l_value
                a = random.choice(range(len(route.details)))
                b = random.choice(range(len(route.details)))
                # route.details[a] += 1
                # route.details[b] -= 1
            