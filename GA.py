import random
from Route import Route


class GeneticAlgorithm(object):

    mutation_rate = 0.5
    crossover_rate = 1

    @classmethod
    def crossover(cls, route_1, route_2):
        if random.random() <= cls.crossover_rate:
            pivot = random.randint(1, route_1.get_length()-2)
            crossover_1 = route_1[:pivot] + route_2[pivot:]
            crossover_2 = route_1[pivot:] + route_2[:pivot]
            return Route(crossover_1), Route(crossover_2)
        else:
            return route_1, route_2
        
    @classmethod
    def mutation(cls, route):
        if random.random() <= cls.mutation_rate:
            l,r = random.sample(range(route.get_length()), 2)
            l_value = route[l]
            r_value = route[r]
            route[l], route[r] = r_value, l_value
