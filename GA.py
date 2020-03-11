import random
from Route import Route
from itertools import repeat
import helpers


class GeneticAlgorithm(object):

    mutation_rate = 0.3
    crossover_rate = 1

    @classmethod
    def crossover(cls, route_1, route_2):
        if random.random() <= cls.crossover_rate:
            route_len = route_1.get_length()
            r = random.randint(3, route_len//4)
            pivot_1 = random.randint(0, route_1.get_length())
            if pivot_1+r > route_len:
                start = pivot_1 + r - route_len
                crossover_1 = route_1[:start] + route_2[start:pivot_1] + route_1[pivot_1:]
                crossover_2 = route_2[:start] + route_1[start:pivot_1] + route_2[pivot_1:]
            else:
                crossover_1 = route_1[:pivot_1] + route_2[pivot_1:]
                crossover_2 = route_2[:pivot_1] + route_1[pivot_1:]
            
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
            l,r = random.sample(range(route.get_length()), 2)
            l_value = route[l]
            r_value = route[r]
            route[l], route[r] = r_value, l_value


    @classmethod
    def remove_instersection(cls, route):
        passed = 0
        a = random.randint(1, route.get_length()-3)
        c = random.randint(1, route.get_length()-3)
        b = a+1
        d = b+1
        abc = helpers.det_matrix(route[a], route[b], route[c])
        abd = helpers.det_matrix(route[a], route[b], route[d])
        cda = helpers.det_matrix(route[c], route[d], route[a])
        cdb = helpers.det_matrix(route[c], route[d], route[b])
        if (abc<0 and abd>0) or (abc>0 and abd<0):
            passed += 1
        if (cdb<0 and cda>0) or (cdb>0 and cda<0):
            passed += 1
        if passed == 2:
            before = route.calculate_distance()
            route[c], route[a] = route[a], route[c]
            after = route.calculate_distance()
            if before < after: 
                route[d], route[c] = route[c], route[d]
                after = route.calculate_distance()
                if before < after:
                    route[d], route[a] = route[a], route[d]
            